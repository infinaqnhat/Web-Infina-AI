import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'; TEAL='#14808a'; OR='#e0613a'
def title(t,top=40,size=64):
    return '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:%dpx;font-weight:800;color:%s;line-height:1.12">%s</div>'%(top,size,N,t)
def dot(n,x,y,d=60,fs=40,col=OR):
    return '<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:50%%;background:%s;color:#fff;font-size:%dpx;font-weight:800;display:flex;align-items:center;justify-content:center">%d</div>'%(x,y,d,d,col,fs,n)
# 1. tools connect to the CRM
c=title('Connect every tool<br>to your CRM',size=62)
c+='<div class="abs sh" style="left:50px;top:210px;width:900px;height:160px;border-radius:16px;background:'+N+';color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-size:60px;font-weight:800;line-height:1.1">CRM</div><div style="font-size:40px;color:#c9d6ee;margin-top:4px">One record for each contact</div></div>'
T=[('Website forms and pages','New leads arrive with a source','#14808a'),('Ad platforms','See which campaign closed','#c2410c'),('Email tool','List stays current','#7c5cc4'),('Direct mail tool','Addresses and responses','#e0613a'),('Review tool','New reviews reach your profile','#e0a21b')]
y=410
c+='<div class="abs" style="left:78px;top:370px;width:8px;height:%dpx;background:#9fb4d6"></div>'%720
for name,sub,col in T:
    c+='<div class="abs" style="left:78px;top:%dpx;width:40px;height:8px;background:#9fb4d6"></div><div class="abs" style="left:110px;top:%dpx;width:840px;height:130px;background:#fff;border-radius:14px;border-left:14px solid %s;box-shadow:0 4px 12px rgba(20,35,70,.1)"><div style="position:absolute;left:28px;top:14px;font-size:44px;font-weight:800;color:%s;white-space:nowrap">%s</div><div style="position:absolute;left:28px;top:72px;font-size:38px;color:#475467;white-space:nowrap">%s</div></div>'%(y+60,y,col,N,name,sub)
    y+=152
c+='<div class="abs" style="left:50px;top:%dpx;width:900px;background:#fff7e6;border-left:8px solid #e0a21b;border-radius:8px;padding:20px 26px;font-size:42px;font-weight:700;color:#1d2433;line-height:1.25">No CRM link, no export: a warning.</div>'%(y+10)
y+=170
soft_connect_m=page(c,'',note='',size=(1000,y+30))
# 2. trial in six steps
T=[('Write the job','Quarterly update to 300 past clients'),('Set a test period','Thirty days is enough'),('Use real data','One real list, one real task'),('Time the work','Compare with how long it takes now'),('Test support','Ask one real question'),('Test the exit','Export your data before it ends')]
c=title('Trial a tool in six steps',size=60)
y=150
for i,(a,b) in enumerate(T):
    c+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:136px;background:#fff;border-radius:16px;box-shadow:0 4px 12px rgba(20,35,70,.1)"></div>'%y
    c+=dot(i+1,76,y+34,68,42)
    c+='<div class="abs" style="left:176px;top:%dpx;font-size:44px;font-weight:800;color:%s;white-space:nowrap">%s</div><div class="abs" style="left:176px;top:%dpx;font-size:38px;color:#475467;white-space:nowrap">%s</div>'%(y+18,N,a,y+78,b)
    y+=156
c+='<div class="abs" style="left:50px;top:%dpx;width:900px;background:#fff7e6;border-left:8px solid #e0a21b;border-radius:8px;padding:20px 26px;font-size:42px;font-weight:700;color:#1d2433;line-height:1.25;text-wrap:balance">Remind yourself the day before it ends.</div>'%(y+10)
y+=170
soft_trial_m=page(c,'',note='',size=(1000,y+30))
# 3. sprawl vs small stack (bar length = monthly cost)
sprawl=[('Contact manager A',40),('Contact manager B',35),('Email tool',30),('Second email tool',25),('Social scheduler',20),('Design tool',15),('Lead platform',99),('Mail automation',60)]
small=[('Simple CRM',40),('Design tool',15)]
tot1=sum(p for _,p in sprawl); tot2=sum(p for _,p in small)+0
SCALE=800.0/tot1
def stack(items,col,y):
    s='<div class="abs" style="left:50px;top:%dpx;width:900px;display:flex;gap:6px"><div style="display:flex;gap:6px;height:56px">'%y
    for n,p in items: s+='<div style="width:%dpx;height:56px;background:%s;border-radius:8px"></div>'%(max(int(p*SCALE)-6,10),col)
    return s+'</div></div>'
t=title('Tool sprawl vs a small stack',size=60)
def card(y,h,head,num,sub,col,bg,items):
    return ('<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:%s;border:4px solid %s;border-radius:16px"></div>'%(y,h,bg,col)
      +'<div class="abs" style="left:84px;top:%dpx;font-size:44px;font-weight:800;color:%s">%s</div>'%(y+24,col,head)
      +'<div class="abs" style="left:84px;top:%dpx;font-size:68px;font-weight:800;color:%s;line-height:1.05;white-space:nowrap">%s<span style="font-size:42px;font-weight:700"> a month</span></div>'%(y+84,col,num)
      +'<div style="position:absolute;left:34px;top:%dpx;width:900px">%s</div>'%(y+190,'')
      +stack(items,col,y+200).replace('left:50px','left:84px')
      +'<div class="abs" style="left:84px;top:%dpx;font-size:38px;color:#475467;white-space:nowrap">%s</div>'%(y+276,sub))
t+=card(160,350,'Tool sprawl','$%d'%tot1,'Overlapping jobs, forgotten trials','#b42318','#fff7f6',sprawl)
t+=card(550,350,'Small stack','$%d'%tot2,'One tool per job, free tiers first','#116b43','#f4fbf7',small)
t+='<div class="abs" style="left:50px;top:940px;width:900px;font-size:42px;font-weight:700;color:'+N+';line-height:1.25">Pay only when a free tool blocks you.</div>'
soft_sprawl_m=page(t,'',note='',size=(1000,1080))
SC=dict(soft_connect_m=soft_connect_m,soft_trial_m=soft_trial_m,soft_sprawl_m=soft_sprawl_m)
if __name__=='__main__': render(sel(sys.argv,SC))
