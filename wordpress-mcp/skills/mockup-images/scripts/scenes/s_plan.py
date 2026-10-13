import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
CH=[('Sphere and referrals','#14808a'),('Print and branding','#1b2a4a'),('Social media','#e0a21b'),('Website and local SEO','#7c5cc4'),('Direct mail','#e0613a'),('Paid ads','#c2410c'),('Test reserve','#98a2b3')]
NEW=[30,25,15,10,0,0,20]; GROW=[20,10,10,20,20,15,5]
def bar(y,label,sub,shares,total):
    s='<div class="abs" style="left:70px;top:%dpx;width:230px"><div style="font-size:26px;font-weight:800;color:%s">%s</div><div style="font-size:19px;color:#667085;margin-top:4px">%s</div></div>'%(y+16,N,label,sub)
    x=320
    for (name,col),p in zip(CH,shares):
        if not p: continue
        w=int(p*1180/100)
        d=int(total*p/100)
        s+='<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:110px;background:%s;color:#fff;border-right:3px solid #fff;display:flex;flex-direction:column;justify-content:center;align-items:center;font-weight:800"><span style="font-size:24px">%d%%</span><span style="font-size:17px;font-weight:600">$%d</span></div>'%(x,y,w,col,p,d)
        x+=w
    return s
leg=''
for i,(n,c) in enumerate(CH): leg+='<div class="abs" style="left:%dpx;top:620px;display:flex;gap:10px;align-items:center;font-size:19px;color:#1d2433"><i style="width:18px;height:18px;border-radius:4px;background:%s"></i>%s</div>'%(70+(i%4)*370,c,n) if i<4 else '<div class="abs" style="left:%dpx;top:662px;display:flex;gap:10px;align-items:center;font-size:19px;color:#1d2433"><i style="width:18px;height:18px;border-radius:4px;background:%s"></i>%s</div>'%(70+((i-4)%4)*370,c,n)
plan_budget=page(bar(190,'New agent','$500 a month',NEW,500)+bar(380,'Growing agent','$1,500 a month',GROW,1500)+leg+'<div class="abs" style="left:70px;top:740px;width:1460px;font-size:22px;color:#475467;line-height:1.45">Same channels, different order. The new agent builds on people who already know them; the growing agent adds channels that reach people who do not.</div>','Where the budget goes: two example plans',note='Shares from the budget table; dollar amounts follow the two example plans.')
# spreadsheet
def cell(t,w,bg='#fff',bold=False,col='#1d2433',align='left'):
    return '<td style="width:%dpx;background:%s;font-weight:%s;color:%s;text-align:%s;padding:9px 12px;border:1px solid #d0d7e2;font-size:18px;white-space:nowrap">%s</td>'%(w,bg,'800' if bold else '500',col,align,t)
Y='#fff4cc';T='#e6f2f1';H='#1f3a5f'
tabs=['Start Here','1 Goal Backward','2 Budget','3 Plan','4 Quarterly Review']
tabhtml=''.join('<span style="padding:9px 18px;font-size:17px;border-radius:8px 8px 0 0;background:%s;color:%s;font-weight:%s;border:1px solid #d0d7e2;border-bottom:none">%s</span>'%('#fff' if t=='3 Plan' else '#e4e8f0','#1f3a5f' if t=='3 Plan' else '#667085','800' if t=='3 Plan' else '500',t) for t in tabs)
hdr=''.join(cell(h,w,H,True,'#fff') for h,w in [('Channel',230),('Audience',250),('Weekly action',280),('Hours per week',150),('Monthly budget',160),('Result to track',260)])
rows=[('Sphere and referrals','Past clients and neighbors','Five personal notes or calls','2','$100','Introductions received'),('Social media','Local first-time buyers','Three posts and ten replies','2','$50','Messages and profile visits'),('Direct mail','One farm area of 300 homes','Monthly mailing, one drop','1','$150','Calls and valuation requests')]
body=''.join('<tr>'+''.join(cell(v,0,Y,False,'#1d2433','right' if i in (3,4) else 'left') for i,v in enumerate(r))+'</tr>' for r in rows)
body+='<tr>'+cell('',0)*0+''.join(cell('',0,Y) for _ in range(6))+'</tr>'
tot='<tr>'+cell('Total',0,T,True)+cell('',0,T)+cell('',0,T)+cell('5',0,T,True,'#1d2433','right')+cell('$300',0,T,True,'#1d2433','right')+cell('',0,T)+'</tr>'
sheet=('<div style="padding:26px 36px"><div style="font-size:30px;font-weight:800;color:#1f3a5f;margin-bottom:16px">Your one-page marketing plan</div>'
 '<table style="border-collapse:collapse;margin-bottom:16px"><tr>'+cell('Goal',150,'#fff',True)+cell('10 closings this year',420,Y)+'</tr><tr>'+cell('Audience (one sentence)',150,'#fff',True)+cell('',420,Y)+'</tr><tr>'+cell('Date of first review',150,'#fff',True)+cell('',420,Y)+'</tr></table>'
 '<table style="border-collapse:collapse"><tr>'+hdr+'</tr>'+body+tot+'</table>'
 '<table style="border-collapse:collapse;margin-top:18px"><tr>'+cell('Monthly budget from the Budget sheet',380)+cell('$500',150,T,False,'#1d2433','right')+'</tr><tr>'+cell('Difference (budget minus plan)',380)+cell('$200',150,T,False,'#1d2433','right')+cell('Plan fits the budget',260,'#fff',True,'#1f8a5b')+'</tr></table></div>')
win=('<div class="abs sh" style="left:60px;top:70px;width:1480px;height:720px;border-radius:12px;background:#fff;overflow:hidden">'
 '<div style="height:46px;background:#217346;color:#fff;display:flex;align-items:center;padding:0 20px;font-size:18px;font-weight:700">real-estate-marketing-plan-template.xlsx</div>'+sheet+
 '<div style="position:absolute;left:0;right:0;bottom:0;height:52px;background:#eef1f6;display:flex;gap:6px;align-items:flex-end;padding:0 16px">'+tabhtml+'</div></div>')
plan_template=page(win+'<div class="abs" style="left:60px;top:812px;font-size:19px;color:#667085">Yellow cells are inputs, teal cells are worked out for you. The numbers shown are the template&rsquo;s example values.</div>','The Excel version of the plan',note='')
# tracker
def tr(name,sp,cv,ap,cl):
    pc='$%d'%(sp/cl) if cl else ''
    pv='$%.2f'%(sp/cv) if cv else ''
    return '<tr>'+cell(name,0)+cell('$%d'%sp,0,Y,False,'#1d2433','right')+cell(str(cv),0,Y,False,'#1d2433','right')+cell(str(ap),0,Y,False,'#1d2433','right')+cell(str(cl),0,Y,False,'#1d2433','right')+cell(pc,0,T,False,'#1d2433','right')+cell(pv,0,T,False,'#1d2433','right')+'</tr>'
data=[('Sphere and referrals',150,42,7,2),('Social media',150,24,3,0),('Website and local SEO',200,11,2,1),('Paid ads',300,36,4,1),('Direct mail',450,18,3,1)]
sp=sum(d[1] for d in data); cv=sum(d[2] for d in data); ap=sum(d[3] for d in data); cl=sum(d[4] for d in data)
th=''.join(cell(h,0,H,True,'#fff') for h in ['Source','Spend','Conversations','Appointments','Closings','Spend per closing','Spend per conversation'])
q=('<div style="padding:26px 36px"><div style="font-size:30px;font-weight:800;color:#1f3a5f">Review every 90 days</div><div style="font-size:19px;color:#667085;margin:6px 0 18px">Record the lead source for every contact. Quarter 1, sample numbers.</div>'
 '<table style="border-collapse:collapse"><tr>'+th+'</tr>'+''.join(tr(*d) for d in data)+
 '<tr>'+cell('Total',0,T,True)+cell('$%d'%sp,0,T,True,'#1d2433','right')+cell(str(cv),0,T,True,'#1d2433','right')+cell(str(ap),0,T,True,'#1d2433','right')+cell(str(cl),0,T,True,'#1d2433','right')+cell('$%d'%(sp/cl),0,T,True,'#1d2433','right')+cell('$%.2f'%(sp/cv),0,T,True,'#1d2433','right')+'</tr></table>'
 '<div style="margin-top:22px;font-size:20px;color:#1d2433;background:#fff7e6;border-left:6px solid #e0a21b;padding:14px 20px;width:1160px"><b>What I learned, and the one thing I will change:</b> Direct mail cost the most per closing. Keep it to one farm area and test one new offer next quarter.</div></div>')
win2=('<div class="abs sh" style="left:60px;top:90px;width:1480px;height:640px;border-radius:12px;background:#fff;overflow:hidden">'
 '<div style="height:46px;background:#217346;color:#fff;display:flex;align-items:center;padding:0 20px;font-size:18px;font-weight:700">real-estate-marketing-plan-template.xlsx</div>'+q+
 '<div style="position:absolute;left:0;right:0;bottom:0;height:52px;background:#eef1f6;display:flex;gap:6px;align-items:flex-end;padding:0 16px">'+tabhtml.replace('background:#fff;color:#1f3a5f;font-weight:800','background:#e4e8f0;color:#667085;font-weight:500').replace('>4 Quarterly Review','>4 Quarterly Review').replace('background:#e4e8f0;color:#667085;font-weight:500;border:1px solid #d0d7e2;border-bottom:none">4 Quarterly Review','background:#fff;color:#1f3a5f;font-weight:800;border:1px solid #d0d7e2;border-bottom:none">4 Quarterly Review')+'</div></div>')
plan_tracker=page(win2+'<div class="abs" style="left:60px;top:760px;width:1480px;font-size:21px;color:#1b2a4a;font-weight:600">Spend per closing shows which channel is worth keeping. Sample numbers, not real results.</div>','Review the numbers every 90 days',note='')
SC=dict(plan_budget=plan_budget,plan_template=plan_template,plan_tracker=plan_tracker)
if __name__=='__main__': render(sel(sys.argv,SC))
