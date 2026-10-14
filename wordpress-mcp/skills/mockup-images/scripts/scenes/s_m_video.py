import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
def title(t,sub=None):
    h='<div class="abs" style="left:50px;top:40px;font-size:62px;font-weight:800;color:'+N+';line-height:1.1">'+t+'</div>'
    if sub: h+='<div class="abs" style="left:50px;top:125px;font-size:40px;color:#667085;font-weight:600">'+sub+'</div>'
    return h
# 1. three formats and a weekly rhythm
cards=[('Listing highlight','One home, its best features'),('Neighborhood spot','A place locals love'),('Quick answer','One common question')]
h=title('Start with three formats','Film three in one session')
y=215
for a,b in cards:
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:200px;background:#fff;border:3px solid #d0d7e2;border-left:14px solid #14808a;border-radius:14px"><div style="position:absolute;left:34px;top:26px;font-size:54px;font-weight:800;color:%s">%s</div><div style="position:absolute;left:34px;top:112px;font-size:42px;color:#475467;font-weight:600">%s</div></div>'%(y,N,a,b)
    y+=225
h+='<div class="abs" style="left:50px;top:%dpx;width:900px;background:#e6f2f1;border-radius:14px;padding:26px 34px;font-size:48px;font-weight:800;color:%s;line-height:1.2">Post one clip a week</div>'%(y+10,N)
vid_formats_m=page(h,'',note='',size=(1000,y+190))
# 2. 30 second script
h=title('A 30-second script','Sample lines to adapt')
blocks=[('Hook','First few seconds','Thinking about selling before spring?','#b42318'),('One point','About 20 seconds','Photos matter most in the week before listing.','#14808a'),('Next step','Last few seconds','Message me for a home value.','#1b2a4a')]
y=215
for a,b,c,col in blocks:
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:330px;background:#fff;border:3px solid #d0d7e2;border-radius:14px"><div style="position:absolute;left:0;top:0;width:900px;height:96px;background:%s;border-radius:11px 11px 0 0"></div><div style="position:absolute;left:34px;top:16px;font-size:52px;font-weight:800;color:#fff">%s</div><div style="position:absolute;right:34px;top:26px;font-size:40px;font-weight:700;color:#fff">%s</div><div style="position:absolute;left:34px;top:130px;width:830px;font-size:50px;font-weight:700;color:#1d2433;line-height:1.25">&#8220;%s&#8221;</div></div>'%(y,col,a,b,c)
    y+=360
vid_script_m=page(h,'',note='',size=(1000,y+10))
# 3. setup checklist
items=['Wipe the lens','Face a window','Camera at eye level','Quiet room','Shoot vertical','Add captions']
h=title('Phone setup checklist','Two minutes before you record')
y=215
for t in items:
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:120px;background:#fff;border:3px solid #d0d7e2;border-radius:14px"><div style="position:absolute;left:28px;top:25px;width:70px;height:70px;border-radius:14px;background:#14808a;color:#fff;font-size:46px;font-weight:800;text-align:center;line-height:70px">&#10003;</div><div style="position:absolute;left:130px;top:28px;font-size:48px;font-weight:700;color:#1d2433">%s</div></div>'%(y,t)
    y+=140
vid_setup_m=page(h,'',note='',size=(1000,y+20))
SC=dict(vid_formats_m=vid_formats_m,vid_script_m=vid_script_m,vid_setup_m=vid_setup_m)
if __name__=='__main__': render(sel(sys.argv,SC))
