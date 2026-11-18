import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
# Realtor name ideas (#1979), mobile-first, canvas 1000 wide. Same content as s_name.py, new layout.
N='#1b2a4a'; OR='#e0613a'
NM='Maple Heights Home Co'
def title(t,sub=''):
    s='<div style="font-size:60px;font-weight:800;color:'+N+';line-height:1.12">'+t+'</div>'
    if sub: s+='<div style="font-size:40px;font-weight:600;color:#667085;margin-top:10px">'+sub+'</div>'
    return s
def dot(n,col=OR,sz=56):
    return '<span style="flex:none;width:'+str(sz)+'px;height:'+str(sz)+'px;border-radius:50%;background:'+col+';color:#fff;font-weight:800;font-size:40px;display:flex;align-items:center;justify-content:center">'+str(n)+'</span>'
def wrap(inner): return '<div class="abs" style="left:50px;top:40px;width:900px">'+inner+'</div>'
def mono(sz,r=None):
    return '<div class="deco" style="flex:none;width:'+str(sz)+'px;height:'+str(sz)+'px;border-radius:'+str(sz//2 if r is None else r)+'px;background:'+N+';color:#fff;display:flex;align-items:center;justify-content:center;font-family:Lora,serif;font-weight:700;font-size:'+str(int(sz*.38))+'px">MH</div>'
def nm(sz,col=N): return '<div class="deco serif" style="font-size:'+str(sz)+'px;font-weight:700;color:'+col+';line-height:1.1">Maple Heights<br>Home Co</div>'
def gb(w,h=14,col='#d0d5dd'): return '<div class="deco" style="height:'+str(h)+'px;width:'+str(w)+'px;background:'+col+';border-radius:7px;margin:7px 0"></div>'

# 1. one name used everywhere
yard=('<div style="position:relative;height:100%;background:#eef2f8"><div style="position:absolute;left:62px;top:96px;width:12px;height:110px;background:#8b6f47"></div>'
 '<div style="position:absolute;left:30px;top:26px;right:30px;height:88px;background:#fff;border:6px solid '+N+';border-radius:8px;display:flex;align-items:center;gap:14px;padding:0 16px">'+mono(52)+nm(22)+'</div></div>')
card=('<div style="height:100%;background:#eef2f8;display:flex;align-items:center;justify-content:center"><div style="width:310px;height:177px;background:#fff;border-radius:8px;box-shadow:0 6px 14px rgba(20,35,70,.18);padding:22px;display:flex;gap:16px;align-items:center">'+mono(60)+'<div>'+nm(22)+gb(100,12)+'</div></div></div>')
email=('<div style="height:100%;background:#fff"><div class="deco" style="background:#f2f5fa;padding:14px 22px"><div style="height:12px;width:55%;background:#d0d5dd;border-radius:6px"></div></div>'
 '<div style="display:flex;gap:16px;align-items:center;padding:22px">'+mono(60)+nm(24)+'</div><div style="padding:0 22px">'+gb(330)+gb(240)+'</div></div>')
social=('<div style="height:100%;background:#fff;display:flex;gap:22px;align-items:center;padding:0 30px">'+mono(120)+'<div>'+nm(26)+gb(120,12)+gb(150,12)+'</div></div>')
web=('<div style="height:100%;background:#fff"><div class="deco" style="height:34px;background:#e9edf3;padding:10px 16px"><div style="height:14px;width:55%;background:#fff;border-radius:7px"></div></div>'
 '<div style="display:flex;gap:16px;align-items:center;padding:16px 22px;border-bottom:2px solid #eef0f4">'+mono(52)+nm(22)+'<div style="margin-left:auto;display:flex;gap:10px"><div class="deco" style="width:40px;height:12px;background:#d0d5dd;border-radius:6px"></div><div class="deco" style="width:40px;height:12px;background:#d0d5dd;border-radius:6px"></div></div></div>'
 '<div style="padding:14px 22px">'+gb(300)+gb(200)+'</div></div>')
def tile(inner,label):
    return ('<div><div class="sh" style="height:210px;border-radius:14px;overflow:hidden;background:#fff">'+inner+'</div>'
        +'<div style="font-size:42px;font-weight:700;color:'+N+';text-align:center;margin-top:14px">'+label+'</div></div>')
note=('<div style="background:'+N+';border-radius:14px;height:210px;padding:0 30px;display:flex;align-items:center;font-size:44px;font-weight:800;color:#fff;line-height:1.2">Hard to spell? People type it wrong.</div>')
grid=('<div style="display:grid;grid-template-columns:1fr 1fr;gap:34px 40px;margin-top:38px">'
 +tile(yard,'Yard sign')+tile(card,'Business card')+tile(email,'Email header')+tile(social,'Social profile')+tile(web,'Website header')+note+'</div>')
hero=('<div class="sh" style="background:#fff;border-radius:18px;padding:24px 30px;margin-top:34px;display:flex;gap:26px;align-items:center">'+mono(96)
 +'<div class="serif" style="font-size:54px;font-weight:700;color:'+N+';line-height:1.1">'+NM+'</div></div>')
name_uses_m=page(wrap(title('One name, used everywhere')+hero+grid),'',note='',size=(1000,1250))

# 2. five naming formulas
F=[('Surname + a group word',['Harper Group','Reyes Home Team']),('Place + a home word',['Maple Heights Homes','Lakeview Home Co']),('A value word + a place',['Trusted Key Realty','Clear Path Homes']),('A symbol + a family or place name',['Cedar and Stone Realty','North Door Homes']),('Your name + your promise',['Dana Lee','The Calm Move'])]
f=''
for i,(a,chips) in enumerate(F):
    f+=('<div class="sh" style="background:#fff;border-radius:16px;padding:20px 26px 22px;margin-top:22px"><div style="display:flex;gap:20px;align-items:center">'+dot(i+1)
     +'<div style="font-size:42px;font-weight:800;color:'+N+';line-height:1.15">'+a+'</div></div>'
     +'<div style="display:flex;flex-wrap:wrap;gap:12px;margin:16px 0 0 76px">'+''.join('<span class="serif" style="background:#eef2fb;color:'+N+';border-radius:999px;padding:6px 22px;font-size:38px;font-weight:700">'+c+'</span>' for c in chips)+'</div></div>')
foot='<div style="font-size:42px;font-weight:700;color:'+N+';margin-top:34px;line-height:1.3;text-wrap:balance">Pick the pair that sounds natural.</div>'
name_formulas_m=page(wrap(title('Five ways to build a name')+f+foot),'',note='',size=(1000,1380))

# 3. five-step test
S=[('Say it aloud','Hard to say, hard to refer'),('Spell it by phone','A friend writes it down'),('Search it','Not confused with another field'),('Check the handles','Matching domain and social handles'),('Ask five people','Note which name they remember')]
c=''
for i,(a,b) in enumerate(S):
    c+=('<div class="sh" style="background:#fff;border-radius:16px;padding:20px 26px;margin-top:22px;display:flex;gap:24px;align-items:center">'+dot(i+1,sz=64)
     +'<div><div style="font-size:44px;font-weight:800;color:'+N+';line-height:1.15">'+a+'</div><div style="font-size:38px;color:#475467;margin-top:4px;line-height:1.25">'+b+'</div></div></div>')
last=('<div style="margin-top:34px;background:#fff7e6;border-left:8px solid #e0a21b;border-radius:10px;padding:20px 28px;font-size:42px;line-height:1.3;color:#1d2433"><strong>Then check:</strong> your broker, state records and trademarks.</div>')
name_test_m=page(wrap(title('Test a name in five steps')+c+last),'',note='',size=(1000,1160))
SC=dict(name_uses_m=name_uses_m,name_formulas_m=name_formulas_m,name_test_m=name_test_m)
if __name__=='__main__': render(sel(sys.argv,SC))
