import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
def title(t,sub=None):
    h='<div class="abs" style="left:50px;top:40px;font-size:62px;font-weight:800;color:'+N+';line-height:1.1">'+t+'</div>'
    if sub: h+='<div class="abs" style="left:50px;top:125px;font-size:40px;color:#667085;font-weight:600">'+sub+'</div>'
    return h
# 1. digital sign-in form on a phone-like card
h=title('Digital sign-in form','Sample form for one open house')
h+='<div class="abs" style="left:50px;top:215px;width:900px;background:#fff;border:3px solid #d0d7e2;border-radius:24px;height:1010px"></div>'
fields=[('Full name','Jordan Smith'),('Mobile phone','Sample entry'),('Email','Sample entry')]
y=250
for a,b in fields:
    h+='<div class="abs" style="left:90px;top:%dpx;font-size:40px;font-weight:700;color:#475467">%s</div><div class="abs" style="left:90px;top:%dpx;width:820px;height:84px;background:#f2f5fa;border:2px solid #d0d7e2;border-radius:12px"><div style="position:absolute;left:24px;top:16px;font-size:42px;color:#98a2b3">%s</div></div>'%(y,a,y+55,b)
    y+=170
h+='<div class="abs" style="left:90px;top:%dpx;font-size:40px;font-weight:700;color:#475467">Working with an agent?</div>'%y
h+='<div class="abs" style="left:90px;top:%dpx;display:flex;gap:24px"><div style="width:170px;height:80px;border-radius:40px;background:#14808a;color:#fff;font-size:42px;font-weight:800;text-align:center;line-height:80px">No</div><div style="width:170px;height:80px;border-radius:40px;background:#e4e8f0;color:#475467;font-size:42px;font-weight:700;text-align:center;line-height:80px">Yes</div></div>'%(y+60)
y+=190
h+='<div class="abs" style="left:90px;top:%dpx;width:820px;display:flex;gap:20px"><div style="width:56px;height:56px;border:4px solid #14808a;border-radius:10px;flex:none"></div><div style="font-size:40px;color:#1d2433;line-height:1.25;font-weight:600">I agree to receive texts about this home</div></div>'%y
y+=130
h+='<div class="abs" style="left:90px;top:%dpx;width:820px;height:100px;background:#1b2a4a;border-radius:14px;color:#fff;font-size:46px;font-weight:800;text-align:center;line-height:100px">Sign in</div>'%y
oh_signin_m=page(h,'',note='',size=(1000,1270))
# 2. safety checklist
items=['Bring a partner','Check phone signal','Find two ways out','Everyone signs in','Sweep before locking up']
h=title('Open house safety','Five steps from NAR\'s tips')
y=215
for i,t in enumerate(items):
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:130px;background:#fff;border:3px solid #d0d7e2;border-radius:14px"><div style="position:absolute;left:28px;top:30px;width:70px;height:70px;border-radius:35px;background:#14808a;color:#fff;font-size:44px;font-weight:800;text-align:center;line-height:70px">&#10003;</div><div style="position:absolute;left:130px;top:34px;font-size:48px;font-weight:700;color:#1d2433">%s</div></div>'%(y,t)
    y+=155
oh_safety_m=page(h,'',note='',size=(1000,y+20))
# 3. follow-up timeline
rows=[('Same day','Thank-you to every visitor','#14808a'),('Next day','Ask who has questions','#14808a'),('Day 3','Neighbor recap','#1b2a4a'),('Day 7','Seller report','#1b2a4a')]
h=title('After the open house','A suggested follow-up plan')
y=215
h+='<div class="abs" style="left:96px;top:240px;width:8px;height:%dpx;background:#d0d7e2"></div>'%(len(rows)*215-100)
for a,b,c in rows:
    h+='<div class="abs" style="left:70px;top:%dpx;width:60px;height:60px;border-radius:30px;background:%s"></div>'%(y+30,c)
    h+='<div class="abs" style="left:170px;top:%dpx;width:780px;height:170px;background:#fff;border:3px solid #d0d7e2;border-radius:14px"><div style="position:absolute;left:30px;top:20px;font-size:56px;font-weight:800;color:%s">%s</div><div style="position:absolute;left:30px;top:100px;font-size:44px;color:#1d2433;font-weight:600">%s</div></div>'%(y,c,a,b)
    y+=215
oh_after_m=page(h,'',note='',size=(1000,y+20))
SC=dict(oh_signin_m=oh_signin_m,oh_safety_m=oh_safety_m,oh_after_m=oh_after_m)
if __name__=='__main__': render(sel(sys.argv,SC))
