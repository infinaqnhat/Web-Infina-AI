import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'; GOLD='#c9a24a'; OR='#e0613a'; TEAL='#14808a'
def bar(w,h=16,c='#d9dee7',m=10): return '<div style="width:%s;height:%dpx;background:%s;border-radius:%dpx;margin-bottom:%dpx"></div>'%(w,h,c,h//2,m)
# 1. #981: pick a site design by goal (replaces the Luxury Presence vs Real Geeks table)
def thumb(inner,bg='#fff'):
    return '<div class="deco" style="flex:none;width:230px;height:150px;border-radius:12px;background:%s;border:2px solid #d0d7e2;overflow:hidden;position:relative">%s</div>'%(bg,inner)
t1='<div style="position:absolute;inset:0;background:url(ph_house.jpg) center/cover"></div><div style="position:absolute;left:18px;bottom:16px;width:130px;height:16px;border-radius:8px;background:#fff"></div><div style="position:absolute;left:18px;bottom:42px;width:90px;height:12px;border-radius:6px;background:rgba(255,255,255,.7)"></div>'
t2='<div style="padding:18px"><div style="display:flex;gap:10px;margin-bottom:14px"><div style="flex:1;height:34px;border-radius:8px;background:#e4e8f0"></div><div style="width:60px;height:34px;border-radius:8px;background:'+OR+'"></div></div>'+bar('90%')+bar('65%')+bar('78%')+'</div>'
t3='<div style="padding:18px"><div style="display:flex;gap:10px;margin-bottom:16px"><div style="width:44px;height:44px;border-radius:8px;background:'+N+'"></div><div style="width:44px;height:44px;border-radius:8px;background:'+GOLD+'"></div><div style="width:44px;height:44px;border-radius:8px;background:'+TEAL+'"></div></div>'+bar('85%',18,'#b9c2d3')+bar('55%')+'</div>'
t4='<div style="padding:16px"><div style="height:20px;width:70%;background:#1f8a5b;border-radius:10px;margin-bottom:12px"></div>'+bar('92%',14,'#d9dee7',8)+bar('80%',14,'#d9dee7',8)+bar('86%',14,'#d9dee7',8)+bar('60%',14,'#d9dee7',8)+'</div>'
rows=[('LUXURY AGENTS','Premium, polished design',thumb(t1)),('LEAD GENERATION','Fast site with IDX sign-ups',thumb(t2)),('CUSTOM BRANDING','Custom WordPress look',thumb(t3)),('CONTENT AND SEO','Built to rank in search',thumb(t4))]
h='<div class="abs" style="left:50px;top:40px;width:900px;font-size:64px;font-weight:800;color:'+N+';line-height:1.1">Pick a site by your goal</div>'
y=170
for lab,ans,th in rows:
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:190px;background:#fff;border-radius:14px;box-shadow:0 5px 14px rgba(20,35,70,.12);display:flex;align-items:center;gap:30px;padding:0 20px;box-sizing:border-box">%s<div style="flex:1"><div style="font-size:38px;font-weight:800;color:%s;letter-spacing:.05em">%s</div><div style="font-size:44px;font-weight:700;color:%s;line-height:1.15;margin-top:6px">%s</div></div></div>'%(y,th,OR,lab,N,ans)
    y+=212
h+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:44px;font-weight:600;color:%s;line-height:1.3">When you must choose, function wins.</div>'%(y+8,N)
web_goal_m=page(h,'',note='',size=(1000,y+130))
# 2. #1011: luxury vs standard design elements
def card(x,y,w,hh,inner,bg): return '<div class="deco" style="position:absolute;left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:14px;background:%s;box-shadow:0 6px 16px rgba(20,35,70,.18);overflow:hidden">%s</div>'%(x,y,w,hh,bg,inner)
std='<div style="height:34px;background:#e4e8f0;display:flex;gap:6px;padding:8px 12px;box-sizing:border-box">'+''.join('<div style="width:34px;height:18px;background:#b9c2d3;border-radius:5px"></div>' for _ in range(7))+'</div><div style="padding:14px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px">'+''.join('<div style="height:96px;background:#cfd6e2;border-radius:6px"></div>' for _ in range(6))+'</div>'
lux='<div style="position:absolute;inset:0;background:url(ph_living.jpg) center/cover"></div><div style="position:absolute;inset:0;background:linear-gradient(to top,rgba(10,18,40,.85),rgba(10,18,40,.05) 60%)"></div><div style="position:absolute;left:22px;top:18px;width:60px;height:10px;border-radius:5px;background:'+GOLD+'"></div><div style="position:absolute;left:22px;bottom:50px;font-family:Lora,serif;font-size:34px;font-weight:700;color:#fff">Cedar Hills</div><div style="position:absolute;left:22px;bottom:24px;width:120px;height:12px;border-radius:6px;background:'+GOLD+'"></div>'
t='<div class="abs" style="left:50px;top:40px;width:900px;font-size:64px;font-weight:800;color:'+N+';line-height:1.1">What makes a site luxury</div>'
t+=card(50,150,440,290,std,'#fff')+card(510,150,440,290,lux,N)
t+='<div class="abs" style="left:50px;top:456px;width:440px;text-align:center;font-size:56px;font-weight:800;color:#667085">Standard</div><div class="abs" style="left:510px;top:456px;width:440px;text-align:center;font-size:56px;font-weight:800;color:'+GOLD+'">Luxury</div>'
pairs=[('Stock photos','Editorial photography'),('Template layout','Custom design'),('Every listing in a grid','Curated featured listings'),('Default typography','Serif headlines')]
y=550
for a,b in pairs:
    t+='<div class="abs" style="left:50px;top:%dpx;width:440px;height:150px;background:#fff;border:2px solid #d0d7e2;border-radius:12px;display:flex;align-items:center;justify-content:center;text-align:center;padding:0 20px;box-sizing:border-box;font-size:42px;font-weight:600;color:#475467;line-height:1.2">%s</div>'%(y,a)
    t+='<div class="abs" style="left:510px;top:%dpx;width:440px;height:150px;background:%s;border-radius:12px;display:flex;align-items:center;justify-content:center;text-align:center;padding:0 20px;box-sizing:border-box;font-size:42px;font-weight:700;color:#fff;line-height:1.2;box-shadow:0 6px 16px rgba(20,35,70,.18)">%s</div>'%(y,N,b)
    y+=170
t+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:44px;font-weight:600;color:%s;line-height:1.3">Every choice should say premium.</div>'%(y+6,N)
web_luxury_m=page(t,'',note='',size=(1000,y+110))
SC=dict(web_goal_m=web_goal_m,web_luxury_m=web_luxury_m)
if __name__=='__main__': render(sel(sys.argv,SC))
