import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
# 1. two sample farms scored on turnover
def card(y,name,homes,sales,pct,verdict,col,bg,bd):
    s='<div class="abs" style="left:50px;top:%dpx;width:900px;height:400px;background:%s;border:3px solid %s;border-radius:16px">'%(y,bg,bd)
    s+='<div style="position:absolute;left:34px;top:24px;font-size:50px;font-weight:800;color:%s">%s</div>'%(N,name)
    s+='<div style="position:absolute;left:34px;top:100px;font-size:42px;color:#475467;font-weight:600">%s homes, %s sales in 12 months</div>'%(homes,sales)
    s+='<div style="position:absolute;left:34px;top:170px;font-size:110px;font-weight:800;color:%s;line-height:1">%s</div>'%(col,pct)
    s+='<div style="position:absolute;left:300px;top:200px;font-size:42px;font-weight:700;color:%s">turnover</div>'%col
    s+='<div style="position:absolute;left:34px;top:310px;font-size:42px;font-weight:800;color:%s">%s</div></div>'%(col,verdict)
    return s
h='<div class="abs" style="left:50px;top:40px;font-size:62px;font-weight:800;color:'+N+';line-height:1.1">Score a farm on turnover</div>'
h+='<div class="abs" style="left:50px;top:125px;font-size:40px;color:#667085;font-weight:600">Sales divided by homes, times 100</div>'
h+=card(215,'Sample farm A','500','25','5%','Below the 6 to 7% guide','#b42318','#fff1f0','#f3b6b0')
h+=card(650,'Sample farm B','500','40','8%','Above the 6 to 7% guide','#116b43','#edf8f1','#a9dbbd')
farm_score_m=page(h,'',note='',size=(1000,1090))
# 2. 12 month calendar
rows=[('Month 1','Set up','Pick the farm, build the list','#667085'),('Months 2 to 4','Introduce yourself','First mailer, notes, a few doors a week','#14808a'),('Months 5 to 8','Be useful','Market updates, recent sales, one event','#14808a'),('Months 9 to 12','Ask and review','Value offer, follow up, judge the farm','#1b2a4a')]
h='<div class="abs" style="left:50px;top:40px;font-size:62px;font-weight:800;color:'+N+';line-height:1.1">Your farming year</div>'
y=150
for a,b,c,col in rows:
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:250px;background:#fff;border:3px solid #d0d7e2;border-left:14px solid %s;border-radius:14px"><div style="position:absolute;left:34px;top:18px;font-size:40px;font-weight:700;color:#667085">%s</div><div style="position:absolute;left:34px;top:70px;font-size:56px;font-weight:800;color:%s">%s</div><div style="position:absolute;left:34px;top:150px;width:830px;font-size:42px;color:#1d2433;line-height:1.25">%s</div></div>'%(y,col,a,N,b,c)
    y+=275
farm_year_m=page(h,'',note='',size=(1000,y+10))
# 3. postage math and what to track
h='<div class="abs" style="left:50px;top:40px;font-size:62px;font-weight:800;color:'+N+';line-height:1.1">Cost and tracking</div>'
h+='<div class="abs" style="left:50px;top:140px;width:900px;background:#e6f2f1;border-radius:16px;padding:30px 34px"><div style="font-size:42px;font-weight:700;color:#475467">500 homes at $0.26 each</div><div style="font-size:84px;font-weight:800;color:#14808a;line-height:1.15">$130</div><div style="font-size:42px;font-weight:700;color:'+N+'">postage per mailing</div><div style="font-size:42px;font-weight:700;color:#475467;margin-top:22px">12 mailings: about $1,560</div></div>'
h+='<div class="abs" style="left:50px;top:620px;font-size:52px;font-weight:800;color:'+N+'">Track every month</div>'
items=['Pieces sent','Responses','Conversations','Listing appointments']
y=720
for i,t in enumerate(items):
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:100px;background:#fff;border:3px solid #d0d7e2;border-radius:12px"><div style="position:absolute;left:30px;top:20px;font-size:44px;font-weight:700;color:#1d2433">%s</div><div style="position:absolute;right:30px;top:24px;width:200px;height:48px;border-bottom:4px solid #b9c2d3"></div></div>'%(y,t)
    y+=120
farm_track_m=page(h,'',note='',size=(1000,y+20))
SC=dict(farm_score_m=farm_score_m,farm_year_m=farm_year_m,farm_track_m=farm_track_m)
if __name__=='__main__': render(sel(sys.argv,SC))
