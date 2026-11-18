import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
from s_m_leadgen import hero,title,dot,N,TEAL,OR
CARD='<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
def sub(t,y=140):
    return '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:40px;font-weight:600;color:#667085">%s</div>'%(y,t)
def pill(txt,col):
    return '<div style="padding:8px 20px;border-radius:999px;background:%s;color:#fff;font-size:38px;font-weight:800;white-space:nowrap">%s</div>'%(col,txt)
# ---- bài 6: newsletter ----
nl_hero_m=hero('ph_living','Real estate<br>newsletter','Templates and a plan')
M=[('Market snapshot','Rotate',TEAL),('Neighborhood news','Rotate',TEAL),('Recent sales','Rotate',TEAL),('One tip','Rotate',TEAL),('A question','Fixed',N),('Contact and opt-out','Fixed',N)]
c=title('Six modules, two stay fixed',size=58)+sub('Sample layout. Rotate the teal ones.',130)
y=215
for i,(t,tag,col) in enumerate(M):
    c+=(CARD%(y,120))+'</div>'+dot(i+1,72,y+30,60,38,col)
    c+='<div class="abs" style="left:156px;top:%dpx;width:520px;height:120px;display:flex;align-items:center;font-size:40px;font-weight:700;color:#1d2433;line-height:1.1">%s</div>'%(y,t)
    c+='<div class="abs" style="left:690px;top:%dpx;width:240px;height:120px;display:flex;align-items:center;justify-content:center">%s</div>'%(y,pill(tag,col))
    y+=138
nl_modules_m=page(c,'',note='',size=(1000,y+14))
c=('<div class="abs" style="left:50px;top:40px;width:900px;height:1065px;background:#fff;border-radius:14px;box-shadow:0 10px 26px rgba(20,35,70,.18);overflow:hidden">'
   '<div style="background:%s;color:#fff;padding:30px 36px"><div style="font-size:38px;letter-spacing:.1em;font-weight:800;color:#ffd9c9">MONTHLY NEWSLETTER</div><div style="font-size:54px;font-weight:800;line-height:1.1;margin-top:6px">Cedar Hills Update</div></div>'%N)
blocks=[('Market snapshot','Homes sold, days to sell, price direction. From your MLS report.',TEAL),
        ('Neighborhood news','One local story: a new park, a school event, a road change.',TEAL),
        ('One tip','Check the furnace filter before winter.',OR),
        ('Question for you','Thinking of moving this year? Reply with one word.',N)]
for lab,body,col in blocks:
    c+='<div style="padding:26px 36px 0"><div style="font-size:38px;font-weight:800;color:%s;line-height:1.1">%s</div><div style="font-size:40px;font-weight:600;color:#1d2433;line-height:1.2;margin-top:6px">%s</div></div><div style="margin:22px 36px 0;border-top:3px solid #e3e8f2"></div>'%(col,lab,body)
c+='<div style="padding:22px 36px;font-size:38px;color:#667085;font-weight:600;line-height:1.25">Cedar Hills Realty, 12 Main St, Sample City<br>Unsubscribe</div></div>'
nl_issue_m=page(c,'',note='',size=(1000,1145))
Q=[('Jan to Mar','Plan the year',TEAL,'Home value, taxes, spring prep'),('Apr to Jun','Market season',N,'Listing prep, local events'),('Jul to Sep','Summer pace',OR,'Home care, school return'),('Oct to Dec','Year-end',TEAL,'Maintenance, holiday notes')]
c=title('A twelve-month plan',size=62)+sub('Sample themes. Adjust for your market.',130)
y=215
for a,b_,col,d in Q:
    c+=(CARD%(y,190))+'<div style="height:78px;background:%s;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 30px;font-size:42px;font-weight:800"><span>%s</span><span>%s</span></div>'%(col,a,b_)
    c+='<div style="padding:20px 30px;font-size:42px;font-weight:600;color:#1d2433;line-height:1.2">%s</div></div>'%d
    y+=212
nl_cal_m=page(c,'',note='',size=(1000,y+14))
# ---- bài 7: subject lines ----
sj_hero_m=hero('ph_kitchen','Real estate email<br>subject lines','60 examples to test')
R=[('Be specific','The Maple Street home you saved'),('Be short','Key word first'),('Be honest','Match what is inside'),('Be personal','A name or a street'),('Ask one thing','One idea per email')]
c=title('Five rules for a subject line',size=58)+sub('Sample examples. Our suggestions.',130)
y=215
for i,(a,b_) in enumerate(R):
    c+=(CARD%(y,150))+'</div>'+dot(i+1,72,y+43,64,40,TEAL if i!=2 else OR)
    c+='<div class="abs" style="left:170px;top:%dpx;width:760px;height:150px;display:flex;flex-direction:column;justify-content:center"><div style="font-size:46px;font-weight:800;color:#1d2433;line-height:1.1">%s</div><div style="font-size:38px;font-weight:600;color:#667085;line-height:1.2;margin-top:4px">%s</div></div>'%(y,a,b_)
    y+=172
sj_rules_m=page(c,'',note='',size=(1000,y+14))
c=title('Count replies, not opens',size=62)+sub('Sample test. Counts are made up.',130)
for k,(lab,line,rep,col,y0) in enumerate([('A','Thanks for touring Oak Lane today','9 replies',N,210),('B','Notes from your visit, Ana','14 replies',TEAL,540)]):
    c+=(CARD%(y0,300))+'<div style="height:78px;background:%s;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 30px;font-size:42px;font-weight:800"><span>Subject %s</span><span>100 sent</span></div>'%(col,lab)
    c+='<div style="padding:22px 30px;font-size:44px;font-weight:700;color:#1d2433;line-height:1.2">"%s"</div><div style="padding:0 30px;font-size:58px;font-weight:800;color:%s">%s</div></div>'%(line,col,rep)
c+='<div class="abs" style="left:50px;top:870px;width:900px;height:130px;background:#fff7ed;border:4px solid %s;border-radius:16px;display:flex;align-items:center;padding:0 30px;font-size:42px;font-weight:800;color:#c2410c;line-height:1.15">B wins. Repeat before you decide.</div>'%OR
sj_test_m=page(c,'',note='',size=(1000,1030))
IN=[('Cedar Hills Realty','Thanks for touring Oak Lane...','Here are the answers to your two',TEAL),('Ana Rivera','Notes from your visit, Ana','I saved the two similar homes',N),
    ('Cedar Hills Realty','What changed in our market...','A short read on sales and prices',N),('Cedar Hills Realty','Still looking, Ana?','No rush. I can send new listings',N)]
c=title('How a phone inbox shows it',size=58)+sub('Sample inbox. Long lines get cut off.',130)
y=215
for frm,subj,prev,col in IN:
    c+=(CARD%(y,230))+'</div><div class="abs" style="left:78px;top:%dpx;width:80px;height:80px;border-radius:50%%;background:%s;color:#fff;font-size:42px;font-weight:800;display:flex;align-items:center;justify-content:center">%s</div>'%(y+24,col,frm[0])
    c+='<div class="abs" style="left:180px;top:%dpx;width:740px;height:230px;display:flex;flex-direction:column;justify-content:center"><div style="font-size:36px;font-weight:700;color:#667085;line-height:1.1">%s</div><div style="font-size:42px;font-weight:800;color:#1d2433;line-height:1.15;margin-top:4px">%s</div><div style="font-size:36px;font-weight:600;color:#667085;line-height:1.15;margin-top:4px">%s</div></div>'%(y,frm,subj,prev)
    y+=250
sj_inbox_m=page(c,'',note='',size=(1000,y+14))
SC=dict(nl_hero_m=nl_hero_m,nl_modules_m=nl_modules_m,nl_issue_m=nl_issue_m,nl_cal_m=nl_cal_m,sj_hero_m=sj_hero_m,sj_rules_m=sj_rules_m,sj_test_m=sj_test_m,sj_inbox_m=sj_inbox_m)
if __name__=='__main__': render(sel(sys.argv,SC))
