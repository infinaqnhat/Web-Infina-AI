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
def row_card(y,col,name,when,fm,h=176):
    if not fm:
        return (CARD%(y,h))+head(col,name,h=78,fs=46)+'<div style="padding:14px 28px;font-size:44px;font-weight:700;color:%s;line-height:1.15">%s</div></div>'%(col,when)
    return (CARD%(y,h))+head(col,name,h=78,fs=46)+'<div style="padding:14px 28px;display:flex;gap:20px;font-size:42px;font-weight:700;color:#1d2433;line-height:1.15"><div style="flex:1">%s</div><div style="flex:1;color:%s">%s</div></div></div>'%(when,col,fm)
# ---- bai 2 follow up email
fu_hero_m=hero('ph_condo','Real estate<br>follow up<br>email templates','Leads, showings, open houses')
W=[('New web lead','Same day','First reply',TEAL),('After a showing','Same evening','Or next morning',N),('After an open house','Next morning','One email to all',TEAL),('Quiet lead','About a week later','Then stop',OR)]
c=title('When to send each email',size=62)+sub('Sample timing. Adjust it to your market.')
y=225
for nm,when,fm,col in W:
    c+=row_card(y,col,nm,when,fm); y+=198
fu_when_m=page(c,'',note='',size=(1000,y+10))
em=('<div class="abs" style="left:50px;top:215px;width:900px;border-radius:16px;background:#fff;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
    '<div style="padding:22px 30px;background:#eef2f7;font-size:40px;color:#667085;font-weight:600;line-height:1.25">Subject: <span style="color:#1d2433;font-weight:800">Thoughts on 12 Cedar Lane?</span></div>'
    '<div style="padding:28px 32px;font-size:44px;line-height:1.35;color:#1d2433">'
    '<div style="font-weight:700">Hi Dana,</div>'
    '<div style="margin-top:14px">It was good to see 12 Cedar Lane with you today. <span style="background:#ffe6dc;border-radius:6px;padding:0 6px">What stood out to you, good or bad?</span></div>'
    '<div style="margin-top:14px">If it is on your list, I can send recent sales nearby.</div>'
    '<div style="margin-top:20px;font-weight:700">Alex, Cedar Hills Realty</div></div></div>')
chips=[('1','One question to answer',OR),('2','Three to six lines',TEAL),('3','A reply address that works',N)]
cy=855
for n_,t_,col in chips:
    em+=dot(int(n_),50,cy,d=70,fs=44,col=col)+'<div class="abs" style="left:140px;top:%dpx;width:810px;font-size:44px;font-weight:700;color:#1d2433;line-height:70px">%s</div>'%(cy,t_)
    cy+=96
fu_email_m=page(title('A short follow up email',size=62)+sub('Sample. The name and address are made up.')+em,'',note='',size=(1000,cy+30))
Q=[('Day 1','First email','Answer the question',TEAL),('Day 8','Short check-in','One line',N),('Day 30','Local market note','Something useful',TEAL),('Day 60','Last email','Offer to stop',OR)]
c=title('A cadence for a quiet lead',size=62)+sub('Sample gaps. Stop after the last email.')
y=225
for d,nm,fm,col in Q:
    c+=row_card(y,col,d+': '+nm,fm,'',h=176); y+=198
c+='<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:44px;font-weight:800;color:%s">Reply or "stop"? Pause the sequence.</div>'%(y+6,OR)
fu_quiet_m=page(c,'',note='',size=(1000,y+110))
# ---- bai 3 realtor email templates
ret_hero_m=hero('ph_house','Realtor<br>email templates','20 emails for every client')
S=[('Offer and contract','5 emails',TEAL),('Inspection and appraisal','4 emails',N),('Financing and closing prep','4 emails',TEAL),('Closing and after','7 emails',OR)]
c=title('20 emails in four stages',size=62)+sub('Sample grouping. Edit it to fit your deals.')
y=225
for nm,n_,col in S:
    c+=(CARD%(y,176))+head(col,nm,h=78,fs=44)+'<div style="padding:14px 28px;font-size:50px;font-weight:800;color:%s;line-height:1.15">%s</div></div>'%(col,n_)
    y+=198
ret_stages_m=page(c,'',note='',size=(1000,y+10))
card=('<div class="abs" style="left:50px;top:215px;width:900px;border-radius:16px;background:#fff;box-shadow:0 6px 16px rgba(20,35,70,.12);overflow:hidden">'
      '<div style="height:80px;background:%s;color:#fff;display:flex;align-items:center;padding:0 28px;font-size:46px;font-weight:800">Offer accepted</div>'
      '<div style="padding:22px 32px 6px;font-size:40px;color:#667085;font-weight:600;line-height:1.25">Subject: <span style="color:#1d2433;font-weight:800">Congratulations, 12 Cedar Lane is under contract</span></div>'
      '<div style="padding:12px 32px 30px;font-size:44px;line-height:1.35;color:#1d2433">'
      '<div style="font-weight:700">Hi Dana,</div>'
      '<div style="margin-top:12px">The seller accepted your offer. The next steps are the inspection and your loan paperwork.</div>'
      '<div style="margin-top:12px">I will send a dated list this afternoon.</div>'
      '<div style="margin-top:18px;font-weight:700">Alex, Cedar Hills Realty</div></div></div>'
      '<div class="abs" style="left:50px;top:%dpx;width:900px;font-size:42px;font-weight:700;color:%s">Send within the hour. Name the next step.</div>')%(TEAL,920,OR)
ret_email_m=page(title('A sample deal email',size=62)+sub('Sample. Names and address are made up.')+card,'',note='',size=(1000,1010))
A=[('Closing day','Welcome home, same day',TEAL),('1 week','Ask how the move is going',N),('30 days','Check in, then ask for a review',TEAL),('1 year','Anniversary note, value update',OR)]
c=title('After closing: four touches',size=62)+sub('Sample timing. Adjust it to your client.')
y=225
for d,nm,col in A:
    c+=row_card(y,col,d,nm,'',h=176); y+=198
ret_after_m=page(c,'',note='',size=(1000,y+10))
SC=dict(fu_hero_m=fu_hero_m,fu_when_m=fu_when_m,fu_email_m=fu_email_m,fu_quiet_m=fu_quiet_m,ret_hero_m=ret_hero_m,ret_stages_m=ret_stages_m,ret_email_m=ret_email_m,ret_after_m=ret_after_m)
if __name__=='__main__': render(sel(sys.argv,SC))
