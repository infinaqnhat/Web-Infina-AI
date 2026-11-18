import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'; OR='#e0613a'; RED='#d62828'
def title(t,top=40): return '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:64px;font-weight:800;color:%s;line-height:1.1">%s</div>'%(top,N,t)
def dot(n,x,y,s=56):
    return '<div style="position:absolute;left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:50%%;background:%s;color:#fff;display:flex;align-items:center;justify-content:center;font-size:40px;font-weight:800;box-shadow:0 3px 8px rgba(0,0,0,.3)">%d</div>'%(x,y,s,s,OR,n)
def row(n,text,y):
    return dot(n,50,y)+'<div class="abs" style="left:132px;top:%dpx;width:830px;height:56px;display:flex;align-items:center;font-size:42px;font-weight:700;color:%s;white-space:nowrap">%s</div>'%(y,N,text)
def bar(w,h=14,c='#d9dfea',m=10): return '<div style="width:%dpx;height:%dpx;background:%s;border-radius:7px;margin-top:%dpx"></div>'%(w,h,c,m)
def lab(y,text): return '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:44px;font-weight:800;color:%s">%s</div>'%(y,N,text)
W,H=760,507
# 1. front and back
front='<div class="paper sh" style="left:120px;top:225px;width:%dpx;height:%dpx;border-radius:8px"><div class="photo" style="position:absolute;inset:0;background-image:url(ph_house.jpg)"></div><div style="position:absolute;left:0;right:0;bottom:0;height:260px;background:linear-gradient(0deg,rgba(14,28,56,.92),rgba(14,28,56,0))"></div><div style="position:absolute;left:0;top:30px;background:%s;color:#fff;font-weight:800;font-size:40px;letter-spacing:.1em;padding:8px 28px">JUST SOLD</div><div class="serif" style="position:absolute;left:34px;bottom:78px;color:#fff;font-size:52px;font-weight:700;line-height:1.1">Just sold on Cedar Lane</div><div style="position:absolute;left:34px;bottom:26px;color:#e6edfb;font-size:42px;font-weight:600">14 days on market</div></div>'%(W,H,RED)
back='<div class="paper sh" style="left:120px;top:865px;width:%dpx;height:%dpx;border-radius:8px">'%(W,H)
back+='<div style="position:absolute;left:32px;top:30px;width:430px" class="serif"><div style="font-size:42px;font-weight:700;color:%s;line-height:1.2">See what homes near you are selling for.</div></div>'%N
back+='<div style="position:absolute;left:32px;top:200px;background:%s;color:#fff;font-size:42px;font-weight:800;padding:10px 26px;border-radius:10px">Free value review</div>'%RED
back+='<div style="position:absolute;left:32px;bottom:30px;display:flex;gap:20px;align-items:flex-end"><div style="background:#fff;border:2px solid #e4e7ec;padding:8px">'+qr2(140)+'</div><div class="deco" style="font-size:24px;line-height:1.4;color:%s;font-weight:700">Dana Lee<br><span style="font-weight:500;color:#475467">Cedar Hills Realty<br>555-0142</span></div></div>'%N
back+='<div class="deco" style="position:absolute;right:26px;top:26px;width:150px;height:110px;border:2px solid #cbd2e0;display:flex;align-items:center;justify-content:center;text-align:center;font-size:22px;color:#667085;line-height:1.3">Postage<br>area</div>'
back+='<div class="deco" style="position:absolute;right:30px;bottom:34px;width:200px;font-size:22px;line-height:1.5;color:#1d2433;border-top:2px solid #e4e7ec;padding-top:10px">Local Postal Customer<br>Cedar Hills</div></div>'
t=title('Just sold: front and back')+lab(150,'Front: one photo, one headline')+front+lab(790,'Back: one offer, one way to reply')+back
post_just_sold_m=page(t,'',note='',size=(1000,865+H+50))
# 2. annotated
CX,CY,CW,CH=80,160,840,560
c='<div class="paper sh" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:10px">'%(CX,CY,CW,CH)
c+='<div class="photo" style="position:absolute;left:0;top:0;right:0;height:335px;background-image:url(ph_house.jpg)"></div><div style="position:absolute;left:0;right:0;top:175px;height:160px;background:linear-gradient(0deg,rgba(14,28,56,.92),rgba(14,28,56,0))"></div>'
c+='<div style="position:absolute;left:0;top:26px;background:%s;color:#fff;font-weight:800;font-size:38px;letter-spacing:.1em;padding:6px 26px">JUST SOLD</div>'%RED
c+='<div class="serif" style="position:absolute;left:30px;top:226px;color:#fff;font-size:46px;font-weight:700;line-height:1.1">Just sold on Cedar Lane</div><div style="position:absolute;left:30px;top:284px;color:#e6edfb;font-size:38px;font-weight:600">14 days on market</div>'
c+='<div style="position:absolute;left:30px;top:362px;background:%s;color:#fff;font-size:42px;font-weight:800;padding:10px 26px;border-radius:10px">Free value review</div>'%RED
c+='<div style="position:absolute;left:30px;top:456px">'+bar(300,14,'#d9dfea',0)+bar(220,14,'#d9dfea',10)+'</div>'
c+='<div style="position:absolute;right:30px;top:352px;background:#fff;border:2px solid #e4e7ec;padding:8px">'+qr2(160)+'</div>'
c+='<div class="deco" style="position:absolute;left:30px;bottom:14px;font-size:26px;color:#475467;white-space:nowrap">Dana Lee &middot; Cedar Hills Realty &middot; 555-0142</div></div>'
pins=dot(1,CX+590,CY+214)+dot(2,CX+750,CY+20)+dot(3,CX+450,CY+358)+dot(4,CX+596,CY+312)+dot(5,CX+560,CY+490)
t=title('Parts of a just-sold card')+c+pins
y=CY+CH+50
for i,s in enumerate(['Headline: what, where, how fast','One strong photo of a nearby home','One offer, not three','One way to respond: call or scan','Your name and brokerage']):
    t+=row(i+1,s,y+i*104)
post_anno_m=page(t,'',note='',size=(1000,y+5*104+30))
# 3. qr tracking
m='<div class="paper sh" style="left:80px;top:160px;width:840px;height:560px;border-radius:10px">'
m+='<div style="background:%s;height:140px;padding:36px 36px"><div class="serif" style="font-size:56px;font-weight:700;color:#fff;line-height:1.1">Market update</div></div>'%N
m+='<div style="position:absolute;left:36px;top:180px;width:420px"><div style="font-size:46px;font-weight:800;color:%s;line-height:1.2">Scan for the full report</div>'%N+bar(300,14,'#d9dfea',28)+bar(220,14,'#d9dfea',12)+'</div>'
m+='<div style="position:absolute;right:36px;top:176px;background:#fff;border:2px solid #e4e7ec;padding:10px">'+qr2(250)+'</div>'
m+='<div class="deco" style="position:absolute;left:36px;bottom:22px;font-size:26px;color:#475467;white-space:nowrap">Dana Lee &middot; Cedar Hills Realty &middot; 555-0142</div></div>'
rows=[('Just sold, Cedar Lane','example.com/js-01',12),('Market update','example.com/mu-02',31),('Seasonal checklist','example.com/se-03',9)]
T=760
tb='<div class="paper sh" style="left:50px;top:%dpx;width:900px;height:%dpx;border-radius:14px"></div>'%(T,100+3*130)
tb+='<div class="abs" style="left:84px;top:%dpx;font-size:44px;font-weight:800;color:%s">Scans per mailing</div>'%(T+26,N)
for i,(a,l,v) in enumerate(rows):
    y=T+100+i*130
    tb+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:2px;background:#e4e7ec"></div>'%y
    tb+='<div class="abs" style="left:84px;top:%dpx"><div style="font-size:42px;font-weight:700;color:#1d2433">%s</div><div style="font-size:38px;color:#14808a;font-weight:600;margin-top:4px">%s</div></div>'%(y+20,a,l)
    tb+='<div class="abs" style="right:84px;top:%dpx;font-size:56px;font-weight:800;color:%s">%d</div>'%(y+30,N,v)
t=title('One QR code per mailing')+m+tb
t+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:44px;font-weight:600;color:%s">Compare cards instead of guessing.</div>'%(T+100+390+36,N)
post_qr_m=page(t,'',note='',size=(1000,T+100+390+36+100))
SC=dict(post_just_sold_m=post_just_sold_m,post_anno_m=post_anno_m,post_qr_m=post_qr_m)
if __name__=='__main__': render(sel(sys.argv,SC))
