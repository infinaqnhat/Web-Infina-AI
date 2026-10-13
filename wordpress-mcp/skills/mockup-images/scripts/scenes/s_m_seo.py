import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
# Real estate SEO (#1871), mobile-first, canvas 1000 wide. Same content as s_seo.py, new layout.
N='#1b2a4a'; OR='#e0613a'
def title(t,sub=''):
    s='<div style="font-size:60px;font-weight:800;color:'+N+';line-height:1.12">'+t+'</div>'
    if sub: s+='<div style="font-size:40px;font-weight:600;color:#667085;margin-top:10px">'+sub+'</div>'
    return s
def dot(n,col=OR,sz=56):
    return '<span style="flex:none;width:'+str(sz)+'px;height:'+str(sz)+'px;border-radius:50%;background:'+col+';color:#fff;font-weight:800;font-size:40px;display:flex;align-items:center;justify-content:center">'+str(n)+'</span>'
def wrap(inner): return '<div class="abs" style="left:50px;top:40px;width:900px">'+inner+'</div>'
def bar(w,col='#d0d5dd',h=22): return '<div style="height:'+str(h)+'px;width:'+str(w)+'%;background:'+col+';border-radius:11px;margin:10px 0"></div>'

# 1. two places to show up: local results and organic results
mapsvg=('<svg width="100%" height="190" viewBox="0 48 330 81" preserveAspectRatio="xMidYMid slice" style="display:block"><rect width="330" height="190" fill="#e9efe6"/>'
 '<path d="M0 60H330M0 140H330M90 0V190M220 0V190" stroke="#fff" stroke-width="12"/><path d="M0 170L330 20" stroke="#f6e4a8" stroke-width="10"/><rect x="100" y="70" width="110" height="60" fill="#d6e6f5"/>'
 '<g fill="#d93025"><circle cx="150" cy="86" r="14"/><circle cx="262" cy="70" r="11" opacity=".75"/><circle cx="55" cy="108" r="11" opacity=".75"/></g></svg>')
listing=('<div style="display:flex;gap:20px;align-items:center;padding:20px 24px 8px"><div class="deco" style="flex:none;width:76px;height:76px;border-radius:12px;background:#14808a;color:#fff;font-weight:800;font-size:34px;display:flex;align-items:center;justify-content:center">D</div>'
 '<div><div style="font-size:42px;font-weight:700;color:#1a56db;line-height:1.15">Dana Lee, Realtor</div><div style="font-size:38px;color:#475467;margin-top:2px"><strong>4.9</strong> <span style="color:#e0a21b">&#9733;&#9733;&#9733;&#9733;&#9733;</span></div></div></div>')
others=''.join('<div style="display:flex;gap:20px;align-items:center;padding:8px 24px"><div class="deco" style="flex:none;width:76px;height:76px;border-radius:12px;background:'+c+'"></div><div style="flex:1">'+bar(70,'#c7d0de')+bar(40)+'</div></div>' for c in ('#7c5cc4','#e0613a'))
local=('<div style="border:3px solid #e4e7ec;border-radius:16px;overflow:hidden">'+mapsvg+listing+others+'</div>')
organic=('<div style="padding:4px 4px"><div class="deco" style="font-size:28px;color:#667085">example.com &rsaquo; maple-heights</div>'
 '<div style="font-size:42px;color:#1a56db;line-height:1.2;margin:6px 0 4px">Maple Heights neighborhood guide</div>'+bar(100)+bar(72)+'</div>')
def mrow(n,inner): return '<div style="display:flex;gap:20px;align-items:flex-start;margin-top:26px">'+dot(n)+'<div style="flex:1">'+inner+'</div></div>'
mock=('<div class="sh" style="background:#fff;border-radius:18px;padding:26px 26px 30px 26px;margin-top:34px">'
 '<div style="border:3px solid #d0d5dd;border-radius:999px;padding:12px 28px;font-size:40px;color:#1d2433">real estate agent Maple Heights</div>'
 +mrow(1,local)+mrow(2,organic)+'</div>')
def leg(n,t,sub):
    return '<div style="display:flex;gap:22px;align-items:flex-start;margin-top:30px">'+dot(n)+'<div><div style="font-size:44px;font-weight:800;color:'+N+';line-height:1.15">'+t+'</div><div style="font-size:40px;color:#475467;margin-top:6px">'+sub+'</div></div></div>'
seo_results_m=page(wrap(title('Two places to show up')+mock+leg(1,'Local results','Profile, reviews, location')+leg(2,'Organic results','Website pages, content, links')),'',note='',size=(1000,1320))

# 2. profile checklist
items=[('Name, phone, website','Match your site exactly'),('Primary category','Secondary only if true'),('Description','Who you help, and where'),('Photos','Refresh every few months'),('Posts','A market update each month'),('Reviews','Ask every client at closing')]
l=''
for a,b in items:
    l+=('<div class="sh" style="background:#fff;border-radius:16px;padding:18px 26px;margin-top:22px;display:flex;gap:24px;align-items:center">'
     +'<span style="flex:none;width:64px;height:64px;border-radius:50%;background:#e6f6ee;color:#116b43;font-weight:800;font-size:40px;display:flex;align-items:center;justify-content:center">&#10003;</span>'
     +'<div><div style="font-size:44px;font-weight:800;color:'+N+';line-height:1.15">'+a+'</div><div style="font-size:38px;color:#475467;margin-top:4px">'+b+'</div></div></div>')
foot='<div style="font-size:42px;font-weight:700;color:'+N+';margin-top:36px;line-height:1.3;text-wrap:balance">Complete, accurate details help a profile appear.</div>'
seo_profile_m=page(wrap(title('Fill in every field you can')+l+foot),'',note='',size=(1000,1240))

# 3. 90-day plan
M=[('MONTH 1','Set up the foundation',['Complete the business profile','Fix name and phone across sites','Ask last ten clients for reviews','Add Search Console to your site'],'#14808a'),
 ('MONTH 2','Fix your key pages',['Write two key neighborhood pages','Give every page a unique title','Add a valuation request page'],'#1b2a4a'),
 ('MONTH 3','Publish and review',['Publish two helpful articles','Link them to neighborhood pages','Post twice on your profile','Review what Search Console shows'],'#e0613a')]
c=''
for m,t,tasks,col in M:
    c+=('<div class="sh" style="background:#fff;border-radius:18px;overflow:hidden;margin-top:28px"><div style="background:'+col+';color:#fff;padding:16px 28px 18px"><div style="font-size:38px;font-weight:800;letter-spacing:.12em">'+m+'</div><div class="serif" style="font-size:46px;font-weight:700;line-height:1.15;margin-top:2px">'+t+'</div></div>'
     +'<div style="padding:16px 28px 14px">'+''.join('<div style="display:flex;gap:16px;font-size:40px;line-height:1.2;color:#1d2433;margin:12px 0"><span class="deco" style="flex:none;width:20px;height:20px;border-radius:5px;background:'+col+';margin-top:12px"></span><span>'+tk+'</span></div>' for tk in tasks)+'</div></div>')
seo_plan_m=page(wrap(title('A 90-day SEO plan','About 4 to 6 hours a month')+c),'',note='',size=(1000,1480))
SC=dict(seo_results_m=seo_results_m,seo_profile_m=seo_profile_m,seo_plan_m=seo_plan_m)
if __name__=='__main__': render(sel(sys.argv,SC))
