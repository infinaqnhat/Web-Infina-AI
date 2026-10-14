import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
def title(t,sub=None):
    h='<div class="abs" style="left:50px;top:40px;font-size:62px;font-weight:800;color:'+N+';line-height:1.1">'+t+'</div>'
    if sub: h+='<div class="abs" style="left:50px;top:125px;font-size:40px;color:#667085;font-weight:600">'+sub+'</div>'
    return h
# 1. 20-second script
rows=[('1','Greet','Hi, I am Avery, local agent.'),('2','Reason','A home down the road just sold.'),('3','One ask','Want a free home estimate?'),('4','Leave','Here is my card. Thanks!')]
h=title('A 20-second script','Sample lines to adapt')
y=215
for n,a,b in rows:
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:200px;background:#fff;border:3px solid #d0d7e2;border-radius:14px"><div style="position:absolute;left:28px;top:56px;width:84px;height:84px;border-radius:42px;background:#14808a;color:#fff;font-size:52px;font-weight:800;text-align:center;line-height:84px">%s</div><div style="position:absolute;left:150px;top:22px;font-size:42px;font-weight:700;color:#14808a">%s</div><div style="position:absolute;left:150px;top:90px;width:720px;font-size:46px;font-weight:700;color:#1d2433;line-height:1.2">%s</div></div>'%(y,n,a,b)
    y+=225
door_script_m=page(h,'',note='',size=(1000,y+10))
# 2. responses
rows=[('Not interested','No problem. Here is my card.'),('Already have an agent','Great. Keep my card for a second opinion.'),('Bad time','May I stop by another day?')]
h=title('Handle common replies','Short, calm, then step back')
y=215
for a,b in rows:
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:270px;background:#fff;border:3px solid #d0d7e2;border-radius:14px"><div style="position:absolute;left:34px;top:24px;font-size:46px;font-weight:800;color:#b42318;line-height:1.15;width:830px">&#8220;%s&#8221;</div><div style="position:absolute;left:34px;top:130px;width:830px;font-size:46px;font-weight:700;color:#116b43;line-height:1.2">You: %s</div></div>'%(y,a,b)
    y+=295
door_replies_m=page(h,'',note='',size=(1000,y+10))
# 3. safety checklist
items=['Tell someone your route','Wear ID, go in daylight','Charge your phone','Park facing the street','Leave if it feels wrong']
h=title('Safe door knocking','Based on NAR\'s safety tips')
y=215
for t in items:
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:130px;background:#fff;border:3px solid #d0d7e2;border-radius:14px"><div style="position:absolute;left:28px;top:30px;width:70px;height:70px;border-radius:35px;background:#14808a;color:#fff;font-size:44px;font-weight:800;text-align:center;line-height:70px">&#10003;</div><div style="position:absolute;left:130px;top:34px;font-size:46px;font-weight:700;color:#1d2433">%s</div></div>'%(y,t)
    y+=152
door_safety_m=page(h,'',note='',size=(1000,y+20))
SC=dict(door_script_m=door_script_m,door_replies_m=door_replies_m,door_safety_m=door_safety_m)
if __name__=='__main__': render(sel(sys.argv,SC))
