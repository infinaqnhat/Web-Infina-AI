import re, sys, json
# Builds reallywise/property-expert-presentation.html from the main deck at the repo root
# (product-presentation.html: styles, slide engine, demos) and the slides in this folder.
# Run from anywhere: python3 reallywise/deck-src/build-property-expert-presentation.py
import os
D = os.path.dirname(os.path.abspath(__file__)) + '/'
REPO = os.path.abspath(D + '../../') + '/'
src = open(REPO + 'product-presentation.html').read()
slides = open(D + 'property-expert-slides.html').read()
qr = json.load(open(D + 'qr.json'))

def rep(s, o, n, c=1):
    assert s.count(o) == c, (o[:80], s.count(o))
    return s.replace(o, n)

def section(s, sid):
    m = re.search(r'\n    <!--[^\n]*-->\n    <section class="slide[^"]*" id="%s".*?\n    </section>\n' % sid, s, flags=re.S)
    assert m, sid
    return m.group(0)

# ----- reused slides: live demos, the print-only page
demo = section(src, 'demo-buyer') + section(src, 'demo-agent')
demo = rep(demo, 'The working Property Expert for 123 Main Street, Austin. Ask it what a real buyer would ask.', 'The working Property Expert for 123 Main Street, Austin. Ask what a real buyer would ask, then book a viewing.')
demo = rep(demo, '<li><span><strong>Ask for a tour</strong> or to talk to the agent. The chat becomes a lead.</span></li>', '<li><span><strong>Book a viewing.</strong> Pick a time and the chat becomes a lead.</span></li>')
demo = demo.replace('reallywise.ai/expert/123-main-street', 'reallywise.ai/l/123-main').replace('<span>reallywise.ai/dashboard</span>', '<span>app.reallywise.ai/chats</span>')

see = section(src, 'see-live')
see = rep(see, 'https://infinaqnhat.github.io/Web-Infina-AI/property-expert-demo-tour.html#tour=1', 'https://infinaqnhat.github.io/Web-Infina-AI/reallywise/property-expert-demo-tour.html#tour=1')
see = rep(see, 'https://infinaqnhat.github.io/Web-Infina-AI/dashboard/chats/index.html#tour=0', 'https://infinaqnhat.github.io/Web-Infina-AI/reallywise/dashboard/chats/index.html#tour=0')
see = rep(see, 'https://drive.google.com/file/d/1rqyiJv--T6Ai9ITCeb0E4X4emLAff89p/view', 'https://infinaqnhat.github.io/Web-Infina-AI/reallywise/uploads/property-expert-promo.mp4')
see = rep(see, '<b>Watch the film</b><span>ReallyWise.ai for U.S. real estate</span>', '<b>Watch the film</b><span>Property Expert in one minute</span>')
see = rep(see, 'href="https://infinaqnhat.github.io/Web-Infina-AI/product-presentation.html">infinaqnhat.github.io/Web-Infina-AI/product-presentation.html</a>', 'href="https://infinaqnhat.github.io/Web-Infina-AI/reallywise/property-expert-presentation.html">infinaqnhat.github.io/Web-Infina-AI/reallywise/property-expert-presentation.html</a>')
see = rep(see, 'On the web this deck is interactive: ask the AI as a buyer, then walk through the agent dashboard. Scan a code or click a link.', 'On the web this deck is interactive: ask Property Expert as a buyer and book a viewing, then walk through the agent dashboard. Scan a code or click a link.')
see = re.sub(r'(<a class="qr" href="[^"]*property-expert-demo-tour[^"]*">)<svg.*?</svg>', lambda m: m.group(1) + qr['buyer'], see, flags=re.S)
see = re.sub(r'(<a class="qr" href="[^"]*dashboard/chats[^"]*">)<svg.*?</svg>', lambda m: m.group(1) + qr['agent'], see, flags=re.S)
see = re.sub(r'(<a class="qr" href="[^"]*promo\.mp4">)<svg.*?</svg>', lambda m: m.group(1) + qr['film'], see, flags=re.S)

slides = slides.replace('DEMO_SLIDES', demo.strip('\n')).replace('SEE_LIVE', see.strip('\n')).replace('QR_LEAD', qr['lead']).replace('QR_REALISA', qr['realisa'])

a = src.index('<main class="deck" id="deck" aria-label="Slides">') + len('<main class="deck" id="deck" aria-label="Slides">')
b = src.index('  </main>')
s = src[:a] + '\n\n' + slides + '\n' + src[b:]

# ----- head
s = rep(s, '<title>ReallyWise.ai · Product Presentation</title>', '<title>ReallyWise Property Expert · Product Presentation</title>')
s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="ReallyWise Property Expert and Realisa: turn every buyer conversation into a booked viewing. Product presentation with a live walkthrough.">', s, count=1)
s = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="ReallyWise Property Expert · Turn every conversation into a booked viewing">', s, count=1)
s = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="An AI expert on every listing and an AI assistant for every agent. Interactive slides with a live walkthrough.">', s, count=1)
s = rep(s, '<meta property="og:site_name" content="ReallyWise.ai">', '<meta property="og:site_name" content="ReallyWise">')
s = re.sub(r'<link href="https://fonts.googleapis.com/css2\?family=Be\+Vietnam\+Pro[^"]*" rel="stylesheet">',
           '<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,500;14..32,600;14..32,700;14..32,800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet">\n  <link rel="icon" href="brand/reallywise-favicon.svg" type="image/svg+xml">', s, count=1)

# ----- brand tokens (guideline v2): navy 900/700, Insight Green, Inter + DM Sans
s = rep(s, "--accent:#001F5C; --accent-dark:#001340; --accent-light:rgba(0,31,92,.08);", "--accent:#012976; --accent-dark:#011F59; --accent-light:rgba(1,41,118,.08);")
s = re.sub(r'--blue:#[0-9a-fA-F]{6}; --blue-light:[^;]+; --sky:#[0-9a-fA-F]{6};', '--blue:#013A9E; --blue-light:rgba(1,58,158,.08); --sky:#3fd18a;', s, count=1)
s = re.sub(r'--green:#[0-9a-fA-F]{6}; --green-light:[^;]+;', '--green:#067a43; --green-light:#e2f6ec; --insight:#0bb563;', s, count=1)
s = re.sub(r"--font:'Be Vietnam Pro'[^;]*;", "--font:'DM Sans',system-ui,sans-serif; --font-display:'Inter','Helvetica Neue',system-ui,sans-serif;", s, count=1)
s = s.replace('0,31,92', '1,41,118').replace('0,19,64', '1,24,72').replace('0,20,60', '1,30,90')
extra = '''
    /* ===== ReallyWise MVP deck ===== */
    h1, h2, h3, .h, .hero-h, .end-h, .tagline, .t-card h3, .poster h3, .toc-item b, .step b, .lc-steps b, .deck-title b { font-family:var(--font-display); }
    .kicker { color:var(--green); }
    .is-dark .kicker { color:var(--sky); }
    .tagline { color:var(--green); }
    .hero-h span, .end-h span { color:var(--sky); }
    .end-h span { display:block; }
    .end-h { font-size:calc(var(--u)*3.6); }
    .btn-blue { background:var(--insight); color:#fff; }
    .btn-blue:hover { background:var(--green); }
    .deck-brand { display:flex; align-items:center; gap:14px; min-width:0; }
    .deck-brand img { height:24px; width:auto; display:block; flex-shrink:0; }
    .deck-brand span { padding-left:14px; border-left:1px solid var(--border); font-size:13px; font-weight:600; color:var(--muted); white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
    .end-logo { width:calc(var(--u)*12); margin-bottom:calc(var(--u)*1.4); display:block; }
    .rw-mark { border-radius:calc(var(--u)*.7) !important; }
    .slots-card { padding:calc(var(--u)*.8) calc(var(--u)*.9); border:1px solid var(--border); border-radius:calc(var(--u)*.9); background:#fff; }
    .slots-card b { display:block; font-size:calc(var(--u)*.98); color:var(--accent); }
    .slots-card > span { display:block; font-size:calc(var(--u)*.85); color:var(--muted); margin-top:calc(var(--u)*.15); }
    .slots { display:flex; flex-wrap:wrap; gap:calc(var(--u)*.4); margin-top:calc(var(--u)*.55); }
    .slots span { font-size:calc(var(--u)*.85); font-weight:600; padding:calc(var(--u)*.35) calc(var(--u)*.7); border-radius:calc(var(--u)*.5); border:1px solid var(--border); color:var(--accent); }
    .slots span.is-on { background:var(--accent); border-color:var(--accent); color:#fff; }
    .live .slots-card { align-self:flex-start; max-width:92%; }
    .mk-today { padding:calc(var(--u)*.7) calc(var(--u)*.9); border-radius:calc(var(--u)*1); border:1px solid var(--border-light); display:flex; flex-direction:column; gap:calc(var(--u)*.4); }
    .mk-today small { font-size:calc(var(--u)*.78); font-weight:800; letter-spacing:.08em; color:var(--green); }
    .mk-today div { display:flex; gap:calc(var(--u)*.8); font-size:calc(var(--u)*.9); }
    .mk-today div b { width:calc(var(--u)*5.2); flex-shrink:0; color:var(--accent); }
    .mk-today div span { color:var(--fg-secondary); }
    .four { flex:1; display:grid; grid-template-columns:repeat(4,1fr); gap:calc(var(--u)*1.3); margin-top:calc(var(--u)*2.6); }
    .four .t-card { padding:calc(var(--u)*1.8); }
    .four .t-card h3 { font-size:calc(var(--u)*1.55); }
    .four .t-card p { font-size:calc(var(--u)*1.08); }
    .film video { position:absolute; inset:0; width:100%; height:100%; background:#000; }
    .t-card.is-answer .ic { background:var(--green-light); color:var(--green); }
'''
s = rep(s, '    /* ===== Print and PDF:', extra + '\n    /* ===== Print and PDF:')
s = rep(s, '      /* lead capture */\n', '      body:not(.view-slides) .four { grid-template-columns:1fr; }\n      body:not(.view-slides) .deck-brand span { display:none; }\n      /* lead capture */\n')

# ----- styles for the hero, team and proposition slides
s = rep(s, '    /* ===== Print and PDF:', open(D + 'new.css').read() + '\n    /* ===== Print and PDF:')
s = rep(s, '      /* lead capture */\n', open(D + 'new-mobile.css').read() + '      /* lead capture */\n')

# ----- header: ReallyWise logo instead of the text title
s = rep(s, '<div class="deck-title"><b>ReallyWise.ai</b><span>Product Presentation · U.S. residential real estate</span></div>',
        '<div class="deck-brand"><img src="brand/Really_Wise_Logo.svg" alt="ReallyWise"><span>Product Presentation · Property Expert + Realisa</span></div>')
s = s.replace('href="uploads/AI-Property-Product-Presentation.pdf"', 'href="uploads/ReallyWise-Property-Expert-Presentation.pdf"')

# ----- script: native film videos, no ecosystem, the new lead story
a = s.index('    // The film: load the player when its slide is first shown, swap films on demand')
b = s.index('    // Lead capture: the steps jump the video')
s = s[:a] + '''    // The film: two videos, picked with the buttons
    var filmVideo = document.getElementById('film-video');
    var filmBtns = [].slice.call(document.querySelectorAll('[data-video]'));
    if (filmBtns.length < 2) filmBtns[0].parentNode.hidden = true;
    filmBtns.forEach(function(b){
      b.addEventListener('click', function(){
        filmBtns.forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        filmVideo.pause();
        filmVideo.setAttribute('poster', b.getAttribute('data-poster'));
        filmVideo.src = b.getAttribute('data-video');
        filmVideo.play().catch(function(){});
      });
    });

''' + s[b:]
a = s.index('    // Ecosystem: highlight one side of the deal')
b = s.index('    // How it works: steps drive the lead card')
s = s[:a] + s[b:]
a = s.index('    var STEPS = [')
b = s.index('    var stepBtns = document.querySelectorAll')
s = s[:a] + '''    var STEPS = [
      { name:'Anonymous visitor', src:'Scanned the yard sign at 123 Main St', temp:12, label:'Just looking',
        feed:[{ t:'Opened Property Expert', d:'From the yard-sign QR. No app, no sign-up.' }] },
      { name:'Anonymous visitor', src:'4 questions in 6 minutes', temp:45, label:'Engaged',
        feed:[{ t:'Asked about the roof and the HOA', d:'Answered from the inspection report and HOA docs' },
              { t:'Learned', d:'First-time buyer · pre-approved · wants a weekend visit' }] },
      { name:'Jordan Lee', src:'Booked a private showing', temp:90, label:'Viewing booked',
        feed:[{ t:'Viewing booked: Sat, 2:00 PM', d:'Lead sent to the agent on the spot, with the full chat', hot:true }] },
      { name:'Jordan Lee', src:'Showing confirmed by the agent', temp:100, label:'Showing confirmed',
        feed:[{ t:'Realisa: confirm Jordan for 2:00 PM', d:'Added to the agent\\'s plan for Saturday' },
              { t:'Reply drafted in the agent\\'s voice', d:'With the HOA answer and parking notes' }] }
    ];
''' + s[b:]
s = rep(s, "      if (id === 'film') loadFilm();\n", "      if (id !== 'film' && !filmVideo.paused) filmVideo.pause();\n")
s = rep(s, "      setLens('all');\n", '')
a = s.index('    // Lead capture: the steps jump the video, and follow it while it plays')
b = s.index('    // How it works: steps drive the lead card')
s = s[:a] + """    // Videos with steps: each step jumps its slide's video, and lights up while that part plays
    var lcVideo = document.getElementById('lc-video');
    [].forEach.call(document.querySelectorAll('.lc-in'), function(box){
      var video = box.querySelector('video'), btns = [].slice.call(box.querySelectorAll('[data-seek]'));
      if (!video || !btns.length) return;
      btns.forEach(function(b){
        b.addEventListener('click', function(){ video.currentTime = +b.getAttribute('data-seek'); video.play().catch(function(){}); });
      });
      video.addEventListener('timeupdate', function(){
        var t = video.currentTime, on = -1, end = video.duration ? video.duration - 8 : 1e9;
        btns.forEach(function(b, i){ if (t >= +b.getAttribute('data-seek') - .2) on = i; });
        btns.forEach(function(b, i){ b.classList.toggle('is-on', i === on && t < end); });
      });
    });

""" + s[b:]
s = rep(s, "      if (id !== 'lead-capture' && lcVideo && !lcVideo.paused) lcVideo.pause();", "      [].forEach.call(document.querySelectorAll('.slide video'), function(v){ if (!v.closest('#' + id) && !v.paused) v.pause(); });")
s = s.replace("try { localStorage.setItem('pp-phone-view', v); }", "try { localStorage.setItem('rw-pp-phone-view', v); }").replace("saved = localStorage.getItem('pp-phone-view');", "saved = localStorage.getItem('rw-pp-phone-view');")

# ----- slide numbers and counts
k = [0]
def lab(m):
    if 'print-only' in m.group(1): return m.group(0)
    k[0] += 1
    return '%sSlide %d, %s"' % (m.group(1), k[0], m.group(2))
s = re.sub(r'(<section class="slide[^"]*"[^>]*? aria-label=")Slide \d+, ([^"]+)"', lab, s)
c = [0]
def numsec(m):
    sec = m.group(0)
    if 'print-only' in sec.split('>', 1)[0]:
        return re.sub(r'<span class="slide-no">\d+</span>', '<span class="slide-no">00</span>', sec)
    c[0] += 1
    return re.sub(r'<span class="slide-no">\d+</span>', '<span class="slide-no">%02d</span>' % c[0], sec)
s = re.sub(r'<section class="slide.*?</section>', numsec, s, flags=re.S)
s = re.sub(r'(<b>1</b> / )\d+', r'\g<1>%d' % k[0], s)
s = re.sub(r'(id="present-count">1 / )\d+', r'\g<1>%d' % k[0], s)
for bad in ['Home Concierge', 'ReallyWise.ai USA', 'Infina']:
    pass
open(REPO + 'reallywise/property-expert-presentation.html', 'w').write(s)
print('slides', k[0])
