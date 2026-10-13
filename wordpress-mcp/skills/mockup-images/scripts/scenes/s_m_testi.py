import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'; OR='#e0613a'; BL='#1b6ef3'
def P(v): return '%dpx'%v
def T(txt,x,y,sz,col=N,wt=800,w=None,extra=''):
    s='<div class="abs" style="left:'+P(x)+';top:'+P(y)+';font-size:'+P(sz)+';font-weight:'+str(wt)+';color:'+col+';line-height:1.2;'
    if w: s+='width:'+P(w)+';'
    return s+extra+'">'+txt+'</div>'
def dot(n,cx,cy,d=60):
    return '<div class="abs" style="left:'+P(cx-d//2)+';top:'+P(cy-d//2)+';width:'+P(d)+';height:'+P(d)+';border-radius:50%;background:'+OR+';color:#fff;font-size:40px;font-weight:800;line-height:1;display:flex;align-items:center;justify-content:center;box-shadow:0 3px 8px rgba(20,35,70,.3);z-index:3">'+str(n)+'</div>'
def bar(x,y,w,h=14,c='#dfe4ee'): return '<div class="abs deco" style="left:'+P(x)+';top:'+P(y)+';width:'+P(w)+';height:'+P(h)+';background:'+c+';border-radius:'+P(h//2)+'"></div>'
def title(t): return T(t,50,40,64,N,800,900)
def stars(x,y,sz=44): return '<div class="abs" style="left:'+P(x)+';top:'+P(y)+';font-size:'+P(sz)+';color:#e0a21b;letter-spacing:3px;line-height:1">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
def card(x,y,w,h,inner,extra=''):
    return '<div class="abs" style="left:'+P(x)+';top:'+P(y)+';width:'+P(w)+';height:'+P(h)+';background:#fff;border-radius:16px;box-shadow:0 8px 22px rgba(20,35,70,.16);'+extra+'">'+inner+'</div>'
def chip(txt,x,y,bg,col,sz=38):
    return '<div class="abs" style="left:'+P(x)+';top:'+P(y)+';background:'+bg+';color:'+col+';font-size:'+P(sz)+';font-weight:800;padding:6px 20px;border-radius:999px;line-height:1.2">'+txt+'</div>'

# 1. weak vs strong
t=title('Strong testimonials name three things')
y=240
w=stars(36,34)+chip('Weak',700,26,'#fdecea','#b42318')
w+=T('&ldquo;Great agent, highly recommend.&rdquo;',36,110,46,'#475467',500,830,'font-family:Lora,serif')
w+=T('&mdash; A client',36,172,38,'#667085',600)
w+='<div class="abs" style="left:36px;right:36px;top:236px;border-top:3px dashed #d0d5dd"></div>'
w+=T('No situation, no result, no name',36,262,40,'#b42318',700,830)
t+=card(50,y,900,340,w)
y2=y+340+50
HL=lambda c,s:'<span style="background:'+c+';padding:2px 6px;border-radius:6px;-webkit-box-decoration-break:clone;box-decoration-break:clone">'+s+'</span>'
s=stars(36,34)+chip('Strong',680,26,'#e6f6ee','#116b43')
s+=T('&ldquo;'+HL('#dbeafe','We were relocating from another state')+' &hellip; '+HL('#dcfce7','We made an offer before we flew home.')+'&rdquo;',36,106,44,'#1d2433',500,828,'font-family:Lora,serif;line-height:1.5')
s+=T('&mdash; '+HL('#fef3c7','Chris and Dana, Riverside'),36,330,40,N,700,830)
s+=chip('Situation',36,420,'#dbeafe','#1e40af')+chip('Result',250,420,'#dcfce7','#116b43')+chip('Person',420,420,'#fef3c7','#92400e')
t+=card(50,y2,900,510,s,'border:5px solid #1f8a5b')
testi_cards_m=page(t,'',note='',size=(1000,y2+510+50))

# 2. ask
t=title('Ask on closing day, in three steps')
PY=230; PH=600
t+='<div class="abs" style="left:50px;top:'+P(PY)+';width:900px;height:'+P(PH)+';background:#f2f4f7;border-radius:30px;box-shadow:0 10px 26px rgba(20,35,70,.18)"></div>'
t+='<div class="abs" style="left:50px;top:'+P(PY)+';width:900px;height:96px;background:#fff;border-radius:30px 30px 0 0;border-bottom:2px solid #e4e7ec"></div>'
t+='<div class="abs" style="left:80px;top:'+P(PY+20)+';width:56px;height:56px;border-radius:50%;background:#9fb4d6;color:'+N+';font-weight:800;font-size:38px;display:flex;align-items:center;justify-content:center">C</div>'+T('Chris',156,PY+24,42,'#1d2433',800)
def bub(y,txt,h,style='bg'):
    if style=='bg': return '<div class="abs" style="left:170px;top:'+P(y)+';width:740px;height:'+P(h)+';background:'+BL+';color:#fff;border-radius:28px 28px 28px 6px;padding:20px 26px;font-size:40px;line-height:1.25;font-weight:500">'+txt+'</div>'
    return '<div class="abs" style="left:170px;top:'+P(y)+';width:740px;height:'+P(h)+';background:#fff;color:'+BL+';border:3px solid '+BL+';border-radius:28px 28px 28px 6px;padding:18px 26px;font-size:40px;line-height:1.25;font-weight:700">'+txt+'</div>'
b1=PY+126; b2=b1+176; b3=b2+176
t+=bub(b1,'Hi Chris, congratulations again on your new home!',140)
t+=bub(b2,'A short note helps neighbors decide who to call.',140)
t+=bub(b3,'example.com/three-questions',90,'link')
t+=dot(1,110,b1+70)+dot(2,110,b2+70)+dot(3,110,b3+45)
y=PY+PH+50
for i,tx in enumerate(['Thank them first','Say in one sentence why it helps','Send a link, not a blank page']):
    t+=dot(i+1,80,y+32)+T(tx,140,y+6,44,N,700,800); y+=86
y+=20
t+='<div class="abs" style="left:50px;top:'+P(y)+';width:900px;background:#fff7e6;border-left:8px solid #e0a21b;border-radius:8px;padding:20px 28px;font-size:42px;line-height:1.25;color:#1d2433"><strong>Follow up once</strong>, a week later. Then stop.</div>'
testi_ask_m=page(t,'',note='',size=(1000,y+170))

# 3. site
FX,FY,FW=50,240,900
fr='<div class="abs deco" style="left:0;top:0;width:900px;height:56px;background:#e9edf3;border-radius:16px 16px 0 0"></div><div class="abs deco" style="left:22px;top:20px;width:16px;height:16px;border-radius:50%;background:#f87171"></div><div class="abs deco" style="left:48px;top:20px;width:16px;height:16px;border-radius:50%;background:#fbbf24"></div><div class="abs deco" style="left:74px;top:20px;width:16px;height:16px;border-radius:50%;background:#34d399"></div><div class="abs deco" style="left:110px;top:12px;width:420px;height:32px;background:#fff;border-radius:8px;font-size:22px;color:#667085;padding:3px 14px">example.com/dana-lee</div>'
fr+='<div class="abs deco" style="left:0;top:56px;width:900px;height:64px;border-bottom:2px solid #eef0f4"></div><div class="abs deco" style="left:80px;top:72px;font-size:28px;font-weight:800;color:'+N+'">Dana Lee</div>'+bar(560,86,90)+bar(670,86,70)+bar(760,86,80)
fr+=T('What clients say',80,150,50,N,800)
data=[('Maya, Cedar Hills',0),('Chris and Dana, Riverside',1)]
for nm,k in data:
    cy=232+k*186
    fr+='<div class="abs" style="left:80px;top:'+P(cy)+';width:770px;height:170px;background:#fff;border:2px solid #e4e7ec;border-radius:14px;box-shadow:0 2px 8px rgba(16,24,40,.06)"></div>'
    fr+='<div class="abs deco" style="left:104px;top:'+P(cy+16)+';font-size:30px;color:#e0a21b;letter-spacing:2px;line-height:1">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'+bar(104,cy+62,640)+bar(104,cy+88,520)
    fr+=T(nm,104,cy+112,40,N,800,720)
fr+='<div class="abs" style="left:80px;top:612px;width:770px;height:290px;background:#f5f7fb;border-radius:14px"></div>'
fr+=T('Talk to Dana',104,636,44,N,800)+bar(104,708,420,48,'#fff')+bar(104,772,420,48,'#fff')
fr+='<div class="abs" style="left:560px;top:708px;width:262px;height:112px;background:'+OR+';border-radius:12px;color:#fff;font-size:44px;font-weight:800;display:flex;align-items:center;justify-content:center">Send</div>'
fr+=bar(104,846,500,16,'#dfe4ee')
t=title('Put testimonials next to the form')
t+='<div class="abs sh" style="left:'+P(FX)+';top:'+P(FY)+';width:'+P(FW)+';height:930px;background:#fff;border-radius:16px">'+fr+'</div>'
def L(xa,xb,cy): return '<div class="abs" style="left:'+P(xa)+';top:'+P(cy-2)+';width:'+P(xb-xa)+';height:4px;background:'+OR+';z-index:2"></div><div class="abs" style="left:'+P(xa-7)+';top:'+P(cy-7)+';width:14px;height:14px;border-radius:50%;background:'+OR+';z-index:2"></div>'
c1=FY+232+85; c2=FY+232+112+25; c3=FY+612+145
t+=dot(1,FX+10,c1)+dot(2,FX+FW-10,c2)+L(FX+FW-380,FX+FW-40,c2)+dot(3,FX+10,c3)
y=FY+930+60
for i,tx in enumerate(['Two or three strong quotes','First name and area','Close to the contact form']):
    t+=dot(i+1,80,y+32)+T(tx,140,y+6,44,N,700,800); y+=86
testi_site_m=page(t,'',note='',size=(1000,y+30))
SC=dict(testi_cards_m=testi_cards_m,testi_ask_m=testi_ask_m,testi_site_m=testi_site_m)
if __name__=='__main__': render(sel(sys.argv,SC))
