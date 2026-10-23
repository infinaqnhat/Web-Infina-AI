import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
from s_m_leadgen import hero,title,dot,N,TEAL,OR
def card(y,h,head,col,body_html):
    return ('<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
            '<div style="height:84px;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:48px;font-weight:800;line-height:1.05">%s</div>'
            '<div style="padding:18px 28px">%s</div></div>')%(y,h,col,head,body_html)
def line(t,fs=44,col='#1d2433',w=700,mt=0):
    return '<div style="font-size:%dpx;font-weight:%d;color:%s;line-height:1.22;margin-top:%dpx">%s</div>'%(fs,w,col,mt,t)
# ---- bai 3: expired listings
exp_hero_m=hero('ph_living','Expired<br>listings','Find them. Reach them lawfully.')
S=[('MLS search',TEAL,'Filter by status and expiration date',''),('Public records',N,'Slower, free, shows owner details',''),('Your network',OR,'Agents and past clients hear first','')]
c=title('Finding expired listings',size=62); y=190
for h_,col,t,_ in S:
    c+=card(y,230,h_,col,line(t,44,'#1d2433',700)); y+=256
exp_sources_m=page(c,'',note='',size=(1000,y+10))
R=[('1','Letter',TEAL,'Mail first. The registry covers calls, not mail.'),('2','Call',N,'Only after the registry and your own list.'),('3','Text',OR,'Only with consent. Check TCPA rules.')]
c=title('Reach them in this order',size=62); y=190
for n,h_,col,t in R:
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:250px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12)"></div>'%y)+dot(int(n),80,y+30,70,46,col)
    c+='<div class="abs" style="left:180px;top:%dpx;width:740px;font-size:54px;font-weight:800;color:%s">%s</div>'%(y+28,col,h_)
    c+='<div class="abs" style="left:180px;top:%dpx;width:740px;font-size:42px;font-weight:600;color:#1d2433;line-height:1.22">%s</div>'%(y+105,t)
    y+=276
exp_order_m=page(c,'',note='',size=(1000,y+10))
K=[('Day 1','Letter goes out',TEAL),('Day 3 to 5','Call if allowed',N),('Week 2','Short note and market update',N),('Week 4','Check in by email or call',OR),('Month 3','Ask again, then pause',OR)]
c=title('A follow-up calendar to adapt',size=60); y=185
for d,t,col in K:
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:150px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12)"></div>'%y)
    c+='<div class="abs" style="left:78px;top:%dpx;width:250px;font-size:44px;font-weight:800;color:%s;line-height:150px;height:150px">%s</div>'%(y,col,d)
    c+='<div class="abs" style="left:340px;top:%dpx;width:590px;font-size:42px;font-weight:600;color:#1d2433;display:flex;align-items:center;height:150px;line-height:1.2">%s</div>'%(y,t)
    y+=170
exp_calendar_m=page(c,'',note='',size=(1000,y+20))
# ---- bai 4: circle prospecting
circ_hero_m=page(('<div class="photo abs" style="left:0;top:0;width:1000px;height:560px;background-image:url(ph_aerial.jpg);transform:scaleX(-1)"></div>'
 '<div class="abs" style="left:0;top:0;width:1000px;height:560px;background:linear-gradient(90deg,rgba(27,42,74,.92) 0%,rgba(27,42,74,.78) 55%,rgba(27,42,74,.25) 100%)"></div>'
 '<div class="abs" style="left:60px;top:150px;width:760px;font-size:78px;font-weight:800;color:#fff;line-height:1.08">Circle<br>prospecting</div>'
 '<div class="abs" style="left:60px;top:372px;width:760px;font-size:46px;font-weight:600;color:#ffd9c9;line-height:1.2">Radius, triggers, routine</div>'),'',note='',size=(1000,560))
T=[('Just listed','Your new listing, announced to neighbors',TEAL),('Just sold','A closing nearby, with the result',N),('Open house preview','A neighbors-only hour first',OR)]
c=title('Why contact a circle',size=62); y=190
for h_,t,col in T:
    c+=card(y,230,h_,col,line(t,42,'#1d2433',700)); y+=256
circ_trigger_m=page(c,'',note='',size=(1000,y+10))
c=title('Start with a small circle',size=62)
cx,cy=500,720
for r,col,op in [(380,'#14808a',.10),(270,'#14808a',.18),(160,'#14808a',.30)]:
    c+='<div class="deco" style="position:absolute;left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:50%%;background:%s;opacity:%s"></div>'%(cx-r,cy-r,2*r,2*r,col,op)
c+='<div class="abs" style="left:%dpx;top:%dpx;width:140px;height:140px;border-radius:50%%;background:%s;color:#fff;display:flex;align-items:center;justify-content:center;text-align:center;font-size:38px;font-weight:800;line-height:1.05">Your listing</div>'%(cx-70,cy-70,OR)
c+='<div class="abs" style="left:50px;top:%dpx;width:900px;text-align:center;font-size:42px;font-weight:700;color:#1d2433">A few blocks to a whole suburb</div>'%(cy+410)
c+='<div class="abs" style="left:50px;top:%dpx;width:900px;text-align:center;font-size:40px;font-weight:600;color:#667085">Size it to what you can contact each week</div>'%(cy+475)
circ_circle_m=page(c,'',note='',size=(1000,cy+560))
W=[('Mon','Pick the trigger home, build the list',TEAL),('Tue','Mail letters or postcards',N),('Wed','Call numbers you may call',N),('Thu','Drop by with a short note',OR),('Fri','Log every result in your CRM',OR)]
c=title('A weekly routine, suggested',size=62); y=185
for d,t,col in W:
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:150px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12)"></div>'%y)
    c+='<div class="abs" style="left:78px;top:%dpx;width:150px;font-size:50px;font-weight:800;color:%s;line-height:150px;height:150px">%s</div>'%(y,col,d)
    c+='<div class="abs" style="left:240px;top:%dpx;width:690px;font-size:42px;font-weight:600;color:#1d2433;display:flex;align-items:center;height:150px;line-height:1.2">%s</div>'%(y,t)
    y+=170
circ_week_m=page(c,'',note='',size=(1000,y+20))
# ---- bai 5: SOI
soi_hero_m=hero('ph_kitchen','Sphere of<br>influence','Build it. Work it.')
G=[('Past clients','People you have closed with',TEAL),('Family and friends','The people who know you best',N),('Neighbors','People near you and near your listings',OR),('Local contacts','Lenders, vendors, business owners',N)]
c=title('Who is in your sphere',size=62); y=185
for h_,t,col in G:
    c+=card(y,222,h_,col,line(t,42,'#1d2433',700)); y+=246
soi_groups_m=page(c,'',note='',size=(1000,y+10))
TI=[('A','Past clients and top referrers','Every month',TEAL),('B','Friends and family','Every quarter',N),('C','Neighbors and acquaintances','Twice a year',OR)]
c=title('Rank, then set a rhythm',size=62); y=190
for l,t,cad,col in TI:
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:290px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12)"></div>'%y)+dot(ord(l)-64+0,0,0,1,1) if False else ''
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:290px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12)"></div>'%y)
    c+='<div class="abs" style="left:80px;top:%dpx;width:100px;height:100px;border-radius:50%%;background:%s;color:#fff;font-size:62px;font-weight:800;display:flex;align-items:center;justify-content:center">%s</div>'%(y+30,col,l)
    c+='<div class="abs" style="left:210px;top:%dpx;width:720px;font-size:44px;font-weight:700;color:#1d2433;line-height:1.2">%s</div>'%(y+34,t)
    c+='<div class="abs" style="left:210px;top:%dpx;width:720px;font-size:50px;font-weight:800;color:%s">%s</div>'%(y+170,col,cad)
    y+=316
soi_tiers_m=page(c,'',note='',size=(1000,y+10))
Rw=[('Maria L.','Past client, 2024','A','Sent market update'),('Dan P.','Neighbor, next door','C','Birthday card'),('Priya S.','College friend','B','Call in March')]
c=title('Five columns are enough',size=62)
c+='<div class="abs" style="left:50px;top:140px;width:900px;font-size:40px;font-weight:600;color:#667085">Name, source, tier, last and next touch</div>'
y=240
for nm,how,tier,nx in Rw:
    col={'A':TEAL,'B':N,'C':OR}[tier]
    c+=card(y,300,nm,col,line(how,42,'#1d2433',700)+line('Tier '+tier+'. Next: '+nx,40,'#475467',600,10)); y+=326
soi_sheet_m=page(c,'',note='',size=(1000,y+10))
SC=dict(exp_hero_m=exp_hero_m,exp_sources_m=exp_sources_m,exp_order_m=exp_order_m,exp_calendar_m=exp_calendar_m,
 circ_hero_m=circ_hero_m,circ_trigger_m=circ_trigger_m,circ_circle_m=circ_circle_m,circ_week_m=circ_week_m,
 soi_hero_m=soi_hero_m,soi_groups_m=soi_groups_m,soi_tiers_m=soi_tiers_m,soi_sheet_m=soi_sheet_m)
if __name__=='__main__': render(sel(sys.argv,SC))
