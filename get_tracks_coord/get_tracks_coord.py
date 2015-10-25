from PIL import Image

'''
I created a png image of path for train to move.
This script finds pixels from image and puts it into 
list for Train.coord.
In addition I added correction -30 to x and -130 to y
and also a some coords ( last for loop) because without train
couldn't get off display'''

img = Image.open('tracks.png')

f = open('train_coord', 'w')

a = []
for j in reversed(range(img.size[1])):
	for i in reversed(range(img.size[0])):
		if img.getpixel((i,j))[0]!=255:
			a.append([i - 30,j -130])

min = 99999
b = []
for i in range(len(a)):
	if a[i][0] < min:
		b.append(a[i])
		min = a[i][0]	


p = a[-1][0] - 1
r = a[-1][1] - 1

for i in range(0,40):
	b.append([p,r])
	p -= 1
	r -= 1

for r in b:
	f.write(str(r) + ',\n')
	


