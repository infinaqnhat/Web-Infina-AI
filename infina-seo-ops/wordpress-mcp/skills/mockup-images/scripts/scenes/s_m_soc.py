import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
TYPE={'Local':('#dbeafe','#1e40af'),'Useful':('#dcfce7','#116b43'),'Personal':('#fde7f3','#9d174d'),'Proof':('#fef3c7','#92400e'),'Listing':('#ede9fe','#5b21b6')}
def title(t,sz=64): return '<div class="abs" style="left:50px;top:40px;width:900px;font-size:%dpx;font-weight:800;color:%s;line-height:1.1">%s</div>'%(sz,N,t)
def dot(n,sz=60): return '<div style="width:%dpx;height:%dpx;border-radius:50%%;background:#e0613a;color:#fff;font-size:40px;font-weight:800;display:flex;align-items:center;justify-content:center;flex:none">%d</div>'%(sz,sz,n)
# 1. four-week calendar: one card per week, three post types
def chip(t): return '<div style="background:%s;color:%s;border-radius:14px;padding:20px 0;text-align:center;font-size:40px;font-weight:800">%s</div>'%(TYPE[t][0],TYPE[t][1],t)
cal=[('Week 1',['Local','Useful','Personal']),('Week 2',['Local','Proof','Useful']),('Week 3',['Local','Useful','Listing']),('Week 4',['Personal','Useful','Proof'])]
g=title('Your first month of posts')
y=150
g+='<div class="abs" style="left:50px;top:%dpx;width:900px;display:grid;grid-template-columns:200px 1fr 1fr 1fr;gap:14px;padding:0 24px;font-size:38px;font-weight:700;color:#667085"><div></div><div style="text-align:center">Post 1</div><div style="text-align:center">Post 2</div><div style="text-align:center">Post 3</div></div>'%y
y+=64
for w,ps in cal:
    g+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:150px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);display:grid;grid-template-columns:200px 1fr 1fr 1fr;gap:14px;align-items:center;padding:0 24px"><div style="font-size:44px;font-weight:800;color:%s">%s</div>%s</div>'%(y,N,w,''.join(chip(p) for p in ps))
    y+=172
g+='<div class="abs" style="left:50px;top:%dpx;width:900px;background:#fff7e6;border-left:8px solid #e0a21b;border-radius:8px;padding:20px 28px;font-size:42px;color:#1d2433;line-height:1.3"><strong>Three good posts beat seven weak ones.</strong> Keep a local post every week.</div>'%(y+10)
y+=10+215
soc_calendar_m=page(g,'',note='',size=(1000,y))
# 2. weekly routine: minutes as bars
R=[('Monday: pick three topics','15 min','','#14808a',15),('Monday or Tuesday: batch posts','60 min','','#1b2a4a',60),('Every day: reply and comment','50 min','10 min a day, five days','#e0a21b',50),('Friday: note the best post','15 min','','#e0613a',15)]
t=title('About 140 minutes a week')
y=170
for name,mins,sub,c,v in R:
    t+='<div class="abs" style="left:50px;top:%dpx;font-size:42px;font-weight:700;color:#1d2433">%s</div>'%(y,name)
    w=max(int(v*10.5),60)
    t+='<div class="abs" style="left:50px;top:%dpx;width:%dpx;height:50px;background:%s;border-radius:8px"></div><div class="abs" style="left:%dpx;top:%dpx;font-size:48px;font-weight:800;color:%s;line-height:1">%s</div>'%(y+66,w,c,50+w+16,y+66,c if c!='#e0a21b' else '#b7791f',mins)
    if sub: t+='<div class="abs" style="left:50px;top:%dpx;font-size:38px;color:#667085">%s</div>'%(y+126,sub)
    y+=196 if sub else 150
y+=20
t+='<div class="abs" style="left:50px;top:%dpx;width:900px;background:#fff;border-radius:14px;box-shadow:0 6px 16px rgba(20,35,70,.12);padding:22px 28px"><div style="font-size:48px;font-weight:800;color:%s">Total: about 140 minutes</div><div style="font-size:40px;color:#475467;margin-top:8px">Batch once, then check in.</div></div>'%(y,N)
y+=190
soc_week_m=page(t,'',note='',size=(1000,y+20))
# 3. caption: post mock with three highlighted parts
def mark(n,bg,txt): return '<span style="background:%s;border-radius:6px;padding:0 6px;-webkit-box-decoration-break:clone;box-decoration-break:clone">%s</span>'%(bg,txt)
post=('<div class="paper sh" style="left:50px;top:150px;width:900px;height:760px;border-radius:16px">'
 '<div style="display:flex;gap:20px;align-items:center;padding:24px 30px"><div class="deco" style="width:76px;height:76px;border-radius:50%;background:#9fb4d6;color:#1b2a4a;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center">DL</div><div><div style="font-size:42px;font-weight:800;color:'+N+'">Dana Lee, Realtor</div><div style="font-size:38px;color:#667085">Cedar Hills</div></div></div>'
 '<div class="photo" style="height:260px;background-image:url(ph_aerial.jpg)"></div>'
 '<div style="padding:28px 32px;font-size:42px;line-height:1.5;color:#1d2433">'+mark(1,'#dbeafe','The Saturday market on Elm Street opens at 8.')+' '+mark(2,'#dcfce7','If you are house hunting nearby, the east side has two homes under contract this week.')+' '+mark(3,'#ffedd5','What would you like to know about this neighborhood?')+'</div></div>')
lab=''
y=960
for n,txt,bg in [(1,'Start with a concrete detail','#dbeafe'),(2,'Add one useful fact','#dcfce7'),(3,'End with one question','#ffedd5')]:
    lab+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:100px;display:flex;align-items:center;gap:22px"><div style="width:60px;height:60px;border-radius:50%%;background:#e0613a;color:#fff;font-size:40px;font-weight:800;display:flex;align-items:center;justify-content:center;flex:none">%d</div><div style="font-size:44px;font-weight:700;color:%s;background:%s;border-radius:10px;padding:6px 16px;line-height:1.2">%s</div></div>'%(y,n,N,bg,txt)
    y+=116
soc_caption_m=page(title('A caption people finish')+post+lab,'',note='',size=(1000,y+30))
SC=dict(soc_calendar_m=soc_calendar_m,soc_week_m=soc_week_m,soc_caption_m=soc_caption_m)
if __name__=='__main__': render(sel(sys.argv,SC))
