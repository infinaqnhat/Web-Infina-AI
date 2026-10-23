import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
from s_m_leadgen import hero,title,dot,N,TEAL,OR
def card(y,head,lines,col,h=None,hh=84,bold=True):
    h=h or (hh+36+len(lines)*66)
    s=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
       '<div style="height:%dpx;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:44px;font-weight:800;line-height:1.1">%s</div>'
       '<div style="padding:18px 28px">')%(y,h,hh,col,head)
    for i,l in enumerate(lines):
        s+='<div style="font-size:%dpx;font-weight:%d;color:%s;line-height:1.28;margin-bottom:8px">%s</div>'%(42 if i==0 else 40,700 if i==0 else 500,'#1d2433' if i==0 else '#475467',l)
    s+='</div></div>'
    return s,y+h+26
# ---- bai 9 expired scripts
exp_hero_m=hero('ph_condo','Expired listing<br>scripts','What to say. How to follow up.')
c=title('The first 20 seconds',size=64); y=150
for head,l,col in [('1  Say who you are','Name and brokerage',TEAL),('2  Say why you called','Your home on Oak Lane came off the market',N),('3  Ask permission','Do you have a minute?',OR)]:
    s,y=card(y,head,[l],col,h=210); c+=s
exp_open_m=page(c,'',note='',size=(1000,y+20))
c=title('Objections and replies',size=64); y=150
for head,l,col in [('We will relist with the same agent','That is fair. What would you want done differently?',TEAL),('We are taking it off the market','Understood. Would a value update help later?',N),('Too many agents have called','I will be brief. May I send one short note?',OR)]:
    s,y=card(y,head,[l],col,h=250,hh=110); c+=s
exp_objections_m=page(c,'',note='',size=(1000,y+20))
c=title('A three-week touch plan',size=64); y=170
for i,(d,a) in enumerate([('Day 1','Call'),('Day 2','Letter'),('Day 5','Call again'),('Day 10','Email'),('Day 21','Mailer or note')]):
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:140px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12)"></div>'%y)
    c+='<div class="abs" style="left:80px;top:%dpx;width:230px;font-size:50px;font-weight:800;color:%s;line-height:140px">%s</div>'%(y,[TEAL,TEAL,N,N,OR][i],d)
    c+='<div class="abs" style="left:330px;top:%dpx;width:600px;font-size:48px;font-weight:700;color:#1d2433;line-height:140px">%s</div>'%(y,a)
    y+=160
exp_touch_m=page(c,'',note='',size=(1000,y+30))
# ---- bai 13 sign in sheet
sign_hero_m=hero('ph_living','Open house<br>sign in sheet','Free template. Consent wording.')
sheet=('<div class="abs" style="left:50px;top:170px;width:900px;background:#fff;border-radius:12px;box-shadow:0 10px 26px rgba(20,35,70,.2);overflow:hidden">'
 '<div style="background:'+N+';color:#fff;padding:22px 28px"><div style="font-size:52px;font-weight:800;line-height:1.1">Open house sign in</div><div style="font-size:40px;font-weight:500;margin-top:6px;color:#cfd8ea">Sample address: 12 Oak Lane</div></div>'
 '<div style="display:flex;padding:14px 28px;background:#eef2fb;font-size:40px;font-weight:800;color:'+N+'"><div style="flex:1.2">Name</div><div style="flex:1.3">Phone</div><div style="flex:1">Agent?</div></div>')
for nm,ph,ag in [('A. Rivera','555-0101','No'),('J. Chen','555-0102','Yes'),('M. Okafor','555-0103','No')]:
    sheet+='<div style="display:flex;padding:20px 28px;border-top:2px solid #e4e7ec;font-size:42px;font-weight:600;color:#1d2433"><div style="flex:1.2">%s</div><div style="flex:1.3">%s</div><div style="flex:1">%s</div></div>'%(nm,ph,ag)
sheet+='<div style="display:flex;align-items:center;gap:18px;padding:24px 28px;border-top:2px solid #e4e7ec;background:#fff7f1"><span style="display:inline-block;width:46px;height:46px;border:5px solid '+OR+';border-radius:8px;flex:none"></span><span style="font-size:42px;font-weight:700;color:#1d2433;line-height:1.2">OK to text me about this home</span></div></div>'
sign_sheet_m=page(title('What the sheet looks like',size=60)+sheet,'',note='',size=(1000,880))
c=title('Three jobs for consent',size=64)
c+=('<div class="abs" style="left:50px;top:190px;width:900px;background:#fff;border-radius:16px;box-shadow:0 8px 20px rgba(20,35,70,.15);padding:30px 28px;display:flex;gap:20px">'
    '<span style="display:inline-block;width:56px;height:56px;border:5px solid '+OR+';border-radius:10px;flex:none;margin-top:6px"></span>'
    '<span style="font-size:42px;font-weight:600;color:#1d2433;line-height:1.3">Yes, my agent may contact me by phone, text and email. Signing is optional.</span></div>')
y=520
for i,(h,t) in enumerate([('Who may contact you','Name the agent'),('How they may reach you','Phone, text, email'),('It is a choice','Signing is optional')]):
    c+=dot(i+1,50,y,64,42,[TEAL,N,OR][i])+'<div class="abs" style="left:140px;top:%dpx;width:810px;font-size:44px;font-weight:800;color:#1d2433;line-height:1.1">%s</div><div class="abs" style="left:140px;top:%dpx;width:810px;font-size:40px;font-weight:500;color:#475467">%s</div>'%(y-2,h,y+52,t)
    y+=150
sign_consent_m=page(c,'',note='',size=(1000,y+10))
c=title('Follow up by timeline',size=64); y=150
for head,l,col in [('Touring this month','Call today',TEAL),('Buying within 3 months','Email today, call this week',N),('Just looking','Monthly market note',OR)]:
    s,y=card(y,head,[l],col,h=230,hh=100); c+=s
sign_followup_m=page(c,'',note='',size=(1000,y+20))
# ---- bai 11 probate
prob_hero_m=hero('ph_kitchen','Probate<br>real estate leads','Earn the listing with patience.')
c=title('Where probate leads start',size=64); y=150
for head,ls,col in [('Referral partners',['Probate attorneys and estate planners','The people the family already trusts'],TEAL),('Public court records',['County filings, where available','Access and rules differ by county'],N),('Paid lead lists',['Check accuracy and the registry','Never assume a number can be called'],OR)]:
    s,y=card(y,head,ls,col,h=300,hh=96); c+=s
prob_sources_m=page(c,'',note='',size=(1000,y+20))
letter=('<div class="abs" style="left:70px;top:150px;width:860px;background:#fff;border-radius:6px;box-shadow:0 14px 30px rgba(20,35,70,.22);padding:56px 56px 60px;font-family:Lora,serif">'
        '<div style="font-size:46px;font-weight:700;color:#1d2433;line-height:1.3">Dear [Name],</div>'
        '<div style="font-size:44px;color:#1d2433;line-height:1.4;margin-top:26px">I am sorry for your loss.</div>'
        '<div style="font-size:44px;color:#1d2433;line-height:1.4;margin-top:22px">When you are ready, I can explain how a sale could work.</div>'
        '<div style="font-size:44px;color:#1d2433;line-height:1.4;margin-top:22px">There is no pressure and no reply is needed.</div>'
        '<div style="font-size:44px;font-weight:700;color:#1d2433;line-height:1.3;margin-top:40px">[Agent name]</div></div>')
prob_letter_m=page(letter,'',note='',size=(1000,860))
c=title('Five steps, in this order',size=64); y=170
for i,s in enumerate(['Send a short, kind note','Work through the attorney','Offer information first','Wait for an invitation','Follow up gently']):
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:140px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12)"></div>'%y)+dot(i+1,80,y+38,64,42,[TEAL,TEAL,N,N,OR][i])
    c+='<div class="abs" style="left:176px;top:%dpx;width:760px;font-size:46px;font-weight:700;color:#1d2433;line-height:140px;height:140px">%s</div>'%(y,s)
    y+=160
prob_steps_m=page(c,'',note='',size=(1000,y+30))
SC=dict(exp_hero_m=exp_hero_m,exp_open_m=exp_open_m,exp_objections_m=exp_objections_m,exp_touch_m=exp_touch_m,
        sign_hero_m=sign_hero_m,sign_sheet_m=sign_sheet_m,sign_consent_m=sign_consent_m,sign_followup_m=sign_followup_m,
        prob_hero_m=prob_hero_m,prob_sources_m=prob_sources_m,prob_letter_m=prob_letter_m,prob_steps_m=prob_steps_m)
if __name__=='__main__': render(sel(sys.argv,SC))
