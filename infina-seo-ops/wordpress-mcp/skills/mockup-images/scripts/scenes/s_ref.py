import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import *
N='#1b2a4a'
# forwardable ask + intro
phone=('<div class="abs sh" style="left:90px;top:100px;width:400px;height:760px;border-radius:44px;background:#101828;padding:16px"><div style="width:100%;height:100%;border-radius:30px;background:#f2f4f7;position:relative;overflow:hidden">'
 '<div style="height:70px;background:#fff;border-bottom:1px solid #e4e7ec;display:flex;align-items:center;gap:12px;padding:0 18px"><div style="width:38px;height:38px;border-radius:50%;background:#b7e4cb;color:#116b43;font-weight:800;display:flex;align-items:center;justify-content:center">M</div><div style="font-weight:700;font-size:18px">Maya</div></div>'
 '<div style="position:absolute;left:16px;right:22px;top:92px;background:#1b6ef3;color:#fff;border-radius:20px 20px 20px 4px;padding:14px 16px;font-size:17px;line-height:1.4">If you know anyone thinking about buying or selling in the next year, I would be glad to help them.</div>'
 '<div style="position:absolute;left:16px;right:22px;top:262px;background:#1b6ef3;color:#fff;border-radius:20px 20px 20px 4px;padding:14px 16px;font-size:17px;line-height:1.4">You can forward them my number, or I can write them a short note.</div>'
 '<div style="position:absolute;right:16px;left:90px;top:400px;background:#e4e7ec;border-radius:20px 20px 4px 20px;padding:14px 16px;font-size:17px">My cousin is moving here in the spring. Can you write her?</div>'
 '<div style="position:absolute;left:16px;right:22px;top:510px;background:#1b6ef3;color:#fff;border-radius:20px 20px 20px 4px;padding:14px 16px;font-size:17px;line-height:1.4">Of course. Thank you, Maya. I will let you know how it goes.</div></div></div>')
steps=('<div class="abs" style="left:590px;top:130px;width:900px">'
 +''.join('<div style="display:flex;gap:20px;margin-bottom:34px;align-items:flex-start"><span class="chip" style="background:#e0613a;color:#fff;font-size:22px;padding:8px 18px">%d</span><div><div style="font-size:29px;font-weight:800;color:%s">%s</div><div style="font-size:22px;color:#475467;margin-top:6px;line-height:1.4">%s</div></div></div>'%(i+1,N,t,d) for i,(t,d) in enumerate([('List your sphere','Past clients, friends, family, neighbors and local contacts, with a note on how you know each person.'),('Stay in touch on a schedule','A quarterly update, a yearly home anniversary note and a seasonal card, with no pitch.'),('Make a direct ask','Say what kind of client you want. People rarely think of it unless you say it.'),('Make it easy','Give them one sentence to forward, or offer to write the introduction yourself.'),('Thank them and keep track','Reply within the hour, tell the referrer what happened, and record the source in your CRM.')]))+'</div>')
referral_ask=page(phone+steps,'The referral system, with the ask written out',note='Sample message. Names are made up.')
# agreement
def field(label,val,w=1): return '<div style="grid-column:span %d"><div style="font-size:14px;font-weight:800;color:#667085;letter-spacing:.08em;margin-bottom:6px">%s</div><div style="border-bottom:2px solid #cbd2e0;padding:4px 0 8px;font-size:21px;color:#1d2433;min-height:36px">%s</div></div>'%(w,label,val)
doc=('<div class="paper sh" style="left:90px;top:110px;width:900px;height:520px;border-radius:6px"><div style="padding:36px 48px"><div class="serif" style="font-size:34px;font-weight:700;color:'+N+'">Referral agreement (sample outline)</div><div style="font-size:17px;color:#667085;margin:6px 0 26px">Between two brokerages. Not legal advice; have your broker review the real document.</div>'
 '<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px 34px">'
 +field('REFERRING AGENT AND BROKERAGE','Dana Lee, Cedar Hills Realty')+field('RECEIVING AGENT AND BROKERAGE','Sam Ortiz, Lakeview Realty Group')
 +field('CLIENT COVERED','Chris Alvarez, relocating to Lakeview',2)
 +field('FEE AND HOW IT IS CALCULATED','__ % of the commission received')+field('WHEN IT IS PAID','At closing, through the brokerages')
 +field('HOW LONG IT LASTS','12 months from signing')+field('SIGNED','_____________  _____________')
 +'</div></div></div>')
notes=('<div class="abs" style="left:1040px;top:140px;width:480px">'
 +''.join('<div style="display:flex;gap:14px;margin-bottom:26px;align-items:flex-start"><span style="flex:none;width:34px;height:34px;border-radius:50%%;background:#e6f6ee;color:#116b43;font-weight:800;font-size:20px;display:flex;align-items:center;justify-content:center">&#10003;</span><div style="font-size:22px;color:#1d2433;line-height:1.4">%s</div></div>'%t for t in ['Who the parties are','Which client it covers','The fee and how it is calculated','When it is paid','How long it lasts'])
 +'<div style="font-size:20px;color:#475467;line-height:1.45;border-top:2px solid #cbd2e0;padding-top:18px;margin-top:10px">Put it in writing, between brokerages. Fees vary by market, so there is no standard number.</div></div>')
referral_agreement=page(doc+notes,'What a written referral agreement covers',note='Sample outline. Names are made up; the fee is left blank on purpose.')
# tracker
def tr(a,b,c,d): return '<tr style="border-bottom:1px solid #e4e7ec"><td style="padding:14px 16px;font-size:20px">%s</td><td style="font-size:20px">%s</td><td style="font-size:20px;text-align:right;padding-right:16px"><b>%s</b></td><td style="font-size:20px;color:#475467">%s</td></tr>'%(a,b,c,d)
tab=('<div class="paper sh" style="left:90px;top:110px;width:1420px;height:380px;border-radius:12px"><div style="padding:28px 36px"><div style="font-size:28px;font-weight:800;color:'+N+'">Referrals this quarter</div><div style="font-size:18px;color:#667085;margin:4px 0 18px">Record the source of every new client, and update it when a deal closes.</div>'
 '<table style="width:100%;border-collapse:collapse"><tr style="background:#eef2f8;color:#475467;font-size:15px;text-transform:uppercase;letter-spacing:.06em"><th style="text-align:left;padding:12px 16px">Referrer</th><th style="text-align:left">Introduced</th><th style="text-align:right;padding-right:16px">Status</th><th style="text-align:left">Thanked</th></tr>'
 +tr('Maya R., past client','Her cousin (relocating)','Appointment','Note sent, outcome shared')+tr('Linda P., neighbor','A coworker (selling)','Listed','Note sent')+tr('Sam O., agent in Lakeview','Chris (moving here)','Closed','Agreement signed, fee paid')+tr('Priya S., lender','A first-time buyer','In conversation','Thank-you call made')
 +'</table></div></div>')
referral_tracker=page(tab+'<div class="abs" style="left:90px;top:540px;width:1420px;font-size:24px;font-weight:600;color:'+N+'">After a quarter, count the conversations and closings that came from referrals, and who sent them. Thank your top referrers in person.</div>','Track your referral results',note='Sample table. Names are made up.')
SC=dict(referral_ask=referral_ask,referral_agreement=referral_agreement,referral_tracker=referral_tracker)
if __name__=='__main__': render(sel(sys.argv,SC))
