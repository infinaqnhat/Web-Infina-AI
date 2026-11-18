import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
from s_m_leadgen import hero,title,dot,N,TEAL,OR
from s_m_lg_b import CARD,head,cards,steps
# Cum 13 fork C: bai 4 comparative market analysis (cma_), bai 5 CMA template (cmt_)
def tbl(ttl,hdr,rows,widths,top=190,rowh=130,fs=42,size=60,last_bold=False):
    c=title(ttl,size=size)
    y=top
    x0=50
    # header
    c+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:%s;border-radius:16px 16px 0 0;display:flex;align-items:center">'%(y,rowh-30,N)
    for w,h in zip(widths,hdr):
        c+='<div style="width:%dpx;padding:0 22px;font-size:40px;font-weight:800;color:#fff;line-height:1.1">%s</div>'%(w,h)
    c+='</div>'
    y+=rowh-30
    for i,r in enumerate(rows):
        bg='#fff' if i%2==0 else '#f3f6fb'
        bold = last_bold and i==len(rows)-1
        c+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:%s;display:flex;align-items:center;box-shadow:0 3px 8px rgba(20,35,70,.08)">'%(y,rowh,bg)
        for j,(w,t) in enumerate(zip(widths,r)):
            col=OR if (bold and j>0) else '#1d2433'
            c+='<div style="width:%dpx;padding:0 22px;font-size:%dpx;font-weight:%d;color:%s;line-height:1.15">%s</div>'%(w,fs,800 if (j==0 or bold) else 700,col,t)
        c+='</div>'
        y+=rowh
    return c,y
def note(y,t,size=36):
    return '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:%dpx;font-weight:600;color:#667085;line-height:1.25">%s</div>'%(y,size,t)

# ---- bai 4: how to do a CMA
cma_hero_m=hero('ph_house','Comparative<br>market analysis','How to do a CMA')
c,y=steps('Five steps of a CMA',['Profile the subject home','Pick recent comparable sales','Adjust for the differences','Set a price range','Present it to the seller'],rowh=140,size=62)
cma_steps_m=page(c,'',note='',size=(1000,y+20))
c,y=cards('Adjusting one comp',[(TEAL,'Comp sold for','$400,000','Sample number'),(OR,'It has a garage you lack','Minus $10,000','Sample adjustment'),(N,'You have a newer kitchen','Plus $6,000','Sample adjustment'),(TEAL,'Adjusted value','$396,000','Sample, not an appraisal')],h=235,size=64)
cma_adjust_m=page(c,'',note='',size=(1000,y+10))
c,y=cards('One CMA email a year',[(TEAL,'Subject line','What is your home worth this year?','Sample wording'),(N,'Body','Two lines and your price range','Keep it short and personal'),(OR,'Attach','A one-page summary','Offer a call, no pressure')],h=262,size=64)
cma_touch_m=page(c,'',note='',size=(1000,y+10))

# ---- bai 5: CMA template
cmt_hero_m=hero('ph_aerial','CMA template','One page, three tables')
c,y=tbl('Table 1: the comps',['Comp','Sold','Beds / baths'],[['A. Sample St','$400,000','3 / 2'],['B. Sample Ave','$405,000','3 / 2'],['C. Sample Rd','$398,000','4 / 2']],[370,270,260],rowh=140,fs=44,size=64)
c+=note(y+30,'Made-up addresses and prices. Use sales from the last few months near the subject home.')
cmt_comps_m=page(c,'',note='',size=(1000,y+130))
c,y=tbl('Table 2: the adjustments',['Difference','Comp','Change'],[['Garage','A','-$10,000'],['Kitchen','A','+$6,000'],['Lot size','B','-$3,500'],['Extra bedroom','C','-$8,000']],[400,140,360],rowh=135,fs=44,size=64)
c+=note(y+30,'Sample adjustments only. Explain each one in a few words.')
cmt_adj_m=page(c,'',note='',size=(1000,y+130))
c,y=tbl('Table 3: the summary',['Comp','Adjusted','Weight'],[['A','$396,000','High'],['B','$401,500','Medium'],['C','$390,000','Low'],['Range','$390,000 to $401,500','']],[200,440,260],rowh=140,fs=44,size=64,last_bold=True)
c+=note(y+30,'Sample. Not an appraisal. A CMA is an agent\'s opinion of the likely sale price.')
cmt_summary_m=page(c,'',note='',size=(1000,y+130))
SC=dict(cma_hero_m=cma_hero_m,cma_steps_m=cma_steps_m,cma_adjust_m=cma_adjust_m,cma_touch_m=cma_touch_m,cmt_hero_m=cmt_hero_m,cmt_comps_m=cmt_comps_m,cmt_adj_m=cmt_adj_m,cmt_summary_m=cmt_summary_m)
if __name__=='__main__': render(sel(sys.argv,SC))
