import re
exec(open("scripts/build_templates/build4.py").read().split("for n,e in E.items():")[0])
S="."
e=dict(subject="Not into a monthly fee?",pre="Pay only if the listing sells.",
 body=[p(GREET),
  p("I realize a monthly subscription isn't how every agent likes to buy software. So here's another way to use Property Expert: pay per closing."),
  p("You set it up on a listing at no upfront cost. Only if that listing sells and closes do we take 7% of your commission on it. If it doesn't sell, you pay nothing."),
  p("For example, on an $800,000 home with a 2.75% listing-side commission ($22,000), that's $1,540, due at closing."),
  p("If you'd rather go this way, just reply \"closing\" with the listing you'd like to start with, and I'll set it up and send the terms in writing."),
  SIG])
html=build(e)
open(S+"/build/out/rw-outbound-ppc.html","w",encoding="utf-8").write(html)
open(S+"/build/preview/rw-outbound-ppc.html","w",encoding="utf-8").write(html.replace('{{ contact.FIRSTNAME | default:"there" }}',"Alex").replace("{{ unsubscribe }}","#"))
print(len(html.encode()),"B", "dashes:",html.count("—"),html.count("–"), "| check math:",800000*0.0275, 800000*0.0275*0.05)
