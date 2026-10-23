import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'; TEAL='#14808a'; OR='#e0613a'
def title(t,top=40,size=64):
    return '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:%dpx;font-weight:800;color:%s;line-height:1.12">%s</div>'%(top,size,N,t)
def dot(n,x,y,d=60,fs=40,col=OR):
    return '<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:50%%;background:%s;color:#fff;font-size:%dpx;font-weight:800;display:flex;align-items:center;justify-content:center">%d</div>'%(x,y,d,d,col,fs,n)
def hero(photo_name,h1,h2):
    b=('<div class="photo abs" style="left:0;top:0;width:1000px;height:560px;background-image:url(%s.jpg)"></div>'%photo_name+
       '<div class="abs" style="left:0;top:0;width:1000px;height:560px;background:linear-gradient(90deg,rgba(27,42,74,.92) 0%%,rgba(27,42,74,.78) 55%%,rgba(27,42,74,.25) 100%%)"></div>'
       '<div class="abs" style="left:60px;top:150px;width:700px;font-size:78px;font-weight:800;color:#fff;line-height:1.08">%s</div>'%h1+
       '<div class="abs" style="left:60px;top:%dpx;width:700px;font-size:46px;font-weight:600;color:#ffd9c9;line-height:1.2">%s</div>'%(150+(84*(1+h1.count('<br>')))+54,h2))
    return page(b,'',note='',size=(1000,560))
# pillar
leadgen_hero_m=hero('ph_aerial','Real estate<br>lead generation','10 sources compared')
rows=[('New agent','Your sphere and open houses','Time and people, little cash',TEAL),
      ('Has a database','Past-client contact and referral asks','The cheapest leads you will find',N),
      ('Has a budget','A farm plus one paid channel','Test small, track every lead',OR)]
c=title('Pick the source that fits you',size=60)
y=200
for i,(a,b_,w,col) in enumerate(rows):
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:262px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
        '<div style="height:84px;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:48px;font-weight:800">%s</div>'
        '<div style="padding:20px 28px"><div style="font-size:44px;font-weight:700;color:%s;line-height:1.2">%s</div>'
        '<div style="font-size:38px;color:#475467;margin-top:10px;line-height:1.25">%s</div></div></div>')%(y,col,a,N,b_,w)
    y+=290
leadgen_start_m=page(c,'',note='',size=(1000,y+10))
groups=[('Mostly sellers',TEAL,['Farming','Door knocking and calls','Expired listings','FSBO sellers']),
        ('Mostly buyers',OR,['Open houses','Portals and lead companies']),
        ('Both',N,['Your sphere','Referrals','Local SEO and social','Paid ads'])]
c=title('Who each source brings',size=64)
y=170
for name,col,items in groups:
    hh=96+len(items)*74+30
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
        '<div style="height:80px;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:48px;font-weight:800">%s</div><div style="padding:14px 28px">')%(y,hh,col,name)
    for it in items:
        c+='<div style="font-size:44px;font-weight:700;color:#1d2433;line-height:74px">%s</div>'%it
    c+='</div></div>'
    y+=hh+26
leadgen_buyer_seller_m=page(c,'',note='',size=(1000,y+20))
R=[('Farm mailers','$1,560','2','$780',TEAL),('Open houses','$400','1','$400',OR),('Paid ads','$3,000','2','$1,500',N)]
c=title('Spend per closing, by source',size=60)
c+='<div class="abs" style="left:50px;top:140px;width:900px;font-size:40px;font-weight:600;color:#667085">Sample year. Divide spend by closings.</div>'
y=225
for nm,sp,cl,per,col in R:
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:250px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
        '<div style="height:80px;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:48px;font-weight:800">%s</div>'
        '<div style="display:flex;padding:22px 28px;gap:24px;align-items:flex-end">'
        '<div style="flex:1"><div style="font-size:38px;color:#667085;font-weight:600">Spend</div><div style="font-size:50px;font-weight:800;color:#1d2433">%s</div></div>'
        '<div style="flex:1"><div style="font-size:38px;color:#667085;font-weight:600">Closings</div><div style="font-size:50px;font-weight:800;color:#1d2433">%s</div></div>'
        '<div style="flex:1.1"><div style="font-size:38px;color:#667085;font-weight:600">Per closing</div><div style="font-size:50px;font-weight:800;color:%s">%s</div></div>'
        '</div></div>')%(y,col,nm,sp,cl,col,per)
    y+=276
leadgen_cost_m=page(c,'',note='',size=(1000,y+10))
# sub-hub
listing_hero_m=hero('ph_house','Listing<br>leads','Find sellers. Win listings.')
G=[('People you know','Sphere and past clients','Referrals',TEAL),
   ('A neighborhood','Farming and circle prospecting','Door knocking and open houses',N),
   ('Sellers who need an agent now','Expired listings','FSBO and life events',OR)]
c=title('Where listings come from',size=64)
y=190
for nm,a,b_,col in G:
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:290px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
        '<div style="height:100px;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:46px;font-weight:800;line-height:1.05">%s</div>'
        '<div style="padding:22px 28px"><div style="font-size:44px;font-weight:700;color:#1d2433;line-height:1.2">%s</div><div style="font-size:44px;font-weight:700;color:#1d2433;margin-top:12px;line-height:1.2">%s</div></div></div>')%(y,col,nm,a,b_)
    y+=316
listing_groups_m=page(c,'',note='',size=(1000,y+10))
S=['Capture the lead','Reply the same day','Offer a value estimate','Book the appointment','Present and sign']
c=title('From seller lead to listing',size=60)
y=190
for i,s in enumerate(S):
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:140px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12)"></div>'%y)+dot(i+1,80,y+38,64,42,[TEAL,TEAL,N,N,OR][i])
    c+='<div class="abs" style="left:176px;top:%dpx;width:740px;font-size:46px;font-weight:700;color:#1d2433;line-height:140px;height:140px">%s</div>'%(y,s)
    y+=160
listing_path_m=page(c,'',note='',size=(1000,y+30))
T=[('Your sphere','8','4','3',TEAL),('Farm mailers','20','3','1',N),('Expired listings','15','2','1',OR)]
c=title('Track seller leads by source',size=60)
c+='<div class="abs" style="left:50px;top:140px;width:900px;font-size:40px;font-weight:600;color:#667085">Sample quarter. Leads, appointments, listings.</div>'
y=225
for nm,l,a,li,col in T:
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:250px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
        '<div style="height:80px;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:48px;font-weight:800">%s</div>'
        '<div style="display:flex;padding:22px 28px;gap:24px">'
        '<div style="flex:1"><div style="font-size:38px;color:#667085;font-weight:600">Leads</div><div style="font-size:56px;font-weight:800;color:#1d2433">%s</div></div>'
        '<div style="flex:1"><div style="font-size:38px;color:#667085;font-weight:600">Appointments</div><div style="font-size:56px;font-weight:800;color:#1d2433">%s</div></div>'
        '<div style="flex:1"><div style="font-size:38px;color:#667085;font-weight:600">Listings</div><div style="font-size:56px;font-weight:800;color:%s">%s</div></div>'
        '</div></div>')%(y,col,nm,l,a,col,li)
    y+=276
listing_tracker_m=page(c,'',note='',size=(1000,y+10))
SC=dict(leadgen_hero_m=leadgen_hero_m,leadgen_start_m=leadgen_start_m,leadgen_buyer_seller_m=leadgen_buyer_seller_m,leadgen_cost_m=leadgen_cost_m,
        listing_hero_m=listing_hero_m,listing_groups_m=listing_groups_m,listing_path_m=listing_path_m,listing_tracker_m=listing_tracker_m)
if __name__=='__main__': render(sel(sys.argv,SC))
