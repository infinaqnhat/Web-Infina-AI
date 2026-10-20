import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'; OR='#e0613a'
def P(v): return '%dpx'%v
def T(txt,x,y,sz,col=N,wt=800,w=None,extra=''):
    s='<div class="abs" style="left:'+P(x)+';top:'+P(y)+';font-size:'+P(sz)+';font-weight:'+str(wt)+';color:'+col+';line-height:1.15;'
    if w: s+='width:'+P(w)+';'
    return s+extra+'">'+txt+'</div>'
def dot(n,cx,cy,d=60):
    return '<div class="abs" style="left:'+P(cx-d//2)+';top:'+P(cy-d//2)+';width:'+P(d)+';height:'+P(d)+';border-radius:50%;background:'+OR+';color:#fff;font-size:40px;font-weight:800;line-height:1;display:flex;align-items:center;justify-content:center;box-shadow:0 3px 8px rgba(20,35,70,.3)">'+str(n)+'</div>'
def bar(x,y,w,h=14,c='#dfe4ee'): return '<div class="abs" style="left:'+P(x)+';top:'+P(y)+';width:'+P(w)+';height:'+P(h)+';background:'+c+';border-radius:'+P(h//2)+'"></div>'
def ph(x,y,w,h,name,r=6,pos='center'): return '<div class="photo abs" style="left:'+P(x)+';top:'+P(y)+';width:'+P(w)+';height:'+P(h)+';border-radius:'+P(r)+';background-image:url('+name+'.jpg);background-position:'+pos+'"></div>'
def paper(x,y,w,h,inner,extra=''):
    return '<div class="paper sh deco" style="left:'+P(x)+';top:'+P(y)+';width:'+P(w)+';height:'+P(h)+';'+extra+'">'+inner+'</div>'
def foot(w,h=44,fs=18):
    return '<div class="abs" style="left:0;bottom:0;width:'+P(w)+';height:'+P(h)+';background:'+N+';color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 14px;font-size:'+P(fs)+';font-weight:600"><span>Dana Lee &middot; Cedar Hills Realty</span><span>555-0142</span></div>'
def title(t): return T(t,50,40,64,N,800,900)

# 1. four layouts (flyer 400x518, 8.5x11)
W,H=400,518
def lab(x,y,a,b): return T(a,x,y,42,N,800,W,'text-align:center')+T(b,x,y+54,38,'#667085',600,W,'text-align:center')
f1=ph(0,0,W,262,'ph_house')+T('418 Maple Lane',16,278,30,N,700,W-32,'font-family:Lora,serif')+T('3 bed &middot; 2 bath &middot; 1,850 sq ft',16,322,18,'#667085',500)+bar(16,360,300)+bar(16,384,240)+bar(16,408,280)+foot(W)
f2=ph(0,0,150,H-44,'ph_house',0,'30% center')+T('OPEN HOUSE',166,22,16,OR,800)+T('Saturday<br>1&ndash;3 pm',166,50,32,N,700,220,'font-family:Lora,serif')+bar(166,150,210)+bar(166,174,170)+bar(166,198,190)+'<div class="abs" style="left:166px;top:250px">'+qr2(110)+'</div>'+bar(166,372,200,12)+foot(W)
f3=T('What is your home worth today?',22,26,36,N,700,W-44,'font-family:Lora,serif')+bar(22,118,300)+bar(22,142,230)+ph(22,190,W-44,150,'ph_aerial')+'<div class="abs" style="left:22px;top:366px">'+qr2(90)+'</div>'+bar(134,384,200,16)+bar(134,414,150,14)+foot(W)
f4=ph(0,0,W,210,'ph_house',0)+ph(0,214,130,100,'ph_living',0)+ph(134,214,132,100,'ph_kitchen',0)+ph(270,214,130,100,'ph_aerial',0)+T('Just listed: 418 Maple Lane',16,330,24,N,700,W-32,'font-family:Lora,serif')+bar(16,376,330)+bar(16,400,280)+bar(16,424,300)+foot(W)
XS=[50,550]; Y0=190; PIT=656
t=title('Four layouts to reuse')+T('Same structure, new photo each time',50,118,38,'#667085',600,900)
for i,(inner,a,b) in enumerate([(f1,'Photo on top','For listings'),(f2,'Photo left','For events, just sold'),(f3,'Big headline','For seller flyers'),(f4,'Four-photo grid','For strong interiors')]):
    x=XS[i%2]; y=Y0+(i//2)*PIT
    t+=paper(x,y,W,H,inner)+lab(x,y+H+14,a,b)
fly_layouts_m=page(t,'',note='',size=(1000,1500))

# 2. anatomy
FX,FY,FW,FH=240,150,520,673
fl=ph(24,100,FW-48,250,'ph_house')
fl+=T('Open house Sunday:<br>418 Maple Lane',24,20,34,N,700,FW-48,'font-family:Lora,serif')
fl+=T('3 bed &middot; 2 bath &middot; 1,850 sq ft',24,368,22,N,800)+bar(24,410,380)+bar(24,436,300)
fl+='<div class="abs" style="left:24px;top:480px;width:'+P(FW-48)+';height:80px;background:'+OR+';border-radius:8px"></div>'+T('Sun 1&ndash;3 pm',44,498,26,'#fff',800)+'<div class="abs" style="right:40px;top:488px;background:#fff;padding:4px;border-radius:4px">'+qr2(64)+'</div>'
fl+='<div class="abs" style="left:0;bottom:0;width:'+P(FW)+';height:100px;background:'+N+'"></div><div class="abs" style="left:24px;top:'+P(FH-84)+';width:68px;height:68px;border-radius:50%;background:#9fb4d6;color:'+N+';font-weight:800;font-size:26px;display:flex;align-items:center;justify-content:center">DL</div>'
fl+='<div class="abs" style="left:104px;top:'+P(FH-76)+';width:52px;height:52px;border-radius:10px;border:2px solid #9fb4d6;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:18px">CH</div>'
fl+=T('Dana Lee, Realtor',176,FH-80,22,'#fff',800)+T('Cedar Hills Realty &middot; 555-0142',176,FH-50,17,'#b9c6e0',500)
t=title('Six parts of a listing flyer')+paper(FX,FY,FW,FH,fl)
def lead(side,n,cy,tx):
    cx=FX-60 if side=='L' else FX+FW+60
    x1=cx+30 if side=='L' else tx
    x2=tx if side=='L' else cx-30
    return '<div class="abs" style="left:'+P(x1)+';top:'+P(cy-2)+';width:'+P(x2-x1)+';height:4px;background:'+OR+'"></div><div class="abs" style="left:'+P(tx-7)+';top:'+P(cy-7)+';width:14px;height:14px;border-radius:50%;background:'+OR+'"></div>'+dot(n,cx,cy)
t+=lead('L',1,FY+60,FX+12)+lead('L',2,FY+225,FX+34)+lead('L',3,FY+380,FX+12)+lead('R',4,FY+520,FX+FW-16)+lead('R',5,FY+FH-50,FX+FW-16)+lead('L',6,FY+FH-50,FX+12)
items=['Headline names the point','One strong photo','Three to five facts','One call to action','Name, brokerage, required details','Headshot and logo']
y=FY+FH+60
for i,s in enumerate(items):
    t+=dot(i+1,80,y+30)+T(s,130,y+6,42,N,700,820)
    y+=82
fly_anno_m=page(t,'',note='',size=(1000,y+30))

# 3. crowded vs clean
starb='clip-path:polygon(50% 0,61% 14%,79% 6%,80% 25%,98% 30%,86% 46%,100% 62%,81% 68%,82% 88%,62% 82%,50% 100%,38% 82%,19% 88%,20% 68%,0 62%,14% 46%,2% 30%,20% 25%,21% 6%,39% 14%)'
crowd='<div class="abs" style="left:0;top:0;width:'+P(W)+';height:'+P(H)+';background:#fff7d6"></div>'
crowd+='<div class="abs" style="right:-14px;top:-10px;width:120px;height:120px;background:#d62828;transform:rotate(14deg);'+starb+';color:#fff;font-weight:800;font-size:16px;display:flex;align-items:center;justify-content:center">SALE!!!</div>'
crowd+='<div class="abs" style="left:12px;top:12px;font:800 28px Impact,\'Liberation Sans\';color:#d62828">LOOK!! AMAZING!!!</div><div class="abs" style="left:12px;top:50px;font:italic 700 16px \'Liberation Serif\';color:#0b5394">Dream house in the BEST neighborhood</div>'
for k,nm in enumerate(['ph_house','ph_living','ph_kitchen','ph_aerial','ph_condo','ph_house']):
    crowd+=ph(12+(k%3)*128,80+(k//3)*60,124,56,nm,0)
crowd+='<div class="abs" style="left:12px;top:208px;width:376px;font:700 14px \'Liberation Mono\';color:#38761d;line-height:1.35">3 BED! 2 BATH! GRANITE! HARDWOOD! NEW ROOF! BIG YARD! CLOSE TO SCHOOLS! SHOPPING! PARKS! GREAT VALUE! MUST SEE! WON\'T LAST! CALL TODAY!</div>'
crowd+='<div class="abs" style="left:12px;top:296px;font:800 22px \'Liberation Sans\';color:#7f6000">ONLY $439,000 (NEGOTIABLE)</div><div class="abs" style="left:12px;top:330px;width:376px;font:600 13px \'Liberation Serif\';color:#222;line-height:1.4">Call 555-0142 or 555-0187 or text 555-0119 or email dana@example.com or visit www.example.com/dana or follow us on every social site. Open house Sat, Sun, or by appointment. Ask about financing, staging, free value review, buyer guide, seller guide, and our newsletter!</div>'
crowd+='<div class="abs" style="left:0;bottom:0;width:'+P(W)+';height:28px;background:#6a1b9a;color:#fff;font:700 11px \'Liberation Sans\';display:flex;align-items:center;justify-content:center">Dana Lee &middot; Cedar Hills Realty &middot; Team Dana &middot; Top Producer</div>'
clean=T('Open house Sunday:<br>418 Maple Lane',22,20,34,N,700,W-44,'font-family:Lora,serif')+ph(22,110,W-44,176,'ph_house')+T('3 bed &middot; 2 bath &middot; 1,850 sq ft',22,300,22,N,800)+bar(22,336,260)+'<div class="abs" style="left:22px;top:366px">'+qr2(74)+'</div>'+bar(112,380,200,16)+bar(112,408,150,14)+foot(W,46)
t=title('A clean flyer gets read')
Y=170
t+=paper(50,Y,W,H,crowd)+paper(550,Y,W,H,clean,'border:6px solid #1f8a5b')
t+='<div class="abs" style="left:462px;top:'+P(Y+H//2-38)+';width:76px;height:76px;border-radius:50%;background:'+N+';color:#fff;font-weight:800;font-size:40px;display:flex;align-items:center;justify-content:center;z-index:5">VS</div>'
t+=T('Crowded',50,Y+H+16,48,'#c2410c',800,W,'text-align:center')+T('Five reasons to do nothing',50,Y+H+74,38,'#667085',600,W,'text-align:center')
t+=T('Clean',550,Y+H+16,48,'#1f8a5b',800,W,'text-align:center')+T('One job, one photo, one action',550,Y+H+74,38,'#667085',600,W,'text-align:center')
fly_vs_m=page(t,'',note='',size=(1000,Y+H+210))
SC=dict(fly_layouts_m=fly_layouts_m,fly_anno_m=fly_anno_m,fly_vs_m=fly_vs_m)
if __name__=='__main__': render(sel(sys.argv,SC))
