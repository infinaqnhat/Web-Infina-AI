import sys, os, segno
from playwright.sync_api import sync_playwright
HERE=os.path.dirname(os.path.abspath(__file__))
PHOTOS=os.path.join(HERE,'..','assets','photos')
OUT=os.environ.get('MOCKUP_OUT') or os.getcwd()   # nơi ghi .html và .jpg; đặt MOCKUP_OUT=thư mục tạm, KHÔNG ghi vào repo
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
def qr2(size=100,color='#111',data='https://example.com/sample'):
    q=segno.make(data,error='m'); n=q.symbol_size(border=0)[0]
    path=[]
    for y,row in enumerate(q.matrix):
        for x,v in enumerate(row):
            if v: path.append('M%d %dh1v1h-1z'%(x,y))
    return '<svg width="%d" height="%d" viewBox="0 0 %d %d" shape-rendering="crispEdges"><path d="%s" fill="%s"/></svg>'%(size,size,n,n,''.join(path),color)
def page(body,tag='',note='Sample layout. Names, numbers and details are made up.',size=(1600,900)):
    t='<div class="tag">%s</div>'%tag if tag else ''
    n='<div class="note">%s</div>'%note if note else ''
    css=CSS.replace('body{width:1600px;height:900px;','body{width:%dpx;height:%dpx;'%size).replace('svg.lines{position:absolute;left:0;top:0;width:1600px;height:900px','svg.lines{position:absolute;left:0;top:0;width:%dpx;height:%dpx'%size)
    return '<!doctype html><html data-w="%d" data-h="%d"><head><meta charset="utf-8">%s<style>%s</style></head><body>%s%s%s</body></html>'%(size[0],size[1],FONTS,css,t,body,n)
PHONE_W=float(os.environ.get('MOCKUP_PHONE_W','340'))  # chiều rộng ảnh hiển thị trên điện thoại (CSS px), ví dụ 340 trong cột bài viết
MIN_PHONE_PX=float(os.environ.get('MOCKUP_MIN_PHONE_PX','12'))
_JS_TEXT="""()=>{const out=[];const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n;const seen=new Set();
while(n=w.nextNode()){const t=n.textContent.trim();if(!t)continue;const e=n.parentElement;if(!e||seen.has(e))continue;seen.add(e);
if(e.closest('.tag,.note'))continue;const cs=getComputedStyle(e);if(cs.visibility==='hidden'||cs.display==='none')continue;
const r=e.getBoundingClientRect();if(r.width<2||r.height<2)continue;out.push([parseFloat(cs.fontSize),t.length])}return out}"""
def mobile_report(pg,canvas_w=1600):
    """Cỡ chữ nhỏ nhất quy ra điện thoại. Ảnh 1600px hiển thị ở PHONE_W px => hệ số PHONE_W/1600."""
    items=pg.evaluate(_JS_TEXT); k=PHONE_W/float(canvas_w)
    if not items: return ''
    mn=min(i[0] for i in items); tot=sum(i[1] for i in items)
    small=sum(i[1] for i in items if i[0]*k<MIN_PHONE_PX)
    flag='OK' if small==0 else 'TOO SMALL'
    return '| phone min %.1fpx, %d%% of chars under %dpx on phone | %s'%(mn*k,round(100*small/max(tot,1)),MIN_PHONE_PX,flag)
def render(scenes):
    """scenes: dict name->html. Ghi m_<name>.jpg (1600x900) vào OUT, kèm ảnh nền ph_*.jpg."""
    import shutil,glob
    os.makedirs(OUT,exist_ok=True)
    for f in glob.glob(os.path.join(PHOTOS,'ph_*.jpg')):
        d=os.path.join(OUT,os.path.basename(f))
        if not os.path.exists(d): shutil.copy(f,d)
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium',args=['--no-sandbox'])
        pg=b.new_page(viewport={'width':1600,'height':900})
        import re as _re
        for name,html in scenes.items():
            path=os.path.join(OUT,name+'.html'); open(path,'w').write(html)
            m=_re.search(r'data-w="(\d+)" data-h="(\d+)"',html); cw,ch=(int(m.group(1)),int(m.group(2))) if m else (1600,900)
            pg.set_viewport_size({'width':cw,'height':ch})
            pg.goto('file://'+path); pg.wait_for_timeout(1200)
            try: pg.evaluate('document.fonts.ready')
            except: pass
            pg.screenshot(path=os.path.join(OUT,'m_'+name+'.jpg'),type='jpeg',quality=90)
            print('ok',name,mobile_report(pg,cw),flush=True)
        b.close()
def sel(argv,scenes):
    names=argv[1:] or list(scenes)
    return {n:scenes[n] for n in names}

# ---- helper UI blocks (dùng chung cho các cảnh) ----
def browser(x,y,w,h,url,inner,title_bar=True):
    """Khung trình duyệt giả. inner là HTML đặt bên dưới thanh địa chỉ (cao 48px)."""
    return ('<div class="abs sh" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:14px;background:#fff;overflow:hidden">'%(x,y,w,h)
      +'<div style="height:48px;background:#e9edf3;display:flex;align-items:center;gap:8px;padding:0 18px"><i style="width:12px;height:12px;border-radius:50%;background:#f87171"></i><i style="width:12px;height:12px;border-radius:50%;background:#fbbf24"></i><i style="width:12px;height:12px;border-radius:50%;background:#34d399"></i>'
      +'<div style="margin-left:18px;background:#fff;border-radius:6px;padding:5px 16px;font-size:15px;color:#667085;width:520px">'+url+'</div></div>'
      +inner+'</div>')
def callout(n,txt,x,y,w=330):
    return '<div class="call" style="left:%dpx;top:%dpx;width:%dpx"><b>%d</b><span>%s</span></div>'%(x,y,w,n,txt)
def leaders(items):
    """items: [(x1,y1,x2,y2)] đường kẻ cam, chấm ở đầu (x2,y2)."""
    s='<svg class="lines">'
    for x1,y1,x2,y2 in items: s+='<line x1="%d" y1="%d" x2="%d" y2="%d"/><circle cx="%d" cy="%d" r="6"/>'%(x1,y1,x2,y2,x2,y2)
    return s+'</svg>'
STARS='<span style="color:#e0a21b;letter-spacing:2px">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'
def photo(name,x,y,w,h,r=6):
    return '<div class="photo abs" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:%dpx;background-image:url(%s.jpg)"></div>'%(x,y,w,h,r,name)
