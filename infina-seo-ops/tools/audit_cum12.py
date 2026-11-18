import json,re,subprocess,html,collections
def get(u): return subprocess.run(['curl','-s',u],capture_output=True,text=True).stdout
allp=[]
for pg in range(1,5):
    r=get(f'https://infina.ai/news/wp-json/wp/v2/posts?per_page=100&page={pg}&_fields=id,slug,date,modified,content&status=publish')
    try:
        j=json.loads(r)
        if not isinstance(j,list): break
        allp+=j
    except Exception: break
print('posts',len(allp))
json.dump(allp,open('all_now.json','w'))
byslug={p['slug']:p for p in allp}
C={ 'real-estate-customer-service':'real estate customer service','real-estate-past-client-follow-up':'real estate past client follow up','real-estate-client-database':'real estate client database','real-estate-thank-you-notes':'real estate thank you notes','real-estate-lead-nurturing':'real estate lead nurturing','how-to-get-seller-leads-in-real-estate':'how to get seller leads in real estate','real-estate-sales-funnel':'real estate sales funnel','ai-lead-nurture-real-estate':'ai lead nurture real estate','warm-leads-real-estate':'warm leads real estate','real-estate-referral-fee':'real estate referral fee'}
PIL='sphere-of-influence-real-estate'
cl=set(C)|{PIL}
def links(p):
    return [(h.rstrip('/').split('/')[-1] if '/news/' in h else h,html.unescape(re.sub(r'<[^>]+>','',a)).strip().lower()) for h,a in re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>',p['content']['rendered'],re.S)]
inb=collections.defaultdict(list)  # dest slug -> list of (src slug, anchor)
for p in allp:
    for s,a in links(p):
        if s!=p['slug'] and not s.startswith('http'): inb[s].append((p['slug'],a))
print('%-42s %5s %5s %4s %4s %4s %4s %6s'%('slug','words','pill','sib','inb','$','kw','dens%'))
for s,kw in list(C.items())+[(PIL,'sphere of influence')]:
    p=byslug[s]; c=p['content']['rendered']
    t=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',c))); w=len(t.split()); n=t.lower().count(kw)
    L=links(p); pill=sum(1 for x,_ in L if x==PIL); sib=len({x for x,_ in L if x in cl and x not in(PIL,s)})
    money=sum(1 for x,_ in L if x=='https://infina.ai/' or x=='https://infina.ai')
    print('%-42s %5d %5s %4d %4d %4d %4d %6.2f'%(s,w,pill if s!=PIL else '-',sib,len({x for x,_ in inb[s]}),money,n,100*n*len(kw.split())/w/ max(1,len(kw.split()))), 'em' if '—' in c else '')
print()
for s in list(C)+[PIL]:
    A=[a for _,a in inb[s]]; d=len(set(A)); srcs={x for x,_ in inb[s]}
    print('%-42s inbound links %2d from %2d posts, distinct anchors %2d (%.0f%%)'%(s,len(A),len(srcs),d,100*d/max(1,len(A))))
    if len(A) and d/len(A)<0.7:
        cnt=collections.Counter(A); print('   dup:',[(a,n) for a,n in cnt.items() if n>1])
# long anchors
for p in allp:
    if p['slug'] in cl:
        for s,a in links(p):
            if len(a.split())>8: print('LONG anchor',p['slug'],a)
# overlap with 277,263,1488,1961 on keyword
for slug in ['crm-pipeline-management','crm-marketing-real-estate','real-estate-customer-engagement-strategies','real-estate-agent-referral']:
    p=byslug.get(slug)
    if p:
        t=html.unescape(re.sub(r'<[^>]+>',' ',p['content']['rendered'])).lower()
        print(slug,{k:t.count(k) for k in ['sales funnel','client database','customer service','referral fee']})
