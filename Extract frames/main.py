from PIL import Image
im = Image.open('base.gif')

x = 1

print("Number of frames: "+str(im.n_frames)) # QUANTIDADE DE FRAMES 

for i in range(5):
    im.seek(x)
    im.save('frame{0}.png'.format(x))
    x = x + 1