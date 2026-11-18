import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
from s_m_leadgen import hero,title,dot,N,TEAL,OR
CARD='<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
def head(col,t,h=80,fs=48):
    return '<div style="height:%dpx;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:%dpx;font-weight:800;line-height:1.05">%s</div>'%(h,col,fs,t)
def cards(ttl,rows,h=250,gap=26,top=180,size=64):
    c=title(ttl,size=size)
    y=240 if len(ttl)>25 else top
    for col,a,b_,c_ in rows:
        c+=(CARD%(y,h))+head(col,a)+'<div style="padding:20px 28px"><div style="font-size:44px;font-weight:700;color:#1d2433;line-height:1.2">%s</div><div style="font-size:38px;color:#475467;margin-top:10px;line-height:1.25">%s</div></div></div>'%(b_,c_)
        y+=h+gap
    return c,y
def steps(ttl,items,rowh=140,top=190,size=60):
    c=title(ttl,size=size); y=top
    cols=[TEAL,TEAL,N,N,OR]
    for i,s in enumerate(items):
        c+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12)"></div>'%(y,rowh)
        c+=dot(i+1,80,y+(rowh-64)//2,64,42,cols[i%5])
        c+='<div class="abs" style="left:176px;top:%dpx;width:760px;height:%dpx;font-size:42px;font-weight:700;color:#1d2433;line-height:1.15;display:flex;align-items:center">%s</div>'%(y,rowh,s)
        y+=rowh+20
    return c,y
# ---- bai 6 buyer leads
buyer_hero_m=hero('ph_living','Buyer leads','Find them. Qualify them.')
c,y=cards('Where buyer leads come from',[(TEAL,'Online','Search, portals and your website','Buyers browse before they call'),(OR,'In person','Open houses and neighbors','Same-day conversations'),(N,'People you know','Sphere, referrals and partners','Warm and slower to scale')],h=262)
buyer_sources_m=page(c,'',note='',size=(1000,y+10))
c,y=steps('Four questions for a new buyer lead',['When do you plan to buy?','Have you talked to a lender?','Which areas and price range?','Are you working with an agent?'],rowh=150)
buyer_qualify_m=page(c,'',note='',size=(1000,y+20))
c,y=cards('Match follow-up to the timeline',[(OR,'Touring this week','Call today','Offer to book showings'),(TEAL,'Buying in 3 to 6 months','Send matching listings weekly','Check in on the lender step'),(N,'Just researching','Monthly market note','Stay useful, no pressure')],h=262,size=60)
buyer_cadence_m=page(c,'',note='',size=(1000,y+10))
# ---- bai 7 free leads
free_hero_m=hero('ph_kitchen','Free real estate<br>leads','A zero-budget weekly plan')
W=[('Sphere outreach',3,TEAL),('Google Business Profile',1,N),('Social and local content',2,TEAL),('Open house or neighbors',4,OR),('Tracking and follow-up',1,N)]
c=title('A zero-budget week: 11 hours',size=60)
c+='<div class="abs" style="left:50px;top:140px;width:900px;font-size:40px;font-weight:600;color:#667085">Suggested hours. Adjust to your week.</div>'
y=215
for nm,h,col in W:
    c+=(CARD%(y,160))+'<div style="padding:16px 28px"><div style="font-size:42px;font-weight:800;color:#1d2433">%s</div><div style="margin-top:14px;display:flex;align-items:center;gap:18px"><div style="height:36px;width:%dpx;background:%s;border-radius:8px"></div><div style="font-size:42px;font-weight:800;color:%s">%d h</div></div></div></div>'%(nm,h*150,col,col,h)
    y+=180
free_week_m=page(c,'',note='',size=(1000,y+20))
c,y=cards('When free sources pay',[(OR,'Open houses','Same day','Meet buyers and neighbors'),(TEAL,'Your sphere','Days to weeks','Past clients and friends'),(N,'Profile, social and local content','Months','Slow, then steady')],h=262,size=62)
free_when_m=page(c,'',note='',size=(1000,y+10))
msg=('<div class="abs" style="left:50px;top:190px;width:900px;border-radius:16px;background:#fff;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
     '<div style="height:80px;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:46px;font-weight:800">Message to a past client</div>'
     '<div style="padding:28px"><div style="background:#e9f1fb;border-radius:20px;padding:26px 28px;font-size:44px;line-height:1.3;color:#1d2433;font-weight:600">Hi Dana, thank you for letting us help with your move. If you have a minute, a short Google review would mean a lot. Here is the link.</div>'
     '<div style="margin-top:22px;font-size:40px;font-weight:700;color:%s">Send it a week after closing</div></div></div>')%(TEAL,OR)
free_review_m=page(title('Ask for a review the easy way',size=60)+msg,'',note='',size=(1000,760))
# ---- bai 8 lead companies
co_hero_m=hero('ph_condo','Lead generation<br>companies','What you pay. What you sign.')
c,y=cards('Three ways they charge',[(TEAL,'Monthly fee','Fixed cost, results vary','You carry the risk'),(N,'Pay per lead','Price set per contact','Leads may be shared'),(OR,'Share at closing','Paid only after a deal closes','Ask your broker first')],h=262)
co_models_m=page(c,'',note='',size=(1000,y+10))
c,y=steps('Ask before you sign',['Exclusive or shared leads?','How long is the contract?','Who owns the lead data?','How fast are leads delivered?','Is there a referral fee?'],rowh=130,size=64)
co_questions_m=page(c,'',note='',size=(1000,y+20))
R=[('Company A','$2,400','1','$2,400',OR),('Company B','$1,800','2','$900',TEAL)]
c=title('Two vendors, two results',size=62)
c+='<div class="abs" style="left:50px;top:160px;width:900px;font-size:40px;font-weight:600;color:#667085">Sample numbers for two made-up vendors.</div>'
y=240
for nm,sp,cl,per,col in R:
    c+=(CARD%(y,250))+head(col,nm)+('<div style="display:flex;padding:22px 28px;gap:24px;align-items:flex-end">'
        '<div style="flex:1"><div style="font-size:38px;color:#667085;font-weight:600">Spend</div><div style="font-size:50px;font-weight:800;color:#1d2433">%s</div></div>'
        '<div style="flex:1"><div style="font-size:38px;color:#667085;font-weight:600">Closings</div><div style="font-size:50px;font-weight:800;color:#1d2433">%s</div></div>'
        '<div style="flex:1.1"><div style="font-size:38px;color:#667085;font-weight:600">Per closing</div><div style="font-size:50px;font-weight:800;color:%s">%s</div></div></div></div>')%(sp,cl,col,per)
    y+=276
co_cost_m=page(c,'',note='',size=(1000,y+10))
SC={k:v for k,v in dict(buyer_hero_m=buyer_hero_m,buyer_sources_m=buyer_sources_m,buyer_qualify_m=buyer_qualify_m,buyer_cadence_m=buyer_cadence_m,free_hero_m=free_hero_m,free_week_m=free_week_m,free_when_m=free_when_m,free_review_m=free_review_m,co_hero_m=co_hero_m,co_models_m=co_models_m,co_questions_m=co_questions_m,co_cost_m=co_cost_m).items()}
if __name__=='__main__': render(sel(sys.argv,SC))
