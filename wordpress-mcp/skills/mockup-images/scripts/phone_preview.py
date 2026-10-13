#!/usr/bin/env python3
"""Mô phỏng ảnh trong bài trên điện thoại (cột 360 CSS px, DPR 2) để kiểm chữ có đọc được không.

    python3 phone_preview.py out.jpg anh1.jpg [anh2.jpg ...]   (các ảnh đặt cạnh nhau, mỗi ảnh một khung điện thoại)

Đoạn chữ thường 16px nằm trên và dưới ảnh làm thước đo: chữ trong ảnh nhỏ hơn đoạn chữ đó nhiều thì chưa đạt.
"""
import sys,os,base64
from playwright.sync_api import sync_playwright
out=sys.argv[1]; imgs=sys.argv[2:]
def frame(p):
    b=base64.b64encode(open(p,'rb').read()).decode()
    return ('<div class="ph"><p>Time is also a budget. A channel that costs nothing but ten hours a week is expensive for an agent who also has to show homes.</p>'
      '<img src="data:image/jpeg;base64,%s"><p>This paragraph is 16px, the size most readers find comfortable. Text inside the picture above should not be much smaller than this.</p></div>'%b)
html=('<html><body style="margin:0;background:#cfd6e4;display:flex;gap:24px;padding:24px;font-family:Inter,Arial,sans-serif">'
 '<style>.ph{width:360px;background:#fff;padding:0 10px;box-sizing:border-box;border-radius:12px}.ph p{font-size:16px;line-height:1.6;color:#344054;margin:16px 0}.ph img{width:100%;display:block;border-radius:8px}</style>'
 +''.join(frame(i) for i in imgs)+'</body></html>')
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':len(imgs)*384+24,'height':900},device_scale_factor=2)
    pg.set_content(html); pg.wait_for_timeout(500)
    pg.screenshot(path=out,type='jpeg',quality=90,full_page=True); b.close()
print('saved',out)
