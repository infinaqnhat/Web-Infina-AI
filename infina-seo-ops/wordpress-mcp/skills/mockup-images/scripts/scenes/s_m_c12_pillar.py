import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
from s_m_leadgen import title,dot,N,TEAL,OR
from s_m_lg_b import CARD,steps
# ---- pillar #2330 refresh (Cum 12): touches per quarter by tier, and the first 30 days after closing
def tier_card(top,col,letter,name,per_year,cells):
    c=(CARD%(top,270))
    c+=('<div style="height:90px;background:%s;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 28px">'
        '<div style="font-size:50px;font-weight:800">Tier %s: %s</div><div style="font-size:46px;font-weight:800">%s a year</div></div>')%(col,letter,name,per_year)
    c+='<div style="display:flex;gap:14px;padding:22px 28px">'
    for q,n in cells:
        on=n>0
        c+=('<div style="flex:1;height:130px;border-radius:12px;background:%s;color:%s;display:flex;flex-direction:column;align-items:center;justify-content:center">'
            '<div style="font-size:38px;font-weight:700;opacity:.85">%s</div><div style="font-size:56px;font-weight:800;line-height:1.1">%s</div></div>')%('#e9f1fb' if on else '#f2f4f7','#1b2a4a' if on else '#98a2b3',q,n if on else '-')
    c+='</div></div>'
    return c
c=title('Touches per quarter, by tier',size=62)
c+='<div class="abs" style="left:50px;top:140px;width:900px;font-size:40px;font-weight:600;color:#667085">A suggested rhythm. Adjust it to your market.</div>'
c+=tier_card(215,TEAL,'A','closest',12,[('Q1',3),('Q2',3),('Q3',3),('Q4',3)])
c+=tier_card(515,N,'B','know your work',4,[('Q1',1),('Q2',1),('Q3',1),('Q4',1)])
c+=tier_card(815,OR,'C','distant',2,[('Q1',1),('Q2',0),('Q3',1),('Q4',0)])
soi_tiers_m=page(c,'',note='',size=(1000,1115))
c,y=steps('The first 30 days after closing',['Closing day: handwritten thank-you note','Week 1: a short move-in list','Day 30: "How is the move going?"','Same week: add tier and dates to your list'],rowh=150,size=62)
soi_30days_m=page(c,'',note='',size=(1000,y+20))
SC=dict(soi_tiers_m=soi_tiers_m,soi_30days_m=soi_30days_m)
if __name__=='__main__': render(sel(sys.argv,SC))
