import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
def title(t,sub=None):
    h='<div class="abs" style="left:50px;top:40px;font-size:62px;font-weight:800;color:'+N+';line-height:1.1">'+t+'</div>'
    if sub: h+='<div class="abs" style="left:50px;top:125px;font-size:40px;color:#667085;font-weight:600">'+sub+'</div>'
    return h
# 1. clean signature in an email frame
h=title('A clean signature','Sample for a made-up agent')
h+='<div class="abs" style="left:50px;top:215px;width:900px;height:760px;background:#fff;border:3px solid #d0d7e2;border-radius:18px"></div>'
h+='<div class="abs" style="left:90px;top:250px;font-size:44px;color:#667085;font-weight:600">Thanks, talk soon.</div>'
h+='<div class="abs" style="left:90px;top:340px;width:820px;height:2px;background:#d0d7e2"></div>'
h+='<div class="abs" style="left:90px;top:380px;font-size:60px;font-weight:800;color:'+N+'">Avery Collins</div>'
h+='<div class="abs" style="left:90px;top:465px;font-size:44px;font-weight:700;color:#14808a">Sales Associate</div>'
h+='<div class="abs" style="left:90px;top:535px;font-size:44px;color:#1d2433;font-weight:600">Harbor Realty Group</div>'
h+='<div class="abs" style="left:90px;top:605px;font-size:44px;color:#1d2433">Mobile 555-0100</div>'
h+='<div class="abs" style="left:90px;top:675px;font-size:44px;color:#1d2433">averycollins.example</div>'
h+='<div class="abs" style="left:90px;top:775px;width:820px;height:110px;background:#14808a;border-radius:14px;color:#fff;font-size:46px;font-weight:800;text-align:center;line-height:110px">Book a 15-minute call</div>'
sig_clean_m=page(h,'',note='',size=(1000,1010))
# 2. cluttered vs clean
h=title('Clutter or clean?','Sample signatures')
h+='<div class="abs" style="left:50px;top:215px;width:900px;height:430px;background:#fff1f0;border:3px solid #f3b6b0;border-radius:16px"><div style="position:absolute;left:34px;top:24px;font-size:52px;font-weight:800;color:#b42318">Too much</div><div style="position:absolute;left:34px;top:110px;width:830px;font-size:42px;color:#1d2433;line-height:1.45;font-weight:600">Three phone numbers<br>Six social icons<br>Four links and a quote<br>A huge banner image</div></div>'
h+='<div class="abs" style="left:50px;top:690px;width:900px;height:430px;background:#edf8f1;border:3px solid #a9dbbd;border-radius:16px"><div style="position:absolute;left:34px;top:24px;font-size:52px;font-weight:800;color:#116b43">Just right</div><div style="position:absolute;left:34px;top:110px;width:830px;font-size:42px;color:#1d2433;line-height:1.45;font-weight:600">Name, title, brokerage<br>One phone number<br>One website<br>One call to action</div></div>'
sig_cmp_m=page(h,'',note='',size=(1000,1160))
# 3. compliance checklist
items=['Licensed name and title','Brokerage name','License number, if required','REALTOR&#174; next to your name','Address and opt-out in marketing']
h=title('Before you hit send','Signature checks')
y=215
for t in items:
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:135px;background:#fff;border:3px solid #d0d7e2;border-radius:14px"><div style="position:absolute;left:28px;top:32px;width:70px;height:70px;border-radius:35px;background:#14808a;color:#fff;font-size:44px;font-weight:800;text-align:center;line-height:70px">&#10003;</div><div style="position:absolute;left:130px;top:36px;font-size:44px;font-weight:700;color:#1d2433">%s</div></div>'%(y,t)
    y+=158
sig_check_m=page(h,'',note='',size=(1000,y+20))
SC=dict(sig_clean_m=sig_clean_m,sig_cmp_m=sig_cmp_m,sig_check_m=sig_check_m)
if __name__=='__main__': render(sel(sys.argv,SC))
