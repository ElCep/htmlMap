htmlMap
=======

## Pense "pas bête" ##
### GDAL/OGR ####
* _gdalwrap_ reprojetter des raster `gdalwarp -s_srs EPSG:2154 -t_srs EPSG:4326 Acidite2012.tiff Acidite2012_4326.tiff`
* _gdalinfo_ pour obtenir les bbox d'un raster `gdalinfo Acidite2012_4326.tiff` (note qu'il existe ogrinfo pour les vector)

## le contenu des dossiers ##

### mapfile ###

* le [readme](mapfile/README.md) qui contient les information pour compiler et configurer
mapserver sur debian
* un [exemple](mapfile/banyuls3857.map) de mapfile sur un couche raster
produisant un WMF avec interprétation des couleurs par le serveur
* un autre [exemple](mapfile/monasteres_wfs.map) qui permet de servir
les données d'un base mySQL en geoJson sous forme d'un flux WFS.
* Les autres fichiers ont permis de faire les testes

### Le dossier leaflet ###

* le [readme](howTo_leaflet/README.md)
* _[event_map.html](howTo_leaflet/event_map.html)_ Une carte qui affiche des popup
avec la latitude et la longitude
* _[loadPoints_geojson.html](howTo_leaflet/loadPoints_geojson.html)_ charge un geojson
et propose des points avec des popup sur banyuls
* _[loadPolygons_geojson.html](howTo_leaflet/loadPolygons_geojson.html)_ charge des
polygones et réalise un choroplèthe sur la ville de Limoges
* _[sandbox.html](howTo_leaflet/sandbox.html)_ le trux pour faire des essais
* _[leaflet_geojson_mapserver.html](howTo_leaflet/leaflet_geojson_mapserver.html)_
permet de récupérer le flux WFS produit par mapserver pour l'exposer.


### Le dossier OpenLayer ###
Nous avons exploré la librairies [OL3](http://openlayers.org/) qui est encore en dev et assez peut documenté
Ici quelques exemple d'utilisation avec mapserver. A noté qu'il faut modifier l'url du webservice
* le [readme](howTo_ol/README.md) qui contient surtout des ressources internet
* _[loadmapfile.html](howTo_ol/loadmapfile.html)_ openLayer permet de charger des données ne sont pas tuillé
au contraire de leaflet (ou il faut passer par un hack)
* _[mapbox_wfs_highlight.html](howTo_ol/mapbox_wfs_highlight)_ qui charge le geoJson
de mapserver et affiche des points et les surligne en rouge  en affichant un attribut
 du geoJson
* _[mapbox_wfs_popinid.html](howTo_ol/mapbox_wfs_popinid.html)_ affiche les
wfs sous forme de geoJson et ouvre un div avec l'atribut du points sous la carte
* _[mapbox_wfs_popinFloat.html](howTo_ol/mapbox_wfs_popinFloat.html)_ affiche un popin sur la position
du  point
* _[sandbox.html](howTo_ol/sandbox.html)_ un truc bien crado

### Le dossier mysql ###
On y retroue un [readme](mysql/readme.md) qui fait le point sur la configuration
de mysql pour pouvoir être attaqué par mapserver.

### Le dossier noMap ###
Il contient quelques teste d'utilisation de leaflet pour afficher des images non
géographique.
* le [readme](noMap/README.md) avec des petites notes
* [pyramid.py](noMap/pyramid.py) est un script python qui effectue le tuilage
des images non géographique. l'idée est de s'abstraire de zoomify (plugin de photoshop)
* [leaflet_no_map.html](noMap/leaflet_no_map.html) charge une image non tuilé
* [leaflet_no_map_tiled.html](noMap/leaflet_no_map_tiled.html) pour charger une image tuiler
* [L.TileLayer.Zoomify.js](noMap/L.TileLayer.Zoomify.js) est le plugin proposer par
[Bjørn Sandvik](http://blog.thematicmapping.org/)  sur son [github](https://github.com/turban/Leaflet.Zoomify)


## Des ressources en vrac ##
* un esemble de [wms très chouette](http://homepage.ntlworld.com/keir.clarke/leaflet/leafletlayers.htm) qui peuvent servire
de fond.
* un convertisseur universel de système de coord http://twcc.fr/
