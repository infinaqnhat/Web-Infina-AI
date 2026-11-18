import re
exec(open("scripts/build_templates/build4.py").read().split("for n,e in E.items():")[0])
OUTD="."
ST='{{ contact.LISTING_STREET }}'
TL="{{ contact.TOUR_LINK | default:'"+TOUR+"' }}"       # personalised tour link, generic tour as fallback
def cond(var,a,b): return '{% if contact.'+var+' %}'+a+'{% else %}'+b+'{% endif %}'
def plink(label): return f'<a href="{TL}" target="_blank" style="color:{LINK};font-weight:bold;text-decoration:underline;">{label}</a>'
subject='A 24/7 expert for {{ contact.LISTING_STREET | default:"your listings" }}'
pre="A short guided tour: you play the buyer, then see what lands in your dashboard."
body=[
 p(GREET),
 p(cond("LISTING_STREET","Congrats on the new listing at "+ST+". Buyers will have questions about it at all hours, and most agents can't answer at 10pm.","Congrats on your new listing. Buyers will have questions about it at all hours, and most agents can't answer at 10pm.")),
 p("I'm Eric, Growth Manager at ReallyWise. We build AI tools for real estate agents, and one of them is Property Expert, made for listing agents."),
 p(cond("TOUR_LINK","I went ahead and set one up for "+ST+". Buyers scan the yard sign or open a link and ask anything about the home, and it answers from the listing's own details, with sources.","It turns each of your listings into a 24/7 expert. Buyers scan the yard sign or open a link and ask anything about the home, and it answers from the listing's own documents (disclosures, inspection report, HOA), with sources.")+" When a buyer asks for a tour, you get the lead with the full chat, and every conversation is logged in your dashboard."),
 p(cond("TOUR_LINK","Here's a short guided tour of it, about a minute. You play the buyer, then you see the agent side:","Here's a short guided tour, about a minute. You play the buyer, then you see what shows up on the agent side:")),
 p(plink("Start the guided tour")),
 p("No signup, and you can skip any step."),
 SIG,
 f'<div style="margin:24px 0 0 0;"><a href="{TL}" target="_blank"><img src="{IMG_GIF}" alt="Animated demo: a buyer asks Property Expert about the HVAC, gets an answer sourced from the inspection report, asks for a tour, and the agent gets a new lead alert" width="520" style="width:100%;max-width:520px;height:auto;display:block;border:1px solid {LINE};border-radius:12px;" /></a>'+'{% if contact.TOUR_LINK %}<p style="margin:8px 0 0 0;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:1.5;color:#6B7285;">Sample home shown. Your own Property Expert is at the link above.</p>{% endif %}</div>']
e=dict(subject=subject,pre=pre,body=body)
html=build(e).replace("<title>"+subject+"</title>","<title>A 24/7 expert for your listing</title>")
open(OUTD+"/build/out/rw-outbound-1b.html","w",encoding="utf-8").write(html)
print(len(html.encode()),"B")
def render(h,ctx):
    h=re.sub(r'\{% if contact\.(\w+) %\}(.*?)\{% else %\}(.*?)\{% endif %\}',lambda m:m.group(2) if ctx.get(m.group(1)) else m.group(3),h,flags=re.S)
    h=re.sub(r'\{\{ contact\.(\w+) \| default:["\']([^"\']*)["\'] \}\}',lambda m:ctx.get(m.group(1)) or m.group(2),h)
    h=re.sub(r'\{\{ contact\.(\w+) \}\}',lambda m:ctx.get(m.group(1),""),h)
    return h.replace("{{ unsubscribe }}","#")
full={"FIRSTNAME":"Alex","LISTING_STREET":"1428 Maple Ave","TOUR_LINK":"https://example.reallywise.ai/expert/1428-maple-ave#tour=1"}
open(OUTD+"/build/preview/rw-outbound-1b.html","w",encoding="utf-8").write(render(html,full))
open(OUTD+"/build/preview/rw-outbound-1b-fallback.html","w",encoding="utf-8").write(render(html,{"FIRSTNAME":"Alex"}))
print(re.findall(r'href="([^"]+)"',render(html,full))[:3], "|", re.findall(r'href="([^"]+)"',render(html,{"FIRSTNAME":"Alex"}))[:2])
