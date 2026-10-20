import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
TYPE={'Local':('#dbeafe','#1e40af'),'Useful':('#dcfce7','#116b43'),'Personal':('#fde7f3','#9d174d'),'Proof':('#fef3c7','#92400e'),'Listing':('#ede9fe','#5b21b6')}
def tag(t): return '<span class="chip" style="background:%s;color:%s;font-size:15px;padding:4px 12px">%s</span>'%(TYPE[t][0],TYPE[t][1],t)
cal=[('Week 1',[('Local','A favorite park or coffee shop in your area'),('Useful','How the offer and acceptance steps work'),('Personal','Why you became an agent')]),
('Week 2',[('Local','A school or community event this month'),('Proof','A recent closing story, with permission'),('Useful','Three things to fix before listing')]),
('Week 3',[('Local','A small business you recommend'),('Useful','A plain-language market update for your area'),('Listing','A home you represent, with the main reasons to visit')]),
('Week 4',[('Personal','A day on your calendar'),('Useful','Your answer to a question from this month'),('Proof','A client thank-you, with permission')])]
g='<div class="abs" style="left:70px;top:120px;width:1460px;display:grid;grid-template-columns:150px 1fr 1fr 1fr;gap:14px">'
g+='<div></div>'+''.join('<div style="font-size:18px;font-weight:800;color:#667085;letter-spacing:.1em">POST %d</div>'%i for i in (1,2,3))
for w,ps in cal:
    g+='<div style="font-size:26px;font-weight:800;color:%s;display:flex;align-items:center">%s</div>'%(N,w)
    for t,d in ps: g+='<div class="sh" style="background:#fff;border-radius:12px;padding:16px 18px;min-height:128px;box-shadow:0 6px 16px rgba(20,35,70,.12)">'+tag(t)+'<div style="font-size:20px;line-height:1.35;color:#1d2433;margin-top:10px">%s</div></div>'%d
g+='</div>'
soc_calendar=page(g+'<div class="abs" style="left:70px;top:808px;font-size:21px;color:#1b2a4a;font-weight:600">Three good posts a week beat seven weak ones. Rotate the types and keep the local post every week.</div>','A four-week starter calendar',note='')
# weekly
days=['Monday','Tuesday','Wednesday','Thursday','Friday']
def blk(h,t,c,txt): return '<div style="background:%s;color:#fff;border-radius:8px;padding:12px 14px;font-size:18px;font-weight:700;line-height:1.35;min-height:%dpx;margin-bottom:10px"><span style="font-size:15px;opacity:.9">%s</span><br>%s</div>'%(c,h,t,txt)
cols=''
for i,d in enumerate(days):
    x=70+i*296
    inner=''
    if d=='Monday': inner+=blk(60,'15 min','#14808a','Pick the week&rsquo;s three post topics')
    if d in ('Monday','Tuesday'): inner+=blk(120,'60 min','#1b2a4a','Batch: photos or video, captions, schedule' if d=='Monday' else 'Batch (if not done Monday)')
    inner+=blk(60,'10 min','#e0a21b','Reply to comments and comment on five local posts')
    if d=='Friday': inner+=blk(70,'15 min','#e0613a','Note the best post, save one idea')
    cols+='<div class="abs" style="left:%dpx;top:130px;width:276px"><div style="font-size:24px;font-weight:800;color:%s;margin-bottom:14px">%s</div>%s</div>'%(x,N,d,inner)
soc_week=page(cols+'<div class="abs" style="left:70px;top:620px;width:1460px;background:#fff;border-radius:12px;padding:22px 30px;font-size:24px;color:#1b2a4a;font-weight:600;box-shadow:0 6px 16px rgba(20,35,70,.12)">About 140 minutes a week, added up from the routine: 15 + 60 + (10 a day for five days) + 15. Batch once, then check in.</div>','A weekly routine that fits a busy schedule',note='Minutes follow the routine table in the guide.')
# caption
post=('<div class="paper sh" style="left:90px;top:80px;width:760px;height:640px;border-radius:14px"><div style="display:flex;gap:14px;align-items:center;padding:18px 24px"><div style="width:52px;height:52px;border-radius:50%;background:#9fb4d6;color:#1b2a4a;font-weight:800;font-size:20px;display:flex;align-items:center;justify-content:center">DL</div><div><div style="font-size:20px;font-weight:800;color:#1b2a4a">Dana Lee, Realtor</div><div style="font-size:15px;color:#667085">Cedar Hills &middot; 2 h</div></div></div>'
 '<div class="photo" style="height:340px;background-image:url(ph_aerial.jpg)"></div>'
 '<div style="padding:22px 28px;font-size:24px;line-height:1.5;color:#1d2433"><span style="background:#dbeafe">The Saturday market on Elm Street opens at 8.</span> <span style="background:#dcfce7">If you are house hunting nearby, the east side has two homes under contract this week.</span> <span style="background:#ffedd5">What would you like to know about this neighborhood?</span></div></div>')
notes=callout(1,'<strong>Start with a concrete detail.</strong> The first line is the part many platforms show.',900,170,620)+callout(2,'<strong>Add one useful fact.</strong> Real places, plain words, no &ldquo;dream home&rdquo;.',900,360,620)+callout(3,'<strong>End with one question.</strong> A question invites replies, and replies become conversations.',900,550,620)
soc_caption=page(post+notes+leaders([(890,200,830,470),(890,390,830,540),(890,580,830,610)]),'A caption people finish reading',note='Sample post. Names and details are made up.')
SC=dict(soc_calendar=soc_calendar,soc_week=soc_week,soc_caption=soc_caption)
if __name__=='__main__': render(sel(sys.argv,SC))
