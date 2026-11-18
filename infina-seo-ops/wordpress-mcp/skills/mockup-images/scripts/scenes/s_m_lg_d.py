import os,sys
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE); sys.path.insert(0,os.path.dirname(HERE))
from common import *
from s_m_leadgen import hero,title,dot,N,TEAL,OR
def card(y,h,head,col,body_html):
    return ('<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
            '<div style="height:80px;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:46px;font-weight:800;line-height:1.05">%s</div>'
            '<div style="padding:18px 28px">%s</div></div>')%(y,h,col,head,body_html)
def line(t,fs=42,bold=700,col='#1d2433',mt=0):
    return '<div style="font-size:%dpx;font-weight:%d;color:%s;line-height:1.22;margin-top:%dpx">%s</div>'%(fs,bold,col,mt,t)
# FSBO
fsbo_hero_m=hero('ph_kitchen','FSBO<br>leads','Find and win owner sellers')
rows=[('Online classifieds',TEAL),('Yard signs on your routes',N),('Community boards',TEAL),('Your sphere and neighbors',OR)]
c=title('Where to look for FSBO sellers',size=60)
y=190
for i,(t,col) in enumerate(rows):
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:140px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12)"></div>'%y)+dot(i+1,80,y+38,64,42,col)
    c+='<div class="abs" style="left:176px;top:%dpx;width:760px;font-size:44px;font-weight:700;color:#1d2433;line-height:140px;height:140px">%s</div>'%(y,t)
    y+=160
c+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:40px;font-weight:600;color:#667085;line-height:1.25">Check each owner has no agent agreement.</div>'%(y+10)
fsbo_where_m=page(c,'',note='',size=(1000,y+120))
P=[('Week 1','A short, honest letter'),('Week 2','A visit, or a call if allowed'),('Month 2','A local market update'),('Month 3','An offer to help again')]
c=title('A 90-day FSBO follow-up',size=60)
y=180
for i,(a,b_) in enumerate(P):
    col=[TEAL,TEAL,N,OR][i]
    c+=card(y,172,a,col,line(b_,44,700))
    y+=198
fsbo_plan_m=page(c,'',note='',size=(1000,y+10))
C=[('Letter','Wording is fair and accurate'),('Visit','Local solicitation rules'),('Call','Registry and your own list'),('Text','Written consent first')]
c=title('Check before first contact',size=60)
y=180
for i,(a,b_) in enumerate(C):
    col=[TEAL,N,OR,'#7c5cc4'][i]
    c+=card(y,172,a,col,line(b_,44,700))
    y+=198
fsbo_checks_m=page(c,'',note='',size=(1000,y+10))
# Zillow
zillow_hero_m=hero('ph_condo','Zillow leads<br>for agents','How they work and what to ask')
S=[('Receive the lead','Zillow connects a buyer or seller to you',TEAL),('Work the client','Reply fast and keep notes',TEAL),('The deal closes','Your commission is paid at closing',N),('Pay the fee','A share goes to Zillow',OR)]
c=title('Pay-when-you-close steps',size=60)
y=170
for i,(a,b_,col) in enumerate(S):
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:200px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12)"></div>'%y)+dot(i+1,80,y+30,64,42,col)
    c+='<div class="abs" style="left:176px;top:%dpx;width:760px;font-size:46px;font-weight:800;color:%s;line-height:1.1">%s</div><div class="abs" style="left:176px;top:%dpx;width:760px;font-size:40px;font-weight:600;color:#475467;line-height:1.2">%s</div>'%(y+24,N,a,y+88,b_)
    y+=224
c+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:38px;font-weight:600;color:#667085;line-height:1.25">General flow. Your terms may differ.</div>'%(y+6)
zillow_how_m=page(c,'',note='',size=(1000,y+90))
Q=['What share of my commission is the fee?','Which ZIP codes and price ranges apply?','What standards keep me in the program?','Which tools or CRM are required?','How long can a fee apply after a lead?']
c=title('Ask before you sign',size=64)
y=170
for i,q in enumerate(Q):
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:160px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12)"></div>'%y)+dot(i+1,80,y+48,64,42,[TEAL,TEAL,N,N,OR][i])
    c+='<div class="abs" style="left:176px;top:%dpx;width:760px;height:160px;display:flex;align-items:center;font-size:42px;font-weight:700;color:#1d2433;line-height:1.2">%s</div>'%(y,q)
    y+=182
zillow_questions_m=page(c,'',note='',size=(1000,y+20))
body=('<div style="display:flex;justify-content:space-between;align-items:baseline"><div style="font-size:42px;font-weight:600;color:#667085">Commission at closing</div><div style="font-size:52px;font-weight:800;color:#1d2433">$9,000</div></div>'
      '<div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:24px"><div style="font-size:42px;font-weight:600;color:#667085">Sample fee share, 30%</div><div style="font-size:52px;font-weight:800;color:'+OR+'">-$2,700</div></div>'
      '<div style="height:3px;background:#e4e7ec;margin:26px 0"></div>'
      '<div style="display:flex;justify-content:space-between;align-items:baseline"><div style="font-size:44px;font-weight:800;color:'+N+'">You keep</div><div style="font-size:56px;font-weight:800;color:'+TEAL+'">$6,300</div></div>')
c=title('Do the math on one closing',size=60)
c+='<div class="abs" style="left:50px;top:140px;width:900px;font-size:40px;font-weight:600;color:#667085">Sample numbers. Not Zillow\'s terms.</div>'
c+=card(230,430,'Sample closing',TEAL,body)
c+='<div class="abs" style="left:50px;top:700px;width:900px;font-size:42px;font-weight:700;color:#1d2433;line-height:1.25">Then add tools and your time. Divide by closings.</div>'
zillow_cost_m=page(c,'',note='',size=(1000,860))
SC=dict(fsbo_hero_m=fsbo_hero_m,fsbo_where_m=fsbo_where_m,fsbo_plan_m=fsbo_plan_m,fsbo_checks_m=fsbo_checks_m,zillow_hero_m=zillow_hero_m,zillow_how_m=zillow_how_m,zillow_questions_m=zillow_questions_m,zillow_cost_m=zillow_cost_m)
if __name__=='__main__': render(sel(sys.argv,SC))
