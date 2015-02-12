# Mise en place d'un visualiseur javaScript
L'idée ici est d'utiliser une librairie javascript pour visualiser des images
des images qui ne sont pas des cartes.

## Tuiler une image non georeferencer
Pour cela on peut utiliser [imagemagick](http://www.imagemagick.org/)
qui va tuiller l'image de départ. Grace à imagemagick on pourra utiliser
la commande `convert` de la manière suivante :

     convert -crop 256x256 +repage big_image.png tiles_%d.png

Ce qui va produire des images de 256x256 pixels dans le dossier
dans lequel on travail

## renomer les tuilles

On pourra utiliser les comande en [ruby](https://www.ruby-lang.org/fr/) pour renomer les
tuile de la manière attendu par leaflet

    tile_width = 256
    tile_height = 256
    image_width = 1024
    image_height = 6144
    n = 0
    # To get this number, look at the number of tiles
    # generated, find the last tile number and add 1
    # e.g. tiles_99.png => total_tiles = 100
    total_tiles = 100

    tiles_per_column = image_width/tile_width

    row = 0
    column = 0
    (n...total_tiles).each do |i|
      filename = "tiles_#{i}.png" # current filename
      target = "map_#{column}_#{row}.png" # new filename

      puts "copy #{filename} to #{target}"

      `cp -f #{filename} #{target}` # rename

      # work out next step
      column = column + 1
      if column >= tiles_per_column
        column = 0
        row = row + 1
      end
    end

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
