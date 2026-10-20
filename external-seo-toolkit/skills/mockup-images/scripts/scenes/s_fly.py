import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
def foot(w):
    return '''<div style="position:absolute;left:0;right:0;bottom:0;height:44px;background:#1b2a4a;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 14px;font-size:12px;font-weight:600"><span>Dana Lee &middot; Cedar Hills Realty</span><span>555-0142</span></div>'''
# 1 layouts
f1='''<div class="paper sh" style="left:60px;top:120px;width:330px;height:427px">
 <div class="photo" style="height:215px;background-image:url(ph_house.jpg)"></div>
 <div style="padding:14px 16px"><div class="serif" style="font-size:25px;font-weight:700;color:#1b2a4a;line-height:1.1">418 Maple Lane</div>
 <div style="font-size:13px;color:#667085;margin:6px 0 8px">3 bed &middot; 2 bath &middot; 1,850 sq ft</div>
 <div style="font-size:13px;line-height:1.5;color:#1d2433">&bull; Renovated kitchen<br>&bull; Fenced yard<br>&bull; Two blocks from the park</div></div>'''+foot(330)+'</div>'
f2='''<div class="paper sh" style="left:440px;top:120px;width:330px;height:427px">
 <div class="photo" style="position:absolute;left:0;top:0;width:150px;bottom:44px;background-image:url(ph_house.jpg);background-position:30% center"></div>
 <div style="position:absolute;left:164px;right:12px;top:18px"><div style="font-size:12px;font-weight:800;letter-spacing:.1em;color:#e0613a">OPEN HOUSE</div>
 <div class="serif" style="font-size:25px;font-weight:700;color:#1b2a4a;line-height:1.1;margin:6px 0 10px">Saturday<br>1&ndash;3 pm</div>
 <div style="font-size:13px;line-height:1.5;color:#1d2433">418 Maple Lane<br>3 bed &middot; 2 bath<br>Light kitchen, quiet street</div>
 <div style="margin-top:18px">'''+qr2(78)+'''<div style="font-size:11px;color:#667085;margin-top:4px">Scan for photos and details</div></div></div>'''+foot(330)+'</div>'
f3='''<div class="paper sh" style="left:820px;top:120px;width:330px;height:427px">
 <div style="padding:26px 20px 0"><div class="serif" style="font-size:31px;font-weight:700;color:#1b2a4a;line-height:1.08">What is your home worth today?</div>
 <div style="font-size:14px;color:#1d2433;margin-top:12px;line-height:1.45">Homes near Maple Lane sold in 18 days on average this quarter.</div></div>
 <div class="photo" style="position:absolute;left:20px;right:20px;top:168px;height:100px;border-radius:6px;background-image:url(ph_aerial.jpg)"></div>
 <div style="position:absolute;left:20px;top:290px;display:flex;gap:12px;align-items:center">'''+qr2(62)+'''<div style="font-size:14px;font-weight:700;color:#1b2a4a;line-height:1.3">Free value review.<br><span style="font-weight:500;color:#667085">Scan or call 555-0142</span></div></div>'''+foot(330)+'</div>'
f4='''<div class="paper sh" style="left:1200px;top:120px;width:330px;height:427px">
 <div class="photo" style="position:absolute;left:0;top:0;width:330px;height:190px;background-image:url(ph_house.jpg)"></div>
 <div class="photo" style="position:absolute;left:0;top:194px;width:108px;height:96px;background-image:url(ph_living.jpg)"></div>
 <div class="photo" style="position:absolute;left:111px;top:194px;width:108px;height:96px;background-image:url(ph_kitchen.jpg)"></div>
 <div class="photo" style="position:absolute;left:222px;top:194px;width:108px;height:96px;background-image:url(ph_aerial.jpg)"></div>
 <div style="position:absolute;left:16px;right:16px;top:304px"><div class="serif" style="font-size:22px;font-weight:700;color:#1b2a4a">Just listed: 418 Maple Lane</div>
 <div style="font-size:13px;color:#1d2433;margin-top:8px;line-height:1.5">3 bed &middot; 2 bath &middot; 1,850 sq ft &middot; Offered at $439,000<br><b style="color:#e0613a">Private showings: 555-0142</b></div></div>'''+foot(330)+'</div>'
caps=''.join('<div class="cap" style="left:%dpx;top:570px;width:330px">%s<small>%s</small></div>'%(x,t,s) for x,t,s in [(60,'Photo on top, facts below','Best for a listing'),(440,'Photo left, text right','Best for events and just sold'),(820,'Big headline, one image','Best for seller flyers'),(1200,'Four-photo grid','Best for strong interiors')])
fly_layouts=page(f1+f2+f3+f4+caps+'<div class="abs" style="left:60px;top:700px;width:1470px;font-size:23px;color:#1b2a4a;font-weight:600;line-height:1.4">Same structure, new photo and text each time: one goal, one photo, a few facts, one action.</div>','Four flyer layouts to reuse')
# 2 annotated
cx=540;cy=120
fl='''<div class="paper sh" style="left:%dpx;top:%dpx;width:520px;height:673px">
 <div class="serif" style="position:absolute;left:24px;top:20px;right:24px;font-size:31px;font-weight:700;color:#1b2a4a;line-height:1.12">Open house Sunday:<br>418 Maple Lane</div>
 <div class="photo" style="position:absolute;left:24px;right:24px;top:100px;height:250px;border-radius:6px;background-image:url(ph_house.jpg)"></div>
 <div style="position:absolute;left:24px;right:24px;top:368px;font-size:17px;line-height:1.5;color:#1d2433"><b>3 bed &middot; 2 bath &middot; 1,850 sq ft</b><br>&bull; Renovated kitchen &nbsp;&bull; Fenced yard<br>&bull; Two blocks from the park</div>
 <div style="position:absolute;left:24px;right:24px;top:470px;height:74px;background:#e0613a;border-radius:8px;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 20px"><div style="font-size:20px;font-weight:800;line-height:1.2">Sun 1&ndash;3 pm<br><span style="font-size:15px;font-weight:600">Scan to see photos and the floor plan</span></div><div style="background:#fff;padding:5px;border-radius:4px">'''%(cx,cy)+qr2(56)+'''</div></div>
 <div style="position:absolute;left:0;right:0;bottom:0;height:112px;background:#1b2a4a;color:#fff;padding:14px 24px;display:flex;align-items:center;gap:16px">
  <div style="width:70px;height:70px;border-radius:50%;background:#9fb4d6;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:26px;color:#1b2a4a;flex:none">DL</div>
  <div style="font-size:15px;line-height:1.45"><b style="font-size:18px">Dana Lee</b>, Realtor<br>Cedar Hills Realty &middot; 555-0142<br><span style="color:#b9c6e0">License number and disclosures as your state requires</span></div>
  <div style="margin-left:auto;width:56px;height:56px;border-radius:10px;border:2px solid #9fb4d6;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:18px">CH</div></div>
</div>'''
def L(n,txt,x,y,w=330,align='left'):
    return '<div class="call" style="left:%dpx;top:%dpx;width:%dpx"><b>%d</b><span>%s</span></div>'%(x,y,w,n,txt)
lines='''<svg class="lines"><line x1="330" y1="178" x2="548" y2="168"/><circle cx="548" cy="168" r="6"/>
<line x1="330" y1="300" x2="600" y2="300"/><circle cx="600" cy="300" r="6"/>
<line x1="330" y1="470" x2="580" y2="528"/><circle cx="580" cy="528" r="6"/>
<line x1="1270" y1="540" x2="1040" y2="628"/><circle cx="1040" cy="628" r="6"/>
<line x1="1270" y1="700" x2="930" y2="727"/><circle cx="930" cy="727" r="6"/>
<line x1="330" y1="730" x2="566" y2="735"/><circle cx="566" cy="735" r="6"/></svg>'''
anno=L(1,'Headline names the point: the address or the main feature',60,150,290)+L(2,'One strong photo, at print quality',60,278,290)+L(3,'Three to five facts, not a full list',60,440,290)+L(4,'One call to action: a number, a link or a QR code',1260,500,300)+L(5,'Your name, brokerage and any required details',1260,675,300)+L(6,'Headshot and logo, same as your card and profiles',60,705,290)
fly_anno=page(fl+lines+anno,'Anatomy of a listing flyer')
# 3 crowded vs clean
crowd='''<div class="paper sh" style="left:170px;top:115px;width:420px;height:545px;background:#fff7d6">
 <div style="position:absolute;right:-16px;top:-10px;width:130px;height:130px;background:#d62828;transform:rotate(14deg);clip-path:polygon(50% 0,61% 14%,79% 6%,80% 25%,98% 30%,86% 46%,100% 62%,81% 68%,82% 88%,62% 82%,50% 100%,38% 82%,19% 88%,20% 68%,0 62%,14% 46%,2% 30%,20% 25%,21% 6%,39% 14%);color:#fff;font-weight:800;font-size:17px;display:flex;align-items:center;justify-content:center;text-align:center">SALE!!!</div>
 <div style="font:800 28px Impact,'Liberation Sans';color:#d62828;padding:12px 14px;line-height:1">LOOK!! AMAZING!!!</div>
 <div style="font:italic 700 17px 'Liberation Serif';color:#0b5394;padding:0 14px">Dream house in the BEST neighborhood</div>
 <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:3px;padding:8px 14px 0"><div class="photo" style="height:62px;background-image:url(ph_house.jpg)"></div><div class="photo" style="height:62px;background-image:url(ph_living.jpg)"></div><div class="photo" style="height:62px;background-image:url(ph_kitchen.jpg)"></div><div class="photo" style="height:62px;background-image:url(ph_aerial.jpg)"></div><div class="photo" style="height:62px;background-image:url(ph_condo.jpg)"></div><div class="photo" style="height:62px;background-image:url(ph_house.jpg);filter:hue-rotate(80deg)"></div></div>
 <div style="font:700 15px 'Liberation Mono';color:#38761d;padding:8px 14px;line-height:1.4">3 BED! 2 BATH! GRANITE! HARDWOOD! NEW ROOF! BIG YARD! CLOSE TO SCHOOLS! SHOPPING! PARKS! GREAT VALUE! MUST SEE! WON'T LAST! BUYERS WANTED! CALL TODAY!</div>
 <div style="font:800 24px 'Liberation Sans';color:#7f6000;padding:0 14px">ONLY $439,000 (NEGOTIABLE)</div>
 <div style="font:600 14px 'Liberation Serif';color:#222;padding:6px 14px;line-height:1.45">Call 555-0142 or 555-0187 or text 555-0119 or email dana@example.com or visit www.example.com/dana or follow us on every social site. Open house Sat, Sun, or by appointment. Ask about financing, staging, free value review, buyer guide, seller guide, and our newsletter!</div>
 <div style="position:absolute;left:0;right:0;bottom:0;height:30px;background:#6a1b9a;color:#fff;font:700 12px 'Liberation Sans';display:flex;align-items:center;justify-content:center">Dana Lee &middot; Cedar Hills Realty &middot; Team Dana &middot; Top Producer</div></div>'''
clean='''<div class="paper sh" style="left:1010px;top:115px;width:420px;height:545px">
 <div class="serif" style="position:absolute;left:22px;right:22px;top:18px;font-size:30px;font-weight:700;color:#1b2a4a;line-height:1.1">Open house Sunday:<br>418 Maple Lane</div>
 <div class="photo" style="position:absolute;left:22px;right:22px;top:100px;height:215px;border-radius:6px;background-image:url(ph_house.jpg)"></div>
 <div style="position:absolute;left:22px;right:22px;top:332px;font-size:16px;line-height:1.5;color:#1d2433"><b>3 bed &middot; 2 bath &middot; 1,850 sq ft</b><br>Sun 1&ndash;3 pm &middot; Renovated kitchen</div>
 <div style="position:absolute;left:22px;top:404px;display:flex;gap:12px;align-items:center">'''+qr2(70)+'''<div style="font-size:16px;font-weight:700;color:#1b2a4a;line-height:1.3">Scan for photos and the floor plan</div></div>
 <div style="position:absolute;left:0;right:0;bottom:0;height:46px;background:#1b2a4a;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 18px;font-size:13px;font-weight:600"><span>Dana Lee &middot; Cedar Hills Realty</span><span>555-0142</span></div></div>'''
vs='<div class="abs" style="left:745px;top:340px;width:110px;height:110px;border-radius:50%;background:#1b2a4a;color:#fff;font-weight:800;font-size:34px;display:flex;align-items:center;justify-content:center">VS</div>'
cp='<div class="cap" style="left:170px;top:690px;width:420px;color:#c2410c">Crowded<small>Five reasons to do nothing</small></div><div class="cap" style="left:1010px;top:690px;width:420px;color:#1f8a5b">Clean<small>One job, one photo, one action</small></div>'
fly_vs=page(crowd+clean+vs+cp,'Crowded flyer vs clean flyer')
SC=dict(fly_layouts=fly_layouts,fly_anno=fly_anno,fly_vs=fly_vs)
if __name__=='__main__': render(sel(sys.argv,SC))
