import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
def title(t,sz=64): return '<div class="abs" style="left:50px;top:40px;width:900px;font-size:%dpx;font-weight:800;color:%s;line-height:1.1">%s</div>'%(sz,N,t)
def dot(n): return '<div style="width:60px;height:60px;border-radius:50%%;background:#e0613a;color:#fff;font-size:40px;font-weight:800;display:flex;align-items:center;justify-content:center;flex:none">%d</div>'%n
# 1. four ads, stacked, each with a numbered goal label
def head(y,n,goal,kind):
    return '<div class="abs" style="left:50px;top:%dpx;width:900px;height:60px;display:flex;align-items:center;gap:20px">%s<div style="font-size:44px;font-weight:800;color:%s">%s</div><div style="margin-left:auto;font-size:38px;color:#667085;font-weight:600">%s</div></div>'%(y,dot(n),N,goal,kind)
def chip(t,bg,fg='#fff'): return '<span style="display:inline-block;background:%s;color:%s;border-radius:10px;padding:8px 22px;font-size:38px;font-weight:800">%s</span>'%(bg,fg,t)
def search(y):
    return ('<div class="paper sh" style="left:50px;top:%dpx;width:900px;height:240px;border-radius:14px;padding:22px 30px">'%y
     +'<div class="deco" style="font-size:26px;color:#667085;font-weight:700"><span style="border:2px solid #98a2b3;border-radius:5px;padding:0 8px;margin-right:10px">Ad</span>example.com/home-value</div>'
     +'<div style="font-size:42px;color:#1a56db;font-weight:700;line-height:1.2;margin-top:10px">What could your home sell for today?</div>'
     +'<div style="margin-top:14px;display:flex;align-items:center;justify-content:space-between"><span style="font-size:38px;color:#475467">Free home value review.</span>'+chip('Request a review','#1a56db')+'</div></div>')
def social(y,img,headline,cta):
    return ('<div class="paper sh" style="left:50px;top:%dpx;width:900px;height:240px;border-radius:14px"><div class="photo" style="position:absolute;left:0;top:0;width:230px;height:240px;background-image:url(%s.jpg)"></div>'%(y,img)
     +'<div style="position:absolute;left:256px;right:24px;top:20px"><div class="deco" style="font-size:26px;color:#667085">Sponsored</div><div style="font-size:42px;font-weight:800;color:'+N+';line-height:1.2;margin-top:2px">'+headline+'</div><div style="margin-top:12px">'+chip(cta,'#e0613a')+'</div></div></div>')
t=title('Four ads you can adapt')
y=150
t+=head(y,1,'Win sellers','Search ad')+search(y+80); y+=80+240+34
t+=head(y,2,'Win first-time buyers','Social ad')+social(y+80,'ph_living','Buying your first home? Start with the real costs.','Download'); y+=80+240+34
t+=head(y,3,'Show local results','Social ad')+social(y+80,'ph_house','Just sold on Maple Street in 12 days','Send message'); y+=80+240+34
t+=head(y,4,'Promote a listing','Social ad')+social(y+80,'ph_condo','Open house this Saturday, 1&nbsp;to&nbsp;3&nbsp;p.m.','Get directions'); y+=80+240+34
t+='<div class="abs" style="left:50px;top:%dpx;width:900px;background:#fff7e6;border-left:8px solid #e0a21b;border-radius:8px;padding:20px 28px;font-size:42px;color:#1d2433;line-height:1.3"><strong>One audience, one offer, one action.</strong> No claims you cannot prove.</div>'%y
adv_examples_m=page(t,'',note='',size=(1000,y+170))
# 2. funnel: spend to one closing
ST=[('$900','Ad spend, 30 days','#475467',900),('30','Leads','#14808a',780),('6','Appointments','#1b2a4a',660),('2','Signed clients','#7c5cc4',540),('1','Closing','#e0613a',420)]
LINK=['Cost per lead: $30','Lead to appointment: 20%','Appointment to client: 33%','']
f=title('Ad spend to one closing')
y=160
for i,(big,lab,c,w) in enumerate(ST):
    x=50+(900-w)//2
    f+='<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:110px;background:%s;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.18);display:flex;align-items:center;gap:20px;padding:0 28px;color:#fff"><span style="font-size:56px;font-weight:800">%s</span><span style="font-size:42px;font-weight:700">%s</span></div>'%(x,y,w,c,big,lab)
    y+=110
    if i<4:
        f+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:70px;text-align:center;font-size:40px;font-weight:700;color:#475467;line-height:70px"><span style="color:#98a2b3">&darr;</span> %s</div>'%(y,LINK[i])
        y+=70
y+=24
f+='<div class="abs" style="left:50px;top:%dpx;width:900px;text-align:center;font-size:52px;font-weight:800;color:#e0613a">Cost per closing: $900</div>'%y
y+=100
f+='<div class="abs" style="left:50px;top:%dpx;width:900px;background:#fff7e6;border-left:8px solid #e0a21b;border-radius:8px;padding:20px 28px;font-size:42px;color:#1d2433;line-height:1.3">A $30 lead sounds cheap. <strong>The $900 closing tells you if the channel is worth keeping.</strong></div>'%y
y+=230
adv_metrics_m=page(f,'',note='',size=(1000,y))
# 3. 30-day test
S=[('Pick one offer','Home value review or buyer guide'),('Start with a small budget','An amount you can afford to lose'),('Define success first','20 leads, 8 conversations, 2 appointments'),('Track the source','Tag every lead with its ad'),('Review at 30 and 90 days','Change one thing at a time')]
c=title('Test one offer in 30 days')
y=150
for i,(k,d) in enumerate(S):
    hh=205 if len(d)>36 else 150
    c+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12)"><div style="position:absolute;left:26px;top:36px">%s</div><div style="position:absolute;left:120px;right:20px;top:20px"><div style="font-size:44px;font-weight:800;color:%s;line-height:1.15">%s</div><div style="font-size:38px;color:#475467;margin-top:8px;line-height:1.2">%s</div></div></div>'%(y,hh,dot(i+1),N,k,d)
    y+=hh+20
y+=30
c+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:16px;background:#d6dce8;border-radius:8px"></div><div class="abs" style="left:50px;top:%dpx;width:300px;height:16px;background:#14808a;border-radius:8px"></div>'%(y,y)
c+='<div class="abs" style="left:50px;top:%dpx;font-size:40px;font-weight:700;color:#14808a">Day 1</div><div class="abs" style="left:250px;top:%dpx;font-size:40px;font-weight:700;color:#14808a;width:420px;text-align:center">Day 30: review</div><div class="abs" style="right:50px;top:%dpx;font-size:40px;font-weight:700;color:#667085">Day 90</div>'%(y+34,y+34,y+34)
y+=110
adv_test_m=page(c,'',note='',size=(1000,y+30))
SC=dict(adv_examples_m=adv_examples_m,adv_metrics_m=adv_metrics_m,adv_test_m=adv_test_m)
if __name__=='__main__': render(sel(sys.argv,SC))
