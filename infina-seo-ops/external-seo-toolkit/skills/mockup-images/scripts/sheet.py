#!/usr/bin/env python3
"""Ghép contact sheet 2 cột để xem nhanh nhiều ảnh: python3 sheet.py out.jpg <tên1> <tên2> ... (đọc m_<tên>.jpg trong thư mục hiện tại)"""
import sys
from PIL import Image
names=sys.argv[2:]; out=sys.argv[1]
W=800;H=450
cols=2; rows=(len(names)+1)//2
s=Image.new('RGB',(cols*W,rows*H),(60,60,60))
for i,n in enumerate(names): s.paste(Image.open('m_'+n+'.jpg').resize((W,H)),((i%cols)*W,(i//cols)*H))
s.save(out,quality=88)
