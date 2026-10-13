import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
# Bio (#1895), mobile-first, canvas 1000 wide. Same content as s_bio.py, new layout.
N='#1b2a4a'; OR='#e0613a'
def title(t,sub=''):
    s='<div style="font-size:60px;font-weight:800;color:'+N+';line-height:1.12">'+t+'</div>'
    if sub: s+='<div style="font-size:40px;font-weight:600;color:#667085;margin-top:10px">'+sub+'</div>'
    return s
def dot(n,col=OR,sz=56):
    return '<span style="flex:none;width:'+str(sz)+'px;height:'+str(sz)+'px;border-radius:50%;background:'+col+';color:#fff;font-weight:800;font-size:40px;display:flex;align-items:center;justify-content:center">'+str(n)+'</span>'
def wrap(inner): return '<div class="abs" style="left:50px;top:40px;width:900px">'+inner+'</div>'
def bars(*ws,col='#d0d5dd'):
    return ''.join('<div style="height:22px;width:'+str(w)+'%;background:'+col+';border-radius:11px;margin:12px 0"></div>' for w in ws)

# 1. profile page with the three essential parts highlighted
def hl(n,bg,bar,ws):
    return ('<div style="display:flex;gap:18px;align-items:center;margin-top:22px">'+dot(n)
        +'<div style="flex:1;background:'+bg+';border-radius:14px;padding:8px 22px">'+bars(*ws,col=bar)+'</div></div>')
card=('<div class="sh" style="background:#fff;border-radius:18px;overflow:hidden;margin-top:36px">'
 +'<div class="deco" style="height:120px;background:linear-gradient(135deg,#14808a,#1b2a4a)"></div>'
 +'<div style="display:flex;gap:26px;padding:0 40px;align-items:flex-start">'
 +'<div class="deco" style="flex:none;margin-top:-56px;width:124px;height:124px;border-radius:50%;background:#e7eefc;border:7px solid #fff;color:'+N+';font-weight:800;font-size:44px;display:flex;align-items:center;justify-content:center">DR</div>'
 +'<div style="margin-top:14px"><div style="font-size:44px;font-weight:800;color:'+N+';line-height:1.15">Daniel Reyes</div><div style="font-size:38px;font-weight:700;color:#14808a;margin-top:2px">Buyer specialist, Cedar Hills</div></div></div>'
 +'<div style="padding:10px 40px 34px 30px">'
 +hl(1,'#dbeafe','#93b4ec',(100,70))+hl(2,'#dcfce7','#86d1a8',(100,62))
 +'<div style="display:flex;gap:18px;align-items:center;margin-top:22px"><span style="flex:none;width:56px"></span><div style="flex:1;padding:0 22px">'+bars(100,45)+'</div></div>'
 +hl(3,'#ffedd5','#f3b98a',(78,))+'</div></div>')
def leg(n,label,bg,sub):
    return ('<div style="display:flex;gap:20px;align-items:flex-start;margin-top:30px">'+dot(n)
        +'<div><span style="background:'+bg+';border-radius:10px;padding:2px 14px;font-size:44px;font-weight:800;color:'+N+'">'+label+'</span>'
        +'<div style="font-size:40px;color:#475467;margin-top:10px;line-height:1.25">'+sub+'</div></div></div>')
legend=leg(1,'Who you help','#dbeafe','First-time buyers in Cedar Hills')+leg(2,'Proof','#dcfce7','Plain language, same-day replies')+leg(3,'Next step','#ffedd5','Call or message Daniel')
bio_profile_m=page(wrap(title('Every bio needs three parts')+card+legend),'',note='',size=(1000,1320))

# 2. before / after
rows=[('I am passionate about real estate.','I help Cedar Hills buyers compare homes without pressure.'),
 ('I provide excellent service.','I reply to every message within the hour.'),
 ('I know the market.','I have sold in Cedar Hills since 2017.'),
 ('I am the number one agent.','Five stars on Google, 40 reviews.')]
r=''
for b,a in rows:
    r+=('<div style="margin-top:36px">'
     +'<div style="display:flex;gap:16px;align-items:center;padding-left:6px"><span style="flex:none;width:48px;height:48px;border-radius:50%;background:#fdecea;color:#b42318;font-weight:800;font-size:38px;display:flex;align-items:center;justify-content:center">&times;</span>'
     +'<span style="font-size:40px;color:#667085;text-decoration:line-through;text-decoration-color:#98a2b3">'+b+'</span></div>'
     +'<div class="sh" style="margin-top:12px;background:#fff;border:4px solid #1f8a5b;border-radius:16px;padding:20px 26px;display:flex;gap:18px;align-items:center">'
     +'<span style="flex:none;width:52px;height:52px;border-radius:50%;background:#e6f6ee;color:#116b43;font-weight:800;font-size:40px;display:flex;align-items:center;justify-content:center">&#10003;</span>'
     +'<span style="font-size:44px;font-weight:700;color:'+N+';line-height:1.2;text-wrap:balance">'+a+'</span></div></div>')
foot='<div style="font-size:40px;font-weight:600;color:#475467;margin-top:44px;line-height:1.3;text-wrap:balance">Name an audience, an area, a strength or a next step.</div>'
bio_beforeafter_m=page(wrap(title('Vague lines, made specific')+r+foot),'',note='',size=(1000,1250))

# 3. three bios, one structure
def bcard(ini,name,role,g,chips):
    ch=''.join('<span style="background:'+bg+';color:'+fg+';border-radius:999px;padding:8px 20px;font-size:38px;font-weight:700">'+t+'</span>' for t,bg,fg in chips)
    return ('<div class="sh" style="background:#fff;border-radius:18px;overflow:hidden;margin-top:24px">'
     +'<div class="deco" style="height:76px;background:'+g+'"></div>'
     +'<div style="display:flex;gap:24px;padding:0 36px;align-items:flex-start">'
     +'<div class="deco" style="flex:none;margin-top:-44px;width:108px;height:108px;border-radius:50%;background:#e7eefc;border:6px solid #fff;color:'+N+';font-weight:800;font-size:38px;display:flex;align-items:center;justify-content:center">'+ini+'</div>'
     +'<div style="margin-top:12px"><div style="font-size:44px;font-weight:800;color:'+N+';line-height:1.15">'+name+'</div><div style="font-size:38px;font-weight:700;color:#14808a;margin-top:2px">'+role+'</div></div></div>'
     +'<div style="display:flex;flex-wrap:wrap;gap:12px;padding:22px 36px 30px">'+ch+'</div></div>')
B=lambda a,b,c:[(a,'#dbeafe','#1e40af'),(b,'#e0f2fe','#075985'),(c,'#dcfce7','#116b43')]
g=bcard('DR','Daniel Reyes','New agent','linear-gradient(135deg,#14808a,#1b2a4a)',B('First-time buyers','Cedar Hills','Plain language'))
g+=bcard('LP','Linda Park','Downsizing specialist','linear-gradient(135deg,#e0613a,#7c2d12)',B('Downsizers','East side suburbs','Coordination'))
g+=bcard('PS','Priya Shah','Relocation specialist','linear-gradient(135deg,#1b2a4a,#4b5f8a)',B('Relocating buyers','Riverside','One-trip tours'))
key=('<div style="display:flex;gap:14px;margin-top:30px;font-size:38px;font-weight:800">'
  '<span style="color:#1e40af">&#9679; Audience</span><span style="color:#075985">&#9679; Area</span><span style="color:#116b43">&#9679; Strength</span></div>'
  '<div style="font-size:42px;font-weight:700;color:'+N+';margin-top:14px">Each bio ends with a next step.</div>')
bio_gallery_m=page(wrap(title('One structure, three agents')+g+key),'',note='',size=(1000,1490))
SC=dict(bio_profile_m=bio_profile_m,bio_beforeafter_m=bio_beforeafter_m,bio_gallery_m=bio_gallery_m)
if __name__=='__main__': render(sel(sys.argv,SC))
