#!/usr/bin/env python3
"""Chèn ảnh mockup vào nội dung bài.   python3 apply_mockups.py <spec.json> <post_id> <in.html> <out.html>

Đọc spec.json (đường dẫn truyền vào; mẫu: references/spec-example.json). Với mỗi bài: xóa figure có alt chứa chuỗi trong "remove", thay figure
có alt chứa chuỗi trong "replace" bằng ảnh mới, chèn ảnh mới ngay TRƯỚC thẻ <h2> có tiêu đề trong
"before_h2". Kiểm tra: chữ (bỏ figure) và danh sách href không đổi so với bản vào.
Không dùng -I vì import patch_imgs ở src/.
"""
import json,os,re,sys
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
from patch_imgs import fig,replace_fig,remove_fig,textonly,links,FIG
specf,pid,fin,fout=sys.argv[1:5]
spec=json.load(open(specf))
p=spec['posts'][pid]; M=spec['media']
s=open(fin).read(); o=s
F=lambda k: fig(*M[k])
for a in p.get('remove',[]): s=remove_fig(s,a)
for a,k in p.get('replace',[]): s=replace_fig(s,a,F(k))
for h,k in p.get('before_h2',[]):
    m=re.findall(r'<h2[^>]*>%s</h2>'%re.escape(h),s); assert len(m)==1,(h,len(m))
    i=s.index(m[0]); s=s[:i]+F(k)+'\n'+s[i:]
assert textonly(s)==textonly(o),'text changed'
assert links(s)==links(o),'links changed'
n=len(FIG.findall(s)); print('figures before/after:',len(FIG.findall(o)),n)
open(fout,'w').write(s)
