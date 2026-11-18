import json,re,subprocess,html,collections
def get(u): return subprocess.run(['curl','-s',u],capture_output=True,text=True).stdout
allp=[]
for pg in range(1,6):
    r=get(f'https://infina.ai/news/wp-json/wp/v2/posts?per_page=100&page={pg}&_fields=id,slug,date,modified,content&status=publish')
    try:
        j=json.loads(r)
        if not isinstance(j,list) or not j: break
        allp+=j
    except Exception: break
print('posts',len(allp))
json.dump(allp,open('all13.json','w'))
by={p['slug']:p for p in allp}
PIL='real-estate-drip-email'
C={'real-estate-drip-campaign-templates':'real estate drip campaign templates','real-estate-follow-up-email':'real estate follow up email templates','realtor-email-templates':'realtor email templates','comparative-market-analysis-real-estate':'comparative market analysis real estate','cma-template':'cma template','real-estate-newsletter':'real estate newsletter templates','real-estate-email-subject-lines':'real estate email subject lines','bad-drip-campaign-real-estate':'real estate drip campaign','video-email-for-real-estate':'video email for real estate',PIL:'real estate drip email'}
cl=set(C)
def links(p):
    return [(h.rstrip('/').split('/')[-1] if '/news/' in h else h,html.unescape(re.sub(r'<[^>]+>','',a)).strip().lower()) for h,a in re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>',p['content']['rendered'],re.S)]
inb=collections.defaultdict(list)
for p in allp:
    for s,a in links(p):
        if s!=p['slug'] and not s.startswith('http'): inb[s].append((p['slug'],a))
print('%-42s %5s %5s %4s %4s %3s %4s %6s'%('slug','words','pill','sib','inb','$','kw','dens%'))
for s,kw in C.items():
    p=by[s]; c=p['content']['rendered']
    t=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',c))); w=len(t.split()); n=len(re.findall(re.escape(kw),t.lower()))
    L=links(p); pill=sum(1 for x,_ in L if x==PIL); sib=len({x for x,_ in L if x in cl and x not in(PIL,s)})
    money=sum(1 for x,_ in L if x.rstrip('/')=='https://infina.ai')
    print('%-42s %5d %5s %4d %4d %3d %4d %6.2f %s'%(s,w,pill if s!=PIL else '-',sib,len({x for x,_ in inb[s]}),money,n,100*n/w,'EM' if '—' in c else ''), p['modified'][:10], p['id'])
print()
for s in C:
    A=[a for _,a in inb[s]]; d=len(set(A)); srcs={x for x,_ in inb[s]}
    print('%-42s inbound %2d from %2d posts, distinct anchors %2d (%.0f%%)'%(s,len(A),len(srcs),d,100*d/max(1,len(A))))
    if A and d/len(A)<0.7:
        print('   dup:',[(a,n) for a,n in collections.Counter(A).items() if n>1])
for p in allp:
    if p['slug'] in cl:
        for s,a in links(p):
            if len(a.split())>8: print('LONG anchor',p['slug'],a)
# donors: share of pillar links pointing to home pillar not needed; list links from donors to cluster
for d in ['real-estate-lead-follow-up-automation-guide','how-to-set-up-automated-lead-follow-up-real-estate','real-estate-lead-nurturing']:
    if d in by: print(d,[ (s) for s,_ in links(by[d]) if s in cl])
# overlap check with key old posts
for slug in ['real-estate-lead-follow-up-automation-guide','how-to-set-up-automated-lead-follow-up-real-estate','real-estate-lead-nurturing','real-estate-email-signature']:
    p=by.get(slug)
    if p:
        t=html.unescape(re.sub(r'<[^>]+>',' ',p['content']['rendered'])).lower()
        print(slug,{k:t.count(k) for k in ['drip email','drip campaign','newsletter','subject line','video email','cma']})
for p in allp:
    t=p['slug']
    if p['id'] in (263,277,2400,2413,2189,1223,1227): 
        tt=html.unescape(re.sub(r'<[^>]+>',' ',p['content']['rendered'])).lower()
        print(p['id'],t,{k:tt.count(k) for k in ['drip email','drip campaign','newsletter','subject line','video email','comparative market analysis']})
