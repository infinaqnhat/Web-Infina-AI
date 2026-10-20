import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
# Mobile-first prototype: canvas 1000x1200, no tiny text. Smallest text 38px => 12.9px on a 340px-wide phone image.
CH=[('Sphere and referrals','#14808a',30,20),('Print and branding','#1b2a4a',25,10),('Social media','#e0a21b',15,10),('Website and local SEO','#7c5cc4',10,20),('Direct mail','#e0613a',0,20),('Paid ads','#c2410c',0,15),('Test reserve','#98a2b3',20,5)]
h='<div class="abs" style="left:50px;top:40px;font-size:64px;font-weight:800;color:'+N+';line-height:1.1">Where the budget goes</div>'
h+='<div class="abs" style="left:50px;top:130px;display:flex;gap:30px;font-size:40px;font-weight:700"><span style="color:#14808a">&#9632; New agent<br><small style="font-weight:600;color:#667085;font-size:38px">$500 a month</small></span><span style="color:#1b2a4a">&#9632; Growing agent<br><small style="font-weight:600;color:#667085;font-size:38px">$1,500 a month</small></span></div>'
y=290
for name,col,a,b in CH:
    h+='<div class="abs" style="left:50px;top:%dpx;font-size:42px;font-weight:700;color:#1d2433">%s</div>'%(y,name)
    for k,(v,c) in enumerate([(a,'#14808a'),(b,'#1b2a4a')]):
        w=int(v*18)
        h+='<div class="abs" style="left:50px;top:%dpx;width:%dpx;height:%dpx;background:%s;border-radius:6px"></div><div class="abs" style="left:%dpx;top:%dpx;font-size:38px;font-weight:800;color:%s">%d%%</div>'%(y+60+k*44,max(w,6),30,c,60+max(w,6),y+53+k*44,c,v)
    y+=150
mobile_budget=page(h,'',note='',size=(1000,1400))
# annotated flyer
fl=('<div class="paper sh" style="left:50px;top:60px;width:380px;height:560px"><div class="photo" style="position:absolute;left:0;top:0;right:0;height:60px;background:#fff"></div>'
 '<div class="serif" style="position:absolute;left:22px;right:22px;top:20px;font-size:28px;font-weight:700;color:#1b2a4a;line-height:1.1">Open house Sunday: 418 Maple Lane</div>'
 '<div class="photo" style="position:absolute;left:22px;right:22px;top:100px;height:200px;border-radius:6px;background-image:url(ph_house.jpg)"></div>'
 '<div style="position:absolute;left:22px;right:22px;top:318px;height:60px"><div style="height:12px;background:#e4e7ec;border-radius:6px;width:80%;margin-bottom:12px"></div><div style="height:12px;background:#e4e7ec;border-radius:6px;width:60%;margin-bottom:12px"></div><div style="height:12px;background:#e4e7ec;border-radius:6px;width:70%"></div></div>'
 '<div style="position:absolute;left:22px;right:22px;top:410px;height:60px;background:#e0613a;border-radius:8px"></div>'
 '<div style="position:absolute;left:0;right:0;bottom:0;height:80px;background:#1b2a4a"></div></div>')
pins=''.join('<div class="num" style="left:%dpx;top:%dpx;width:46px;height:46px;font-size:26px;font-weight:800">%d</div>'%(x,y,n) for n,(x,y) in enumerate([(30,36),(30,178),(30,336),(30,432),(30,590),(380,590)],1))
legend=''
for i,t in enumerate(['Headline','One strong photo','3 to 5 facts','One action','Name and details','Headshot and logo']):
    legend+='<div class="abs" style="left:490px;top:%dpx;display:flex;gap:18px;align-items:center;font-size:48px;font-weight:700;color:%s"><b style="flex:none;width:58px;height:58px;border-radius:50%%;background:#e0613a;color:#fff;display:flex;align-items:center;justify-content:center;font-size:34px">%d</b>%s</div>'%(90+i*98,N,i+1,t)
mobile_flyer=page(fl+pins+legend,'',note='',size=(1000,720))
SC=dict(mobile_budget=mobile_budget,mobile_flyer=mobile_flyer)
if __name__=='__main__': render(sel(sys.argv,SC))
