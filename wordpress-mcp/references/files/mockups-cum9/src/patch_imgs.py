import re,sys,json
def fig(url,alt,caption=None):
    alt=alt.replace('"','&quot;')
    cap='<figcaption class="wp-element-caption">%s</figcaption>'%caption if caption else ''
    return '<figure class="wp-block-image aligncenter"><img decoding="async" src="%s" alt="%s" />%s</figure>'%(url,alt,cap)
FIG=re.compile(r'<figure class="wp-block-image[^>]*>.*?</figure>',re.S)
def remove_fig(s,alt_sub):
    ms=[m for m in FIG.finditer(s) if alt_sub in m.group(0)]
    assert len(ms)==1,(alt_sub,len(ms))
    m=ms[0]; 
    # remove with trailing newline
    end=m.end()+(1 if s[m.end():m.end()+1]=='\n' else 0)
    return s[:m.start()]+s[end:]
def replace_fig(s,alt_sub,new):
    ms=[m for m in FIG.finditer(s) if alt_sub in m.group(0)]
    assert len(ms)==1,(alt_sub,len(ms)); m=ms[0]
    return s[:m.start()]+new+s[m.end():]
def insert_after(s,anchor,new):
    assert s.count(anchor)==1,(anchor[:50],s.count(anchor))
    i=s.index(anchor)+len(anchor)
    return s[:i]+'\n'+new+s[i:]
def insert_before(s,anchor,new):
    assert s.count(anchor)==1,(anchor[:50],s.count(anchor))
    i=s.index(anchor)
    return s[:i]+new+'\n'+s[i:]
def textonly(s):
    s=FIG.sub('',s); return re.sub(r'\s+','',re.sub(r'<[^>]+>','',s))
def links(s): return sorted(re.findall(r'href="([^"]+)"',s))
