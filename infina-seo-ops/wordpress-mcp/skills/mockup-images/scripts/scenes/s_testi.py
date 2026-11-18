import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
stars='<div style="color:#e0a21b;font-size:26px;letter-spacing:3px">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
weak='''<div class="paper sh" style="left:120px;top:150px;width:640px;height:520px;border-radius:14px;padding:38px 42px">
 <div class="chip" style="background:#fdecea;color:#b42318;position:absolute;right:30px;top:26px">Weak</div>
 '''+stars+'''
 <div class="serif" style="font-size:44px;line-height:1.3;margin-top:28px;color:#475467">&ldquo;Great agent, highly recommend.&rdquo;</div>
 <div style="margin-top:34px;font-size:22px;color:#667085;font-weight:600">&mdash; A client</div>
 <div style="position:absolute;left:42px;right:42px;bottom:36px;border-top:2px dashed #d0d5dd;padding-top:20px;font-size:21px;color:#98a2b3;line-height:1.5">No situation &middot; No result &middot; No name<br>Any agent could use this line</div></div>'''
strong='''<div class="paper sh" style="left:840px;top:150px;width:640px;height:520px;border-radius:14px;padding:38px 42px;border:3px solid #1f8a5b">
 <div class="chip" style="background:#e6f6ee;color:#116b43;position:absolute;right:30px;top:26px">Strong</div>
 '''+stars+'''
 <div class="serif" style="font-size:33px;line-height:1.38;margin-top:22px;color:#1d2433">&ldquo;<span style="background:#dbeafe;padding:0 3px">We were relocating from another state</span> and she arranged all our tours in one weekend. <span style="background:#dcfce7;padding:0 3px">We made an offer before we flew home.</span>&rdquo;</div>
 <div style="margin-top:26px;font-size:22px;color:#1d2433;font-weight:700"><span style="background:#fef3c7;padding:0 4px">&mdash; Chris and Dana, Riverside</span> <span style="font-weight:500;color:#667085">relocation buyers</span></div>
 <div style="position:absolute;left:42px;right:42px;bottom:30px;display:flex;gap:12px;flex-wrap:wrap">
  <span class="chip" style="background:#dbeafe;color:#1e40af">Situation</span><span class="chip" style="background:#dcfce7;color:#116b43">Result</span><span class="chip" style="background:#fef3c7;color:#92400e">Person</span></div></div>'''
testi_cards=page(weak+strong+'<div class="abs" style="left:120px;top:730px;font-size:25px;font-weight:600;color:#1b2a4a;width:1360px">A strong testimonial names a situation, a result and a person. Invented here to show structure; use only real client words.</div>','Weak vs strong testimonial',note='')
# ask
phone='''<div class="abs sh" style="left:130px;top:70px;width:400px;height:770px;border-radius:44px;background:#101828;padding:16px">
 <div style="width:100%;height:100%;border-radius:30px;background:#f2f4f7;position:relative;overflow:hidden">
  <div style="height:70px;background:#fff;border-bottom:1px solid #e4e7ec;display:flex;align-items:center;gap:12px;padding:0 18px"><div style="width:38px;height:38px;border-radius:50%;background:#9fb4d6;color:#1b2a4a;font-weight:800;display:flex;align-items:center;justify-content:center">C</div><div style="font-weight:700;font-size:18px">Chris</div></div>
  <div style="position:absolute;left:16px;right:34px;top:96px;background:#1b6ef3;color:#fff;border-radius:20px 20px 20px 4px;padding:14px 16px;font-size:17px;line-height:1.4">Hi Chris, congratulations again on your new home!</div>
  <div style="position:absolute;left:16px;right:20px;top:176px;background:#1b6ef3;color:#fff;border-radius:20px 20px 20px 4px;padding:14px 16px;font-size:17px;line-height:1.4">A short note from you helps neighbors decide who to call. Could you answer 3 quick questions? It takes two minutes.</div>
  <div style="position:absolute;left:16px;right:60px;top:316px;background:#fff;color:#1b6ef3;border:2px solid #1b6ef3;border-radius:20px 20px 20px 4px;padding:12px 16px;font-size:16px;font-weight:700">example.com/three-questions</div>
  <div style="position:absolute;right:16px;left:90px;top:410px;background:#e4e7ec;color:#1d2433;border-radius:20px 20px 4px 20px;padding:14px 16px;font-size:17px">Sure, I will send it tonight!</div>
  <div style="position:absolute;left:16px;right:34px;top:490px;background:#1b6ef3;color:#fff;border-radius:20px 20px 20px 4px;padding:14px 16px;font-size:17px;line-height:1.4">Thank you! Take your time.</div>
 </div></div>'''
steps='''<div class="abs" style="left:640px;top:120px;width:880px">
 <div style="display:flex;gap:22px;margin-bottom:34px;align-items:flex-start"><div class="chip" style="background:#e0613a;color:#fff;font-size:24px;padding:10px 20px">1</div><div><div style="font-size:30px;font-weight:800;color:#1b2a4a">Thank them first</div><div style="font-size:23px;color:#475467;margin-top:6px;line-height:1.4">Ask on closing day or right after, while the details are fresh.</div></div></div>
 <div style="display:flex;gap:22px;margin-bottom:34px;align-items:flex-start"><div class="chip" style="background:#e0613a;color:#fff;font-size:24px;padding:10px 20px">2</div><div><div style="font-size:30px;font-weight:800;color:#1b2a4a">Say in one sentence why it helps</div><div style="font-size:23px;color:#475467;margin-top:6px;line-height:1.4">&ldquo;A short note helps neighbors decide who to call.&rdquo;</div></div></div>
 <div style="display:flex;gap:22px;margin-bottom:34px;align-items:flex-start"><div class="chip" style="background:#e0613a;color:#fff;font-size:24px;padding:10px 20px">3</div><div><div style="font-size:30px;font-weight:800;color:#1b2a4a">Send a link or three short questions</div><div style="font-size:23px;color:#475467;margin-top:6px;line-height:1.5">Not a blank page. For example:<br>&bull; What was happening when you hired an agent?<br>&bull; What did we do that mattered most?<br>&bull; What would you tell a friend?</div></div></div>
 <div style="font-size:22px;color:#667085;border-top:2px solid #cbd2e0;padding-top:20px;line-height:1.5"><b style="color:#1b2a4a">Follow up once</b>, about a week later. Do not push after that.</div></div>'''
testi_ask=page(phone+steps,'How to ask for a testimonial')
# site
cards=''
data=[('Maya','first-time buyer, Cedar Hills','I had never made an offer on anything. She walked me through each step before I had to decide, and I never felt rushed.'),
      ('Chris and Dana','relocation buyers, Riverside','We toured eight homes in one weekend because she planned the route in advance. We made an offer before we flew home.'),
      ('Ruth','downsizer, Brookfield','She coordinated the movers, the repairs, and the closing date so we only had one thing to worry about.')]
for i,(n,w,q) in enumerate(data):
    cards+='<div style="background:#fff;border:1px solid #e4e7ec;border-radius:12px;padding:14px 22px;box-shadow:0 2px 8px rgba(16,24,40,.06)">'+stars.replace('26px','20px')+'<div class="serif" style="font-size:19px;line-height:1.4;margin:8px 0 10px;color:#1d2433">&ldquo;'+q+'&rdquo;</div><div style="font-size:17px;font-weight:700;color:#1b2a4a">'+n+'</div><div style="font-size:15px;color:#667085">'+w+'</div></div>'
site='''<div class="abs sh" style="left:90px;top:80px;width:1420px;height:740px;border-radius:14px;background:#fff;overflow:hidden">
 <div style="height:48px;background:#e9edf3;display:flex;align-items:center;gap:8px;padding:0 18px"><i style="width:12px;height:12px;border-radius:50%;background:#f87171"></i><i style="width:12px;height:12px;border-radius:50%;background:#fbbf24"></i><i style="width:12px;height:12px;border-radius:50%;background:#34d399"></i><div style="margin-left:18px;background:#fff;border-radius:6px;padding:5px 16px;font-size:15px;color:#667085;width:520px">example.com/dana-lee</div></div>
 <div style="height:62px;display:flex;align-items:center;justify-content:space-between;padding:0 40px;border-bottom:1px solid #eef0f4"><div style="font-weight:800;font-size:22px;color:#1b2a4a">Dana Lee <span style="font-weight:500;color:#667085;font-size:17px">&middot; Cedar Hills Realty</span></div><div style="font-size:16px;color:#475467;display:flex;gap:26px"><span>Buy</span><span>Sell</span><span style="font-weight:700;color:#1b2a4a;border-bottom:3px solid #e0613a;padding-bottom:3px">Clients say</span><span>Contact</span></div></div>
 <div style="padding:22px 40px;display:grid;grid-template-columns:1fr 340px;gap:30px">
  <div><div style="font-size:30px;font-weight:800;color:#1b2a4a;margin-bottom:6px">What clients say</div><div style="font-size:17px;color:#667085;margin-bottom:14px">Shown with each client&rsquo;s written permission. Recent reviews on my Google profile too.</div><div style="display:grid;grid-template-columns:1fr;gap:12px">'''+cards+'''</div></div>
  <div style="background:#f5f7fb;border-radius:12px;padding:26px;align-self:start"><div style="font-size:23px;font-weight:800;color:#1b2a4a;margin-bottom:14px">Talk to Dana</div>
   <div style="height:44px;border:1px solid #d0d5dd;border-radius:8px;background:#fff;margin-bottom:12px;padding:11px 14px;color:#98a2b3;font-size:16px">Your name</div><div style="height:44px;border:1px solid #d0d5dd;border-radius:8px;background:#fff;margin-bottom:12px;padding:11px 14px;color:#98a2b3;font-size:16px">Phone or email</div><div style="height:90px;border:1px solid #d0d5dd;border-radius:8px;background:#fff;margin-bottom:14px;padding:11px 14px;color:#98a2b3;font-size:16px">What are you planning?</div>
   <div style="background:#e0613a;color:#fff;font-weight:700;text-align:center;border-radius:8px;padding:13px;font-size:17px">Send</div></div></div></div>
 <div class="abs" style="left:90px;top:838px;font-size:17px;color:#667085">Fictional sample page and quotes, written to show where testimonials sit: near the contact form, with first name and area.</div>'''
testi_site=page(site,'',note='')
SC=dict(testi_cards=testi_cards,testi_ask=testi_ask,testi_site=testi_site)
if __name__=='__main__': render(sel(sys.argv,SC))
