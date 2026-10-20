import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
# matrix from the Ten Quick Wins table: (cost, effort)
ideas=[('Quarterly market update note','Low','Low'),('Home anniversary note','Low','Low'),('Ask for introductions by name','Low','Low'),('Weekly question-and-answer post','Low','Low'),('Google Business Profile updates','Low','Low'),('Ask for Google reviews at closing','Low','Low'),('Neighborhood spotlight post','Low','Medium'),('Just-sold postcard to nearby homes','Medium','Low'),('Open house invite to neighbors','Low','Medium'),('Listing presentation packet','Low','Medium')]
cells={}
for n,c,e in ideas: cells.setdefault((c,e),[]).append(n)
g=''
X0,Y0=320,170;CW,CH=600,170
for ci,c in enumerate(['Low','Medium']):
    for ei,e in enumerate(['Low','Medium']):
        items=cells.get((c,e),[])
        bg='#e6f6ee' if (c,e)==('Low','Low') else '#fff'
        g+='<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;background:%s;border-radius:12px;box-shadow:0 6px 16px rgba(20,35,70,.1);padding:16px 18px;display:flex;flex-wrap:wrap;gap:8px;align-content:flex-start">'%(X0+ei*(CW+14),Y0+ci*(CH+14),CW,CH,bg)
        g+=''.join('<span class="chip" style="background:%s;color:%s;font-size:16px;padding:6px 12px">%s</span>'%('#c6ecd7' if bg=='#e6f6ee' else '#eef2fb','#116b43' if bg=='#e6f6ee' else N,n) for n in items)+'</div>'
g+=''.join('<div class="abs" style="left:%dpx;top:132px;width:%dpx;text-align:center;font-size:22px;font-weight:800;color:%s">Effort: %s</div>'%(X0+i*(CW+14),CW,N,t) for i,t in enumerate(['Low','Medium']))
g+=''.join('<div class="abs" style="left:70px;top:%dpx;width:230px;font-size:22px;font-weight:800;color:%s;display:flex;align-items:center;height:%dpx">Cost: %s</div>'%(Y0+i*(CH+14),N,CH,t) for i,t in enumerate(['Low','Medium']))
ideas_matrix=page(g+'<div class="abs" style="left:320px;top:560px;width:1214px;font-size:22px;font-weight:600;color:'+N+'">Start in the green box: six ideas that cost little and take little effort.</div>','Ten quick wins by cost and effort',note='Placed from the quick-wins table.')
# note mocks
note1=('<div class="paper sh" style="left:90px;top:120px;width:640px;height:420px;border-radius:6px;background:#fffdf7;transform:rotate(-1.2deg)"><div style="padding:40px 46px;font-family:Lora,serif;font-style:italic;font-size:25px;line-height:1.6;color:#2a3550"><div style="font-size:19px;font-style:normal;font-weight:800;color:#e0613a;letter-spacing:.1em;margin-bottom:14px">HOME ANNIVERSARY NOTE</div>Happy one year in the house on Cedar Lane, Maya! If you are ever curious what homes on your street are selling for, I would be glad to send you a quick update.<div style="margin-top:20px;font-style:normal;font-family:Inter;font-weight:700;font-size:20px">Dana</div></div></div>')
note2=('<div class="paper sh" style="left:800px;top:120px;width:700px;height:420px;border-radius:8px"><div style="background:'+N+';color:#fff;padding:18px 28px"><div style="font-size:15px;font-weight:800;letter-spacing:.14em;color:#9fb4d6">QUARTERLY MARKET UPDATE</div><div class="serif" style="font-size:28px;font-weight:700;margin-top:4px">Cedar Hills, this quarter</div></div><div style="padding:24px 28px;font-size:21px;line-height:1.55;color:#1d2433">Homes near you took about <b>21 days</b> to sell this quarter. Two sold above the asking price.<br><br>If you would like to know what that means for your home, reply to this note and I will send a short report.<div style="margin-top:16px;color:#667085;font-size:18px">Dana Lee &middot; Cedar Hills Realty &middot; 555-0142</div></div></div>')
ideas_notes=page(note1+note2+'<div class="abs" style="left:90px;top:600px;width:1410px;font-size:24px;font-weight:600;color:'+N+';line-height:1.5">Two low-cost ideas for your sphere: a short handwritten note on the home anniversary, and a plain quarterly update. Specific and personal beats long.</div>','Two sphere ideas, written out',note='Sample notes. Names and numbers are made up.')
SC=dict(ideas_matrix=ideas_matrix,ideas_notes=ideas_notes)
if __name__=='__main__': render(sel(sys.argv,SC))
