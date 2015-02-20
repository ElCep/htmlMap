# Mise en place d'un visualiseur javaScript
L'idée ici est d'utiliser une librairie javascript pour visualiser des images
des images qui ne sont pas des cartes.

## Tuiler une image non georeferencer
Pour cela on peut utiliser [imagemagick](http://www.imagemagick.org/)
combiné avec [python](https://www.python.org/).

On aura besoin de quelques librairies en plus d'`imageMagick` et `ImageMagick-devel`

    sudo pip install wand

On pourra piramider des images avec  le petit script python que j'ai préparer :
[pyramid.py](pyramid.py)

## tuiller avec leaflet
deux possibilitée s'offre à nous : utiliser des images tuillé ou non

 * pour utiliser des images tuillé on pourra se reporter a cette
 [exemple](leaflet_no_map.html)

 * pour utilisé des images tuillé grace à imagemagick on pourra
 se reporté a cet [exemple là](leaflet_no_map_tilled.html)


## resosurce :
 * comment tuiller une images [geotribu](http://www.geotribu.net/node/697)
 mais nécessite une image georef

 * Pour une image non tuiller et non géo on peut se raporter a [cet article](http://kempe.net/blog/2014/06/14/leaflet-pan-zoom-image.html)

 * Pour des images non géographique tuiller on peut se rapporter à [cet article de blog](http://omarriott.com/aux/leaflet-js-non-geographical-imagery/)
