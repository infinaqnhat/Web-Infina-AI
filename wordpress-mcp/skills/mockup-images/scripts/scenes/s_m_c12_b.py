import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
from s_m_leadgen import hero,title,dot,N,TEAL,OR
CARD='<div class="abs" style="left:50px;top:%dpx;width:900px;height:%dpx;background:#fff;border-radius:16px;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
def head(col,t,h=80,fs=48):
    return '<div style="height:%dpx;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:%dpx;font-weight:800;line-height:1.05">%s</div>'%(h,col,fs,t)
def sub(t,top=140):
    return '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:40px;font-weight:600;color:#667085">%s</div>'%(top,t)
# ---- bai 3 client database
cdb_hero_m=hero('ph_living','Real estate<br>client database','Tier it. Clean it.')
T=[('A','Recent clients and referrers','12 touches a year',TEAL),
   ('B','Past clients who know your work','4 touches a year',N),
   ('C','Old leads and distant contacts','2 touches a year',OR)]
c=title('Three tiers of care',size=64)+sub('Sample plan. Adjust the numbers to your time.')
y=225
for t_,who,n_,col in T:
    c+=(CARD%(y,262))+head(col,'Tier '+t_)+'<div style="padding:20px 28px"><div style="font-size:44px;font-weight:700;color:#1d2433;line-height:1.2">%s</div><div style="font-size:42px;font-weight:800;color:%s;margin-top:12px">%s</div></div></div>'%(who,col,n_)
    y+=290
cdb_tiers_m=page(c,'',note='',size=(1000,y+10))
F=[('Name and contact','Dana Reyes, mobile and email'),('Source','Referral from a past client'),('Tier','A'),('Closing date','Sep 12'),('Last contact','Oct 14, coffee'),('Consent','Email OK, calls OK'),('Notes','Moving to a larger home next spring')]
c=title('One contact, seven fields',size=62)+sub('Sample record. The person is made up.')
c+=(CARD%(225,len(F)*108+40))
for i,(k,v) in enumerate(F):
    c+='<div style="padding:12px 28px 0"><div style="font-size:38px;font-weight:600;color:#667085;line-height:1.1">%s</div><div style="font-size:44px;font-weight:800;color:#1d2433;line-height:1.1;margin-top:4px">%s</div></div>'%(k,v)
c+='</div>'
cdb_fields_m=page(c,'',note='',size=(1000,225+len(F)*108+70))
c=title('Before and after a clean-up',size=62)+sub('Sample list. Names are made up.')
B=['Dana Reyes','Dana Reyes','Sam Ortiz (bounced)','Lee Park','No source, no tier']
A_=['Dana Reyes, tier A','Sam Ortiz removed','Lee Park, tier B','Next touch set']
y=225
c+=(CARD%(y,len(B)*96+110))+head('#98a2b3','Before')+'<div style="padding:10px 28px">'+''.join('<div style="font-size:44px;font-weight:700;color:#1d2433;line-height:96px">%s</div>'%b for b in B)+'</div></div>'
y+=len(B)*96+110+30
c+=(CARD%(y,len(A_)*96+110))+head(TEAL,'After')+'<div style="padding:10px 28px">'+''.join('<div style="font-size:44px;font-weight:700;color:#1d2433;line-height:96px">%s</div>'%b for b in A_)+'</div></div>'
y+=len(A_)*96+110
cdb_clean_m=page(c,'',note='',size=(1000,y+30))
# ---- bai 4 thank you notes
tyn_hero_m=hero('ph_kitchen','Real estate<br>thank you notes','8 templates by moment')
W=[('Offer accepted','Within 1 day','Email or text',TEAL),('Closing','Within 2 to 3 days','Handwritten',N),('Referral','Within 1 day','Call, then a note',TEAL),('Open house visit','Within 1 day','Email',OR),('Home anniversary','On the date','Handwritten card',N)]
c=title('When to send each note',size=62)+sub('Sample timing. Adjust it to your clients.')
y=225
for nm,when,fm,col in W:
    c+=(CARD%(y,176))+'<div style="height:78px;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:46px;font-weight:800">%s</div><div style="padding:14px 28px;display:flex;gap:20px;font-size:42px;font-weight:700;color:#1d2433;line-height:1.15"><div style="flex:1">%s</div><div style="flex:1;color:%s">%s</div></div></div>'%(col,nm,when,col,fm)
    y+=198
tyn_when_m=page(c,'',note='',size=(1000,y+10))
card=('<div class="abs" style="left:50px;top:200px;width:900px;border-radius:16px;background:#fff;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
      '<div style="height:80px;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:46px;font-weight:800">After closing</div>'
      '<div style="padding:30px 32px;font-family:Lora,serif;font-size:44px;line-height:1.35;color:#1d2433">'
      '<div style="font-weight:700">Dear Dana,</div>'
      '<div style="margin-top:14px">Congratulations on your new home. It was a pleasure helping you from the first showing to the keys.</div>'
      '<div style="margin-top:14px">Call me any time you have a question about the house.</div>'
      '<div style="margin-top:20px;font-weight:700">Alex, Cedar Hills Realty</div></div></div>'
      '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:40px;font-weight:700;color:%s">Short, specific, no sales pitch</div>')%(TEAL,860,OR)
tyn_card_m=page(title('A short closing note',size=60)+card,'',note='',size=(1000,950))
L=[('Oct 14','Dana R.','Closing','Handwritten'),('Oct 15','Sam O.','Referral','Call + note'),('Oct 20','Lee P.','Open house','Email')]
c=title('Log who you thanked',size=62)+sub('Sample log. Names are made up.')
y=225
for d,p_,m_,f_ in L:
    c+=(CARD%(y,250))+head(TEAL,d+', '+p_)+'<div style="padding:20px 28px"><div style="font-size:44px;font-weight:700;color:#1d2433">Moment: %s</div><div style="font-size:44px;font-weight:700;color:%s;margin-top:10px">Format: %s</div></div></div>'%(m_,OR,f_)
    y+=276
tyn_track_m=page(c,'',note='',size=(1000,y+10))
SC=dict(cdb_hero_m=cdb_hero_m,cdb_tiers_m=cdb_tiers_m,cdb_fields_m=cdb_fields_m,cdb_clean_m=cdb_clean_m,tyn_hero_m=tyn_hero_m,tyn_when_m=tyn_when_m,tyn_card_m=tyn_card_m,tyn_track_m=tyn_track_m)
if __name__=='__main__': render(sel(sys.argv,SC))
