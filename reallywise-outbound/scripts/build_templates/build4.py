import os
OUT="build/out"
IMG_BUYER="https://infinaqnhat.github.io/Web-Infina-AI/reallywise/uploads/pp-pdf-buyer.jpg"
IMG_GIF="https://raw.githubusercontent.com/infinaqnhat/Web-Infina-AI/claude/epic-ride-msgpbj/reallywise/email/rw-demo-buyer.gif"
DEMO="https://reallywise-app.infina.dev"
TOUR="https://infinaqnhat.github.io/Web-Infina-AI/property-expert-demo-tour.html?agent=dashboard#tour=1"
IMG_AGENT="https://infinaqnhat.github.io/Web-Infina-AI/reallywise/uploads/pp-pdf-agent.jpg"
ADDR="ReallyWise, 68 Circular Rd #02-01, Singapore 049422"
FONT="Arial,Helvetica,sans-serif"
INK,MUTED,LINK,LINE="#071843","#6B7285","#067A43","#DCE1EC"
GREET='Hi {{ contact.FIRSTNAME | default:"there" }},'
def p(t,first=False):
    st=f"margin:0 0 14px 0;font-family:{FONT};font-size:15px;line-height:1.6;color:{INK};"
    return f'<p style="{st}">{t}</p>'
def link(href,label):
    return f'<a href="{href}" target="_blank" style="color:{LINK};font-weight:bold;text-decoration:underline;">{label}</a>'
SIG=(f'<p style="margin:18px 0 0 0;font-family:{FONT};font-size:15px;line-height:1.5;color:{INK};"><strong>Eric</strong><br>Growth Manager @ ReallyWise<br><span style="color:{MUTED};">eric@reallywise.ai</span></p>')
def image(src,alt,href=None):
    tag=f'<img src="{src}" alt="{alt}" width="520" style="width:100%;max-width:520px;height:auto;display:block;border:1px solid {LINE};border-radius:12px;" />'
    inner=f'<a href="{href}" target="_blank">{tag}</a>' if href else tag
    return f'<div style="margin:24px 0 0 0;">{inner}</div>'
FOOT=(f'<p style="margin:36px 0 0 0;font-family:{FONT};font-size:12px;line-height:1.6;color:{MUTED};">{ADDR}<br>Not relevant? Reply "stop" and I won\'t write again, or <a href="{{{{ unsubscribe }}}}" style="color:{MUTED};text-decoration:underline;">unsubscribe</a>.</p>')
E={
 "1":dict(subject="Try it as a buyer: 123 Main St",pre="A short guided tour: you play the buyer, then see what lands in your dashboard.",
  body=[p(GREET),
        p("I'm Eric, Growth Manager at ReallyWise. We build AI tools for real estate agents, and one of them is Property Expert, made for listing agents."),
        p("It turns each of your listings into a 24/7 expert. Buyers scan the yard sign or open a link and ask anything about the home, and it answers from the listing's own documents (disclosures, inspection report, HOA), with sources. When a buyer asks for a tour, you get the lead with the full chat, and every conversation is logged in your dashboard."),
        p("Here's a short guided tour, about a minute. You play the buyer, then you see what shows up on the agent side:"),
        p(link(TOUR,"Start the guided tour")),
        p("No signup, and you can skip any step."),SIG,
        image(IMG_GIF,"Animated demo: a buyer asks Property Expert about the HVAC, gets an answer sourced from the inspection report, asks for a tour, and the agent gets a new lead alert",TOUR)]),
 "2":dict(subject="Free for your first 3 months",pre="Open an account and try Property Expert on your listings. The first 3 months are on us.",
  body=[p(GREET),
        p("A few days ago I sent you a guided tour of Property Expert. If it looked useful, here's a reason to try it on your own listings."),
        p("Listing agents who open an account by the end of Q1 2027 and try Property Expert get their first 3 months free. Set it up for a current listing, put the QR code or link on the sign or in your listing materials, and see what buyers actually ask."),
        p(link(DEMO,"Create your first Property Expert")),
        p("If you try it, I'd love to hear what worked and what didn't. Just reply to this email."),SIG,
        image(IMG_AGENT,"The ReallyWise agent dashboard: every buyer chat in one inbox, with the AI's work visible",DEMO)]),
 "3":dict(subject="Should I close the loop?",pre="If Property Expert isn't a fit, tell me what you do need.",
  body=[p(GREET),
        p("I'll close the loop here so I'm not cluttering your inbox. It looks like Property Expert may not be what you need right now, and that's completely fine."),
        p("If there's something else in your day-to-day as a realtor that you wish a tool handled, I'd like to hear it. Our team is happy to set up an interview to talk it through and build around what you need."),
        p("Just reply to this email and describe what you have in mind. Even a couple of lines is enough."),
        p("Thanks for your time."),SIG]),
}
def build(e):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e["subject"]}</title>
</head>
<body style="margin:0;padding:0;background-color:#FFFFFF;">
<div style="display:none;max-height:0;overflow:hidden;">{e["pre"]}</div>
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0"><tr><td align="left" style="padding:24px 20px 24px 20px;">
<table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0" style="max-width:600px;width:100%;"><tr><td align="left" style="padding:0px 0px 0px 0px;">
{chr(10).join(e["body"])}
{FOOT}
</td></tr></table>
</td></tr></table>
</body>
</html>'''
for n,e in E.items():
    h=build(e); open(os.path.join(OUT,f"rw-outbound-{n}.html"),"w",encoding="utf-8").write(h); print(n,len(h.encode()),"B")
