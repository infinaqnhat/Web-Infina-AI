import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'; OR='#e0613a'; TL='#14808a'
def dot(n,x=None,y=None,s=56):
    pos='' if x is None else 'position:absolute;left:%dpx;top:%dpx;'%(x,y)
    return '<div style="%swidth:%dpx;height:%dpx;border-radius:50%%;background:%s;color:#fff;display:flex;align-items:center;justify-content:center;font-size:40px;font-weight:800;flex:none;box-shadow:0 3px 8px rgba(0,0,0,.25)">%d</div>'%(pos,s,s,OR,n)
def card(x,y,w,inner,bg='#fff'):
    return '<div class="paper sh" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:10px;background:%s">%s</div>'%(x,y,w,int(w/1.75),bg,inner)
def av(s,bg='#9fb4d6',fg=N): return '<div class="deco" style="width:%dpx;height:%dpx;border-radius:50%%;background:%s;color:%s;font-weight:800;font-size:%dpx;display:flex;align-items:center;justify-content:center;flex:none">DL</div>'%(s,s,bg,fg,s//3)
def bar(w,h=12,c='#d9dfea',m=8): return '<div style="width:%dpx;height:%dpx;background:%s;border-radius:6px;margin-top:%dpx"></div>'%(w,h,c,m)
def title(t,top=40): return '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:64px;font-weight:800;color:%s;line-height:1.1">%s</div>'%(top,N,t)
def side(x,y,h,n,label,sub,w=420):
    return '<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;display:flex;gap:18px;align-items:center">%s<div><div style="font-size:42px;font-weight:800;color:%s;line-height:1.15">%s</div><div style="font-size:38px;font-weight:500;color:#475467;line-height:1.2;margin-top:6px">%s</div></div></div>'%(x,y,w,h,dot(n) if n else '',N,label,sub)
def row(n,text,y):
    return dot(n,50,y)+'<div class="abs" style="left:132px;top:%dpx;width:820px;height:56px;display:flex;align-items:center;font-size:42px;font-weight:700;color:%s">%s</div>'%(y,N,text)
# 1. four layouts
l1=card(50,160,440,'<div style="padding:26px;display:flex;gap:20px;align-items:center;height:100%">'+av(96)+'<div><div class="serif deco" style="font-size:30px;font-weight:700;color:'+N+'">Dana Lee</div>'+bar(90,10,'#8fd0d4',6)+bar(150,12,'#d9dfea',12)+bar(130,12)+bar(110,12)+'</div></div>')
l2=card(50,440,440,'<div style="padding:30px 32px;display:flex;flex-direction:column;justify-content:center;height:100%;border-left:10px solid '+N+'"><div class="serif deco" style="font-size:32px;font-weight:700;color:'+N+'">Marcus Bell</div>'+bar(160,10,'#b7c0d1',8)+bar(220,12,'#d9dfea',20)+bar(170,12)+'</div>')
l3=card(50,720,440,'<div class="photo" style="height:100%;background-image:url(ph_aerial.jpg);position:relative"><div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(14,28,56,.85),rgba(14,28,56,.1))"></div><div style="position:absolute;left:28px;top:36px"><div class="serif deco" style="font-size:32px;font-weight:700;color:#fff">Priya Shah</div>'+bar(150,10,'#cfdcf7',10)+bar(110,10,'#cfdcf7',8)+'</div></div>')
l4=card(50,1000,440,'<div style="padding:24px 28px;display:flex;gap:20px;align-items:center;height:100%;background:#fff7f1;border-top:8px solid '+OR+'">'+av(88,'#f6c7b2','#7c2d12')+'<div><div class="serif deco" style="font-size:28px;font-weight:700;color:'+N+'">Linda Park</div>'+bar(140,12,'#e6cdbf',12)+bar(110,12,'#e6cdbf')+'</div></div>')
t=title('Four card layouts to copy')
t+=l1+l2+l3+l4
for i,(lb,sb) in enumerate([('Headshot and details','Back: QR code'),('Clean text card','Back: brokerage logo'),('Local photo card','Back: contact and QR'),('Referral card','Back: referral line')]):
    t+=side(530,160+i*280,251,i+1,lb,sb)
t+='<div class="abs" style="left:50px;top:1300px;width:900px;font-size:44px;font-weight:600;color:%s">The front says who you are.</div>'%N
card_layouts_m=page(t,'',note='',size=(1000,1400))
# 2. front and back
front=card(50,160,480,'<div style="padding:26px;display:flex;gap:22px;align-items:center;height:100%">'+av(100)+'<div><div class="serif deco" style="font-size:32px;font-weight:700;color:'+N+'">Dana Lee</div>'+bar(150,10,'#8fd0d4',6)+bar(150,12,'#d9dfea',14)+bar(130,12)+bar(120,12)+'</div></div>')
back1=card(50,470,480,'<div style="padding:26px;display:flex;gap:22px;align-items:center;height:100%;background:'+N+'"><div style="background:#fff;padding:8px;border-radius:6px">'+qr2(120)+'</div><div style="flex:1">'+bar(150,16,'#cfdcf7',0)+bar(120,16,'#cfdcf7',10)+bar(90,12,'#7f93b8',16)+'</div></div>')
back2=card(50,780,480,'<div style="padding:26px;display:flex;align-items:center;height:100%;background:#fff7f1;border-top:8px solid '+OR+'"><div style="width:100%"><div class="serif deco" style="font-size:34px;font-weight:700;color:'+N+';line-height:1.2">Know someone moving?</div>'+bar(250,14,'#e6cdbf',14)+bar(200,14,'#e6cdbf',8)+'</div></div>')
t=title('Simple front, useful back')
t+=front+back1+back2
for i,(lb,sb) in enumerate([('Front','Name, one line, phone, email'),('Back: QR code','Opens a page for card holders'),('Back: referral line','Optional, easy to pass on')]):
    t+=side(570,160+i*310,274,None,lb,sb,w=380)
t+='<div class="abs" style="left:50px;top:1120px;width:900px;font-size:44px;font-weight:600;color:%s">Use the back for one action.</div>'%N
card_back_m=page(t,'',note='',size=(1000,1220))
# 3. proof
def line(txt,sz,y,c='#1d2433',w=700): return '<div class="abs deco" style="left:96px;top:%dpx;font-size:%dpx;color:%s;font-weight:600;white-space:nowrap;width:%dpx">%s</div>'%(y,sz,c,w,txt)
big='<div class="paper sh" style="left:50px;top:160px;width:900px;height:514px;border-radius:14px">'
big+='<div class="abs deco serif" style="left:96px;top:44px;font-size:62px;font-weight:700;color:'+N+'">Dana Lee</div>'
big+=line('555-0142',38,140)+line('dana@example.com',38,215)+line('Cedar Hills Realty',38,290)
big+='<div class="abs deco" style="left:96px;top:440px;font-size:28px;color:#667085">License number, if your state requires it</div>'
big+='<div class="abs" style="right:44px;top:200px;background:#fff;border:2px solid #e4e7ec;padding:10px">'+qr2(190)+'</div></div>'
pins=dot(1,78,216)+dot(2,78,295)+dot(3,78,370)+dot(5,78,445)+dot(4,670,334)
t=title('Proof it before you print')+big+pins
y=730
for i,s in enumerate(['Name matches your license','Phone: call it','Email: send yourself a test','QR code: scan on two phones','Brokerage and license line']):
    t+=row(i+1,s,y+i*104)
card_proof_m=page(t,'',note='',size=(1000,y+5*104+40))
SC=dict(card_layouts_m=card_layouts_m,card_back_m=card_back_m,card_proof_m=card_proof_m)
if __name__=='__main__': render(sel(sys.argv,SC))
