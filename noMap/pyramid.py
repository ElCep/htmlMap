##script pour tuiller des grosses images non geographique
##pour utiliser L.TileLayer.Zoomift.js

import os
from wand.image import Image ##API for imageMagick
#from wand.display import display




os.chdir("/home/delaye/github/htmlMap/noMap/")
with Image(filename='orig/barbe.jpg') as img:
    print img.size
    iSize = img.size
    imgW = iSize[0]
    imgH = iSize[1]
    #for tsi in range(256,imgW,256):
     #   ts = imgW - tsi
     #  z = 1
    tileSize = 500
    nbTiles = (imgW/tileSize) * (imgH/tileSize)
    print nbTiles
    myfilename = "out/"
    dir = os.path.dirname(myfilename)
    if not os.path.exists(dir):
        os.makedirs(dir)
    row = 1
    column = 1
    for i in range(1, nbTiles,1):
        with img[((column-1)*tileSize):(column*tileSize), ((row-1)*tileSize):(row*tileSize)] as chunk:
            chunk.save(filename='{}tile_{}_{}.jpg'.format(myfilename,column,row))
        column += 1
        print column
        if(column >= imgW/tileSize):
            column = 1
            row += 1
        #z += 1
