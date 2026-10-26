import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
from s_m_leadgen import hero,title,dot,N,TEAL,OR
from s_m_lg_b import CARD,head,cards,steps
# ---- bai 1 customer service
cs_hero_m=hero('ph_living','Real estate<br>customer service','Earn the next client')
c,y=steps('The first 12 months after closing',['Week 1: thank-you note and move-in list','Day 30: how is the move going?','Day 90: a useful local tip','Month 6: neighborhood market note','Month 12: home anniversary'],rowh=150,size=60)
cs_timeline_m=page(c,'',note='',size=(1000,y+20))
c,y=cards('When to ask for referrals',[(TEAL,'Good moment','Right after a smooth closing','The client is happy and has time'),(TEAL,'Good moment','After you solved a small problem','They just watched you deliver'),(OR,'Wait','While a problem is still open','Fix it first, then ask')],h=262,size=64)
cs_ask_m=page(c,'',note='',size=(1000,y+10))
c,y=cards('Who keeps each client',[(TEAL,'Client\'s agent','Keeps the touches for year one','Owner named in the client record'),(N,'Transaction coordinator','Answers closing paperwork questions','Hands the client back to the agent'),(OR,'Team lead','Reviews missed check-ins monthly','Sample roles, adjust to your team')],h=262,size=64)
cs_owner_m=page(c,'',note='',size=(1000,y+10))
# ---- bai 2 past client follow-up
pcf_hero_m=hero('ph_kitchen','Past client<br>follow-up','A plan for a busy year')
c,y=cards('One touch each quarter',[(TEAL,'Q1','Local market snapshot','Email'),(N,'Q2','Home anniversary note','Handwritten note'),(OR,'Q3','Seasonal tip or local event','Text, only with consent'),(TEAL,'Q4','Thank-you and a check-in question','Card or postcard')],h=250,size=64)
pcf_quarter_m=page(c,'',note='',size=(1000,y+10))
c,y=steps('Six steps to set it up',['List your past clients','Add the closing dates','Choose four touches a year','Write the messages','Schedule them in your CRM','Review once a year'],rowh=130,size=64)
pcf_steps_m=page(c,'',note='',size=(1000,y+20))
def bubble(top,label,text,col):
    return ('<div class="abs" style="left:50px;top:%dpx;width:900px;border-radius:16px;background:#fff;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
            '<div style="height:70px;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:42px;font-weight:800">%s</div>'
            '<div style="padding:22px 28px"><div style="background:#e9f1fb;border-radius:20px;padding:22px 26px;font-size:40px;line-height:1.3;color:#1d2433;font-weight:600">%s</div></div></div>')%(top,col,label,text)
c=title('Three sample touches',size=62)
c+=bubble(160,'Market note',"Homes on your street sold in about 3 weeks this spring. Want to see what yours might fetch?",TEAL)
c+=bubble(530,'Anniversary',"Happy one year in your home! How is it going? Glad to recommend a handyman if you need one.",N)
c+=bubble(900,'Thank-you',"Thank you for trusting me with your move. If a friend is thinking about one, I am glad to help.",OR)
c+='<div class="abs" style="left:50px;top:1270px;width:900px;font-size:36px;font-weight:600;color:#667085">Sample messages with made-up details.</div>'
pcf_msgs_m=page(c,'',note='',size=(1000,1340))
SC=dict(cs_hero_m=cs_hero_m,cs_timeline_m=cs_timeline_m,cs_ask_m=cs_ask_m,cs_owner_m=cs_owner_m,pcf_hero_m=pcf_hero_m,pcf_quarter_m=pcf_quarter_m,pcf_steps_m=pcf_steps_m,pcf_msgs_m=pcf_msgs_m)
if __name__=='__main__': render(sel(sys.argv,SC))
