import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
def title(t,sub=None):
    h='<div class="abs" style="left:50px;top:40px;font-size:62px;font-weight:800;color:'+N+';line-height:1.1">'+t+'</div>'
    if sub: h+='<div class="abs" style="left:50px;top:125px;font-size:40px;color:#667085;font-weight:600">'+sub+'</div>'
    return h
# 1. letter anatomy
parts=[('1','Their name','Dear Jordan,','#14808a'),('2','Why you write','A home nearby just sold.','#14808a'),('3','Local proof','Here is what it sold for.','#1b2a4a'),('4','One ask','Want a free home report?','#b42318')]
h=title('Anatomy of one letter','Sample lines, one page')
y=215
for n,a,b,c in parts:
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:210px;background:#fff;border:3px solid #d0d7e2;border-radius:14px"><div style="position:absolute;left:28px;top:60px;width:84px;height:84px;border-radius:42px;background:%s;color:#fff;font-size:52px;font-weight:800;text-align:center;line-height:84px">%s</div><div style="position:absolute;left:150px;top:24px;font-size:42px;font-weight:700;color:%s">%s</div><div style="position:absolute;left:150px;top:100px;width:720px;font-size:50px;font-weight:700;color:#1d2433;line-height:1.2">%s</div></div>'%(y,c,n,c,a,b)
    y+=235
letter_anatomy_m=page(h,'',note='',size=(1000,y+10))
# 2. checks before mailing an expired letter
items=['Listing is truly expired','Not listed with another broker','Your board\'s rules checked','Brokerage name on the letter']
h=title('Before you mail','Expired listing checks')
y=215
for t in items:
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:140px;background:#fff;border:3px solid #d0d7e2;border-radius:14px"><div style="position:absolute;left:28px;top:35px;width:70px;height:70px;border-radius:35px;background:#14808a;color:#fff;font-size:44px;font-weight:800;text-align:center;line-height:70px">&#10003;</div><div style="position:absolute;left:130px;top:40px;width:740px;font-size:44px;font-weight:700;color:#1d2433;line-height:1.1">%s</div></div>'%(y,t)
    y+=165
letter_checks_m=page(h,'',note='',size=(1000,y+20))
# 3. sequence
rows=[('Week 1','Letter','#14808a'),('Week 3','Postcard','#14808a'),('Week 5','Call or visit, if the rules allow','#1b2a4a')]
h=title('A simple touch sequence','Suggested order')
y=215
for a,b,c in rows:
    h+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:210px;background:#fff;border:3px solid #d0d7e2;border-left:14px solid %s;border-radius:14px"><div style="position:absolute;left:34px;top:24px;font-size:44px;font-weight:700;color:#667085">%s</div><div style="position:absolute;left:34px;top:92px;width:820px;font-size:54px;font-weight:800;color:%s;line-height:1.15">%s</div></div>'%(y,c,a,N,b)
    y+=235
letter_seq_m=page(h,'',note='',size=(1000,y+10))
SC=dict(letter_anatomy_m=letter_anatomy_m,letter_checks_m=letter_checks_m,letter_seq_m=letter_seq_m)
if __name__=='__main__': render(sel(sys.argv,SC))
