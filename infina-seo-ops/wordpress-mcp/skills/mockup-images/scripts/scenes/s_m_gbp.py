import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
# Google Business Profile for realtors (#1937), mobile-first, canvas 1000 wide. Same content as s_gbp.py, new layout.
N='#1b2a4a'; OR='#e0613a'
def title(t,sub=''):
    s='<div style="font-size:60px;font-weight:800;color:'+N+';line-height:1.12">'+t+'</div>'
    if sub: s+='<div style="font-size:40px;font-weight:600;color:#667085;margin-top:10px">'+sub+'</div>'
    return s
def dot(n,col=OR,sz=56):
    return '<span style="flex:none;width:'+str(sz)+'px;height:'+str(sz)+'px;border-radius:50%;background:'+col+';color:#fff;font-weight:800;font-size:40px;display:flex;align-items:center;justify-content:center">'+str(n)+'</span>'
def wrap(inner): return '<div class="abs" style="left:50px;top:40px;width:900px">'+inner+'</div>'
def bar(w,col='#d0d5dd',h=22): return '<div style="height:'+str(h)+'px;width:'+str(w)+'%;background:'+col+';border-radius:11px;margin:8px 0"></div>'

# 1. profile with seven numbered fields
def row(n,inner):
    return '<div style="display:flex;gap:22px;align-items:center;margin:20px 0">'+(dot(n) if n else '<span style="flex:none;width:56px"></span>')+'<div style="flex:1">'+inner+'</div></div>'
btn=lambda t:'<span style="background:#e8f0fe;color:#1a56db;border-radius:10px;padding:8px 26px;font-size:38px;font-weight:700">'+t+'</span>'
strip=('<div style="position:relative;height:200px;display:flex;gap:4px"><div class="photo" style="flex:2;background-image:url(ph_house.jpg)"></div>'
 '<div style="flex:1;display:flex;flex-direction:column;gap:4px"><div class="photo" style="flex:1;background-image:url(ph_living.jpg)"></div><div class="photo" style="flex:1;background-image:url(ph_aerial.jpg)"></div></div>'
 '<div style="position:absolute;left:20px;top:20px;border:4px solid #fff;border-radius:50%">'+dot(7)+'</div></div>')
card=('<div class="sh" style="background:#fff;border-radius:18px;overflow:hidden;margin-top:34px">'+strip
 +'<div style="padding:10px 30px 18px 30px">'
 +row(1,'<div style="font-size:44px;font-weight:800;color:'+N+'">Dana Lee, Realtor</div>')
 +row(2,bar(40,'#c7d0de',24))
 +row(3,bar(66))
 +row(4,bar(52,'#9ad8b4'))
 +row(5,'<div style="display:flex;gap:14px">'+btn('Call')+btn('Website')+'</div>')
 +row(6,bar(100)+bar(70))
 +'</div></div>')
items=[('Name','your real-world name'),('Category','most specific true one'),('Service area','address hidden if no office'),('Hours','when clients can reach you'),('Phone and site','a number you answer'),('Description','who you help, and where'),('Photos','headshot, office, local')]
lst=''.join('<div style="display:flex;gap:22px;align-items:center;margin-top:20px">'+dot(i+1)+'<div style="font-size:42px;line-height:1.2;color:#475467"><strong style="color:'+N+'">'+a+':</strong> '+b+'</div></div>' for i,(a,b) in enumerate(items))
gbp_fields_m=page(wrap(title('Seven fields to get right')+card+'<div style="margin-top:14px">'+lst+'</div>'),'',note='',size=(1000,1450))

# 2. review: ask, reply, never pay
stars='<span style="color:#e0a21b;font-size:48px;letter-spacing:3px">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'
rev=('<div class="sh" style="background:#fff;border-radius:18px;padding:30px 34px;margin-top:34px">'
 +'<div style="display:flex;gap:22px;align-items:center"><div class="deco" style="flex:none;width:84px;height:84px;border-radius:50%;background:#9fb4d6;color:'+N+';font-weight:800;font-size:34px;display:flex;align-items:center;justify-content:center">MR</div>'
 +'<div><div style="font-size:44px;font-weight:800;color:'+N+'">Maya R.</div></div><div style="margin-left:auto">'+stars+'</div></div>'
 +'<div class="serif" style="font-size:44px;line-height:1.3;color:#1d2433;margin-top:22px">&ldquo;Dana walked us through every step.&rdquo;</div>'
 +'<div style="margin-top:26px;background:#f1f6fb;border-left:8px solid #14808a;border-radius:10px;padding:18px 24px"><div style="font-size:38px;font-weight:800;color:#14808a">Reply from the owner</div><div style="font-size:42px;line-height:1.3;color:#1d2433;margin-top:4px;text-wrap:balance">Thank you, Maya! Enjoy the new home.</div></div></div>')
def rule(n,t,col=OR,tc=N):
    return '<div style="display:flex;gap:22px;align-items:center;margin-top:26px">'+dot(n,col)+'<div style="font-size:44px;font-weight:800;color:'+tc+';line-height:1.2">'+t+'</div></div>'
rules=rule(1,'Ask every client at closing')+rule(2,'Reply to every review')+rule(3,'Never pay for a review','#b42318','#b42318')
bad=('<div style="margin-top:34px;background:#fdecea;border:4px dashed #f0a39b;border-radius:16px;padding:22px 28px;font-size:42px;line-height:1.3;color:#b42318;text-wrap:balance"><strong>Not allowed:</strong> a gift card for a five-star review</div>')
gbp_review_m=page(wrap(title('Ask, reply, never pay')+rev+rules+bad),'',note='',size=(1000,1120))

# 3. true name vs keyword-stuffed name
def nbox(col,bg,tag,name,sub,ok):
    return ('<div class="sh" style="background:#fff;border:6px solid '+col+';border-radius:18px;overflow:hidden;margin-top:34px">'
     +'<div style="background:'+bg+';padding:18px 30px;font-size:40px;font-weight:800;color:'+col+'">'+tag+'</div>'
     +'<div style="padding:28px 30px 32px"><div style="font-size:'+('56' if ok else '44')+'px;font-weight:800;color:'+N+';line-height:1.2">'+name+'</div>'
     +'<div style="font-size:40px;color:#475467;margin-top:14px;line-height:1.3">'+sub+'</div></div></div>')
nm=nbox('#1f8a5b','#e6f6ee','&#10003; Real-world name','Dana Lee, Realtor','The name on your sign, site and cards.',True)
nm+=nbox('#b42318','#fdecea','&times; Keyword-stuffed name','Dana Lee | #1 Realtor in Cedar Hills | Best Homes For Sale','Can get a profile suspended.',False)
nm+='<div style="font-size:44px;font-weight:700;color:'+N+';margin-top:38px;line-height:1.3;text-wrap:balance">Same name on your profile, website and cards.</div>'
gbp_name_m=page(wrap(title('Use your real name only')+nm),'',note='',size=(1000,1030))
SC=dict(gbp_fields_m=gbp_fields_m,gbp_review_m=gbp_review_m,gbp_name_m=gbp_name_m)
if __name__=='__main__': render(sel(sys.argv,SC))
