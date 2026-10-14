import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'; TEAL='#14808a'; OR='#e0613a'
def title(t,sub=''):
    s='<div class="abs" style="left:50px;top:40px;width:900px;font-size:64px;font-weight:800;color:'+N+';line-height:1.1">'+t+'</div>'
    if sub: s+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:40px;font-weight:600;color:#667085">%s</div>'%(40+(2 if len(t)>22 else 1)*70+8,sub)
    return s
def dot(n,x,y,sz=64):
    return '<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:50%%;background:%s;color:#fff;font-size:42px;font-weight:800;display:flex;align-items:center;justify-content:center;box-shadow:0 3px 8px rgba(0,0,0,.25)">%d</div>'%(x,y,sz,sz,OR,n)

# 1. five-step path, lead to closed deal (replaces CrYfiWG)
steps=[('Lead captured','IDX form, inquiry, saved search'),('Reply in minutes','SMS, email or AI chat'),('Pipeline stage','Four to six clear stages'),('Long-term nurture','Leads 6 to 18 months out'),('Closed deal','First contact through closing')]
b=title('From lead to closed deal')
y0=190; step=164
b+='<div class="abs" style="left:89px;top:%dpx;width:8px;height:%dpx;background:#b9c6dc;border-radius:4px"></div>'%(y0+60,step*4)
for i,(a,c) in enumerate(steps):
    y=y0+i*step
    last=(i==4)
    col=TEAL if last else OR
    b+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:140px;background:#fff;border-radius:16px;box-shadow:0 5px 14px rgba(20,35,70,.12);border-left:0"></div>'%y
    b+='<div class="abs" style="left:62px;top:%dpx;width:76px;height:76px;border-radius:50%%;background:%s;color:#fff;font-size:48px;font-weight:800;display:flex;align-items:center;justify-content:center;box-shadow:0 3px 8px rgba(0,0,0,.2)">%s</div>'%(y+32,col,'&#10003;' if last else str(i+1))
    b+='<div class="abs" style="left:166px;top:%dpx;width:760px;font-size:46px;font-weight:800;color:%s;line-height:1.15">%s</div><div class="abs" style="left:166px;top:%dpx;width:760px;font-size:38px;font-weight:500;color:#475467;line-height:1.15">%s</div>'%(y+18,N,a,y+80,c)
yy=y0+5*step+10
b+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:42px;font-weight:700;color:%s;line-height:1.25;text-wrap:balance">Stop at step 1 and it is an address book.</div>'%(yy,TEAL)
crm_flow_m=page(b,"",note="",size=(1000,yy+100))

# 2. six criteria checklist (replaces CrYfGUB)
crit=[('Lead capture and IDX','Leads flow in, no manual import'),('Automated follow-up','Replies by SMS, email or AI chat'),('Long-term nurture','Covers leads 6 to 18 months out'),('Pipeline view','Every lead, first contact to closing'),('Mobile app','Log notes right after a showing'),('Deep integrations','Portals, MLS and IDX, texting, calendar')]
b=title('Six checks for a CRM')
y=185
b+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:#fff;border-radius:20px;box-shadow:0 8px 22px rgba(20,35,70,.14)"></div>'%(y-20,6*150+20)
b+='<div class="abs deco" style="left:360px;top:%dpx;width:280px;height:30px;background:#c9d3e6;border-radius:15px"></div>'%(y-36)
for i,(a,c) in enumerate(crit):
    yy=y+i*150
    b+='<div class="abs" style="left:84px;top:%dpx;width:66px;height:66px;border:6px solid %s;border-radius:14px;background:#fff"></div>'%(yy+22,TEAL)
    b+='<div class="abs" style="left:182px;top:%dpx;width:740px;font-size:46px;font-weight:800;color:%s;line-height:1.15">%s</div><div class="abs" style="left:182px;top:%dpx;width:750px;font-size:38px;font-weight:500;color:#475467;line-height:1.15">%s</div>'%(yy+6,N,a,yy+70,c)
    if i<5: b+='<div class="abs deco" style="left:84px;top:%dpx;width:832px;height:2px;background:#e1e6f0"></div>'%(yy+138)
yy=y+6*150+50
b+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:42px;font-weight:700;color:%s;line-height:1.25;text-wrap:balance">Judge vendors on these, not on the feature list.</div>'%(yy,TEAL)
crm_criteria_m=page(b,'',note='',size=(1000,yy+140))

# 3. mock site with six numbered checks (replaces CQfb7Nn)
def idot(n,sz=64,extra=''):
    return '<div style="flex:none;width:%dpx;height:%dpx;border-radius:50%%;background:%s;color:#fff;font-size:42px;font-weight:800;display:flex;align-items:center;justify-content:center;box-shadow:0 3px 8px rgba(0,0,0,.25);%s">%d</div>'%(sz,sz,OR,extra,n)
bx,by,bw=50,175,900
m='<div class="abs sh" style="left:%dpx;top:%dpx;width:%dpx;border-radius:18px;background:#fff;overflow:hidden;padding-bottom:26px">'%(bx,by,bw)
m+='<div style="height:96px;background:#e9edf3;display:flex;align-items:center;gap:14px;padding:0 20px"><div style="flex:1;height:60px;background:#fff;border-radius:30px;display:flex;align-items:center;padding:0 24px;font-size:40px;color:#475467;font-weight:600">cedarhills.example.com</div>'+idot(5)+'</div>'
m+='<div style="position:relative;height:230px;background:linear-gradient(rgba(27,42,74,.35),rgba(27,42,74,.55)),url(ph_house.jpg);background-size:cover;background-position:center"><div class="deco" style="position:absolute;left:30px;top:30px;width:200px;height:20px;background:rgba(255,255,255,.75);border-radius:10px"></div>'
m+='<div style="position:absolute;right:24px;top:18px;display:flex;align-items:center;gap:14px">'+idot(4)+'<div class="deco" style="width:46px;height:78px;border:5px solid #fff;border-radius:10px;background:rgba(255,255,255,.25)"></div></div>'
m+='<div style="position:absolute;left:24px;right:24px;top:118px;height:84px;background:#fff;border-radius:42px;display:flex;align-items:center;justify-content:space-between;padding:0 10px 0 28px;font-size:42px;color:#475467;font-weight:600">Search homes<span style="flex:none">'+idot(1,64)+'</span></div></div>'
m+='<div style="display:flex;gap:14px;padding:20px 20px 0">'
for ph in ('ph_condo.jpg','ph_kitchen.jpg','ph_living.jpg'):
    m+='<div style="flex:1;height:150px;border-radius:12px;background:url(%s);background-size:cover;background-position:center"></div>'%ph
m+='</div>'
m+='<div style="display:flex;gap:16px;padding:22px 20px 0;align-items:center"><div style="background:'+OR+';color:#fff;font-size:42px;font-weight:800;padding:12px 28px;border-radius:12px;white-space:nowrap">Save this search</div>'+idot(2)+'</div>'
m+='<div style="display:flex;gap:16px;padding:22px 20px 0;align-items:center"><div style="background:'+TEAL+';color:#fff;font-size:42px;font-weight:800;padding:12px 28px;border-radius:12px;white-space:nowrap">Sent to CRM</div>'+idot(3)+'<div style="flex:1"></div><div style="background:#e4e8f0;color:'+N+';font-size:42px;font-weight:800;padding:12px 28px;border-radius:12px;white-space:nowrap">Edit page</div>'+idot(6)+'</div>'
m+='</div>'
bh=84+0
b=title('Six checks for a site builder')+m
lab=['Live IDX feed','Lead capture on search','CRM built in or linked','Fast on mobile','Control of SEO fields','Easy to maintain']
y=by+96+230+20+150+22+66+22+66+26+50
for i,t in enumerate(lab):
    yy=y+i*80
    b+=dot(i+1,50,yy,60)
    b+='<div class="abs" style="left:134px;top:%dpx;width:820px;font-size:44px;font-weight:700;color:%s;line-height:1.2">%s</div>'%(yy+6,N,t)
builder_checks_m=page(b,'',note='',size=(1000,y+6*80+40))

# 4. which builder fits which agent (replaces CQfDl3B)
cards=[('NEW OR SOLO AGENT','Placester or Real Geeks','Low maintenance, IDX search','#14808a'),
       ('PRODUCING AGENT, SMALL TEAM','AgentFire','Neighborhood pages for local SEO','#1d4e89'),
       ('HIGH-VOLUME TEAM, BROKERAGE','Sierra Interactive or kvCORE','Lead routing and accountability','#1b2a4a'),
       ('DESIGN OVER IDX','Squarespace or Wix','No native IDX: add a widget','#8b5a2b')]
b=title('Pick a builder by agent type')
y=170
for r,nm,why,col in cards:
    b+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:222px;background:#fff;border-radius:16px;box-shadow:0 5px 14px rgba(20,35,70,.12);overflow:hidden"><div style="position:absolute;left:0;top:0;width:18px;height:100%%;background:%s"></div>'%(y,col)
    b+='<div style="position:absolute;left:46px;top:16px;font-size:38px;font-weight:800;letter-spacing:.03em;color:%s">%s</div>'%(OR,r)
    b+='<div style="position:absolute;left:46px;top:68px;width:830px;font-size:50px;font-weight:800;color:%s;line-height:1.15">%s</div>'%(N,nm)
    b+='<div style="position:absolute;left:46px;top:140px;width:830px;font-size:40px;font-weight:500;color:#475467;line-height:1.2">%s</div></div>'%why
    y+=246
b+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:42px;font-weight:700;color:%s;line-height:1.25;text-wrap:balance">Start from your lead volume, then check the MLS board.</div>'%(y+6,TEAL)
builder_match_m=page(b,'',note='',size=(1000,y+130))

SC=dict(crm_flow_m=crm_flow_m,crm_criteria_m=crm_criteria_m,builder_checks_m=builder_checks_m,builder_match_m=builder_match_m)
if __name__=='__main__': render(sel(sys.argv,SC))
