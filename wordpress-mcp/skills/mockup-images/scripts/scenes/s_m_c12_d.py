import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
from s_m_leadgen import hero,title,dot,N,TEAL,OR
CARD='<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
def head(col,t,h=84,fs=46):
    return '<div style="height:%dpx;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:%dpx;font-weight:800;line-height:1.05">%s</div>'%(h,col,fs,t)
def sample(y,t='Sample numbers. Made up for illustration.'):
    return '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:36px;font-weight:600;color:#667085">%s</div>'%(y,t)

# ---------- bai 7: real estate sales funnel
sf_hero_m=hero('ph_living','Real estate<br>sales funnel','Five stages, one number each')

ST=[('New lead','Name and contact saved',N),('Contacted','A real two-way reply',N),('Appointment','Meeting or tour booked',TEAL),('Agreement','Contract signed',TEAL),('Past client','Closed, still in touch',OR)]
c=title('Five stages, one event each',size=60)
y=170; ws=[900,840,780,720,660]
for i,(a,b_,col) in enumerate(ST):
    w=ws[i]; x=50+(900-w)//2
    c+=('<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:150px;background:%s;border-radius:16px;color:#fff">'
        '<div style="position:absolute;left:22px;top:41px;width:68px;height:68px;border-radius:50%%;background:#fff;color:%s;font-size:44px;font-weight:800;display:flex;align-items:center;justify-content:center">%d</div>'
        '<div style="position:absolute;left:112px;top:20px;width:%dpx;font-size:46px;font-weight:800;line-height:1.1">%s</div>'
        '<div style="position:absolute;left:112px;top:82px;width:%dpx;font-size:38px;font-weight:600;line-height:1.15;color:#e8eefc">%s</div></div>')%(x,y,w,col,col,i+1,w-130,a,w-130,b_)
    y+=170
sf_stages_m=page(c,'',note='',size=(1000,y+20))

ROWS=[('New leads',100,N,''),('Contacted',60,N,'60% reached'),('Appointments',18,TEAL,'30% of contacted'),('Agreements',6,TEAL,'33% of appointments'),('Closed',5,OR,'')]
c=title('Sample month: where leads drop',size=58)
y=240
for a,n,col,note_ in ROWS:
    c+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:44px;font-weight:800;color:%s;line-height:1.1">%s</div>'%(y,N,a)
    bw=max(8,int(n/100*620))
    c+='<div class="abs" style="left:50px;top:%dpx;width:%dpx;height:64px;background:%s;border-radius:10px"></div>'%(y+58,bw,col)
    c+='<div class="abs" style="left:%dpx;top:%dpx;font-size:50px;font-weight:800;color:%s;line-height:64px">%d</div>'%(50+bw+22,y+58,N,n)
    if note_: c+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:38px;font-weight:600;color:#475467">%s</div>'%(y+130,note_)
    y+=200 if note_ else 150
c+='<div class="abs" style="left:50px;top:%dpx;width:900px;padding:22px 26px;background:#fff3ee;border-left:12px solid %s;border-radius:12px;font-size:42px;font-weight:700;color:%s;line-height:1.2">Biggest loss: 40 leads never reached</div>'%(y+10,OR,N)
c+=sample(y+170)
sf_sample_m=page(c,'',note='',size=(1000,y+240))

M=[('Contact rate','reached ÷ new leads',N),('Appointment rate','appointments ÷ contacted',TEAL),('Agreement rate','agreements ÷ appointments',TEAL),('Repeat and referral rate','came back or referred ÷ past clients, once a year',OR)]
c=title('One number per stage',size=62)
y=180
for a,f,col in M:
    h=210 if len(f)>30 else 190
    c+=(CARD%(y,h))+'<div style="width:20px;height:%dpx;background:%s;position:absolute;left:0;top:0"></div>'%(h,col)
    c+='<div style="padding:22px 28px 0 52px"><div style="font-size:50px;font-weight:800;color:%s;line-height:1.1">%s</div><div style="font-size:40px;font-weight:600;color:#475467;margin-top:14px;line-height:1.2">%s</div></div></div>'%(N,a,f)
    y+=h+22
sf_metrics_m=page(c,'',note='',size=(1000,y+10))

# ---------- bai 8: ai lead nurture
ain_hero_m=hero('ph_kitchen','AI lead<br>nurture','What it can and cannot do')

def two_cards(ttl,groups):
    c=title(ttl,size=60); y=180
    for col,name,items in groups:
        h=84+len(items)*74+36
        c+=(CARD%(y,h))+head(col,name)+'<div style="padding:16px 28px">'
        for it in items: c+='<div style="font-size:42px;font-weight:700;color:#1d2433;line-height:74px">%s</div>'%it
        c+='</div></div>'; y+=h+26
    return c,y
c,y=two_cards('Who does what',[(TEAL,'The chatbot handles',['Fast first reply','Light questions','Check-ins and reminders','Saving every answer']),(N,'You handle',['Price and offers','Showings and tours','Upset or confused clients','Negotiation'])])
ain_split_m=page(c,'',note='',size=(1000,y))

H=['Lead asks about price, offer or showing','Lead names another agent','Lead is upset or wants a person','Lead gives a firm timeline','Bot is unsure what was meant']
c=title('Hand off to a person when:',size=60,top=40)
y=200
for i,s in enumerate(H):
    c+='<div class="abs" style="left:50px;top:%dpx;width:900px;height:150px;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12)"></div>'%y
    c+=dot(i+1,80,y+43,64,42,OR if i<4 else TEAL)
    c+='<div class="abs" style="left:176px;top:%dpx;width:760px;height:150px;font-size:42px;font-weight:700;color:#1d2433;line-height:1.15;display:flex;align-items:center">%s</div>'%(y,s)
    y+=170
ain_handoff_m=page(c,'',note='',size=(1000,y+20))

def bub(y,who,t,h):
    if who=='bot':
        return '<div class="abs" style="left:50px;top:%dpx;width:720px;height:%dpx;background:%s;color:#fff;border-radius:26px 26px 26px 6px;padding:22px 28px;font-size:40px;font-weight:600;line-height:1.25">%s</div>'%(y,h,TEAL,t)
    return '<div class="abs" style="left:230px;top:%dpx;width:720px;height:%dpx;background:#e4e8f0;color:#1d2433;border-radius:26px 26px 6px 26px;padding:22px 28px;font-size:40px;font-weight:600;line-height:1.25">%s</div>'%(y,h,t)
c=title('Sample check-in with a quiet lead',size=54)
y=190
for who,t,h in [('bot','Hi Maria, this is the assistant for the agent you spoke with in May. Still thinking about a move this year?',250),
                ('lead','Maybe in the spring. What are prices like on my street now?',190),
                ('bot','I can send recent sales. Want a quick market note from your agent?',190),
                ('lead','Yes please',110)]:
    c+=bub(y,who,t,h); y+=h+24
c+='<div class="abs" style="left:50px;top:%dpx;width:900px;padding:22px 26px;background:#fff3ee;border-left:12px solid %s;border-radius:12px;font-size:40px;font-weight:700;color:%s;line-height:1.2">Handoff: agent notified to send the market note</div>'%(y+6,OR,N)
c+=sample(y+170,'Sample conversation. Names and messages are made up.')
ain_chat_m=page(c,'',note='',size=(1000,y+245))

SC=dict(sf_hero_m=sf_hero_m,sf_stages_m=sf_stages_m,sf_sample_m=sf_sample_m,sf_metrics_m=sf_metrics_m,ain_hero_m=ain_hero_m,ain_split_m=ain_split_m,ain_handoff_m=ain_handoff_m,ain_chat_m=ain_chat_m)
if __name__=='__main__': render(sel(sys.argv,SC))
