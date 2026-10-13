#!/usr/bin/env python3
"""Đưa ảnh mockup lên host tạm (uguu.se) để `upload_media` của WordPress MCP tải về.

    python3 upload_staging.py <thư_mục_chứa_jpg> <tên1> <tên2> ...      (đọc <thư_mục>/<tên>.jpg)

In URL từng ảnh và lưu vào <thư_mục>/urls_mock.json. URL uguu hết hạn sau vài giờ, nên gọi
`upload_media` ngay sau bước này. Dùng lại hàm upload của wordpress-mcp/scripts/gen_article_images.py.
"""
import sys,json,os,importlib.util
HERE=os.path.dirname(os.path.abspath(__file__))
spec=importlib.util.spec_from_file_location('g',os.path.join(HERE,'..','..','..','scripts','gen_article_images.py'))
g=importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
d=sys.argv[1]; out_path=os.path.join(d,'urls_mock.json')
out=json.load(open(out_path)) if os.path.exists(out_path) else {}
for n in sys.argv[2:]:
    if n in out: continue
    out[n]=g.upload_uguu(open(os.path.join(d,n+'.jpg'),'rb').read()); print(n,out[n],flush=True)
    json.dump(out,open(out_path,'w'),indent=1)
