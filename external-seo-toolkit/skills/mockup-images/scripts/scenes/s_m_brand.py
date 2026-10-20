import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'; BR='#1d4e89'; GOLD='#e0a21b'
def mono(sz,bg=BR,fg='#fff'): return '<div class="deco" style="width:%dpx;height:%dpx;border-radius:50%%;background:%s;color:%s;display:flex;align-items:center;justify-content:center;font-family:Lora,serif;font-weight:700;font-size:%dpx;flex:none">DL</div>'%(sz,sz,bg,fg,int(sz*.38))
# 1. brand sheet
items=[('POSITIONING','I help first-time buyers in Cedar Hills.'),('VOICE','Plain. Warm. Specific.'),('LOGO','Minimum size 0.75 in'),('COLORS AND FONTS','Lora headings, Inter body'),('HEADSHOT AND BIO','One photo, a short and a long bio'),('REQUIRED LINES','Brokerage, license, disclosures')]
b='<div class="abs" style="left:0;top:0;width:1000px;height:160px;background:'+BR+'"></div><div class="abs" style="left:50px;top:24px;font-size:60px;font-weight:800;color:#fff;font-family:Lora,serif">Brand sheet</div><div class="abs" style="left:50px;top:102px;font-size:36px;color:#cfe0f5">One page for every printer and designer</div>'
y=200
for i,(k,v) in enumerate(items):
    b+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:132px;background:#fff;border-radius:12px;box-shadow:0 4px 12px rgba(20,35,70,.1)"><div style="position:absolute;left:26px;top:14px;font-size:36px;font-weight:800;color:#e0613a;letter-spacing:.06em">%s</div><div style="position:absolute;left:26px;top:62px;font-size:44px;font-weight:700;color:%s">%s</div></div>'%(y,k,N,v)
    if k=='LOGO': b+='<div class="abs" style="left:800px;top:%dpx">%s</div>'%(y+34,mono(70))
    if k=='COLORS AND FONTS': b+=''.join('<div class="abs" style="left:%dpx;top:%dpx;width:44px;height:44px;border-radius:8px;background:%s"></div>'%(700+j*56,y+16,c) for j,c in enumerate([BR,GOLD,'#1d2433']))
    y+=148
brand_sheet_m=page(b,'',note='',size=(1000,y+20))
# 2. one look: 2x2 tiles, minimal text
def tile(x,y,w,h,inner,label):
    return '<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;background:#fff;border-radius:14px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">%s</div><div class="abs" style="left:%dpx;top:%dpx;width:%dpx;text-align:center;font-size:40px;font-weight:700;color:%s">%s</div>'%(x,y,w,h,inner,x,y+h+12,w,N,label)
card='<div style="padding:30px;display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%">'+mono(100)+'<div class="serif" style="font-size:44px;font-weight:700;color:'+BR+';margin-top:14px">Dana Lee</div><div style="font-size:38px;font-weight:800;color:'+GOLD+';letter-spacing:.04em;margin-top:2px">REALTOR</div></div>'
web='<div style="background:'+BR+';height:130px;display:flex;align-items:center;gap:16px;padding:0 24px">'+mono(70,'#fff',BR)+'<div class="serif" style="font-size:44px;font-weight:700;color:#fff">Dana Lee</div></div><div style="padding:22px 24px"><div style="height:18px;width:80%;background:#e4e7ec;border-radius:9px;margin-bottom:12px"></div><div style="height:18px;width:55%;background:#e4e7ec;border-radius:9px;margin-bottom:20px"></div><div style="display:inline-block;background:'+GOLD+';color:#1d2433;font-size:36px;font-weight:800;padding:10px 24px;border-radius:8px">Get the guide</div></div>'
sign='<div style="padding:30px;background:#f1f4f9;height:100%;position:relative"><div style="background:#fff;border:8px solid '+BR+';border-radius:10px;height:200px;display:flex;align-items:center;justify-content:center;gap:16px">'+mono(80)+'<div><div class="serif" style="font-size:44px;font-weight:700;color:'+BR+'">Dana Lee</div><div style="font-size:38px;font-weight:800;color:'+GOLD+'">FOR SALE</div></div></div><div style="position:absolute;left:70px;top:240px;width:14px;height:100px;background:#8b6f47"></div></div>'
post='<div style="padding:26px"><div style="display:flex;gap:16px;align-items:center">'+mono(70)+'<div style="font-size:40px;font-weight:800;color:'+BR+'">Dana Lee</div></div><div class="serif" style="font-size:46px;color:'+BR+';font-weight:700;line-height:1.2;margin-top:22px">Three things to fix before you list</div></div>'
t='<div class="abs" style="left:50px;top:40px;font-size:64px;font-weight:800;color:'+N+';line-height:1.1">One look, everywhere</div>'
t+=tile(50,150,430,360,card,'Business card')+tile(520,150,430,360,web,'Website')+tile(50,610,430,360,sign,'Yard sign')+tile(520,610,430,360,post,'Social post')
t+='<div class="abs" style="left:50px;top:1070px;width:900px;font-size:44px;font-weight:600;color:'+N+';line-height:1.3">Same name, blue, gold and type on every piece.</div>'
brand_looks_m=page(t,'',note='',size=(1000,1200))
# 3. mixed vs consistent
def mix(x,items,label,col,sub):
    s='<div class="abs" style="left:%dpx;top:150px;width:430px;text-align:center"><div style="font-size:56px;font-weight:800;color:%s">%s</div><div style="font-size:38px;color:#667085;margin-top:2px">%s</div></div>'%(x,col,label,sub)
    y=300
    for inner,bg in items:
        s+='<div class="abs" style="left:%dpx;top:%dpx;width:430px;height:200px;background:%s;border-radius:12px;box-shadow:0 4px 12px rgba(20,35,70,.12);display:flex;align-items:center;justify-content:center;overflow:hidden">%s</div>'%(x,y,bg,inner)
        y+=224
    return s
bad=[('<div style="font:700 56px Impact,Liberation Sans;color:#d62828">DANA LEE</div>','#fff7d6'),('<div style="font:700 46px Liberation Mono;color:#38761d">dana lee realty</div>','#f1f8e9'),('<div style="font:italic 700 50px Liberation Serif;color:#6a1b9a">Dana Lee Group</div>','#f3e5f5')]
good=[('<div style="text-align:center">'+'<div class="serif" style="font-size:56px;font-weight:700;color:'+BR+'">Dana Lee</div></div>','#fff'),('<div style="display:flex;gap:18px;align-items:center">'+mono(90)+'<div class="serif" style="font-size:50px;font-weight:700;color:'+BR+'">Dana Lee</div></div>','#fff'),('<div style="text-align:center"><div class="serif" style="font-size:56px;font-weight:700;color:'+BR+'">Dana Lee</div><div style="font-size:38px;font-weight:800;color:'+GOLD+'">REALTOR</div></div>','#fff')]
t='<div class="abs" style="left:50px;top:40px;font-size:64px;font-weight:800;color:'+N+';line-height:1.1">Mixed vs consistent</div>'
t+=mix(50,bad,'Mixed','#c2410c','Different type and color')+mix(520,good,'Consistent','#1f8a5b','One name, one blue')
t+='<div class="abs" style="left:50px;top:1000px;width:900px;font-size:42px;font-weight:600;color:'+N+';line-height:1.3">Lay your card, flyer and sign side by side. Do they look like one agent?</div>'
brand_mixed_m=page(t,'',note='',size=(1000,1130))
SC=dict(brand_sheet_m=brand_sheet_m,brand_looks_m=brand_looks_m,brand_mixed_m=brand_mixed_m)
if __name__=='__main__': render(sel(sys.argv,SC))
