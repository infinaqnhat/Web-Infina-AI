import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'; TL='#14808a'
def title(t,top=40): return '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:64px;font-weight:800;color:%s;line-height:1.1">%s</div>'%(top,N,t)
DOOR='<svg width="%d" height="%d" viewBox="0 0 64 76"><path d="M4 76V28Q4 4 32 4Q60 4 60 28V76Z" fill="%s"/><path d="M20 76V36Q20 20 32 20Q44 20 44 36V76Z" fill="%s"/></svg>'
def lg(w,fg=TL,tx=N,hole='#fff',ac=TL):
    s=w/360.0
    return '<div class="deco" style="display:flex;align-items:center;gap:%dpx"><div style="flex:none">'%int(14*s)+DOOR%(int(64*s),int(76*s),fg,hole)+'</div><div><div class="serif" style="font-size:%dpx;font-weight:700;color:%s;line-height:1;white-space:nowrap">Cedar &amp; Stone</div><div style="font-size:%dpx;letter-spacing:.3em;color:%s;margin-top:%dpx;font-weight:700">REALTY</div></div></div>'%(max(int(34*s),8),tx,max(int(13*s),5),ac,max(int(6*s),2))
# 1. five types
word='<div class="serif deco" style="font-size:44px;font-weight:700;color:%s;text-align:center;line-height:1.1">Harper<br>Group</div>'%N
mono='<div class="deco" style="width:130px;height:130px;border-radius:50%%;background:%s;color:#fff;display:flex;align-items:center;justify-content:center"><span class="serif" style="font-size:54px;font-weight:700">DL</span></div>'%N
emb='<div class="deco"><svg width="170" height="170" viewBox="0 0 190 190"><defs><path id="ca" d="M30 95a65 65 0 0 1 130 0"/><path id="cb" d="M22 100a73 73 0 0 0 146 0" /></defs><circle cx="95" cy="95" r="90" fill="none" stroke="#1b2a4a" stroke-width="5"/><circle cx="95" cy="95" r="62" fill="none" stroke="#b88a2e" stroke-width="2"/><text font-family="Lora" font-weight="700" font-size="15" fill="#1b2a4a" letter-spacing="3"><textPath href="#ca" startOffset="50%" text-anchor="middle">PARK REALTY</textPath></text><text font-family="Lora" font-weight="700" font-size="14" fill="#1b2a4a" letter-spacing="3"><textPath href="#cb" startOffset="50%" text-anchor="middle">EST. 2017</textPath></text><text x="95" y="112" text-anchor="middle" font-family="Lora" font-weight="700" font-size="52" fill="#1b2a4a">P</text></svg></div>'
head='<div class="deco" style="display:flex;align-items:center;gap:14px"><svg width="96" height="96" viewBox="0 0 104 104"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#14808a"/><stop offset="1" stop-color="#1b2a4a"/></linearGradient></defs><circle cx="52" cy="52" r="50" fill="url(#g)"/><circle cx="52" cy="40" r="17" fill="#e7eefc"/><path d="M18 92Q20 62 52 62Q84 62 86 92Q70 102 52 102Q34 102 18 92Z" fill="#e7eefc"/></svg><div class="serif" style="font-size:34px;font-weight:700;color:%s;line-height:1.1">Dana<br>Lee</div></div>'%N
types=[('Wordmark','Simple, clear, works everywhere',word),('Monogram','Compact, good for profile pictures',mono),('Symbol + wordmark','Memorable once the icon is known',lg(300)),('Emblem or badge','Feels established; detail can vanish small',emb),('Headshot-based','Personal; hard to print in one color',head)]
t=title('Pick one of five logo types')
for i,(n,s,l) in enumerate(types):
    y=160+i*215
    t+='<div class="paper sh" style="left:50px;top:%dpx;width:360px;height:190px;border-radius:12px;display:flex;align-items:center;justify-content:center">%s</div>'%(y,l)
    t+='<div class="abs" style="left:445px;top:%dpx;width:505px;height:190px;display:flex;flex-direction:column;justify-content:center"><div style="font-size:44px;font-weight:800;color:%s;line-height:1.15">%s</div><div style="font-size:38px;color:#475467;margin-top:6px;line-height:1.2">%s</div></div>'%(y,N,n,s)
logo_types_m=page(t,'',note='',size=(1000,160+5*215+10))
# 2. small and one color
ICON=DOOR%(56,66,TL,'#fff')
def rowlab(y,h,txt): return '<div class="abs" style="left:520px;top:%dpx;width:400px;height:%dpx;display:flex;align-items:center;font-size:42px;font-weight:800;color:%s;line-height:1.15">%s</div>'%(y,h,N,txt)
c1='<div class="paper sh" style="left:50px;top:160px;width:900px;height:430px;border-radius:14px"></div>'
c1+='<div class="abs" style="left:90px;top:160px;height:150px;display:flex;align-items:center">'+lg(380)+'</div>'+rowlab(160,150,'Full size')
c1+='<div class="abs" style="left:50px;top:310px;width:900px;height:2px;background:#e4e7ec"></div>'
c1+='<div class="abs" style="left:90px;top:312px;height:140px;display:flex;align-items:center">'+lg(190)+'</div>'+rowlab(312,140,'Small print size')
c1+='<div class="abs" style="left:50px;top:452px;width:900px;height:2px;background:#e4e7ec"></div>'
c1+='<div class="abs" style="left:90px;top:454px;height:136px;display:flex;align-items:center">'+DOOR%(52,62,TL,'#fff')+'</div>'+rowlab(454,136,'Icon only')
oc='<div class="paper sh" style="left:50px;top:650px;width:430px;height:240px;border-radius:14px;display:flex;align-items:center;justify-content:center">'+lg(330,'#111','#111','#fff','#111')+'</div>'
oc+='<div class="paper sh" style="left:520px;top:650px;width:430px;height:240px;border-radius:14px;background:%s;display:flex;align-items:center;justify-content:center">'%N+lg(330,'#fff','#fff',N,'#fff')+'</div>'
def cap(x,a,b): return '<div class="abs" style="left:%dpx;top:910px;width:430px;text-align:center"><div style="font-size:44px;font-weight:800;color:%s">%s</div><div style="font-size:38px;color:#475467;margin-top:4px">%s</div></div>'%(x,N,a,b)
oc+=cap(50,'One color','Stamps and forms')+cap(520,'Reversed','Signs, dark photos')
logo_small_m=page(title('Test it small, in one color')+c1+oc,'',note='',size=(1000,1070))
# 3. cliche vs distinct
roof='<svg width="170" height="150" viewBox="0 0 150 130"><path d="M10 70L75 12L140 70" fill="none" stroke="#1b2a4a" stroke-width="10" stroke-linejoin="round"/><rect x="34" y="70" width="82" height="50" fill="none" stroke="#1b2a4a" stroke-width="10"/><rect x="66" y="92" width="18" height="28" fill="#1b2a4a"/></svg>'
key='<svg width="170" height="150" viewBox="0 0 150 130"><circle cx="45" cy="65" r="30" fill="none" stroke="#c2410c" stroke-width="12"/><path d="M75 65H140M118 65v26M136 65v18" stroke="#c2410c" stroke-width="12" stroke-linecap="round" fill="none"/></svg>'
chim='<svg width="170" height="150" viewBox="0 0 150 130"><path d="M16 66L75 14L134 66V118H16Z" fill="#14808a"/><rect x="100" y="16" width="16" height="30" fill="#14808a"/><rect x="62" y="82" width="26" height="36" fill="#fff"/></svg>'
good='<div class="deco" style="display:flex;align-items:center;gap:26px"><svg width="150" height="150" viewBox="0 0 110 110"><circle cx="55" cy="55" r="52" fill="#1b2a4a"/><path d="M14 66Q27 56 40 66T66 66T96 66" fill="none" stroke="#7fd1d6" stroke-width="6" stroke-linecap="round"/><path d="M20 82Q31 74 42 82T64 82T90 82" fill="none" stroke="#7fd1d6" stroke-width="5" stroke-linecap="round" opacity=".7"/><circle cx="55" cy="38" r="11" fill="#e0a21b"/></svg><div><div class="serif" style="font-size:64px;font-weight:700;color:#1b2a4a;line-height:1">Lakeview</div><div style="font-size:26px;letter-spacing:.34em;color:#14808a;margin-top:10px;font-weight:700">HOME CO</div></div></div>'
BAD='<svg width="64" height="64" viewBox="0 0 64 64"><circle cx="32" cy="32" r="32" fill="#c2410c"/><path d="M20 20L44 44M44 20L20 44" stroke="#fff" stroke-width="7" stroke-linecap="round"/></svg>'
OKI='<svg width="64" height="64" viewBox="0 0 64 64"><circle cx="32" cy="32" r="32" fill="#1f8a5b"/><path d="M17 33L28 44L47 22" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>'
def panel(y,bd,inner,ic,lab,lc,sub):
    return '<div class="paper sh" style="left:50px;top:%dpx;width:900px;height:410px;border-radius:16px;border:5px solid %s"><div style="height:230px;display:flex;align-items:center;justify-content:center;gap:34px">%s</div><div style="position:absolute;left:34px;right:34px;top:236px;display:flex;align-items:center;gap:20px">%s<div><div style="font-size:52px;font-weight:800;color:%s;line-height:1.1">%s</div><div style="font-size:40px;color:#475467;line-height:1.2;margin-top:4px">%s</div></div></div></div>'%(y,bd,inner,ic,lc,lab,sub)
t=title('Skip the roof, key, chimney')
t+=panel(160,'#fecdca','<div class="deco" style="display:flex;gap:40px">'+roof+key+chim+'</div>',BAD,'Overused','#b42318','On thousands of agent logos')
t+=panel(600,'#b7e4cb',good,OKI,'Distinct','#116b43','Drawn from the place you work')
t+='<div class="abs" style="left:50px;top:1040px;width:900px;font-size:44px;font-weight:600;color:%s;line-height:1.25">Search other agents&rsquo; logos first.</div>'%N
logo_cliche_m=page(t,'',note='',size=(1000,1150))
SC=dict(logo_types_m=logo_types_m,logo_small_m=logo_small_m,logo_cliche_m=logo_cliche_m)
if __name__=='__main__': render(sel(sys.argv,SC))
