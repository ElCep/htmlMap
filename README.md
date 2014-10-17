htmlMap
=======

## Pense "pas bête" ##
### GDAL/OGR ####
* _gdalwrap_ reprojetter des raster `gdalwarp -s_srs EPSG:2154 -t_srs EPSG:4326 Acidite2012.tiff Acidite2012_4326.tiff`
* _gdalinfo_ pour obtenir les bbox d'un raster `gdalinfo Acidite2012_4326.tiff` (note qu'il existe ogrinfo pour les vector)

## le contenu des dossiers ##

### mapfile ###

* le [readme](mapfile/README.md)
* un [exemple](mapfile/banyuls3857.map) de mapfile sur un couche raster 

### Le dossier leaflet ###

* le [readme](howTo_leaflet/README.md)
* _[event_map.html](howTo_leaflet/event_map.html)_ Une carte qui affiche des popup
avec la latitude et la longitude
* _[loadPoints_geojson.html](howTo_leaflet/loadPoints_geojson.html)_ charge un geojson
et propose des points avec des popup sur banyuls
* _[loadPolygons_geojson.html](howTo_leaflet/loadPolygons_geojson.html)_ charge des
polygones et réalise un choroplèthe sur la ville de Limoges
* _[sandbox.html](howTo_leaflet/sandbox.html)_ le trux pour faire des essais

### Le dossier OpenLayer ###

* le [readme](howTo_ol/README.md)
* _[loadmapfile.html](howTo_ol/loadmapfile.html)_ openLayer permet de charger des données ne sont pas tuillé
au contraire de leaflet (il faut passer par un hack)
* _[sandbox.html](howTo_ol/sandbox.html)_ un truc bien crado
