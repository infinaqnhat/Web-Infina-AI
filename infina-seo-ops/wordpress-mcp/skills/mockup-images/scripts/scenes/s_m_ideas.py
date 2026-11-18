import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'; TEAL='#14808a'; OR='#e0613a'
def title(t,top=40,size=64):
    return '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:%dpx;font-weight:800;color:%s;line-height:1.12">%s</div>'%(top,size,N,t)
def bar(x,y,w,h=18,col='#e4e7ec'):
    return '<div class="deco" style="position:absolute;left:%dpx;top:%dpx;width:%dpx;height:%dpx;background:%s;border-radius:%dpx"></div>'%(x,y,w,h,col,h//2)
# 1. quick wins matrix: counts per cell, then the six in the green box
ideas=[('Quarterly market update note','Low','Low'),('Home anniversary note','Low','Low'),('Ask for introductions by name','Low','Low'),('Weekly question-and-answer post','Low','Low'),('Google Business Profile updates','Low','Low'),('Ask for Google reviews at closing','Low','Low'),('Neighborhood spotlight post','Low','Medium'),('Just-sold postcard to nearby homes','Medium','Low'),('Open house invite to neighbors','Low','Medium'),('Listing presentation packet','Low','Medium')]
cnt={}
for n,c,e in ideas: cnt[(c,e)]=cnt.get((c,e),0)+1
LX=50; LW=250; CW=325; GAP=0
g=title('Start with the six quick wins',size=62)
y0=170
for i,e in enumerate(['Low effort','Medium effort']):
    g+='<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;text-align:center;font-size:40px;font-weight:800;color:%s">%s</div>'%(LX+LW+i*(CW+0),y0,CW,N,e)
y=y0+70
for ci,c in enumerate(['Low','Medium']):
    g+='<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:180px;display:flex;align-items:center;font-size:40px;font-weight:800;color:%s">%s cost</div>'%(LX,y,LW,N,c)
    for ei,e in enumerate(['Low','Medium']):
        n=cnt.get((c,e),0); green=(c,e)==('Low','Low')
        bg='#1f8a5b' if green else '#fff'; fg='#fff' if green else '#475467'
        g+='<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:180px;background:%s;border-radius:16px;box-shadow:0 4px 12px rgba(20,35,70,.12);display:flex;flex-direction:column;align-items:center;justify-content:center;border:%s"><div style="font-size:72px;font-weight:800;color:%s;line-height:1">%d</div><div style="font-size:38px;font-weight:700;color:%s;margin-top:6px">%s</div></div>'%(LX+LW+ei*CW+(8 if ei else 0),y,CW-8,bg,'0' if green else '2px solid #e1e6ef',fg,n,fg,'idea' if n==1 else 'ideas')
    y+=196
y+=20
LIST=[i[0] for i in ideas if (i[1],i[2])==('Low','Low')]
h=100+len(LIST)*74+20
g+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:#e6f6ee;border:4px solid #1f8a5b;border-radius:16px"><div style="position:absolute;left:30px;top:22px;font-size:42px;font-weight:800;color:#116b43">Low cost, low effort</div>'%(y,h)
for i,t in enumerate(LIST):
    g+='<div style="position:absolute;left:30px;top:%dpx;display:flex;gap:16px;align-items:center;font-size:42px;font-weight:600;color:#1d2433;white-space:nowrap"><span style="width:22px;height:22px;border-radius:50%%;background:%s;flex:none"></span>%s</div>'%(100+i*74,OR,t)
g+='</div>'
ideas_matrix_m=page(g,'',note='',size=(1000,y+h+50))
# 2. two sphere notes
t=title('Two sphere notes,<br>short and personal',size=62)
t+='<div class="abs" style="left:50px;top:210px;font-size:44px;font-weight:800;color:'+OR+'">Home anniversary note</div>'
t+=('<div class="abs sh" style="left:50px;top:285px;width:900px;height:360px;background:#fffdf7;border-radius:8px;transform:rotate(-1deg)"><div class="serif" style="position:absolute;left:44px;top:38px;right:44px;font-style:italic;font-size:46px;line-height:1.35;color:#2a3550">Happy one year in the house on Cedar Lane, Maya!</div>'
    +bar(44,205,700)+bar(44,243,540)+'<div class="serif" style="position:absolute;left:44px;top:282px;font-style:italic;font-size:44px;color:#2a3550">Dana</div></div>')
t+='<div class="abs" style="left:50px;top:720px;font-size:44px;font-weight:800;color:'+OR+'">Quarterly market update</div>'
t+=('<div class="abs sh" style="left:50px;top:795px;width:900px;background:#fff;border-radius:16px;overflow:hidden"><div style="background:'+N+';color:#fff;padding:22px 30px;font-size:44px;font-weight:700;font-family:Lora,serif">Cedar Hills, this quarter</div>'
    '<div style="padding:26px 30px 26px"><div style="display:flex;align-items:baseline;gap:18px"><span style="font-size:72px;font-weight:800;color:'+TEAL+';line-height:1">21 days</span><span style="font-size:42px;font-weight:600;color:#1d2433">to sell, on average</span></div>'
    '<div style="font-size:42px;font-weight:600;color:#1d2433;margin-top:16px">Two sold above the asking price.</div>'
    '<div class="deco" style="position:relative;height:60px;margin-top:6px">'+bar(0,16,820)+bar(0,44,560)+'</div>'
    '<div style="font-size:38px;color:#667085;margin-top:6px">Dana Lee &middot; Cedar Hills Realty &middot; 555-0142</div></div></div>')
ideas_notes_m=page(t,'',note='',size=(1000,1290))
SC=dict(ideas_matrix_m=ideas_matrix_m,ideas_notes_m=ideas_notes_m)
if __name__=='__main__': render(sel(sys.argv,SC))
