import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'; T='#14808a'; O='#e0613a'; G='#1f8a5b'
def title(txt,h=1):
    return '<div class="abs" style="left:50px;top:40px;width:900px;font-size:64px;font-weight:800;color:'+N+';line-height:1.12">'+txt+'</div>'
def card(y,h,inner,border=None,bg='#fff'):
    b='border-left:12px solid '+border+';' if border else ''
    return '<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:%s;border-radius:14px;box-shadow:0 6px 16px rgba(20,35,70,.12);%soverflow:hidden">%s</div>'%(y,h,bg,b,inner)
def tri(x,y,col):
    return '<div class="abs" style="left:%dpx;top:%dpx;width:0;height:0;border-left:44px solid transparent;border-right:44px solid transparent;border-top:44px solid %s"></div>'%(x,y,col)
def bar(w,h=16,col='#e4e7ec',extra=''):
    return '<div class="deco" style="width:%s;height:%dpx;background:%s;border-radius:8px;%s"></div>'%(w,h,col,extra)

# 1. #610: pick an IDX website by goal (replaces the platform comparison table)
goals=[('Best all-in-one','Real Geeks','IDX search, lead capture, CRM',T),
       ('Best for local SEO','AgentFire','Neighborhood pages, live MLS stats','#1d4e89'),
       ('Best for SEO listing pages','Showcase IDX','Google-indexed pages, not iFrames',O),
       ('Best for high lead volume','Sierra Interactive','Predictive CRM, very fast search',N)]
h=title('Pick your IDX site by goal')
y=145
for g,name,sub,col in goals:
    inner=('<div style="position:absolute;left:34px;top:16px;font-size:42px;font-weight:800;color:'+col+'">'+g+'</div>'
           '<div style="position:absolute;left:34px;top:70px;font-size:48px;font-weight:800;color:'+N+'">'+name+'</div>'
           '<div style="position:absolute;left:34px;top:134px;font-size:38px;font-weight:500;color:#475467">'+sub+'</div>')
    h+=card(y,196,inner,border=col)
    y+=222
h+='<div class="abs" style="left:50px;top:%dpx;width:900px;background:#e6f2f1;border-radius:14px;padding:22px 30px;font-size:42px;font-weight:700;color:%s;line-height:1.25">Already have a website? A standalone IDX plugin also works.</div>'%(y+4,N)
y+=4+170
idx_pick_m=page(h,'',note='',size=(1000,y+40))

# 2. #610: test before you commit (replaces the evaluation graphic)
steps=['Search your MLS zip codes on a phone','Time the page load and listing cards',"Check your MLS board's approved vendors",'Set the registration prompt to save or alert','Send a dummy lead to the CRM']
h=title('Test before you commit')
y=160
for i,s in enumerate(steps):
    inner=('<div style="position:absolute;left:28px;top:30px;width:76px;height:76px;border-radius:50%;background:'+O+';color:#fff;font-size:48px;font-weight:800;display:flex;align-items:center;justify-content:center">'+str(i+1)+'</div>'
           '<div style="position:absolute;left:132px;top:0;width:740px;height:136px;display:flex;align-items:center;font-size:44px;font-weight:700;color:'+N+';line-height:1.2">'+s+'</div>')
    h+=card(y,136,inner)
    y+=160
idx_test_m=page(h,'',note='',size=(1000,y+30))

# 3. #616: three IDX sites, three strengths (wireframes carry no text and no ratings)
def frame(inner):
    return ('<div class="abs deco" style="left:30px;top:30px;width:300px;height:240px;background:#fff;border:3px solid #cdd5e3;border-radius:12px;overflow:hidden">'
            '<div style="height:30px;background:#e9edf3;display:flex;align-items:center;gap:6px;padding:0 10px"><i style="width:10px;height:10px;border-radius:50%;background:#f87171"></i><i style="width:10px;height:10px;border-radius:50%;background:#fbbf24"></i><i style="width:10px;height:10px;border-radius:50%;background:#34d399"></i></div>'
            '<div style="position:relative;height:207px">'+inner+'</div></div>')
def pin(x,y,col=O):
    return '<div class="abs" style="left:%dpx;top:%dpx;width:22px;height:22px;border-radius:50%%;background:%s;border:4px solid #fff"></div>'%(x,y,col)
w1=frame('<div class="abs" style="left:12px;top:10px;width:276px;height:34px;background:#eef1f6;border:2px solid #cdd5e3;border-radius:17px"></div>'
         '<div class="abs" style="left:12px;top:56px;width:170px;height:138px;background:#d9ece8;border-radius:8px"></div>'+pin(40,80)+pin(100,125)+pin(135,75,T)+
         '<div class="abs" style="left:192px;top:56px;width:96px;height:40px;background:#eef1f6;border-radius:6px"></div><div class="abs" style="left:192px;top:104px;width:96px;height:40px;background:#eef1f6;border-radius:6px"></div><div class="abs" style="left:192px;top:152px;width:96px;height:40px;background:#eef1f6;border-radius:6px"></div>')
w2=frame(photo('ph_house',0,0,294,110,0)+'<div class="abs" style="left:14px;top:40px;width:130px;height:16px;background:rgba(255,255,255,.9);border-radius:8px"></div>'
         +photo('ph_condo',12,122,86,74,6)+photo('ph_living',104,122,86,74,6)+photo('ph_aerial',196,122,86,74,6))
rows=''
for k,c in enumerate([O,'#e0a21b','#c9d1de','#c9d1de']):
    rows+='<div class="abs" style="left:12px;top:%dpx;width:270px;height:38px;background:%s;border-radius:8px"></div><div class="abs" style="left:24px;top:%dpx;width:18px;height:18px;border-radius:50%%;background:%s"></div><div class="abs" style="left:56px;top:%dpx;width:150px;height:12px;background:rgba(255,255,255,.85);border-radius:6px"></div>'%(14+k*46,'#fff1e8' if k==0 else '#eef1f6',24+k*46,c,27+k*46)
w3=frame(rows)
st=[('Fast search and lead capture','Real Geeks',w1),('Design and neighborhood pages','AgentFire',w2),('Built for high-volume teams','Sierra Interactive',w3)]
h=title('Three sites, three strengths')
y=150
for s,name,w in st:
    inner=w+('<div style="position:absolute;left:372px;top:30px;width:500px;font-size:44px;font-weight:800;color:'+N+';line-height:1.2">'+s+'</div>'
             '<div style="position:absolute;left:372px;top:196px;font-size:40px;font-weight:700;color:'+T+'">'+name+'</div>')
    h+=card(y,300,inner)
    y+=326
idx_strengths_m=page(h,'',note='',size=(1000,y+10))

# 4. #616: when to ask for registration (replaces the conversion chart)
h=title('When to ask for registration')
h+=card(170,170,'<div style="padding:22px 34px"><div style="font-size:46px;font-weight:800;color:'+G+'">Visitor browses listings</div><div style="font-size:40px;color:#475467;margin-top:8px">No sign-up needed yet</div></div>',border=G)
h+=tri(456,356,'#b9c2d3')
chips=''.join('<div style="display:flex;align-items:center;gap:16px;font-size:44px;font-weight:700;color:'+N+'"><i style="flex:none;width:26px;height:26px;border-radius:50%;background:'+O+'"></i>'+c+'</div>' for c in ['Saves a listing','Requests a showing','Sets a price drop alert'])
h+=card(420,330,'<div style="padding:22px 34px"><div style="font-size:42px;font-weight:800;color:'+O+';margin-bottom:16px">High-intent moments</div><div style="display:flex;flex-direction:column;gap:18px">'+chips+'</div></div>',border=O)
h+=tri(456,766,'#b9c2d3')
h+=card(830,170,'<div style="padding:22px 34px"><div style="font-size:46px;font-weight:800;color:#fff">Registration prompt appears</div><div style="font-size:40px;color:#d6eeee;margin-top:8px">A motivated lead signs up</div></div>',bg=T)
h+=card(1040,150,'<div style="padding:20px 34px;display:flex;align-items:center;gap:22px;height:100%"><div style="flex:none;width:64px;height:64px;border-radius:50%;background:#c2410c;color:#fff;font-size:44px;font-weight:800;display:flex;align-items:center;justify-content:center">&#10005;</div><div style="font-size:42px;font-weight:700;color:#7a271a;line-height:1.2">Not on arrival, before any results</div></div>',bg='#fdecea')
idx_prompt_m=page(h,'',note='',size=(1000,1240))

SC=dict(idx_pick_m=idx_pick_m,idx_test_m=idx_test_m,idx_strengths_m=idx_strengths_m,idx_prompt_m=idx_prompt_m)
if __name__=='__main__': render(sel(sys.argv,SC))
