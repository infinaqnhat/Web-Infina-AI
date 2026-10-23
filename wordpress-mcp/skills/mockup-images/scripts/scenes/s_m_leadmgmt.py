import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'; TEAL='#14808a'; OR='#e0613a'
def title(t,top=40,size=60):
    return '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:%dpx;font-weight:800;color:%s;line-height:1.12">%s</div>'%(top,size,N,t)
def dot(n,x,y,d=64,fs=42,col=OR):
    return '<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:50%%;background:%s;color:#fff;font-size:%dpx;font-weight:800;display:flex;align-items:center;justify-content:center">%d</div>'%(x,y,d,d,col,fs,n)
STEPS=[('Capture','Every source, one record',TEAL),('Assign','One owner and a reply deadline',TEAL),('Qualify','Timeline, need, other agent',N),('Nurture','Follow-up by segment',N),('Measure','Source, stage, closings',OR)]
c=title('Five jobs of lead management')
y=170
for i,(a,b,col) in enumerate(STEPS):
    c+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:190px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12)"></div>'%y
    c+=dot(i+1,76,y+63,64,42,col)
    c+='<div class="abs" style="left:170px;top:%dpx;width:760px;font-size:50px;font-weight:800;color:%s;line-height:1.1">%s</div>'%(y+32,col,a)
    c+='<div class="abs" style="left:170px;top:%dpx;width:760px;font-size:40px;font-weight:600;color:#475467;line-height:1.2">%s</div>'%(y+104,b)
    y+=210
leadmgmt_loop_m=page(c,'',note='',size=(1000,y+20))
R=[('Round robin','Even split. Ignores skill.',TEAL),('Weighted','More leads to chosen agents.',TEAL),('By area','Territory or ZIP code.',N),('By skill','Match the specialty.',N),('Lead pond','Agents claim on demand.',OR)]
c=title('Ways to route a lead')
y=160
for a,b,col in R:
    c+=('<div class="abs" style="left:50px;top:%dpx;width:900px;height:190px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
        '<div style="width:22px;height:190px;background:%s;position:absolute;left:0;top:0"></div>'
        '<div style="padding:26px 28px 0 52px"><div style="font-size:50px;font-weight:800;color:%s;line-height:1.1">%s</div>'
        '<div style="font-size:42px;font-weight:600;color:#475467;margin-top:14px;line-height:1.2">%s</div></div></div>')%(y,col,N,a,b)
    y+=210
leadmgmt_routing_m=page(c,'',note='',size=(1000,y+20))
SC=dict(leadmgmt_loop_m=leadmgmt_loop_m,leadmgmt_routing_m=leadmgmt_routing_m)
if __name__=='__main__': render(sel(sys.argv,SC))
