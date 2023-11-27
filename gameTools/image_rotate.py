import os

from PIL import Image

dirWithFiles="./pliki"

dirfiles = os.listdir(dirWithFiles)

for dir in dirfiles:
    print(dirWithFiles + "/" + dir)
    nameOfFile = dirWithFiles + "/" + dir

    name = nameOfFile.split(".")
    nameok = name[1]
    im = Image.open(nameOfFile)

    for i in range(1, 360):
        im_rotate = im.rotate(i)
        im_rotate.save('./Wszystko' + str(nameok) + str(i) + '.png', quality=95)

    im.close()