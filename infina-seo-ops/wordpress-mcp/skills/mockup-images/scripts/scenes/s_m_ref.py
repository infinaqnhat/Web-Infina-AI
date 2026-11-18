import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
def title(t,sz=64): return '<div class="abs" style="left:50px;top:40px;width:900px;font-size:%dpx;font-weight:800;color:%s;line-height:1.1">%s</div>'%(sz,N,t)
def dot(n,sz=60,fs=40,bg='#e0613a'): return '<div style="width:%dpx;height:%dpx;border-radius:50%%;background:%s;color:#fff;font-size:%dpx;font-weight:800;display:flex;align-items:center;justify-content:center;flex:none">%d</div>'%(sz,sz,bg,fs,n)
# 1. referral system: five steps, then the ask as a text message
STEPS=['List your sphere','Stay in touch on a schedule','Make a direct ask','Make it easy','Thank them, keep track']
r=title('Five steps to referrals')
y=150
for i,s in enumerate(STEPS):
    hot=(i==2)
    r+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:96px;background:%s;border-radius:14px;box-shadow:0 4px 12px rgba(20,35,70,.1);display:flex;align-items:center;gap:22px;padding:0 24px;%s"><div style="width:56px;height:56px;border-radius:50%%;background:#e0613a;color:#fff;font-size:40px;font-weight:800;display:flex;align-items:center;justify-content:center;flex:none">%d</div><div style="font-size:44px;font-weight:%d;color:%s">%s</div></div>'%(y,'#fff4ec' if hot else '#fff','border:3px solid #e0613a;' if hot else '',i+1,800 if hot else 700,N,s)
    y+=112
y+=24
r+='<div class="abs" style="left:50px;top:%dpx;font-size:42px;font-weight:700;color:#e0613a">Step 3 as a text message</div>'%y
y+=70
ph=('<div class="abs sh" style="left:50px;top:%dpx;width:900px;height:730px;border-radius:48px;background:#101828;padding:18px"><div style="width:100%%;height:100%%;border-radius:32px;background:#f2f4f7;position:relative;overflow:hidden">'%y
 +'<div style="height:96px;background:#fff;border-bottom:1px solid #e4e7ec;display:flex;align-items:center;gap:18px;padding:0 28px"><div class="deco" style="width:58px;height:58px;border-radius:50%;background:#b7e4cb;color:#116b43;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center">M</div><div style="font-weight:800;font-size:42px">Maya</div></div>'
 +'<div style="position:absolute;left:24px;right:90px;top:128px;background:#1b6ef3;color:#fff;border-radius:30px 30px 30px 6px;padding:22px 28px;font-size:42px;line-height:1.3">If you know anyone thinking about buying or selling in the next year, I would be glad to help them.</div>'
 +'<div style="position:absolute;right:24px;left:150px;top:380px;background:#e4e7ec;border-radius:30px 30px 6px 30px;padding:22px 28px;font-size:42px;line-height:1.3">My cousin is moving here in the spring.</div>'
 +'<div style="position:absolute;left:24px;right:200px;top:560px;background:#1b6ef3;color:#fff;border-radius:30px 30px 30px 6px;padding:22px 28px;font-size:42px;line-height:1.3">Of course. Thank you, Maya.</div></div></div>')
r+=ph
y+=730
referral_ask_m=page(r,'',note='',size=(1000,y+50))
# 2. agreement: simplified document + five numbered checks
doc='<div class="paper sh" style="left:50px;top:150px;width:900px;height:520px;border-radius:8px"><div style="padding:30px 40px"><div class="serif" style="font-size:52px;font-weight:700;color:'+N+'">Referral agreement</div>'
for i in range(5):
    wd=[78,62,70,54,46][i]
    doc+='<div style="display:flex;align-items:center;gap:22px;margin-top:%dpx"><div style="width:54px;height:54px;border-radius:50%%;background:#e0613a;color:#fff;font-size:38px;font-weight:800;display:flex;align-items:center;justify-content:center;flex:none">%d</div><div class="deco" style="flex:1"><div style="height:16px;width:%d%%;background:#e4e7ec;border-radius:8px"></div><div style="height:4px;background:#cbd2e0;margin-top:14px;border-radius:2px"></div></div></div>'%(24 if i else 28,i+1,wd)
doc+='</div></div>'
items=['Who the parties are','Which client it covers','The fee and how it is calculated','When it is paid','How long it lasts']
l=''
y=710
for i,t in enumerate(items):
    l+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:80px;display:flex;align-items:center;gap:22px">%s<div style="font-size:42px;font-weight:700;color:#1d2433">%s</div></div>'%(y,dot(i+1),t)
    y+=90
y+=20
l+='<div class="abs" style="left:50px;top:%dpx;width:900px;background:#fff7e6;border-left:8px solid #e0a21b;border-radius:8px;padding:20px 28px;font-size:42px;color:#1d2433;line-height:1.3"><strong>Put it in writing, between brokerages.</strong> Fees vary, so there is no standard number.</div>'%y
y+=230
referral_agreement_m=page(title('What the agreement covers')+doc+l,'',note='',size=(1000,y))
# 3. tracker: cards
RW=[('Maya R.','Past client sent her cousin','Appointment','#dbeafe','#1e40af'),('Linda P.','Neighbor sent a coworker','Listed','#ede9fe','#5b21b6'),('Sam O.','Agent sent Chris, moving here','Closed','#dcfce7','#116b43'),('Priya S.','Lender sent a first-time buyer','In conversation','#fef3c7','#92400e')]
t=title('Know who sends you clients')
t+='<div class="paper sh" style="left:50px;top:150px;width:900px;height:%dpx;border-radius:16px"><div style="background:#14808a;color:#fff;height:100px;padding:0 30px;display:flex;align-items:center;font-size:44px;font-weight:800">Referrals this quarter</div>'%(100+4*160)
for i,(n,sub,st,bg,fg) in enumerate(RW):
    t+='<div style="position:absolute;left:0;right:0;top:%dpx;height:160px;border-bottom:%s"><div style="position:absolute;left:30px;top:22px;font-size:44px;font-weight:800;color:%s">%s</div><div style="position:absolute;left:30px;top:90px;font-size:38px;color:#475467">%s</div><div style="position:absolute;right:30px;top:24px;background:%s;color:%s;border-radius:12px;padding:6px 20px;font-size:38px;font-weight:800">%s</div></div>'%(100+i*160,'2px solid #e4e7ec' if i<3 else 'none',N,n,sub,bg,fg,st)
t+='</div>'
y=150+100+640+40
t+='<div class="abs" style="left:50px;top:%dpx;width:900px;background:#fff7e6;border-left:8px solid #e0a21b;border-radius:8px;padding:20px 28px;font-size:42px;color:#1d2433;line-height:1.3"><strong>Count closings by referrer.</strong> Thank your top referrers in person.</div>'%y
y+=230
referral_tracker_m=page(t,'',note='',size=(1000,y))
SC=dict(referral_ask_m=referral_ask_m,referral_agreement_m=referral_agreement_m,referral_tracker_m=referral_tracker_m)
if __name__=='__main__': render(sel(sys.argv,SC))
