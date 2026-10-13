import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
# 1. budget split, mobile-first (1000 wide)
CH=[('Sphere and referrals',30,20),('Print and branding',25,10),('Social media',15,10),('Website and local SEO',10,20),('Direct mail',0,15+5),('Paid ads',0,15),('Test reserve',20,5)]
CH=[('Sphere and referrals',30,20),('Print and branding',25,10),('Social media',15,10),('Website and local SEO',10,20),('Direct mail',0,20),('Paid ads',0,15),('Test reserve',20,5)]
h='<div class="abs" style="left:50px;top:40px;font-size:64px;font-weight:800;color:'+N+';line-height:1.1">Where the budget goes</div>'
h+='<div class="abs" style="left:50px;top:135px;width:900px;display:flex;gap:40px;font-size:42px;font-weight:700;line-height:1.2"><div style="color:#14808a"><span style="font-size:36px">&#9632;</span> New agent<br><span style="font-weight:600;color:#667085;font-size:38px">$500 a month</span></div><div style="color:'+N+'"><span style="font-size:36px">&#9632;</span> Growing agent<br><span style="font-weight:600;color:#667085;font-size:38px">$1,500 a month</span></div></div>'
y=315
for name,a,b in CH:
    h+='<div class="abs" style="left:50px;top:%dpx;font-size:42px;font-weight:700;color:#1d2433">%s</div>'%(y,name)
    for k,(v,c) in enumerate([(a,'#14808a'),(b,N)]):
        w=max(int(v*19),8)
        h+='<div class="abs" style="left:50px;top:%dpx;width:%dpx;height:34px;background:%s;border-radius:6px"></div><div class="abs" style="left:%dpx;top:%dpx;font-size:38px;font-weight:800;color:%s">%d%%</div>'%(y+62+k*46,w,c,66+w,y+58+k*46,c,v)
    y+=158
plan_budget_m=page(h,'',note='',size=(1000,y+10))
# 2. spreadsheet, card rows
rows=[('Sphere and referrals','Five notes or calls a week','$100'),('Social media','Three posts, ten replies','$50'),('Direct mail','One mailing a month','$150')]
b='<div class="abs" style="left:0;top:0;width:1000px;height:92px;background:#217346"></div><div class="abs" style="left:40px;top:20px;font-size:40px;font-weight:800;color:#fff">Excel plan template</div>'
b+='<div class="abs" style="left:50px;top:130px;font-size:60px;font-weight:800;color:#1f3a5f;line-height:1.1">Your one-page plan</div>'
b+='<div class="abs" style="left:50px;top:215px;width:900px;background:#fff4cc;border:2px solid #e8d48a;border-radius:10px;padding:16px 24px;font-size:44px;font-weight:700;color:'+N+'">Goal: 10 closings this year</div>'
y=320
for a,c,d in rows:
    b+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:150px;background:#fff4cc;border:2px solid #e8d48a;border-radius:10px"><div style="position:absolute;left:24px;top:16px;font-size:44px;font-weight:800;color:%s">%s</div><div style="position:absolute;left:24px;top:82px;font-size:38px;color:#475467">%s</div><div style="position:absolute;right:24px;top:30px;font-size:56px;font-weight:800;color:#1f3a5f">%s</div></div>'%(y,N,a,c,d)
    y+=170
b+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:130px;background:#e6f2f1;border-radius:10px"><div style="position:absolute;left:24px;top:14px;font-size:44px;font-weight:800;color:%s">Total: $300 a month</div><div style="position:absolute;left:24px;top:76px;font-size:38px;color:#116b43;font-weight:700">Budget $500: the plan fits</div></div>'%(y,N)
y+=150
b+='<div class="abs" style="left:50px;top:%dpx;display:flex;gap:12px;font-size:36px;font-weight:700"><span style="background:#e4e8f0;color:#667085;padding:8px 18px;border-radius:10px 10px 0 0;font-weight:600">Goal</span><span style="background:#e4e8f0;color:#667085;padding:8px 18px;border-radius:10px 10px 0 0;font-weight:600">Budget</span><span style="background:#fff;color:#1f3a5f;padding:8px 18px;border-radius:10px 10px 0 0;border:2px solid #d0d7e2">Plan</span><span style="background:#e4e8f0;color:#667085;padding:8px 18px;border-radius:10px 10px 0 0;font-weight:600">Review</span></div>'%y
plan_template_m=page(b,'',note='',size=(1000,y+100))
# 3. spend per closing
data=[('Sphere and referrals',75,'2 closings'),('Website and local SEO',200,'1 closing'),('Paid ads',300,'1 closing'),('Direct mail',450,'1 closing'),('Social media',None,'0 closings')]
t='<div class="abs" style="left:50px;top:40px;font-size:60px;font-weight:800;color:'+N+';line-height:1.1">Spend per closing</div><div class="abs" style="left:50px;top:120px;font-size:40px;color:#667085;font-weight:600">Quarter 1, by lead source</div>'
y=230
for name,v,cl in data:
    t+='<div class="abs" style="left:50px;top:%dpx;font-size:42px;font-weight:700;color:#1d2433">%s</div><div class="abs" style="right:50px;top:%dpx;font-size:38px;color:#667085">%s</div>'%(y,name,y+4,cl)
    if v:
        w=int(v*1.7)
        t+='<div class="abs" style="left:50px;top:%dpx;width:%dpx;height:44px;background:#14808a;border-radius:8px"></div><div class="abs" style="left:%dpx;top:%dpx;font-size:44px;font-weight:800;color:#14808a">$%d</div>'%(y+68,w,66+w,y+62,v)
    else:
        t+='<div class="abs" style="left:50px;top:%dpx;font-size:42px;font-weight:800;color:#b42318">No closing yet</div>'%(y+64)
    y+=165
t+='<div class="abs" style="left:50px;top:%dpx;width:900px;background:#fff7e6;border-left:8px solid #e0a21b;border-radius:8px;padding:18px 26px;font-size:40px;color:#1d2433;line-height:1.3"><strong>All sources: $250 per closing.</strong> Direct mail costs the most, so change it first.</div>'%y
y+=230
plan_tracker_m=page(t,'',note='',size=(1000,y+20))
SC=dict(plan_budget_m=plan_budget_m,plan_template_m=plan_template_m,plan_tracker_m=plan_tracker_m)
if __name__=='__main__': render(sel(sys.argv,SC))
