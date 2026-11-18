import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
def title(t,sub=None):
    h='<div class="abs" style="left:50px;top:40px;font-size:62px;font-weight:800;color:'+N+';line-height:1.1">'+t+'</div>'
    if sub: h+='<div class="abs" style="left:50px;top:125px;font-size:40px;color:#667085;font-weight:600">'+sub+'</div>'
    return h
# 1. check before dialing
items=['Registry checked in the last 31 days','Not on your own do-not-call list','Between 8 a.m. and 9 p.m. their time','Relationship on record, if you rely on one']
h=title('Check before you dial','Four checks for every list')
y=215
for t in items:
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:190px;background:#fff;border:3px solid #d0d7e2;border-radius:14px"><div style="position:absolute;left:28px;top:60px;width:70px;height:70px;border-radius:35px;background:#14808a;color:#fff;font-size:44px;font-weight:800;text-align:center;line-height:70px">&#10003;</div><div style="position:absolute;left:130px;top:30px;width:740px;font-size:46px;font-weight:700;color:#1d2433;line-height:1.2">%s</div></div>'%(y,t)
    y+=215
cc_check_m=page(h,'',note='',size=(1000,y+10))
# 2. objection replies
rows=[('Not interested','Understood, thanks for your time.'),('Already have an agent','Great. I am here for a second opinion.'),('Send me something','Happy to. Best email?')]
h=title('Replies to common objections','Calm, brief, then respect the answer')
y=215
for a,b in rows:
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:270px;background:#fff;border:3px solid #d0d7e2;border-radius:14px"><div style="position:absolute;left:34px;top:24px;font-size:46px;font-weight:800;color:#b42318;width:830px;line-height:1.15">&#8220;%s&#8221;</div><div style="position:absolute;left:34px;top:130px;width:830px;font-size:46px;font-weight:700;color:#116b43;line-height:1.2">You: %s</div></div>'%(y,a,b)
    y+=295
cc_replies_m=page(h,'',note='',size=(1000,y+10))
# 3. call log row
h=title('Log every call','Sample entry')
fields=[('Date','Oct 21'),('Outcome','Wants a value estimate'),('Next step','Email it today'),('Do not call?','No')]
y=215
for a,b in fields:
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:170px;background:#fff;border:3px solid #d0d7e2;border-radius:14px"><div style="position:absolute;left:34px;top:20px;font-size:40px;font-weight:700;color:#667085">%s</div><div style="position:absolute;left:34px;top:80px;width:830px;font-size:52px;font-weight:800;color:%s;line-height:1.1">%s</div></div>'%(y,a,N,b)
    y+=195
cc_log_m=page(h,'',note='',size=(1000,y+10))
SC=dict(cc_check_m=cc_check_m,cc_replies_m=cc_replies_m,cc_log_m=cc_log_m)
if __name__=='__main__': render(sel(sys.argv,SC))
