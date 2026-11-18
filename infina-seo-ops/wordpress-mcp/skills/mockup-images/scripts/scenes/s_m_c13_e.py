import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
from s_m_leadgen import hero,title,dot,N,TEAL,OR
CARD='<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
def sub(t,y=140):
    return '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:40px;font-weight:600;color:#667085">%s</div>'%(y,t)
# ---- bài 8: bad drip campaign ----
bd_hero_m=hero('ph_aerial','Bad drip<br>campaign','How to audit yours')
P=[('One message for everyone','Buyer and past client get the same email'),
   ('No stop on reply','A reply, then another scheduled email'),
   ('Too many, too fast','Three emails in three days'),
   ('No clear opt-out','No unsubscribe link or address'),
   ('Misleading subject','"Re: our call" with no call'),
   ('Stale content','A spring email sent in November'),
   ('No goal per email','Four asks in one message'),
   ('Broken personalization','"Hi {first_name}"')]
c=title('Eight problems to check',size=62)+sub('Sample list. Our judgment.',130)
y=205
for i,(a,b_) in enumerate(P):
    col=OR if i in (1,3) else (TEAL if i%2==0 else N)
    c+=(CARD%(y,128))+'</div>'+dot(i+1,72,y+34,60,38,col)
    c+='<div class="abs" style="left:156px;top:%dpx;width:780px;height:128px;display:flex;flex-direction:column;justify-content:center"><div style="font-size:42px;font-weight:800;color:#1d2433;line-height:1.1">%s</div><div style="font-size:38px;font-weight:600;color:#667085;margin-top:4px;line-height:1.1">%s</div></div>'%(y,a,b_)
    y+=144
c+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:40px;font-weight:700;color:%s">Fix the orange two first.</div>'%(y+4,OR)
bd_problems_m=page(c,'',note='',size=(1000,y+80))
A=[('Enroll a test lead','1 min',TEAL),('Read every email on your phone','3 min',N),('Click every link','2 min',TEAL),
   ('Reply to the test email','1 min',OR),('Check the footer','1 min',N),('Read the dates and offers','2 min',TEAL)]
c=title('The ten-minute audit',size=64)+sub('Sample timing. Adjust it to your sequence.',130)
y=205
for i,(t,m,col) in enumerate(A):
    c+=(CARD%(y,130))+'</div>'+dot(i+1,72,y+35,60,38,col)
    c+='<div class="abs" style="left:156px;top:%dpx;width:580px;height:130px;display:flex;align-items:center;font-size:42px;font-weight:700;color:#1d2433;line-height:1.1">%s</div>'%(y,t)
    c+='<div class="abs" style="left:742px;top:%dpx;width:190px;height:130px;display:flex;align-items:center;justify-content:center"><div style="padding:8px 20px;border-radius:999px;background:%s;color:#fff;font-size:40px;font-weight:800">%s</div></div>'%(y,col,m)
    y+=146
c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:110px;background:%s;border-radius:16px;display:flex;align-items:center;justify-content:space-between;padding:0 36px;color:#fff"><span style="font-size:44px;font-weight:700">Total</span><span style="font-size:60px;font-weight:800">10 min</span></div>')%(y+6,N)
bd_audit_m=page(c,'',note='',size=(1000,y+150))
c=title('A reply should stop the emails',size=58)+sub('Sample flow. The fix is our suggestion.',135)
def box(y,h,col,label,steps,mark):
    s=(CARD%(y,h))+'<div style="height:78px;background:%s;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 28px;font-size:46px;font-weight:800"><span>%s</span><span>%s</span></div><div style="padding:8px 28px">'%(col,label,mark)
    for k in steps:
        s+='<div style="font-size:42px;font-weight:700;color:#1d2433;line-height:1.2;margin-top:14px">%s</div>'%k
    return s+'</div></div>'
c+=box(215,330,OR,'Bad drip campaign','',  'X') .replace('<div style="padding:8px 28px"></div>','<div style="padding:8px 28px"><div style="font-size:42px;font-weight:700;color:#1d2433;line-height:1.2;margin-top:14px">1. Lead replies: "Not yet, maybe spring"</div><div style="font-size:42px;font-weight:700;color:#1d2433;line-height:1.2;margin-top:14px">2. Email 4 still goes out</div><div style="font-size:42px;font-weight:700;color:%s;line-height:1.2;margin-top:14px">3. Lead feels ignored</div></div>'%OR)
c+=box(580,425,TEAL,'Good drip campaign',['1. Lead replies: "Not yet, maybe spring"','2. The sequence pauses at once','3. You answer, in your own voice','4. Resume later only if it fits'],'OK')
bd_stop_m=page(c,'',note='',size=(1000,1030))
# ---- bài 9: video email for real estate ----
ve_hero_m=hero('ph_condo','Video email<br>for real estate','30 to 60 seconds')
S=[('1','Who you are','"Hi Ana, this is Sam from Cedar Hills Realty."',TEAL),
   ('2','Why you are writing','"I saw you asked about homes near the park."',N),
   ('3','What happens next','"Is spring still your plan? Just reply and tell me."',OR)]
c=title('A three-line script',size=64)+sub('Sample script. Names are made up.',130)
y=205
for n,lab,q,col in S:
    c+=(CARD%(y,250))+'<div style="height:84px;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:46px;font-weight:800">%s. %s</div>'%(col,n,lab)
    c+='<div style="padding:22px 28px;font-size:44px;font-weight:600;color:#1d2433;line-height:1.25;font-style:italic">%s</div></div>'%q
    y+=272
c+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:40px;font-weight:700;color:%s">About ten seconds. One idea.</div>'%(y,TEAL)
ve_script_m=page(c,'',note='',size=(1000,y+90))
c=('<div class="abs" style="left:50px;top:40px;width:900px;height:880px;background:#fff;border-radius:12px;box-shadow:0 10px 26px rgba(20,35,70,.18);overflow:hidden">'
   '<div style="padding:26px 34px;background:#eef2f9;border-bottom:3px solid #d6dce8"><div style="font-size:38px;font-weight:700;color:#667085">Subject</div><div style="font-size:46px;font-weight:800;color:#1d2433;line-height:1.15;margin-top:6px">A quick hello from Cedar Hills Realty</div></div>'
   '<div style="padding:28px 34px"><div style="font-size:42px;font-weight:600;color:#1d2433;line-height:1.25">Hi Ana, I made a short video for you.</div>'
   '<div style="margin-top:26px;height:380px;border-radius:14px;background:linear-gradient(135deg,#1b2a4a,#14808a);display:flex;align-items:center;justify-content:center;position:relative">'
   '<div style="width:140px;height:140px;border-radius:50%%;background:#fff;display:flex;align-items:center;justify-content:center"><div style="width:0;height:0;border-top:36px solid transparent;border-bottom:36px solid transparent;border-left:62px solid %s;margin-left:14px"></div></div>'
   '<div style="position:absolute;left:24px;bottom:18px;font-size:40px;font-weight:800;color:#fff">Watch (45 sec)</div></div>'
   '<div style="font-size:42px;font-weight:700;color:%s;line-height:1.25;margin-top:26px">Is spring still your plan? Just reply.</div>'
   '<div style="margin-top:28px;border-top:3px solid #d6dce8;padding-top:14px;font-size:38px;font-weight:600;color:#667085;line-height:1.25">Sam, Cedar Hills Realty<br>100 Sample St. Unsubscribe</div></div></div>')%(N,OR)
ve_send_m=page(c,'',note='',size=(1000,960))
T=[('Day 0','Send the video link',TEAL),('Day 1','Reply fast if they answer',TEAL),('Day 4','One short email nudge',N),('Day 10','Back to your drip emails',N)]
c=title('After the video',size=64)+sub('Sample days. Our suggestion, not a rule.',130)
y=205
for i,(d,t,col) in enumerate(T):
    c+=(CARD%(y,150))+'<div style="position:absolute;left:0;top:0;width:210px;height:150px;background:%s;color:#fff;display:flex;align-items:center;justify-content:center;font-size:48px;font-weight:800">%s</div>'%(col,d)
    c+='<div style="position:absolute;left:236px;top:0;width:640px;height:150px;display:flex;align-items:center;font-size:42px;font-weight:700;color:#1d2433;line-height:1.15">%s</div></div>'%t
    y+=170
c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:150px;background:%s;border-radius:16px;display:flex;align-items:center;padding:0 36px;color:#fff;font-size:44px;font-weight:800;line-height:1.2">Any reply: stop the automatic emails and answer yourself.</div>')%(y+16,OR)
ve_follow_m=page(c,'',note='',size=(1000,y+200))
SC=dict(bd_hero_m=bd_hero_m,bd_problems_m=bd_problems_m,bd_audit_m=bd_audit_m,bd_stop_m=bd_stop_m,ve_hero_m=ve_hero_m,ve_script_m=ve_script_m,ve_send_m=ve_send_m,ve_follow_m=ve_follow_m)
if __name__=='__main__': render(sel(sys.argv,SC))
