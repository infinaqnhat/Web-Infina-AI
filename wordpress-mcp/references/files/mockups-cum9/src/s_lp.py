import sys
from common import *
def slide(x,y,w,h,inner,title,n=''):
    return '<div class="paper sh" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:8px">%s</div>'%(x,y,w,h,inner)
# pricing slide 1280x720 scaled to 1200x675
price='''<div style="position:absolute;left:0;top:0;right:0;height:96px;background:#1b2a4a;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 48px"><div class="serif" style="font-size:38px;font-weight:700">Pricing recommendation</div><div style="font-size:20px;color:#b9c6e0">418 Maple Lane &middot; Cedar Hills</div></div>
<div style="position:absolute;left:48px;top:128px;right:48px;font-size:21px;font-weight:700;color:#1b2a4a">Three comparable sales I weighed most</div>
<table style="position:absolute;left:48px;top:170px;width:1104px;border-collapse:collapse;font-size:21px">
<tr style="background:#eef2f8;color:#475467;font-size:17px;text-transform:uppercase;letter-spacing:.06em"><th style="text-align:left;padding:12px 16px">Address</th><th style="text-align:left">Sold</th><th style="text-align:left">Bed / bath</th><th style="text-align:left">Sq ft</th><th style="text-align:left">How it differs from your home</th></tr>
<tr style="border-bottom:1px solid #e4e7ec"><td style="padding:16px">412 Cedar Lane</td><td><b>$438,000</b></td><td>3 / 2</td><td>1,720</td><td>Newer kitchen, no fence</td></tr>
<tr style="border-bottom:1px solid #e4e7ec"><td style="padding:16px">27 Birch Court</td><td><b>$421,500</b></td><td>3 / 2</td><td>1,790</td><td>Smaller lot, older roof</td></tr>
<tr><td style="padding:16px">905 Oak Avenue</td><td><b>$449,000</b></td><td>4 / 2</td><td>1,880</td><td>Extra bedroom, busier street</td></tr></table>
<div style="position:absolute;left:48px;top:420px;font-size:21px;font-weight:700;color:#1b2a4a">Recommended list range</div>
<div style="position:absolute;left:48px;top:470px;width:1104px;height:18px;background:#e4e7ec;border-radius:9px"></div>
<div style="position:absolute;left:467px;top:466px;width:353px;height:26px;background:#14808a;border-radius:13px"></div>
<div style="position:absolute;left:440px;top:506px;font-size:34px;font-weight:800;color:#14808a">$429,000 &ndash; $445,000</div>
<div style="position:absolute;left:48px;top:506px;font-size:17px;color:#667085">$410,000</div><div style="position:absolute;right:48px;top:506px;font-size:17px;color:#667085">$460,000</div>
<div style="position:absolute;left:48px;right:48px;bottom:36px;background:#fff7e6;border-left:6px solid #e0a21b;padding:14px 20px;font-size:20px;color:#1d2433"><b>What could move the number:</b> condition after the inspection, timing of your move, and any new listing nearby.</div>'''
lp_price=page(slide(200,70,1200,675,price,'')+'',' ',note='Sample slide. Addresses and prices are made up.')
plan='''<div style="position:absolute;left:0;top:0;right:0;height:96px;background:#1b2a4a;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 48px"><div class="serif" style="font-size:38px;font-weight:700">Marketing plan, with dates</div><div style="font-size:20px;color:#b9c6e0">Prepared for the Parks</div></div>
<div style="position:absolute;left:48px;right:48px;top:150px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:28px">
 <div style="border-top:8px solid #14808a;background:#f5f8fc;padding:22px 24px;min-height:380px"><div style="font-size:16px;font-weight:800;color:#14808a;letter-spacing:.08em">DAYS &minus;7 TO &minus;1</div><div style="font-size:28px;font-weight:800;color:#1b2a4a;margin:6px 0 16px">Before the launch</div><div style="font-size:21px;line-height:1.65;color:#1d2433">Professional photos<br>Listing description, reviewed with you<br>Prep tips: declutter, repairs, curb appeal</div></div>
 <div style="border-top:8px solid #e0613a;background:#fdf3ee;padding:22px 24px;min-height:380px"><div style="font-size:16px;font-weight:800;color:#e0613a;letter-spacing:.08em">DAY 0</div><div style="font-size:28px;font-weight:800;color:#1b2a4a;margin:6px 0 16px">Launch day</div><div style="font-size:21px;line-height:1.65;color:#1d2433">Listing goes live on the major portals<br>Yard sign and flyer box<br>Email to my buyer list</div></div>
 <div style="border-top:8px solid #1b2a4a;background:#f5f8fc;padding:22px 24px;min-height:380px"><div style="font-size:16px;font-weight:800;color:#1b2a4a;letter-spacing:.08em">DAYS 1&ndash;14</div><div style="font-size:28px;font-weight:800;color:#1b2a4a;margin:6px 0 16px">First two weeks</div><div style="font-size:21px;line-height:1.65;color:#1d2433">Open house on the first weekend<br>Mailers to the nearby streets<br>Social posts<br>Weekly update call with you</div></div></div>
<div style="position:absolute;left:48px;right:48px;bottom:30px;font-size:20px;color:#475467">Every step has a date, so you always know what happens next.</div>'''
lp_plan=page(slide(200,70,1200,675,plan,''),' ',note='Sample slide. Dates and steps are an example.')
titles=['Welcome and agenda','About you and your area','What the seller wants','Market snapshot','Comparable sales','Pricing recommendation','Marketing plan and timeline','Preparation and showing plan','Process from signing to closing','Terms and compensation','Results and testimonials','Next steps and questions']
cols=['#14808a','#1b2a4a','#e0613a']
thumbs=''
for i,t in enumerate(titles):
    c=cols[i//4 % 3] if False else ('#1b2a4a' if i<3 else '#14808a' if i<7 else '#e0613a' if i<10 else '#1b2a4a')
    x=70+(i%4)*370; y=90+(i//4)*250
    thumbs+='<div class="paper sh" style="left:%dpx;top:%dpx;width:330px;height:186px;border-radius:6px"><div style="height:12px;background:%s"></div><div style="padding:14px 16px"><div style="font-size:15px;font-weight:800;color:%s;letter-spacing:.08em">SLIDE %d</div><div class="serif" style="font-size:22px;font-weight:700;color:#1b2a4a;line-height:1.2;margin-top:6px">%s</div><div style="margin-top:14px;height:8px;width:75%%;background:#e4e7ec;border-radius:4px"></div><div style="margin-top:8px;height:8px;width:55%%;background:#e4e7ec;border-radius:4px"></div><div style="margin-top:8px;height:8px;width:65%%;background:#e4e7ec;border-radius:4px"></div></div></div>'%(x,y,c,c,i+1,t)
lp_outline=page(thumbs+'<div class="abs" style="left:70px;top:812px;font-size:22px;color:#1b2a4a;font-weight:600">Twelve slides you can cover in about forty-five minutes. A longer deck usually means you are reading, not talking.</div>','A 12-slide listing presentation outline',note='')
SC=dict(lp_price=lp_price,lp_plan=lp_plan,lp_outline=lp_outline)
if __name__=='__main__': render(sel(sys.argv,SC))
