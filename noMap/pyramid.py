##script pour tuiller des grosses images non geographique
##pour utiliser L.TileLayer.Zoomift.js


import wand ##API for imageMagick
import os
from wand.image import Image
from wand.display import display


os.chdir("/home/delaye/github/htmlMap/noMap/")
with Image(filename='orig/barbe.jpg') as img:
    print img.size
    iSize = img.size
    for z in "1", "2", "3", "4", "5", "6":
        myfilename = "out/"+z+"/"
        print myfilename
        dir = os.path.dirname(myfilename)
        if not os.path.exists(dir):
          os.makedirs(dir)
        with img.clone() as iclone:
          cloneSize = str(int(z)*10)+"%"
          iclone.transform(resize=cloneSize)
          iclone.transform("256x256")
          iclone.save(filename=myfilename+'mona-lisa-'+z+'-{0}.png'.format(z))
