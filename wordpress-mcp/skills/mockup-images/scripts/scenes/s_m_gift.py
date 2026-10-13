import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
def title(t,sz=64): return '<div class="abs" style="left:50px;top:40px;width:900px;font-size:%dpx;font-weight:800;color:%s;line-height:1.1">%s</div>'%(sz,N,t)
def box(y,html): return '<div class="abs" style="left:50px;top:%dpx;width:900px;background:#fff7e6;border-left:8px solid #e0a21b;border-radius:8px;padding:20px 28px;font-size:42px;color:#1d2433;line-height:1.3">%s</div>'%(y,html)
# 1. generic card vs personal note
gen=('<div class="paper sh" style="left:50px;top:150px;width:900px;height:300px;border-radius:10px"><div style="padding:28px 36px;height:100%;display:flex;flex-direction:column;justify-content:space-between">'
 '<div style="display:flex;justify-content:space-between;align-items:center"><div style="font:800 40px Impact,Liberation Sans;color:#6a1b9a">DANA LEE REALTY</div><div class="deco" style="font-size:24px;color:#6a1b9a;font-weight:700">TOP PRODUCER</div></div>'
 '<div style="font:600 44px Liberation Serif;color:#444;text-align:center">Thank you for your business!</div>'
 '<div style="font:700 38px Liberation Sans;color:#6a1b9a;text-align:center">Call me for all your real estate needs!</div></div></div>')
cg='<div class="abs" style="left:50px;top:480px;width:900px"><div style="font-size:46px;font-weight:800;color:#c2410c">Generic card</div><div style="font-size:38px;color:#475467;margin-top:4px">Logos and a sales line read as advertising</div></div>'
per=('<div class="paper sh" style="left:50px;top:620px;width:900px;height:300px;border-radius:8px;background:#fffdf7;transform:rotate(-1deg)"><div style="padding:30px 42px;font-family:Lora,serif;font-style:italic;font-size:42px;line-height:1.4;color:#2a3550">Maya and Sam,<br>I loved watching you stand on the porch and say, &ldquo;This is the one.&rdquo;'
 '<div class="deco" style="margin-top:18px"><div style="height:14px;width:70%;background:#e4e0d2;border-radius:7px"></div><div style="height:14px;width:45%;background:#e4e0d2;border-radius:7px;margin-top:12px"></div></div></div></div>')
cp='<div class="abs" style="left:50px;top:960px;width:900px"><div style="font-size:46px;font-weight:800;color:#1f8a5b">Personal note</div><div style="font-size:38px;color:#475467;margin-top:4px">One specific moment from the closing</div></div>'
gift_note_m=page(title('Personal beats generic')+gen+cg+per+cp+box(1100,'<strong>Specific beats expensive.</strong> Skip the logos.'),'',note='',size=(1000,1290))
# 2. timeline after closing
T=[('Closing day','Give the gift and a handwritten note','#14808a'),('A week after move-in','Send a note: how did the move go?','#1b2a4a'),('Home anniversary','A card and a short street update','#e0613a')]
t=title('Three touches after closing')
y=210
t+='<div class="abs" style="left:84px;top:%dpx;width:8px;height:%dpx;background:#cbd2e0;border-radius:4px"></div>'%(y+40,2*220)
for i,(a,b,c) in enumerate(T):
    t+='<div class="abs" style="left:50px;top:%dpx;width:76px;height:76px;border-radius:50%%;background:%s;border:8px solid #e4eaf4"></div>'%(y,c)
    t+='<div class="abs" style="left:160px;top:%dpx;width:790px;height:190px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);border-left:10px solid %s"><div style="position:absolute;left:30px;top:24px;right:20px;font-size:46px;font-weight:800;color:%s">%s</div><div style="position:absolute;left:30px;top:96px;right:20px;font-size:40px;color:#1d2433;line-height:1.25">%s</div></div>'%(y-56,c,c,a,b)
    y+=220
y-=20
t+=box(y,'<strong>Put all three dates in your CRM</strong> the day the deal closes.')
y+=190
t+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:40px;color:#475467;line-height:1.3">Order gifts early: delays are common.</div>'%y
gift_timeline_m=page(t,'',note='',size=(1000,y+130))
# 3. gift log as cards
L=[('Maya and Sam','$38','Oct 3 &middot; Tool kit and a note','Sent a referral in January','#116b43'),('Ruth B.','$25','Sep 12 &middot; Restaurant gift card','Hired me again, listing next spring','#116b43'),('Chris and Dana','$45','Aug 28 &middot; Local basket and area guide','Thanked me; no referral yet','#667085')]
g=title('Log every gift and its result')
g+='<div class="paper sh" style="left:50px;top:150px;width:900px;height:%dpx;border-radius:16px"><div style="background:#14808a;color:#fff;height:100px;padding:0 30px;display:flex;align-items:center;font-size:44px;font-weight:800">Closing gift log</div>'%(100+3*250)
for i,(n,cost,gf,resp,col) in enumerate(L):
    g+='<div style="position:absolute;left:0;right:0;top:%dpx;height:250px;border-bottom:%s"><div style="position:absolute;left:30px;top:20px;font-size:44px;font-weight:800;color:%s">%s</div><div style="position:absolute;right:30px;top:12px;font-size:56px;font-weight:800;color:%s">%s</div><div style="position:absolute;left:30px;top:92px;font-size:38px;color:#475467">%s</div><div style="position:absolute;left:30px;top:152px;right:30px;font-size:40px;font-weight:700;color:%s">%s</div></div>'%(100+i*250,'2px solid #e4e7ec' if i<2 else 'none',N,n,N,cost,gf,col,resp)
g+='</div>'
y=150+100+750+40
g+=box(y,'<strong>Keep the cost, date and a description.</strong> After a year, compare results with spend.')
y+=230
gift_log_m=page(g,'',note='',size=(1000,y))
SC=dict(gift_note_m=gift_note_m,gift_timeline_m=gift_timeline_m,gift_log_m=gift_log_m)
if __name__=='__main__': render(sel(sys.argv,SC))
