import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
from s_m_leadgen import hero,title,dot,N,TEAL,OR
from s_m_lg_b import cards,steps,CARD,head
# ---- bai 5 lead nurturing
ln_hero_m=hero('ph_living','Real estate<br>lead nurturing','A simple program for slow leads')
c,y=cards('Three tracks for slow leads',[(OR,'New: first 30 days','Fast replies, a few touches a week','Goal: a first conversation'),(TEAL,'Warm: months 1 to 6','Every 2 to 3 weeks, useful and local','Goal: a clear timeline'),(N,'Long-term: months 6 to 24','Monthly or quarterly check-in','Goal: stay known and welcome')],h=262,size=62)
c+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:36px;font-weight:600;color:#667085">Sample rhythm. Adjust it to your market.</div>'%y
ln_tracks_m=page(c,'',note='',size=(1000,y+80))
msg=('<div class="abs" style="left:50px;top:190px;width:900px;border-radius:16px;background:#fff;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
     '<div style="height:80px;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:46px;font-weight:800">Monthly check-in</div>'
     '<div style="padding:28px"><div style="background:#e9f1fb;border-radius:20px;padding:26px 28px;font-size:44px;line-height:1.3;color:#1d2433;font-weight:600">Hi Sam, three homes sold on your street this month. Has your timeline changed, or are you still thinking about spring? Happy to send details.</div>'
     '<div style="margin-top:22px;font-size:40px;font-weight:700;color:%s">One question, easy to answer</div></div></div>')%(TEAL,OR)
ln_message_m=page(title('A check-in a slow lead can answer',size=60)+msg,'',note='',size=(1000,780))
c,y=steps('Four reasons to stop contact',['They ask you to stop','They hire another agent','Their number is on the registry','No reply for a long, set period'],rowh=150,size=62)
c+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:36px;font-weight:600;color:#667085">Sample rules. Pick your own limit.</div>'%y
ln_stop_m=page(c,'',note='',size=(1000,y+80))
# ---- bai 6 seller leads
sl_hero_m=hero('ph_house','How to get<br>seller leads','From people you already know')
c,y=cards('A four-touch seller campaign',[(TEAL,'Week 1: Market update','What sold nearby this month','No ask, just useful'),(N,'Week 3: Value offer','A free home value estimate','Reply with a yes or no'),(OR,'Week 6: Local story','A sale, a trend or a tip','Stay in their mind'),(TEAL,'Week 9: Direct question','Thinking of selling this year?','One line, easy reply')],h=250,gap=22,size=60)
c+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:36px;font-weight:600;color:#667085">Sample plan for one list.</div>'%y
sl_touch_m=page(c,'',note='',size=(1000,y+80))
msg=('<div class="abs" style="left:50px;top:190px;width:900px;border-radius:16px;background:#fff;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
     '<div style="height:80px;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:46px;font-weight:800">Touch 4: the direct question</div>'
     '<div style="padding:28px"><div style="background:#e9f1fb;border-radius:20px;padding:26px 28px;font-size:44px;line-height:1.3;color:#1d2433;font-weight:600">Hi Jo, homes near you are selling fast. Are you thinking about a move this year? A simple yes or no is fine.</div>'
     '<div style="margin-top:22px;font-size:40px;font-weight:700;color:%s">Short. Friendly. Easy to answer.</div></div></div>')%(OR,TEAL)
sl_message_m=page(title('A short seller message',size=60)+msg,'',note='',size=(1000,780))
c,y=steps('Before you call a past client',['Check the registry','Find the last closing date','Check for opt-out requests','Log the call and the result'],rowh=150,size=62)
c+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:36px;font-weight:600;color:#667085">Ask your broker if unsure.</div>'%y
sl_rules_m=page(c,'',note='',size=(1000,y+80))
SC=dict(ln_hero_m=ln_hero_m,ln_tracks_m=ln_tracks_m,ln_message_m=ln_message_m,ln_stop_m=ln_stop_m,sl_hero_m=sl_hero_m,sl_touch_m=sl_touch_m,sl_message_m=sl_message_m,sl_rules_m=sl_rules_m)
if __name__=='__main__': render(sel(sys.argv,SC))
