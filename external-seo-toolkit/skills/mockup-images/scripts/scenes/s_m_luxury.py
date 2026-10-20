import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
def title(t,sub=None):
    h='<div class="abs" style="left:50px;top:40px;font-size:62px;font-weight:800;color:'+N+';line-height:1.1">'+t+'</div>'
    if sub: h+='<div class="abs" style="left:50px;top:125px;font-size:40px;color:#667085;font-weight:600">'+sub+'</div>'
    return h
# 1. brand sheet
h=title('A simple luxury brand sheet','Sample for a made-up agent')
h+='<div class="abs" style="left:50px;top:215px;width:900px;height:250px;background:#1b2a4a;border-radius:16px"><div style="position:absolute;left:40px;top:50px;font-family:Georgia,serif;font-size:76px;color:#f4ead2;line-height:1.1">Avery Collins</div><div style="position:absolute;left:40px;top:160px;font-size:40px;letter-spacing:6px;color:#d9c48f;font-weight:600">COASTAL ESTATES</div></div>'
h+='<div class="abs" style="left:50px;top:500px;font-size:46px;font-weight:800;color:'+N+'">Two colors and one neutral</div>'
sw=[('#1b2a4a','Navy'),('#d9c48f','Champagne'),('#f6f2e8','Ivory')]
for i,(c,n) in enumerate(sw):
    h+='<div class="abs" style="left:%dpx;top:580px;width:280px;height:150px;background:%s;border:3px solid #d0d7e2;border-radius:14px"></div><div class="abs" style="left:%dpx;top:745px;font-size:40px;font-weight:700;color:#1d2433">%s</div>'%(50+i*310,c,50+i*310,n)
h+='<div class="abs" style="left:50px;top:850px;font-size:46px;font-weight:800;color:'+N+'">Tone of voice</div>'
for i,t in enumerate(['Calm','Precise','Discreet']):
    h+='<div class="abs" style="left:%dpx;top:925px;width:280px;height:100px;background:#fff;border:3px solid #14808a;border-radius:50px;color:#14808a;font-size:46px;font-weight:800;text-align:center;line-height:94px">%s</div>'%(50+i*310,t)
lux_brand_m=page(h,'',note='',size=(1000,1090))
# 2. launch plan
rows=[('Weeks before','Photos, video, floor plan','#667085'),('Private preview','Your buyer network first','#14808a'),('Launch','Follow your MLS rules','#14808a'),('After','Seller report','#1b2a4a')]
h=title('A planned listing launch','A suggested order of steps')
y=215
for a,b,c in rows:
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:200px;background:#fff;border:3px solid #d0d7e2;border-left:14px solid %s;border-radius:14px"><div style="position:absolute;left:34px;top:24px;font-size:56px;font-weight:800;color:%s">%s</div><div style="position:absolute;left:34px;top:112px;font-size:44px;color:#1d2433;font-weight:600">%s</div></div>'%(y,c,N,a,b)
    y+=225
lux_launch_m=page(h,'',note='',size=(1000,y+10))
# 3. two ways to launch
def card(y,name,lines,col,bg,bd):
    s='<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:%s;border:3px solid %s;border-radius:16px"><div style="position:absolute;left:34px;top:24px;font-size:56px;font-weight:800;color:%s">%s</div>'%(y,130+len(lines)*80,bg,bd,col,name)
    for i,l in enumerate(lines):
        s+='<div style="position:absolute;left:34px;top:%dpx;font-size:44px;font-weight:600;color:#1d2433">&#9679; %s</div>'%(115+i*80,l)
    return s+'</div>'
h=title('Two ways to launch','Based on NAR\'s 2025 policy update')
h+=card(215,'Public launch',['Filed with the MLS','IDX and syndication on'],N,'#fff','#d0d7e2')
h+=card(215+130+160+40,'Delayed marketing',['Still filed with the MLS','IDX and syndication wait','Signed seller disclosure','MLS sets the length'],'#14808a','#e6f2f1','#a7d3cf')
lux_private_m=page(h,'',note='',size=(1000,215+290+40+130+320+30))
SC=dict(lux_brand_m=lux_brand_m,lux_launch_m=lux_launch_m,lux_private_m=lux_private_m)
if __name__=='__main__': render(sel(sys.argv,SC))
