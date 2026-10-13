import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'; OR='#e0613a'; TL='#14808a'
def P(v): return '%dpx'%v
def T(txt,x,y,sz,col=N,wt=800,w=None,extra=''):
    s='<div class="abs" style="left:'+P(x)+';top:'+P(y)+';font-size:'+P(sz)+';font-weight:'+str(wt)+';color:'+col+';line-height:1.2;'
    if w: s+='width:'+P(w)+';'
    return s+extra+'">'+txt+'</div>'
def title(t): return T(t,50,40,64,N,800,900)
def bar(x,y,w,h=14,c='#dfe4ee'): return '<div class="abs deco" style="left:'+P(x)+';top:'+P(y)+';width:'+P(w)+';height:'+P(h)+';background:'+c+';border-radius:'+P(h//2)+'"></div>'

# 1. pricing slide
SY=160; SH=900
s='<div class="abs" style="left:0;top:0;width:900px;height:150px;background:'+N+'"></div>'
s+=T('Pricing recommendation',40,22,50,'#fff',700,820,'font-family:Lora,serif')+T('418 Maple Lane &middot; Cedar Hills',40,92,38,'#b9c6e0',500,820)
s+=T('Three comparable sales',40,176,38,'#667085',600)
comps=[('412 Cedar Lane','$438,000'),('27 Birch Court','$421,500'),('905 Oak Avenue','$449,000')]
y=232
for a,p in comps:
    s+='<div class="abs" style="left:40px;top:'+P(y)+';width:820px;height:90px;background:#f5f8fc;border-radius:12px;border-left:8px solid '+TL+'"></div>'
    s+=T(a,70,y+22,42,'#1d2433',700)+T(p,500,y+18,48,N,800,330,'text-align:right')
    y+=104
y+=22
s+=T('Recommended list range',40,y,38,'#667085',600)
y+=64
BX,BW=40,820
s+='<div class="abs" style="left:'+P(BX)+';top:'+P(y)+';width:'+P(BW)+';height:24px;background:#e4e7ec;border-radius:12px"></div>'
s+='<div class="abs" style="left:'+P(BX+int(BW*0.38))+';top:'+P(y-4)+';width:'+P(int(BW*0.32))+';height:32px;background:'+TL+';border-radius:16px"></div>'
s+=T('$410,000',BX,y+44,38,'#667085',600)+T('$460,000',BX+BW-220,y+44,38,'#667085',600,220,'text-align:right')
y+=116
s+=T('$429,000 &ndash; $445,000',40,y,56,TL,800,820)
y+=96
t=title('Three sales set the range')
SH=y+SY-SY
t+='<div class="paper sh" style="left:50px;top:'+P(SY)+';width:900px;height:'+P(y)+';border-radius:12px">'+s+'</div>'
ny=SY+y+40
t+='<div class="abs" style="left:50px;top:'+P(ny)+';width:900px;background:#fff7e6;border-left:8px solid #e0a21b;border-radius:8px;padding:20px 28px;font-size:42px;line-height:1.28;color:#1d2433"><strong>What could move it:</strong> condition, timing, a new listing nearby.</div>'
lp_price_m=page(t,'',note='',size=(1000,ny+210))

# 2. marketing plan
t=title('Every step has a date')+T('Marketing plan for the Parks',50,124,40,'#667085',600)
ph=[('DAYS &minus;7 TO &minus;1','Before the launch',TL,'#f3f8fa',['Professional photos','Listing description, reviewed with you','Prep tips: declutter, repairs']),
    ('DAY 0','Launch day',OR,'#fdf3ee',['Live on the major portals','Yard sign and flyer box','Email to my buyer list']),
    ('DAYS 1&ndash;14','First two weeks',N,'#f1f3f9',['Open house, first weekend','Mailers and social posts','Weekly update call with you'])]
y=215; CH=[330,330,330]
rail_top=y+50
for i,(tag,ttl,c,bg,items) in enumerate(ph):
    h=CH[i]
    t+='<div class="abs" style="left:110px;top:'+P(y)+';width:840px;height:'+P(h)+';background:'+bg+';border-top:8px solid '+c+';border-radius:10px;box-shadow:0 4px 12px rgba(20,35,70,.1)"></div>'
    t+=T(tag,140,y+30,38,c,800,780,'letter-spacing:.06em')+T(ttl,140,y+80,48,N,800,780)
    for k,it in enumerate(items):
        t+=T('&bull; '+it,140,y+156+k*54,40,'#1d2433',500,790)
    t+='<div class="abs" style="left:50px;top:'+P(y+34)+';width:44px;height:44px;border-radius:50%;background:'+c+';border:6px solid #fff;box-shadow:0 2px 6px rgba(20,35,70,.25);z-index:3"></div>'
    y+=h+30
t+='<div class="abs" style="left:68px;top:'+P(rail_top)+';width:8px;height:'+P(2*(h+30))+';background:#c4cde0;border-radius:4px;z-index:2"></div>'
lp_plan_m=page(t,'',note='',size=(1000,y+10))

# 3. outline
titles=['Welcome and agenda','About you and your area','What the seller wants','Market snapshot','Comparable sales','Pricing recommendation','Marketing plan and timeline','Preparation and showing plan','Process from signing to closing','Terms and compensation','Results and testimonials','Next steps and questions']
t=title('Twelve slides, 45 minutes')
y=150
for i,tt in enumerate(titles):
    c=N if i<3 else TL if i<7 else OR if i<10 else N
    t+='<div class="abs" style="left:50px;top:'+P(y)+';width:900px;height:84px;background:#fff;border-radius:10px;box-shadow:0 3px 10px rgba(20,35,70,.1)"></div>'
    t+='<div class="abs" style="left:62px;top:'+P(y+10)+';width:112px;height:64px;background:#f5f8fc;border-top:8px solid '+c+';border-radius:6px;color:'+c+';font-size:44px;font-weight:800;display:flex;align-items:center;justify-content:center;line-height:1">'+str(i+1)+'</div>'
    t+=T(tt,196,y+20,42,N,700,740)
    y+=96
lp_outline_m=page(t,'',note='',size=(1000,y+30))
SC=dict(lp_price_m=lp_price_m,lp_plan_m=lp_plan_m,lp_outline_m=lp_outline_m)
if __name__=='__main__': render(sel(sys.argv,SC))
