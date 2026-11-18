import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'; TEAL='#14808a'; OR='#e0613a'
def title(t,top=40,size=64):
    return '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:%dpx;font-weight:800;color:%s;line-height:1.12">%s</div>'%(top,size,N,t)
def dot(n,x,y,d=60,fs=40,col=OR):
    return '<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:50%%;background:%s;color:#fff;font-size:%dpx;font-weight:800;display:flex;align-items:center;justify-content:center">%d</div>'%(x,y,d,d,col,fs,n)
def bar(x,y,w,h=18,col='#e4e7ec'):
    return '<div class="deco" style="position:absolute;left:%dpx;top:%dpx;width:%dpx;height:%dpx;background:%s;border-radius:%dpx"></div>'%(x,y,w,h,col,h//2)
# 1. channels: bar length = time to results, tag = cost
CH=[('Print and branding',40,'Immediate, but indirect','Low',TEAL,'#667085'),
    ('Paid ads',120,'Days to weeks','Medium to high',TEAL,'#c2410c'),
    ('Sphere and referrals',270,'Weeks to months','Low',TEAL,TEAL),
    ('Social media',360,'Months','Low',TEAL,'#e0a21b'),
    ('Direct mail',360,'Months of repetition','Medium',TEAL,'#e0613a'),
    ('Website and local SEO',560,'6 to 12 months','Low to medium',TEAL,'#7c5cc4')]
COST={'Low':('#e6f6ee','#116b43'),'Low to medium':('#eef2fb','#3b4a6b'),'Medium':('#fff1e0','#a8560a'),'Medium to high':('#fde8e4','#b42318')}
c=title('How fast channels pay back')
c+='<div class="abs" style="left:50px;top:130px;width:900px;font-size:40px;font-weight:600;color:#667085;line-height:1.25">Bar: time to results. Tag: cost.</div>'
y=215
for name,w,when,cost,bc,_ in CH:
    bg,fg=COST[cost]
    c+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:152px;background:#fff;border-radius:16px;box-shadow:0 4px 12px rgba(20,35,70,.1)"></div>'%y
    c+='<div class="abs" style="left:76px;top:%dpx;font-size:42px;font-weight:800;color:#1d2433">%s</div>'%(y+12,name)
    c+='<div class="abs" style="right:76px;top:%dpx;font-size:38px;font-weight:800;color:%s;background:%s;border-radius:999px;padding:0 18px;line-height:54px">%s</div>'%(y+14,fg,bg,cost)
    c+='<div class="abs" style="left:76px;top:%dpx;width:%dpx;height:36px;background:%s;border-radius:8px"></div>'%(y+90,w,bc)
    c+='<div class="abs" style="left:%dpx;top:%dpx;font-size:38px;font-weight:600;color:#475467;white-space:nowrap;line-height:44px">%s</div>'%(76+w+16,y+86,when)
    y+=170
pillar_channels_m=page(c,'',note='',size=(1000,y+10))
# 2. stages
S=[('New agent','Sphere outreach, bio, one social channel','Time, little budget, people who know you',TEAL),
   ('Growing agent','Local SEO, a mailer, one paid channel','Proof of results, income to test spend',N),
   ('Established agent or team','Referral systems, past-client programs, listing presentations','Most next deals are already in your database',OR)]
c=title('The right mix changes with your stage',size=60)
y=200
for i,(t,p,w,col) in enumerate(S):
    est=(i==2)
    hh=110; bh=hh+(230 if est else 170)
    c+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden"><div style="height:%dpx;background:%s;color:#fff;display:flex;align-items:center;gap:20px;padding:0 28px"><span style="display:inline-flex;width:64px;height:64px;border-radius:50%%;background:#fff;color:%s;align-items:center;justify-content:center;font-size:42px;font-weight:800;flex:none">%d</span><span style="font-size:48px;font-weight:800;line-height:1.05">%s</span></div><div style="padding:22px 28px"><div style="font-size:42px;font-weight:700;color:%s;line-height:1.22">%s</div><div style="font-size:38px;color:#475467;line-height:1.25;margin-top:12px">%s</div></div></div>'%(y,bh,hh,col,col,i+1,t,N,p,w)
    y+=bh
    if i<2:
        c+='<div class="abs" style="left:50px;top:%dpx;width:900px;text-align:center;font-size:44px;line-height:1;color:#98a2b3;font-weight:800">&darr;</div>'%(y+8)
        y+=64
pillar_stage_m=page(c,'',note='',size=(1000,y+40))
# 3. lead source
form=('<div class="abs sh" style="left:50px;top:200px;width:900px;border-radius:16px;background:#fff;overflow:hidden">'
 '<div class="deco" style="height:56px;background:#e9edf3;padding:12px 22px;font-size:26px;color:#667085">crm.example.com/contacts/new</div>'
 '<div style="padding:28px 30px 30px"><div style="font-size:46px;font-weight:800;color:'+N+'">New contact</div>'
 '<div class="deco" style="display:flex;gap:16px;margin-top:20px"><div style="flex:1;height:60px;border:2px solid #d0d5dd;border-radius:10px"></div><div style="flex:1;height:60px;border:2px solid #d0d5dd;border-radius:10px"></div></div>'
 '<div style="font-size:38px;font-weight:800;color:'+OR+';margin-top:26px">LEAD SOURCE (required)</div>'
 '<div style="border:4px solid '+OR+';border-radius:12px;background:#fff7f1;padding:16px 22px;margin-top:10px;font-size:42px;font-weight:700;color:#1d2433;display:flex;justify-content:space-between;align-items:center"><span>Referral from a past client</span><span style="font-size:40px">&#9662;</span></div>'
 '<div class="deco" style="display:flex;gap:12px;flex-wrap:wrap;margin-top:18px"><span class="chip" style="background:#eef2fb;color:#1b2a4a;font-size:24px">Social media</span><span class="chip" style="background:#eef2fb;color:#1b2a4a;font-size:24px">Website</span><span class="chip" style="background:#eef2fb;color:#1b2a4a;font-size:24px">Paid ad</span><span class="chip" style="background:#eef2fb;color:#1b2a4a;font-size:24px">Direct mail</span></div>'
 '<div style="margin-top:24px;background:#e6f6ee;border-radius:10px;padding:16px 22px;font-size:40px;line-height:1.25;color:#116b43;font-weight:700">At closing: update the source.</div>'
 '</div></div>')
q=['Which source gave the most conversations?','Which gave the most closings?','Which cost the most per closing?']
t=title('Record the lead source<br>on day one',size=60)+form
y=860
t+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:44px;font-weight:800;color:%s">After a few months, ask:</div>'%(y,N)
y+=80
for i,x in enumerate(q):
    t+=dot(i+1,50,y,60,38)+'<div class="abs" style="left:130px;top:%dpx;width:820px;font-size:42px;font-weight:600;color:#1d2433;line-height:1.2">%s</div>'%(y+4,x)
    y+=(135 if len(x)>34 else 100)
pillar_leadsource_m=page(t,'',note='',size=(1000,y+30))
SC=dict(pillar_channels_m=pillar_channels_m,pillar_stage_m=pillar_stage_m,pillar_leadsource_m=pillar_leadsource_m)
if __name__=='__main__': render(sel(sys.argv,SC))
