import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
# channel map: x = time to results, y = cost (from the pillar comparison table)
CH=[('Print and branding',0,0,'#98a2b3'),('Paid ads',1,2,'#c2410c'),('Sphere and referrals',2,0,'#14808a'),('Social media',3,0,'#e0a21b'),('Direct mail',3,1,'#e0613a'),('Website and local SEO',4,0.5,'#7c5cc4')]
X0,Y0,W,H=230,150,1240,520
cols=['Immediate,\nbut indirect','Days to\nweeks','Weeks to\nmonths','Months','6 to 12\nmonths']
rows=['High','Medium','Low']
g=''
for i,c in enumerate(cols): g+='<div class="abs" style="left:%dpx;top:%dpx;width:240px;text-align:center;font-size:19px;font-weight:700;color:#475467;white-space:pre-line">%s</div>'%(X0+i*W/5+4,Y0+H+14,c)
for j,r in enumerate(rows): g+='<div class="abs" style="left:70px;top:%dpx;font-size:20px;font-weight:800;color:%s">%s</div>'%(Y0+j*H/3+H/6-12,N,'Cost: '+r)
g+='<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;background:#fff;border-radius:12px;box-shadow:0 6px 16px rgba(20,35,70,.1)"></div>'%(X0,Y0,W,H)
for i in range(1,5): g+='<div class="abs" style="left:%dpx;top:%dpx;width:2px;height:%dpx;background:#eef0f4"></div>'%(X0+i*W/5,Y0,H)
for j in range(1,3): g+='<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:2px;background:#eef0f4"></div>'%(X0,Y0+j*H/3,W)
for name,xi,yi,col in CH:
    cx=X0+xi*W/5+W/10; cy=Y0+H-(yi*H/3+H/6)  # yi 0=low bottom
    # y levels: low(0)->bottom row, medium(1)->mid, high(2)->top
    g+='<div class="abs" style="left:%dpx;top:%dpx;width:200px;height:84px;margin-left:-100px;margin-top:-42px;background:%s;color:#fff;border-radius:42px;display:flex;align-items:center;justify-content:center;text-align:center;font-weight:800;font-size:19px;line-height:1.2;padding:0 14px">%s</div>'%(cx,cy,col,name)
pillar_channels=page(g+'<div class="abs" style="left:230px;top:76px;font-size:21px;color:#1b2a4a;font-weight:600">Where each channel sits: how fast it pays back and what it costs</div>','Real estate marketing channels compared',note='Placed from the channel comparison table. Paid ads are medium to high; website and SEO low to medium.')
# stages
S=[('New agent','Sphere outreach, a simple profile and bio, one social channel','You have time but little budget, and people who know you are the fastest first clients','#14808a'),('Growing agent','Add local SEO, a consistent mailer, and one paid channel','You have proof of results to show, and enough income to test spend','#1b2a4a'),('Established agent or team','Referral systems, past-client programs, listing presentations','Most of your next deals are already in your database','#e0613a')]
c=''
for i,(t,p,w,col) in enumerate(S):
    x=70+i*500
    c+='<div class="paper sh" style="left:%dpx;top:150px;width:470px;height:380px;border-radius:14px"><div style="background:%s;color:#fff;padding:22px 28px"><div style="font-size:15px;font-weight:800;letter-spacing:.14em;opacity:.85">STAGE %d</div><div class="serif" style="font-size:29px;font-weight:700;margin-top:4px;line-height:1.15">%s</div></div><div style="padding:24px 28px"><div style="font-size:15px;font-weight:800;color:%s;letter-spacing:.1em">PRIORITY</div><div style="font-size:23px;font-weight:700;color:%s;line-height:1.3;margin:6px 0 22px">%s</div><div style="font-size:15px;font-weight:800;color:#667085;letter-spacing:.1em">WHY</div><div style="font-size:20px;color:#475467;line-height:1.45;margin-top:6px">%s</div></div></div>'%(x,col,i+1,t,col,N,p,w)
for x in (540,1040): c+='<div class="abs" style="left:%dpx;top:320px;font-size:40px;color:#98a2b3;font-weight:800">&rarr;</div>'%x
pillar_stage=page(c+'<div class="abs" style="left:70px;top:590px;width:1460px;font-size:23px;color:'+N+';font-weight:600">The right marketing mix changes with your stage. Add channels as your proof and budget grow.</div>','Marketing by career stage',note='')
# lead source form
form=('<div style="padding:30px 40px"><div style="font-size:26px;font-weight:800;color:'+N+'">New contact</div><div style="font-size:17px;color:#667085;margin:4px 0 22px">Record the lead source the day someone first reaches you.</div>'
 '<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px 24px">'
 '<div><div style="font-size:15px;color:#667085;margin-bottom:6px">Name</div><div style="border:1px solid #d0d5dd;border-radius:8px;padding:12px 14px;font-size:19px">Chris Alvarez</div></div>'
 '<div><div style="font-size:15px;color:#667085;margin-bottom:6px">Phone or email</div><div style="border:1px solid #d0d5dd;border-radius:8px;padding:12px 14px;font-size:19px">555-0166</div></div>'
 '<div style="grid-column:1 / span 2"><div style="font-size:15px;font-weight:800;color:#e0613a;margin-bottom:6px">LEAD SOURCE (required)</div><div style="border:2px solid #e0613a;border-radius:8px;padding:12px 14px;font-size:19px;display:flex;justify-content:space-between;background:#fff7f1"><span>Referral from a past client</span><span>&#9662;</span></div></div></div>'
 '<div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:18px"><span class="chip" style="background:#eef2fb;color:#1b2a4a;font-size:15px">Referral</span><span class="chip" style="background:#eef2fb;color:#1b2a4a;font-size:15px">Social media</span><span class="chip" style="background:#eef2fb;color:#1b2a4a;font-size:15px">Website</span><span class="chip" style="background:#eef2fb;color:#1b2a4a;font-size:15px">Paid ad</span><span class="chip" style="background:#eef2fb;color:#1b2a4a;font-size:15px">Direct mail</span><span class="chip" style="background:#eef2fb;color:#1b2a4a;font-size:15px">Open house</span></div>'
 '<div style="margin-top:26px;background:#e6f6ee;border-radius:10px;padding:14px 18px;font-size:18px;color:#116b43"><strong>When the deal closes:</strong> update the source and add the closing, so you can see which source paid back.</div></div>')
qs=('<div class="abs" style="left:900px;top:130px;width:620px">'
 '<div style="font-size:26px;font-weight:800;color:'+N+';margin-bottom:22px">After a few months, ask three questions</div>'
 +''.join('<div style="display:flex;gap:16px;margin-bottom:22px;align-items:flex-start"><span class="chip" style="background:#e0613a;color:#fff;height:34px">%d</span><div style="font-size:23px;color:#1d2433;line-height:1.35">%s</div></div>'%(i+1,t) for i,t in enumerate(['Which source produced the most conversations?','Which produced the most closings?','Which cost the most per closing?']))
 +'<div style="font-size:21px;color:#475467;line-height:1.45;border-top:2px solid #cbd2e0;padding-top:18px">Those answers often differ, and the second and third matter more than the first.</div></div>')
pillar_leadsource=page(browser(60,120,780,540,'crm.example.com/contacts/new',form)+qs,'One habit: record the lead source',note='Sample form. Names and numbers are made up.')
SC=dict(pillar_channels=pillar_channels,pillar_stage=pillar_stage,pillar_leadsource=pillar_leadsource)
if __name__=='__main__': render(sel(sys.argv,SC))
