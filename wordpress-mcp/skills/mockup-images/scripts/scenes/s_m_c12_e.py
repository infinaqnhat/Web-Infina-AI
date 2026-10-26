import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
from s_m_leadgen import hero,title,dot,N,TEAL,OR
CARD='<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
def sub(t,y=140):
    return '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:40px;font-weight:600;color:#667085">%s</div>'%(y,t)
# ---- bài 9: warm leads ----
wl_hero_m=hero('ph_house','Warm leads<br>in your database','7 signals to look for')
S=[('They replied, even "not now"','Strong',TEAL),('They clicked a link','Strong',TEAL),('They asked about price or value','Strong',TEAL),
   ('They came back to your site','Medium',N),('They reappeared after months','Medium',N),('You heard about a life event','Medium',N),('They opened several emails','Weak',OR)]
c=title('Seven signals, strongest first',size=58)
c+=sub('Sample ranking. Our judgment.',130)
y=215
for i,(t,s,col) in enumerate(S):
    c+=(CARD%(y,118))+'</div>'+dot(i+1,72,y+28,62,38,col)
    c+='<div class="abs" style="left:156px;top:%dpx;width:560px;height:118px;display:flex;align-items:center;font-size:38px;font-weight:700;color:#1d2433;line-height:1.1">%s</div>'%(y,t)
    c+='<div class="abs" style="left:742px;top:%dpx;width:190px;height:118px;display:flex;align-items:center;justify-content:center"><div style="padding:8px 18px;border-radius:999px;background:%s;color:#fff;font-size:36px;font-weight:800">%s</div></div>'%(y,col,s)
    y+=136
wl_signals_m=page(c,'',note='',size=(1000,y+14))
L=[('A. Rivera','Clicked a value page','Mar 3','Send a value range today',TEAL),('B. Chen','Replied: "maybe next spring"','Mar 4','Ask what changes by spring',TEAL),
   ('C. Okafor','Visited three listings','Mar 5','Offer similar homes',N),('D. Lund','Back after 8 months','Mar 6','Ask what has changed',N),('E. Patel','Opened 3 emails, no click','Mar 6','Wait for a click or reply',OR)]
c=title('A weekly signal list',size=60)+sub('Sample list. Names and details are made up.',130)
y=205
for nm,sg,dt,nx,col in L:
    c+=(CARD%(y,200))+'<div style="height:64px;background:%s;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 28px;font-size:40px;font-weight:800"><span>%s</span><span style="font-size:36px;font-weight:600">%s</span></div>'%(col,nm,dt)
    c+='<div style="padding:12px 28px"><div style="font-size:38px;font-weight:700;color:#1d2433;line-height:1.2">%s</div><div style="font-size:38px;color:%s;font-weight:700;margin-top:6px;line-height:1.2">Next: %s</div></div></div>'%(sg,col,nx)
    y+=220
wl_list_m=page(c,'',note='',size=(1000,y+14))
M=[('After a reply','Thanks for the note, Ana. When do you think you might move?',TEAL),
   ('After a click','I saw you looked at the Maple St. home. Want two more like it?',N),
   ('After a value question','Here is a range and how I got it. Want me to walk you through it?',OR)]
c=title('Three short replies',size=62)+sub('Sample messages. Use your own voice.',130)
y=205
for lab,msg,col in M:
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:40px;font-weight:800;color:%s">%s</div>'%(y,col,lab))
    c+=('<div class="abs" style="left:50px;top:%dpx;width:860px;background:#fff;border-radius:28px 28px 28px 6px;box-shadow:0 6px 16px rgba(20,35,70,.12);padding:26px 32px;font-size:42px;font-weight:600;color:#1d2433;line-height:1.25;border-left:10px solid %s">%s</div>')%(y+62,col,msg)
    y+=330
wl_replies_m=page(c,'',note='',size=(1000,y))
# ---- bài 10: referral fee ----
rf_hero_m=hero('ph_living','Real estate<br>referral fee','Terms, math and rules')
def row(y,op,lab,val,col,h=170):
    return (CARD%(y,h))+'</div>'+('<div class="abs" style="left:78px;top:%dpx;width:80px;height:%dpx;display:flex;align-items:center;justify-content:center;font-size:62px;font-weight:800;color:%s">%s</div>'%(y,h,col,op))+\
      ('<div class="abs" style="left:170px;top:%dpx;width:420px;height:%dpx;display:flex;align-items:center;font-size:40px;font-weight:700;color:#475467;line-height:1.1">%s</div>'%(y,h,lab))+\
      ('<div class="abs" style="left:560px;top:%dpx;width:370px;height:%dpx;display:flex;align-items:center;justify-content:flex-end;font-size:58px;font-weight:800;color:%s">%s</div>'%(y,h,col,val))
c=title('Fee math on one sale',size=62)+sub('Sample numbers. Not a recommended rate.',135)
c+=row(210,'','Sale price','$400,000',N)+row(400,'×','Commission rate','2.5%',N)+row(590,'=','Commission','$10,000',TEAL)+row(780,'×','Fee percentage','25%',N)
c+=('<div class="abs" style="left:50px;top:970px;width:900px;height:190px;background:%s;border-radius:16px;display:flex;align-items:center;justify-content:space-between;padding:0 36px;color:#fff"><span style="font-size:44px;font-weight:700">Referral fee</span><span style="font-size:76px;font-weight:800">$2,500</span></div>'%OR)
rf_math_m=page(c,'',note='',size=(1000,1200))
F=[('Agent refers the client','The introduction',TEAL),('Agreement is signed','Fee, base, end date',TEAL),('The deal closes','No closing, no fee',N),
   ('Receiving brokerage is paid','Commission check arrives',N),('Referral share is paid','Broker to broker, then the agent',OR)]
c=title('How the fee moves',size=62)+sub('Sample flow. Ask your broker.',130)
y=205
for i,(a,b_,col) in enumerate(F):
    c+=(CARD%(y,150))+'</div>'+dot(i+1,76,y+43,64,40,col)
    c+='<div class="abs" style="left:170px;top:%dpx;width:760px;height:150px;display:flex;flex-direction:column;justify-content:center"><div style="font-size:44px;font-weight:800;color:#1d2433;line-height:1.1">%s</div><div style="font-size:36px;font-weight:600;color:#667085;margin-top:6px">%s</div></div>'%(y,a,b_)
    y+=172
rf_flow_m=page(c,'',note='',size=(1000,y+14))
T=[('Parties','Both agents and brokerages'),('Client','Name, contact, buying or selling'),('Fee','Percentage and what it is a percentage of'),
   ('Trigger','Paid only if the deal closes'),('Term','End date and what if the client switches'),('Signatures','Both agents, and brokers if required')]
c=('<div class="abs" style="left:50px;top:40px;width:900px;background:#fff;border-radius:12px;box-shadow:0 10px 26px rgba(20,35,70,.18);padding:36px 38px;height:1090px">'
   '<div style="font-size:36px;letter-spacing:.1em;font-weight:800;color:%s">TERM SHEET</div>'
   '<div style="font-size:56px;font-weight:800;color:#1d2433;line-height:1.1;margin-top:10px">Referral agreement</div>'
   '<div style="font-size:36px;color:#c2410c;font-weight:700;margin-top:10px;line-height:1.2">A checklist for your broker. Not a contract.</div>')%TEAL
for k,v in T:
    c+='<div style="margin-top:26px;border-top:3px solid #d6dce8;padding-top:16px"><div style="font-size:36px;font-weight:800;color:%s">%s</div><div style="font-size:40px;font-weight:600;color:#1d2433;line-height:1.2">%s</div></div>'%(N,k,v)
c+='</div>'
rf_terms_m=page(c,'',note='',size=(1000,1170))
SC=dict(wl_hero_m=wl_hero_m,wl_signals_m=wl_signals_m,wl_list_m=wl_list_m,wl_replies_m=wl_replies_m,rf_hero_m=rf_hero_m,rf_math_m=rf_math_m,rf_flow_m=rf_flow_m,rf_terms_m=rf_terms_m)
if __name__=='__main__': render(sel(sys.argv,SC))
