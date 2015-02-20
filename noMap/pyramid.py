##script pour tuiller des grosses images non geographique
##pour utiliser L.TileLayer.Zoomift.js

import os
from wand.image import Image ##API for imageMagick
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
            i = 0
            wi = 0
            hi = 0
            for h in range(0, img.height, 256):
                for w in range(0, img.width, 256):
                  w_end = w + 256
                  h_end = h + 256
                  with img[w:w_end, h:h_end] as chunk:
                      chunk.save(filename=myfilename+'tiles_{}_{}_{}.jpg'.format(z,wi,i))
                  wi += 1
                  hi += 1
                i += 1
