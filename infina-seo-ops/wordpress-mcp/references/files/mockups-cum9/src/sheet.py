import sys
from PIL import Image
names=sys.argv[2:]; out=sys.argv[1]
W=800;H=450
cols=2; rows=(len(names)+1)//2
s=Image.new('RGB',(cols*W,rows*H),(60,60,60))
for i,n in enumerate(names): s.paste(Image.open('m_'+n+'.jpg').resize((W,H)),((i%cols)*W,(i//cols)*H))
s.save(out,quality=88)
