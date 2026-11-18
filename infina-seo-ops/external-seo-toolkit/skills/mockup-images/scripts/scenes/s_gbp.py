import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
row=lambda ico,txt,col='#1d2433':'<div style="display:flex;gap:14px;align-items:center;font-size:19px;color:%s;margin:12px 0"><span style="width:22px;color:#14808a;font-weight:800">%s</span><span>%s</span></div>'%(col,ico,txt)
card=('<div class="paper sh" style="left:520px;top:100px;width:560px;height:600px;border-radius:14px">'
 +'<div style="position:absolute;left:0;top:0;right:0;height:170px;display:flex;gap:4px"><div class="photo" style="flex:2;background-image:url(ph_house.jpg)"></div><div style="flex:1;display:flex;flex-direction:column;gap:4px"><div class="photo" style="flex:1;background-image:url(ph_living.jpg)"></div><div class="photo" style="flex:1;background-image:url(ph_aerial.jpg)"></div></div></div>'
 +'<div style="position:absolute;left:28px;right:28px;top:190px">'
 +'<div style="font-size:30px;font-weight:800;color:'+N+'">Dana Lee, Realtor</div>'
 +'<div style="font-size:18px;margin-top:4px;color:#475467"><b>4.9</b> '+STARS+' <span style="color:#667085">(38 reviews)</span></div>'
 +'<div style="font-size:19px;color:#475467;margin-top:8px">Real estate agent</div>'
 +'<div style="border-top:1px solid #e4e7ec;margin-top:14px"></div>'
 +row('&#9679;','Serves Cedar Hills and nearby')+row('&#9719;','<b style="color:#1f8a5b">Open</b> &middot; Mon&ndash;Fri 9 am&ndash;6 pm')
 +'<div style="display:flex;gap:12px;margin:18px 0"><span class="chip" style="background:#e8f0fe;color:#1a56db;border-radius:8px;padding:10px 24px;font-size:18px">Call 555-0142</span><span class="chip" style="background:#e8f0fe;color:#1a56db;border-radius:8px;padding:10px 24px;font-size:18px">Website</span></div>'
 +'<div style="font-size:18px;line-height:1.5;color:#1d2433;border-top:1px solid #e4e7ec;padding-top:16px">I help first-time buyers and downsizers in Cedar Hills and nearby neighborhoods. I answer calls and messages the same day.</div>'
 +'</div></div>')
fields=card+leaders([(440,148,545,160),(440,268,545,310),(440,358,545,372),(440,448,545,421),(440,538,545,456),(1120,488,810,528),(1120,628,1060,615)])
fields+=callout(7,'Photos: a clear headshot, your office and local photos',80,128,360)+callout(1,'Name: your real-world name, no tagline',80,250,340)+callout(2,'Category: the most specific true one',80,340,340)+callout(3,'Service area, address hidden if no office',80,430,340)+callout(4,'Hours you can really answer',80,520,340)
fields+=callout(5,'Phone and website: a number you answer, a page made for visitors',1130,450,400)+callout(6,'Description: who you help and where, in plain words',1130,610,400)
# fix: the hours leader should point at the hours row (y 372) and callout 4 sits at 622: add line from callout
gbp_fields=page(fields,'Fields of a business profile (sample)',note='Sample profile. Name, numbers and ratings are made up.')
# review
rev=('<div class="paper sh" style="left:80px;top:170px;width:760px;height:450px;border-radius:14px;padding:34px 40px">'
 +'<div style="display:flex;gap:16px;align-items:center"><div style="width:56px;height:56px;border-radius:50%;background:#9fb4d6;color:#1b2a4a;font-weight:800;font-size:22px;display:flex;align-items:center;justify-content:center">MR</div><div><div style="font-size:22px;font-weight:800;color:'+N+'">Maya R.</div><div style="font-size:16px;color:#667085">2 weeks ago</div></div></div>'
 +'<div style="font-size:26px;margin:18px 0 10px">'+STARS+'</div>'
 +'<div class="serif" style="font-size:25px;line-height:1.5;color:#1d2433">&ldquo;Dana walked us through every step of buying our first home and answered every message the same day.&rdquo;</div>'
 +'<div style="margin-top:26px;background:#f3f6fb;border-left:5px solid #14808a;border-radius:6px;padding:20px 24px"><div style="font-size:17px;font-weight:800;color:#14808a;margin-bottom:6px">Response from the owner</div><div style="font-size:21px;line-height:1.5;color:#1d2433">Thank you, Maya! It was a pleasure helping you find the house on Cedar Lane. Enjoy the new home. &mdash; Dana</div></div></div>')
rules=('<div class="abs" style="left:900px;top:150px;width:620px">'
 +'<div style="display:flex;gap:16px;margin-bottom:28px"><span class="chip" style="background:#e0613a;color:#fff;height:34px">1</span><div><div style="font-size:27px;font-weight:800;color:'+N+'">Ask every client at closing</div><div style="font-size:21px;color:#475467;margin-top:4px;line-height:1.4">Send a direct link to your review page.</div></div></div>'
 +'<div style="display:flex;gap:16px;margin-bottom:28px"><span class="chip" style="background:#e0613a;color:#fff;height:34px">2</span><div><div style="font-size:27px;font-weight:800;color:'+N+'">Reply to every review</div><div style="font-size:21px;color:#475467;margin-top:4px;line-height:1.4">A few plain sentences, including the critical ones. Never argue in public.</div></div></div>'
 +'<div style="display:flex;gap:16px;margin-bottom:28px"><span class="chip" style="background:#b42318;color:#fff;height:34px">3</span><div><div style="font-size:27px;font-weight:800;color:#b42318">Never pay or reward for one</div><div style="font-size:21px;color:#475467;margin-top:4px;line-height:1.4">A gift card for a five-star review is the clearest thing to avoid. Never write or buy a review.</div></div></div>'
 +'<div style="background:#fdecea;border:2px dashed #f0a39b;border-radius:10px;padding:18px 22px;font-size:20px;color:#b42318;line-height:1.4"><b>Not allowed:</b> &ldquo;Leave a 5-star review and get a $10 gift card.&rdquo;</div></div>')
gbp_review=page(rev+rules,'Reviews: ask, reply, never pay',note='Sample review. Names are made up.')
# name
def box(x,name,col,bg,tag,note,ok):
    return ('<div class="paper sh" style="left:%dpx;top:170px;width:640px;height:380px;border-radius:14px;border:4px solid %s">'%(x,col)
     +'<div style="background:'+bg+';padding:26px 32px"><span class="chip" style="background:'+col+';color:#fff">'+tag+'</span></div>'
     +'<div style="padding:34px 36px"><div style="font-size:'+('34' if ok else '27')+'px;font-weight:800;color:'+N+';line-height:1.3">'+name+'</div><div style="font-size:19px;color:#475467;margin:10px 0 16px">Real estate agent</div><div style="font-size:21px;line-height:1.5;color:#1d2433">'+note+'</div></div></div>')
nm=box(110,'Dana Lee, Realtor','#1f8a5b','#e6f6ee','Use the real-world name','The name on your sign, website and cards, exactly as clients know it.',True)
nm+=box(850,'Dana Lee | #1 Realtor in Cedar Hills | Best Homes For Sale','#b42318','#fdecea','Keyword-stuffed name','Taglines and keywords added to the name can get a profile suspended.',False)
gbp_name=page(nm+'<div class="abs" style="left:110px;top:620px;width:1380px;font-size:25px;font-weight:600;color:'+N+'">Google expects the name you really use. Keep it the same on your profile, website and cards.</div>','True name vs keyword-stuffed name',note='')
SC=dict(gbp_fields=gbp_fields,gbp_review=gbp_review,gbp_name=gbp_name)
if __name__=='__main__': render(sel(sys.argv,SC))
