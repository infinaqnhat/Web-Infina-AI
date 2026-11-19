# Builds reallywise/property-expert-short.html, the short version of the MVP deck:
# the two AI products and how it works, nothing else.
# It is cut from reallywise/property-expert-presentation.html, so build that first.
# Run from anywhere: python3 reallywise/deck-src/build-property-expert-short.py
import os, re
D = os.path.dirname(os.path.abspath(__file__)) + '/'
REPO = os.path.abspath(D + '../../') + '/'
s = open(REPO + 'reallywise/property-expert-presentation.html').read()
FULL = 'https://infinaqnhat.github.io/Web-Infina-AI/reallywise/property-expert-presentation.html'

def rep(o, n, c=1):
    global s
    assert s.count(o) == c, (o[:80], s.count(o))
    s = s.replace(o, n)

# ----- keep only these slides, in this order
KEEP = ['hero', 'team', 'property-expert', 'realisa', 'how', 'thanks']
a = s.index('<main class="deck" id="deck" aria-label="Slides">') + len('<main class="deck" id="deck" aria-label="Slides">')
b = s.index('  </main>')
secs = {}
for m in re.finditer(r'\n    <!--[^\n]*-->\n    <section class="slide[^"]*" id="([^"]+)".*?\n    </section>\n', s[a:b], flags=re.S):
    secs[m.group(1)] = m.group(0)
s = s[:a] + '\n' + ''.join(secs[k] for k in KEEP) + '\n' + s[b:]

# ----- kickers follow the new order
rep('<span class="kicker anim"><i>04</i>Product 1</span>', '<span class="kicker anim"><i>02</i>Product 1</span>')
rep('<span class="kicker anim"><i>06</i>Product 2</span>', '<span class="kicker anim"><i>03</i>Product 2</span>')
rep('<span class="kicker anim"><i>03</i>How it works</span>', '<span class="kicker anim"><i>04</i>How it works</span>')

# ----- buttons that pointed at slides this version leaves out
rep('data-go="film">Start the presentation', 'data-go="team">Start the presentation')
rep('<button type="button" class="btn btn-ghost" data-go="demo-buyer">Jump to the live demo</button>',
    '<a class="btn btn-ghost" href="%s#demo-buyer">See the full deck and live demo</a>' % FULL)
rep('<button type="button" class="head-btn is-solid" data-go="demo-buyer">Try the demo</button>',
    '<a class="head-btn is-solid" href="%s#demo-buyer">Full deck</a>' % FULL)
rep('<div class="prod-cta anim d4"><button type="button" class="btn btn-navy" data-go="demo-buyer">Try it live</button></div>',
    '<div class="prod-cta anim d4"><a class="btn btn-navy" href="%s#demo-buyer">Try it live</a></div>' % FULL)
rep('<button type="button" class="btn btn-glass" data-go="demo-buyer">Back to the live demo</button>',
    '<a class="btn btn-glass" href="%s#demo-buyer">See the live demo</a>' % FULL)
rep('<span>Product Presentation · Property Expert + Realisa</span>', '<span>Short version · Property Expert + Realisa</span>')
rep('href="uploads/ReallyWise-Property-Expert-Presentation.pdf"', 'href="uploads/ReallyWise-Property-Expert-Short.pdf"')
rep('Interactive version with the live demo: <a href="%s">' % FULL, 'Full deck with the live demo: <a href="%s">' % FULL)
s = re.sub(r'<title>[^<]*</title>', '<title>ReallyWise Property Expert · Short version</title>', s, count=1)

# ----- scripts: the film slide is not in this version
rep("    if (filmBtns.length < 2) filmBtns[0].parentNode.hidden = true;\n", "    if (filmBtns.length === 1) filmBtns[0].parentNode.hidden = true;\n")
rep("      if (id !== 'film' && !filmVideo.paused) filmVideo.pause();\n", "      if (filmVideo && id !== 'film' && !filmVideo.paused) filmVideo.pause();\n")
s = s.replace("'rw-pp-phone-view'", "'rw-short-phone-view'")

# ----- slide numbers and counts
k = [0]
def lab(m):
    k[0] += 1
    return '%sSlide %d, %s"' % (m.group(1), k[0], m.group(2))
s = re.sub(r'(<section class="slide[^"]*"[^>]*? aria-label=")Slide \d+, ([^"]+)"', lab, s)
c = [0]
def num(m):
    c[0] += 1
    return '<span class="slide-no">%02d</span>' % c[0]
s = re.sub(r'<span class="slide-no">\d+</span>', num, s)
s = re.sub(r'(<b>1</b> / )\d+', r'\g<1>%d' % k[0], s)
s = re.sub(r'(id="present-count">1 / )\d+', r'\g<1>%d' % k[0], s)
for gone in ['data-go="film"', 'data-go="demo-buyer"', 'data-go="demo-agent"', 'data-go="lead-capture"', 'data-go="proposition"']:
    assert gone not in s, gone
open(REPO + 'reallywise/property-expert-short.html', 'w').write(s)
print('slides', k[0])
