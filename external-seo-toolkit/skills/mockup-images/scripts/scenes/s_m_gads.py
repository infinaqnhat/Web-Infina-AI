import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'; TEAL='#14808a'; OR='#e0613a'; GREEN='#1f8a5b'; RED='#b42318'
def title(t,top=40,size=64):
    return '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:%dpx;font-weight:800;color:%s;line-height:1.12">%s</div>'%(top,size,N,t)
def dot(n,x,y,d=60,fs=40,col=OR):
    return '<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:50%%;background:%s;color:#fff;font-size:%dpx;font-weight:800;display:flex;align-items:center;justify-content:center">%d</div>'%(x,y,d,d,col,fs,n)
def bar(x,y,w,h=18,col='#e4e7ec'):
    return '<div class="deco" style="position:absolute;left:%dpx;top:%dpx;width:%dpx;height:%dpx;background:%s;border-radius:%dpx"></div>'%(x,y,w,h,col,h//2)
# 1. radius yes, ZIP no
def mapsvg(kind):
    s='<div class="deco" style="height:260px"><svg width="900" height="260" viewBox="0 0 900 300" preserveAspectRatio="xMidYMid slice"><rect width="900" height="300" fill="#e9efe6"/><path d="M0 90H900M0 215H900M200 0V300M470 0V300M740 0V300" stroke="#fff" stroke-width="18"/><path d="M0 285L900 15" stroke="#f6e4a8" stroke-width="14"/><rect x="250" y="110" width="140" height="80" fill="#d6e6f5"/>'
    if kind=='ok': s+='<circle cx="450" cy="150" r="125" fill="#14808a" fill-opacity=".2" stroke="#14808a" stroke-width="7"/><circle cx="450" cy="150" r="14" fill="#d93025"/>'
    else: s+='<g fill="#c2410c" fill-opacity=".18" stroke="#c2410c" stroke-width="6" stroke-dasharray="14 8"><path d="M40 30L440 20L470 140L60 150Z"/><path d="M470 140L860 120L850 280L480 285Z"/><path d="M60 150L470 140L480 285L70 285Z"/></g><g font-family="Inter" font-weight="800" font-size="34" fill="#c2410c"><text x="190" y="100">ZIP A</text><text x="620" y="215">ZIP B</text><text x="200" y="235">ZIP C</text></g>'
    return s+'</svg></div>'
def panel(top,col,head,icon,m,sub):
    return ('<div class="abs" style="left:50px;top:%dpx;width:900px;background:#fff;border:6px solid %s;border-radius:16px;overflow:hidden;box-shadow:0 6px 16px rgba(20,35,70,.12)">'%(top,col)
      +'<div style="background:%s;color:#fff;padding:0 26px;height:104px;display:flex;align-items:center;gap:18px;font-size:46px;font-weight:800"><span style="display:inline-flex;width:62px;height:62px;border-radius:50%%;background:#fff;color:%s;align-items:center;justify-content:center;font-size:40px">%s</span>%s</div>'%(col,col,icon,head)
      +m+'<div style="padding:18px 26px 22px;font-size:40px;font-weight:600;color:#1d2433;line-height:1.28">'+sub+'</div></div>')
t=title('Radius yes, ZIP code no')
t+=panel(140,GREEN,'Allowed: city or radius','&#10003;',mapsvg('ok'),'A radius needs at least 1 km around a point.')
t+=panel(650,RED,'Not allowed: ZIP codes','&#10005;',mapsvg('zip'),'Also barred: age, gender, parental and marital status.')
t+='<div class="abs" style="left:50px;top:1200px;width:900px;font-size:40px;font-weight:600;color:'+N+';line-height:1.3">Check Google&rsquo;s current housing rules.</div>'
gads_targeting_m=page(t,'',note='',size=(1000,1290))
# 2. search -> ad -> page
def step(n,label,y): return dot(n,50,y,60,38)+'<div class="abs" style="left:130px;top:%dpx;font-size:44px;font-weight:800;color:%s">%s</div>'%(y+6,N,label)
def arrow(y): return '<div class="abs" style="left:50px;top:%dpx;width:60px;text-align:center;font-size:48px;line-height:1;color:#98a2b3;font-weight:800">&darr;</div>'%y
s=title('One search, one offer,<br>one page',size=60)
s+=step(1,'A seller searches',200)
s+='<div class="abs" style="left:50px;top:280px;width:900px;border:3px solid #d0d5dd;border-radius:999px;background:#fff;padding:20px 32px;font-size:40px;color:#1d2433;white-space:nowrap">what is my home worth in Cedar Hills</div>'
s+=arrow(375)
s+=step(2,'Your ad appears',445)
s+='<div class="abs sh" style="left:50px;top:525px;width:900px;background:#fff;border-radius:16px;padding:26px 30px;height:250px"><div class="deco" style="font-size:26px;color:#667085;font-weight:700"><span style="border:2px solid #98a2b3;border-radius:6px;padding:1px 10px;margin-right:12px">Ad</span>example.com/home-value</div><div style="font-size:46px;color:#1a56db;font-weight:700;line-height:1.2;margin-top:16px">What Is Your Home Worth Today?</div>'+bar(30,168,820)+bar(30,204,560)+'</div>'
s+=arrow(795)
s+=step(3,'The page matches the offer',865)
land='<div style="height:60px;background:#e9edf3;padding:14px 22px;font-size:26px;color:#667085" class="deco">example.com/home-value</div><div style="padding:26px 30px"><div class="serif" style="font-size:48px;font-weight:700;color:'+N+';line-height:1.18">What is your Cedar Hills home worth?</div><div class="deco" style="border:2px solid #d0d5dd;border-radius:10px;height:62px;margin-top:24px"></div><div class="deco" style="border:2px solid #d0d5dd;border-radius:10px;height:62px;margin-top:16px"></div><div style="background:'+OR+';color:#fff;font-weight:800;text-align:center;border-radius:12px;padding:16px;font-size:42px;margin-top:22px">Request my review</div></div>'
s+='<div class="abs sh" style="left:50px;top:945px;width:900px;border-radius:16px;background:#fff;overflow:hidden">'+land+'</div>'
gads_search_m=page(s,'',note='',size=(1000,1500))
# 3. four-week test
W=[('Week 1','Pick one offer and one area','One ad group, two ads, small budget',TEAL),('Week 2','Add negative keywords','Pause clicks that bring no contacts',N),('Week 3','Fix the landing page','Shorter form, phone number higher','#7c5cc4'),('Week 4','Count leads and cost','Then scale, change the offer, or stop',OR)]
c=title('A four-week Google Ads test',size=60)
y=160
for a,b,d,col in W:
    c+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:200px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden"><div style="position:absolute;left:0;top:0;width:230px;height:200px;background:%s;color:#fff;display:flex;align-items:center;justify-content:center;font-size:54px;font-weight:800;line-height:1.05;text-align:center">%s</div><div style="position:absolute;left:260px;right:24px;top:0;height:200px;display:flex;flex-direction:column;justify-content:center"><div style="font-size:44px;font-weight:800;color:%s;line-height:1.15">%s</div><div style="font-size:38px;color:#475467;margin-top:8px;line-height:1.2;text-wrap:balance">%s</div></div></div>'%(y,col,a.replace(' ','<br>'),N,b,d)
    y+=224
c+='<div class="abs" style="left:50px;top:%dpx;width:900px;background:#fff7e6;border-left:8px solid #e0a21b;border-radius:8px;padding:20px 26px;font-size:42px;font-weight:700;color:#1d2433;line-height:1.25">Change one thing at a time.</div>'%y
gads_weeks_m=page(c,'',note='',size=(1000,y+190))
SC=dict(gads_targeting_m=gads_targeting_m,gads_search_m=gads_search_m,gads_weeks_m=gads_weeks_m)
if __name__=='__main__': render(sel(sys.argv,SC))
