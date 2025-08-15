import imageio
import os

vpath = 'sample.mp4'
output = 'Frames'
os.makedirs(output, exist_ok=True)

reader = imageio.get_reader(vpath)
print(reader)
for i,frame in enumerate(reader):
    imageio.imwrite(f"{output}/{i:05d}.jpg", frame)
    print(f"{i} Frames extracted")

