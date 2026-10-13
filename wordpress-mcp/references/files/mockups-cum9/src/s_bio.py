import sys
from common import *
N='#1b2a4a'
who='background:#dbeafe;border-radius:4px;padding:1px 3px'
proof='background:#dcfce7;border-radius:4px;padding:1px 3px'
nxt='background:#ffedd5;border-radius:4px;padding:1px 3px'
site='''<div class="abs sh" style="left:90px;top:110px;width:1420px;height:640px;border-radius:14px;background:#fff;overflow:hidden">
 <div style="height:48px;background:#e9edf3;display:flex;align-items:center;gap:8px;padding:0 18px"><i style="width:12px;height:12px;border-radius:50%;background:#f87171"></i><i style="width:12px;height:12px;border-radius:50%;background:#fbbf24"></i><i style="width:12px;height:12px;border-radius:50%;background:#34d399"></i><div style="margin-left:18px;background:#fff;border-radius:6px;padding:5px 16px;font-size:15px;color:#667085;width:520px">example.com/about</div></div>
 <div style="height:62px;display:flex;align-items:center;padding:0 40px;border-bottom:1px solid #eef0f4;font-weight:800;font-size:22px;color:#1b2a4a">Cedar Hills Realty</div>
 <div style="display:flex;gap:46px;padding:44px 56px">
  <div style="flex:none;text-align:center"><div style="width:230px;height:230px;border-radius:50%;background:#9fb4d6;color:#1b2a4a;font-weight:800;font-size:76px;display:flex;align-items:center;justify-content:center">DR</div><div style="margin-top:18px;font-size:19px;color:#475467;line-height:1.5">555-0138<br>daniel@example.com</div></div>
  <div style="flex:1"><div style="font-size:42px;font-weight:800;color:#1b2a4a">Daniel Reyes</div><div style="font-size:21px;color:#14808a;font-weight:700;margin:4px 0 22px">Buyer specialist, Cedar Hills</div>
   <div class="serif" style="font-size:25px;line-height:1.62;color:#1d2433">Daniel Reyes <span style="'''+who+'''">helps first-time buyers in Cedar Hills find a home they can afford and understand each step along the way.</span> <span style="'''+proof+'''">A former teacher, he explains the process in plain language and answers every message the same day.</span> Outside work, he coaches youth basketball. <span style="'''+nxt+'''">Call or message Daniel to talk about your first home.</span></div>
   <div style="display:flex;gap:14px;margin-top:34px"><span class="chip" style="background:#dbeafe;color:#1e40af">Who you help</span><span class="chip" style="background:#dcfce7;color:#116b43">Proof</span><span class="chip" style="background:#ffedd5;color:#9a3412">Next step</span></div></div></div></div>
 <div class="abs" style="left:90px;top:772px;font-size:18px;color:#667085">Fictional agent and bio, written to show the structure. Replace every invented fact with something true about you.</div>'''
bio_profile=page(site,'',note='')
rows=[('I am passionate about real estate.','I help buyers in Cedar Hills compare homes without pressure.'),
 ('I provide excellent service.','I reply to every message within the hour on business days.'),
 ('I know the market.','I have sold in Cedar Hills since 2017 and know its streets and schools.'),
 ('I am the number one agent.','My clients rate me five stars on Google, with 40 reviews.')]
r=''
for i,(b,a) in enumerate(rows):
    y=150+i*148
    r+='<div class="paper sh" style="left:70px;top:%dpx;width:600px;height:118px;border-radius:12px;display:flex;align-items:center;padding:0 28px;gap:18px"><span style="flex:none;width:36px;height:36px;border-radius:50%%;background:#fdecea;color:#b42318;font-weight:800;font-size:22px;display:flex;align-items:center;justify-content:center">&times;</span><span class="serif" style="font-size:25px;color:#667085;text-decoration:line-through;text-decoration-color:#d0d5dd">%s</span></div>'%(y,b)
    r+='<div class="abs" style="left:690px;top:%dpx;width:60px;height:118px;display:flex;align-items:center;justify-content:center;font-size:40px;color:#14808a;font-weight:800">&rarr;</div>'%y
    r+='<div class="paper sh" style="left:770px;top:%dpx;width:760px;height:118px;border-radius:12px;border:3px solid #1f8a5b;display:flex;align-items:center;padding:0 28px;gap:18px"><span style="flex:none;width:36px;height:36px;border-radius:50%%;background:#e6f6ee;color:#116b43;font-weight:800;font-size:22px;display:flex;align-items:center;justify-content:center">&#10003;</span><span class="serif" style="font-size:25px;color:#1d2433;line-height:1.35">%s</span></div>'%(y,a)
head='<div class="abs" style="left:70px;top:108px;font-size:19px;font-weight:800;letter-spacing:.1em;color:#b42318">BEFORE: VAGUE</div><div class="abs" style="left:770px;top:108px;font-size:19px;font-weight:800;letter-spacing:.1em;color:#116b43">AFTER: SPECIFIC</div>'
bio_beforeafter=page(head+r+'<div class="abs" style="left:70px;top:752px;width:1460px;font-size:22px;color:#475467;line-height:1.45">Each stronger line names an audience, an area, one strength, or a next step. The details here are placeholders: use only facts that are true for you.</div>','Rewrite weak bio lines',note='')
def pc(x,name,ini,role,txt,chips,col):
    ch=''.join('<span class="chip" style="background:%s;color:%s;font-size:15px;padding:5px 12px">%s</span>'%(bg,fg,t) for t,bg,fg in chips)
    return '''<div class="paper sh" style="left:%dpx;top:110px;width:470px;height:690px;border-radius:14px">
 <div style="height:130px;background:%s"></div><div style="margin:-62px 0 0 32px;width:124px;height:124px;border-radius:50%%;background:#fff;border:6px solid #fff;box-shadow:0 4px 12px rgba(16,24,40,.18);display:flex;align-items:center;justify-content:center"><div style="width:100%%;height:100%%;border-radius:50%%;background:#e7eefc;color:#1b2a4a;font-weight:800;font-size:38px;display:flex;align-items:center;justify-content:center">%s</div></div>
 <div style="padding:14px 32px 0"><div style="font-size:31px;font-weight:800;color:#1b2a4a">%s</div><div style="font-size:18px;color:#14808a;font-weight:700;margin:2px 0 14px">%s</div>
 <div class="serif" style="font-size:20px;line-height:1.55;color:#1d2433">%s</div><div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:20px">%s</div></div></div>'''%(x,col,ini,name,role,txt,ch)
B=('background:#dbeafe','color:#1e40af')
chips=lambda a,b,c,d:[(a,'#dbeafe','#1e40af'),(b,'#e0f2fe','#075985'),(c,'#dcfce7','#116b43'),(d,'#ffedd5','#9a3412')]
g=pc(60,'Daniel Reyes','DR','New agent, first-time buyers','Daniel Reyes helps first-time buyers in Cedar Hills find a home they can afford and understand each step along the way. A former teacher, he explains the process in plain language and answers every message the same day. Call or message Daniel to talk about your first home.',chips('Audience: first-time buyers','Area: Cedar Hills','Strength: plain language','Next step: call'),'linear-gradient(135deg,#14808a,#1b2a4a)')
g+=pc(565,'Linda Park','LP','Downsizing specialist','Linda Park guides homeowners in the east side suburbs through the move to a smaller home. She coordinates movers, repairs, and timing so that clients can focus on the transition rather than the logistics. Call Linda for a no-pressure conversation about your timeline.',chips('Audience: downsizers','Area: east side suburbs','Strength: coordination','Next step: call'),'linear-gradient(135deg,#e0613a,#7c2d12)')
g+=pc(1070,'Priya Shah','PS','Relocation specialist','Priya Shah helps people moving to the Riverside area from other cities. She prepares neighborhood overviews, schedules tours for a single trip, and stays in touch until move-in day. Reach out to Priya to plan your visit.',chips('Audience: relocating buyers','Area: Riverside','Strength: one-trip tours','Next step: plan a visit'),'linear-gradient(135deg,#1b2a4a,#4b5f8a)')
bio_gallery=page(g,'Three bios, one structure',note='Fictional agents and bios, written to show the structure.')
SC=dict(bio_profile=bio_profile,bio_beforeafter=bio_beforeafter,bio_gallery=bio_gallery)
if __name__=='__main__': render(sel(sys.argv,SC))
