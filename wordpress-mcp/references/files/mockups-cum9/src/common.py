import sys, os, segno
from playwright.sync_api import sync_playwright
HERE=os.path.dirname(os.path.abspath(__file__))
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Lora:ital,wght@0,500;0,700;1,500&display=swap">'
CSS='''
*{box-sizing:border-box}
:root{--navy:#1b2a4a;--teal:#14808a;--ink:#1d2433;--muted:#667085;--line:#d6dce8;--good:#1f8a5b;--bad:#c2410c;--accent:#e0613a;--gold:#b88a2e}
html,body{margin:0;padding:0}
body{width:1600px;height:900px;position:relative;overflow:hidden;background:linear-gradient(135deg,#e4eaf4 0%,#f3f5fa 100%);font-family:Inter,'Liberation Sans',Arial,sans-serif;color:var(--ink)}
.tag{position:absolute;left:44px;top:30px;font-size:19px;letter-spacing:.14em;text-transform:uppercase;color:#52627f;font-weight:700}
.note{position:absolute;right:44px;bottom:26px;font-size:17px;color:#6b778c}
.sh{box-shadow:0 22px 44px rgba(20,35,70,.20),0 3px 8px rgba(20,35,70,.14)}
.abs{position:absolute}
.paper{background:#fff;overflow:hidden;position:absolute}
.photo{background-size:cover;background-position:center}
.serif{font-family:Lora,'Liberation Serif',serif}
.chip{display:inline-block;padding:6px 14px;border-radius:999px;font-weight:700;font-size:17px}
.cap{position:absolute;font-size:20px;font-weight:700;color:var(--navy);text-align:center}
.cap small{display:block;font-weight:500;font-size:16px;color:var(--muted);margin-top:4px}
.call{position:absolute;display:flex;gap:12px;align-items:flex-start;font-size:21px;font-weight:600;color:var(--navy);line-height:1.25}
.call b{flex:none;width:36px;height:36px;border-radius:50%;background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-size:19px}
.num{width:30px;height:30px;border-radius:50%;background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:700;position:absolute}
svg.lines{position:absolute;left:0;top:0;width:1600px;height:900px;pointer-events:none}
svg.lines line{stroke:var(--accent);stroke-width:2.5}
svg.lines circle{fill:var(--accent)}
'''
def qr(data='https://example.com/sample',color='#111',size=100):
    s=segno.make(data,error='m').svg_inline(scale=1,border=0,dark=color,light=None)
    # svg_inline gives fixed width/height; make responsive
    import re
    s=re.sub(r'width="\d+" height="\d+"','width="%d" height="%d"'%(size,size),s,1)
    s=s.replace('<svg ','<svg viewBox="0 0 %d %d" shape-rendering="crispEdges" '%(0,0),1)
    return s
def qr2(size=100,color='#111',data='https://example.com/sample'):
    q=segno.make(data,error='m'); n=q.symbol_size(border=0)[0]
    path=[]
    for y,row in enumerate(q.matrix):
        for x,v in enumerate(row):
            if v: path.append('M%d %dh1v1h-1z'%(x,y))
    return '<svg width="%d" height="%d" viewBox="0 0 %d %d" shape-rendering="crispEdges"><path d="%s" fill="%s"/></svg>'%(size,size,n,n,''.join(path),color)
def page(body,tag='',note='Sample layout. Names, numbers and details are made up.'):
    t='<div class="tag">%s</div>'%tag if tag else ''
    n='<div class="note">%s</div>'%note if note else ''
    return '<!doctype html><html><head><meta charset="utf-8">%s<style>%s</style></head><body>%s%s%s</body></html>'%(FONTS,CSS,t,body,n)
def render(scenes):
    """scenes: dict name->html"""
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium',args=['--no-sandbox'])
        pg=b.new_page(viewport={'width':1600,'height':900})
        for name,html in scenes.items():
            path=os.path.join(HERE,name+'.html'); open(path,'w').write(html)
            pg.goto('file://'+path); pg.wait_for_timeout(1200)
            try: pg.evaluate('document.fonts.ready')
            except: pass
            pg.screenshot(path=os.path.join(HERE,'m_'+name+'.jpg'),type='jpeg',quality=90)
            print('ok',name,flush=True)
        b.close()
def sel(argv,scenes):
    names=argv[1:] or list(scenes)
    return {n:scenes[n] for n in names}
