import sys
from common import *
N='#1b2a4a'
def front(x,y,w,h,scale=1.0):
    f=scale
    return '''<div class="paper sh" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:6px">
 <div class="photo" style="position:absolute;left:0;top:0;right:0;bottom:0;background-image:url(ph_house.jpg)"></div>
 <div style="position:absolute;left:0;right:0;bottom:0;height:%dpx;background:linear-gradient(0deg,rgba(14,28,56,.92),rgba(14,28,56,0))"></div>
 <div style="position:absolute;left:0;top:%dpx;background:#d62828;color:#fff;font-weight:800;font-size:%dpx;letter-spacing:.12em;padding:%dpx %dpx">JUST SOLD</div>
 <div class="serif" style="position:absolute;left:%dpx;right:%dpx;bottom:%dpx;color:#fff;font-size:%dpx;font-weight:700;line-height:1.15">Just sold on Cedar Lane:<br>14 days on market</div></div>'''%(x,y,w,h,int(h*.5),int(24*f),int(20*f),int(8*f),int(18*f),int(26*f),int(26*f),int(22*f),int(40*f))
def back(x,y,w,h,f=1.0):
    P=lambda v:str(int(v*f))
    return ('<div class="paper sh" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:6px">'%(x,y,w,h)
     +'<div style="position:absolute;left:'+P(26)+'px;top:'+P(26)+'px;width:'+str(int(w*.5))+'px">'
     +'<div class="serif" style="font-size:'+P(26)+'px;font-weight:700;color:#1b2a4a;line-height:1.2">See what homes near you are selling for.</div>'
     +'<div style="font-size:'+P(18)+'px;color:#1d2433;margin-top:'+P(10)+'px;line-height:1.45">Call or scan for a free value review.</div>'
     +'<div style="display:flex;gap:'+P(14)+'px;align-items:center;margin-top:'+P(18)+'px">'+qr2(int(84*f))
     +'<div style="font-size:'+P(16)+'px;line-height:1.4;color:#1b2a4a;font-weight:700">Dana Lee<br><span style="font-weight:500;color:#475467">Cedar Hills Realty<br>555-0142</span></div></div></div>'
     +'<div style="position:absolute;right:'+P(22)+'px;top:'+P(22)+'px;width:'+P(110)+'px;height:'+P(80)+'px;border:2px solid #cbd2e0;display:flex;align-items:center;justify-content:center;text-align:center;font-size:'+P(13)+'px;color:#667085;line-height:1.3">Postage<br>area</div>'
     +'<div style="position:absolute;right:'+P(26)+'px;bottom:'+P(40)+'px;width:'+str(int(w*.34))+'px;font-size:'+P(17)+'px;line-height:1.6;color:#1d2433;border-top:2px solid #e4e7ec;padding-top:'+P(10)+'px">Local Postal Customer<br>Cedar Hills</div></div>')
fb=front(90,140,640,427)+back(820,140,640,427,1.3)
post_just_sold=page(fb+'<div class="cap" style="left:90px;top:600px;width:640px">Front<small>One photo, one plain headline</small></div><div class="cap" style="left:820px;top:600px;width:640px">Back<small>One offer, one way to respond, your name and brokerage</small></div><div class="abs" style="left:90px;top:730px;width:1370px;font-size:25px;font-weight:600;color:'+N+'">A just-sold postcard: show a result on a nearby street, then invite a free home value review.</div>','Just sold postcard, front and back',note='Sample card. Address and results are made up.')
# annotated
big=front(90,130,900,600,1.35)
def L(n,txt,x,y,w=470): return '<div class="call" style="left:%dpx;top:%dpx;width:%dpx"><b>%d</b><span>%s</span></div>'%(x,y,w,n,txt)
# the front has no band with offer; build a more complete one
card='''<div class="paper sh" style="left:90px;top:130px;width:900px;height:620px;border-radius:8px">
 <div class="photo" style="position:absolute;left:0;top:0;right:0;height:400px;background-image:url(ph_house.jpg)"></div>
 <div style="position:absolute;left:0;right:0;top:230px;height:170px;background:linear-gradient(0deg,rgba(14,28,56,.92),rgba(14,28,56,0))"></div>
 <div style="position:absolute;left:0;top:30px;background:#d62828;color:#fff;font-weight:800;font-size:26px;letter-spacing:.12em;padding:10px 26px">JUST SOLD</div>
 <div class="serif" style="position:absolute;left:36px;bottom:238px;color:#fff;font-size:44px;font-weight:700;line-height:1.12">Just sold on Cedar Lane: 14 days on market</div>
 <div style="position:absolute;left:36px;top:424px;width:600px"><div style="font-size:27px;font-weight:700;color:#1b2a4a">See what homes near you are selling for.</div><div style="font-size:23px;color:#d62828;font-weight:800;margin-top:6px">Call or scan for a free value review.</div></div>
 <div style="position:absolute;right:36px;top:424px;background:#fff;border:2px solid #e4e7ec;padding:8px">'''+qr2(110)+'''</div>
 <div style="position:absolute;left:36px;right:36px;bottom:20px;display:flex;justify-content:space-between;font-size:20px;color:#475467;border-top:2px solid #e4e7ec;padding-top:12px"><span><b style="color:#1b2a4a">Dana Lee</b> &middot; Cedar Hills Realty &middot; 555-0142</span><span>Licensed under Cedar Hills Realty</span></div></div>'''
lines='''<svg class="lines"><line x1="1050" y1="188" x2="858" y2="440"/><circle cx="858" cy="440" r="6"/>
<line x1="1050" y1="328" x2="720" y2="210"/><circle cx="720" cy="210" r="6"/>
<line x1="1050" y1="468" x2="640" y2="598"/><circle cx="640" cy="598" r="6"/>
<line x1="1050" y1="598" x2="930" y2="612"/><circle cx="930" cy="612" r="6"/>
<line x1="1050" y1="708" x2="945" y2="720"/><circle cx="945" cy="720" r="6"/></svg>'''
calls=L(1,'Headline in plain words: what happened, where, how fast',1050,160)+L(2,'One strong photo of a nearby home',1050,300)+L(3,'One offer, not three',1050,440)+L(4,'One way to respond: call, or scan a code that is tracked',1050,565)+L(5,'Your name, brokerage and required details',1050,685)
post_anno=page(card+lines+calls,'What goes on a just-sold postcard',note='Sample card. Address and results are made up.')
# qr / tracking
mu='''<div class="paper sh" style="left:90px;top:130px;width:700px;height:467px;border-radius:8px">
 <div style="background:#1b2a4a;color:#fff;padding:26px 30px"><div style="font-size:15px;font-weight:800;letter-spacing:.14em;color:#9fb4d6">MARKET UPDATE</div><div class="serif" style="font-size:33px;font-weight:700;margin-top:6px;line-height:1.15">Three numbers for Cedar Hills this quarter</div></div>
 <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;padding:24px 30px 0">
  <div style="background:#f2f5fa;border-radius:8px;padding:16px"><div style="font-size:30px;font-weight:800;color:#1b2a4a">$438,000</div><div style="font-size:16px;color:#667085;margin-top:4px">Median price</div></div>
  <div style="background:#f2f5fa;border-radius:8px;padding:16px"><div style="font-size:30px;font-weight:800;color:#1b2a4a">21</div><div style="font-size:16px;color:#667085;margin-top:4px">Days on market</div></div>
  <div style="background:#f2f5fa;border-radius:8px;padding:16px"><div style="font-size:30px;font-weight:800;color:#1b2a4a">38</div><div style="font-size:16px;color:#667085;margin-top:4px">Homes for sale</div></div></div>
 <div style="display:flex;gap:20px;align-items:center;padding:26px 30px"><div style="border:2px solid #e4e7ec;padding:7px">'''+qr2(100)+'''</div><div style="font-size:22px;font-weight:700;color:#1b2a4a;line-height:1.35">Scan for the full report.<br><span style="font-weight:500;color:#667085;font-size:18px">Dana Lee &middot; Cedar Hills Realty &middot; 555-0142</span></div></div></div>'''
tbl='''<div class="paper sh" style="left:850px;top:130px;width:660px;height:467px;border-radius:8px;padding:30px 32px">
 <div style="font-size:28px;font-weight:800;color:#1b2a4a">One link per mailing</div><div style="font-size:19px;color:#667085;margin:6px 0 18px">So you can see which card brought a response.</div>
 <table style="width:100%;border-collapse:collapse;font-size:20px"><tr style="background:#eef2f8;color:#475467;font-size:15px;text-transform:uppercase;letter-spacing:.06em"><th style="text-align:left;padding:10px 12px">Mailing</th><th style="text-align:left">Link</th><th style="text-align:right;padding-right:12px">Scans</th></tr>
 <tr style="border-bottom:1px solid #e4e7ec"><td style="padding:14px 12px">Just sold, Cedar Lane</td><td style="color:#14808a">example.com/js-01</td><td style="text-align:right;padding-right:12px"><b>12</b></td></tr>
 <tr style="border-bottom:1px solid #e4e7ec"><td style="padding:14px 12px">Market update</td><td style="color:#14808a">example.com/mu-02</td><td style="text-align:right;padding-right:12px"><b>31</b></td></tr>
 <tr><td style="padding:14px 12px">Seasonal checklist</td><td style="color:#14808a">example.com/se-03</td><td style="text-align:right;padding-right:12px"><b>9</b></td></tr></table>
 <div style="margin-top:22px;font-size:18px;color:#667085">Sample counts, not real results.</div></div>'''
post_qr=page(mu+tbl+'<div class="abs" style="left:90px;top:660px;width:1420px;font-size:25px;font-weight:600;color:'+N+';line-height:1.45">Give each mailing its own QR code or short link, then record the scans and calls in your CRM. After a few mailings you can compare cards instead of guessing.</div>','Track every card with its own link',note='')
SC=dict(post_just_sold=post_just_sold,post_anno=post_anno,post_qr=post_qr)
if __name__=='__main__': render(sel(sys.argv,SC))
