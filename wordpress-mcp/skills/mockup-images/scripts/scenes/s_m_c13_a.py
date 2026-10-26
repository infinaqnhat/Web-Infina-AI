import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
from s_m_leadgen import hero,title,dot,N,TEAL,OR
from s_m_lg_b import CARD,head,cards,steps
# ---- pillar: real estate drip email
de_hero_m=hero('ph_house','Real estate<br>drip email','Build it in five steps')
c,y=steps('Five steps to a drip campaign',['Segment your list','Give each email one goal','Write and order six emails','Stop the series when a lead replies','Measure replies, not opens'],rowh=150,size=60)
de_steps_m=page(c,'',note='',size=(1000,y+20))
F=[('Day 0','Welcome','Thanks for reaching out, a quick question',TEAL),('Day 3','Useful guide','A short checklist for your next step',TEAL),('Day 10','Local note','What is happening on your street this month',N),('Day 17','Proof','How one family handled a tight timeline',N),('Day 28','Question','Is your timeline still the same?',OR),('Day 42','Soft offer','Want a 15-minute plan for your move?',OR)]
c=title('A six-email frame',size=62)
c+='<div class="abs" style="left:50px;top:140px;width:900px;font-size:38px;font-weight:600;color:#667085">Sample timing and subject lines.</div>'
y=215
for d,g,s,col in F:
    c+=(CARD%(y,200))+'<div style="display:flex;height:200px"><div style="width:190px;background:%s;color:#fff;display:flex;align-items:center;justify-content:center;font-size:48px;font-weight:800">%s</div><div style="padding:18px 24px;flex:1"><div style="font-size:44px;font-weight:800;color:#1d2433">%s</div><div style="font-size:38px;color:#475467;margin-top:8px;line-height:1.2">%s</div></div></div></div>'%(col,d,g,s)
    y+=222
de_frame_m=page(c,'',note='',size=(1000,y+20))
c,y=cards('When a campaign stops',[(TEAL,'Pause','The lead replies','Answer in your own words'),(N,'Pause','An appointment is booked','Move to a call and a showing'),(OR,'End','Someone unsubscribes','Honor it within 10 business days')],h=262,size=64)
de_stop_m=page(c,'',note='',size=(1000,y+10))
# ---- bai 1: drip campaign templates
dt_hero_m=hero('ph_condo','Drip campaign<br>templates','Four sequences to copy')
c,y=cards('Four sequences at a glance',[(TEAL,'Buyer','6 emails over about 6 weeks','Learn what they want'),(OR,'Seller','5 emails over about 5 weeks','Offer a short conversation'),(N,'Open house','4 emails over about 2 weeks','Move fast while it is fresh'),(TEAL,'Past client','4 touches a year','Stay in mind for referrals')],h=250,size=62)
dt_overview_m=page(c,'',note='',size=(1000,y+10))
c,y=steps('Buyer sequence: six emails',['Day 0: welcome, ask what they want','Day 3: a short buying checklist','Day 10: homes that match their answers','Day 17: a neighborhood they asked about','Day 28: a light question on financing','Day 42: offer a 15-minute plan call'],rowh=140,size=60)
dt_buyer_m=page(c,'',note='',size=(1000,y+20))
em=('<div class="abs" style="left:50px;top:190px;width:900px;border-radius:16px;background:#fff;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
   '<div style="height:80px;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:44px;font-weight:800">Same day: open house thank-you</div>'
   '<div style="padding:28px"><div style="font-size:38px;font-weight:700;color:#667085">Subject</div><div style="font-size:44px;font-weight:800;color:#1d2433;margin-bottom:22px">Thanks for stopping by</div>'
   '<div style="background:#e9f1fb;border-radius:20px;padding:26px 28px;font-size:42px;line-height:1.3;color:#1d2433;font-weight:600">Hi Taylor, thanks for visiting the open house at 12 Sample Street. The property sheet is attached. If you would like a second look, reply with a day that suits you.</div>'
   '<div style="margin-top:22px;font-size:38px;font-weight:700;color:%s">Footer: name, address, unsubscribe link</div></div></div>')%(TEAL,OR)
dt_openhouse_m=page(title('A sample first email',size=62)+em+'<div class="abs" style="left:50px;top:960px;width:900px;font-size:36px;font-weight:600;color:#667085">Sample email. Names and address are made up.</div>','',note='',size=(1000,1030))
SC=dict(de_hero_m=de_hero_m,de_steps_m=de_steps_m,de_frame_m=de_frame_m,de_stop_m=de_stop_m,dt_hero_m=dt_hero_m,dt_overview_m=dt_overview_m,dt_buyer_m=dt_buyer_m,dt_openhouse_m=dt_openhouse_m)
if __name__=='__main__': render(sel(sys.argv,SC))
