import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
# integrations
def node(x,y,t,sub,col): return '<div class="abs sh" style="left:%dpx;top:%dpx;width:300px;height:110px;border-radius:14px;background:#fff;border-top:8px solid %s;display:flex;flex-direction:column;justify-content:center;padding:0 22px"><div style="font-size:23px;font-weight:800;color:%s">%s</div><div style="font-size:16px;color:#667085;margin-top:4px">%s</div></div>'%(x,y,col,N,t,sub)
CRM=('<div class="abs sh" style="left:650px;top:300px;width:300px;height:170px;border-radius:16px;background:#1b2a4a;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-size:32px;font-weight:800">CRM</div><div style="font-size:17px;color:#9fb4d6;margin-top:6px">one record for each contact</div></div>')
nodes=node(110,140,'Website forms and landing pages','New leads arrive with a source','#14808a')+node(110,420,'Ad platforms','See which campaign closed','#c2410c')+node(1190,140,'Email tool','List stays current','#7c5cc4')+node(1190,420,'Direct mail tool','Addresses and responses','#e0613a')+node(650,600,'Review tool','New reviews reach your profile','#e0a21b')
lines=leaders([(410,195,650,330),(410,475,650,440),(950,330,1190,195),(950,440,1190,475)])
lines=lines.replace('stroke','stroke')
soft_connect=page(nodes+CRM+lines+'<div class="abs" style="left:110px;top:790px;width:1380px;font-size:22px;color:'+N+';font-weight:600">Pick tools that connect to your CRM, so a lead arrives with its source and unsubscribes stay honored.</div>','Which tools should talk to each other',note='')
# trial
T=[('Write the job','&ldquo;Send a quarterly update to my 300 past clients without copying and pasting.&rdquo;'),('Set a test period','Thirty days is enough for most tools.'),('Use real data','Import a small, real list and run one real task from start to finish.'),('Time the work','Compare how long it took with how long it takes now.'),('Test support','Ask one real question and note how long the answer takes.'),('Test the exit','Export your data before the trial ends.')]
c=''
for i,(a,b) in enumerate(T):
    x=70+(i%3)*500; y=130+(i//3)*270
    c+='<div class="paper sh" style="left:%dpx;top:%dpx;width:470px;height:240px;border-radius:14px"><div class="num" style="left:22px;top:22px;width:42px;height:42px;font-size:21px">%d</div><div style="position:absolute;left:22px;right:22px;top:84px"><div style="font-size:26px;font-weight:800;color:%s">%s</div><div style="font-size:20px;color:#475467;margin-top:8px;line-height:1.4">%s</div></div></div>'%(x,y,i+1,N,a,b)
soft_trial=page(c+'<div class="abs" style="left:70px;top:690px;width:1460px;background:#fff7e6;border-left:6px solid #e0a21b;border-radius:8px;padding:16px 24px;font-size:22px;color:#1d2433"><strong>Put a reminder on your calendar the day before the trial ends.</strong> If the tool did not save time or improve a result you care about, cancel.</div>','How to trial a tool before you commit',note='')
# sprawl vs small stack
def sub(x,items,col,bg):
    return ''.join('<div class="paper sh" style="left:%dpx;top:%dpx;width:%dpx;height:56px;border-radius:8px;background:%s;display:flex;align-items:center;justify-content:space-between;padding:0 18px;font-size:18px;color:#1d2433"><span>%s</span><span style="font-weight:800;color:%s">%s</span></div>'%(x,150+i*68,420,bg,n,col,p) for i,(n,p) in enumerate(items))
sprawl=[('Contact manager A','$40'),('Contact manager B (trial forgotten)','$35'),('Email tool','$30'),('Second email tool','$25'),('Social scheduler','$20'),('Design tool','$15'),('Lead platform','$99'),('Mail automation','$60')]
small=[('Simple CRM','$40'),('Free email tier','$0'),('Free scheduler','$0'),('Design tool','$15')]
tot1=sum(int(p[1:]) for _,p in sprawl); tot2=sum(int(p[1:]) for _,p in small)
soft_sprawl=page(sub(110,sprawl,'#b42318','#fff7f6')+sub(850,small,'#116b43','#f4fbf7')+'<div class="abs" style="left:110px;top:716px;width:420px;font-size:24px;font-weight:800;color:#b42318">Tool sprawl: $%d a month<br><span style="font-size:17px;font-weight:500;color:#667085">Overlapping jobs, forgotten trials</span></div><div class="abs" style="left:850px;top:424px;width:420px;font-size:24px;font-weight:800;color:#116b43">Small stack: $%d a month<br><span style="font-size:17px;font-weight:500;color:#667085">One tool per job, free tiers first</span></div><div class="abs" style="left:620px;top:360px;width:110px;height:110px;border-radius:50%%;background:%s;color:#fff;font-weight:800;font-size:34px;display:flex;align-items:center;justify-content:center">VS</div>'%(tot1,tot2,N),'Tool sprawl vs a small stack',note='Sample subscriptions and prices. Made up.')
SC=dict(soft_connect=soft_connect,soft_trial=soft_trial,soft_sprawl=soft_sprawl)
if __name__=='__main__': render(sel(sys.argv,SC))
