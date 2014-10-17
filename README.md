htmlMap
=======

## Pense "pas bête" ##
### GDAL/OGR ####
* _gdalwrap_ reprojetter des raster `gdalwarp -s_srs EPSG:2154 -t_srs EPSG:4326 Acidite2012.tiff Acidite2012_4326.tiff`
* _gdalinfo_ pour obtenir les bbox d'un raster `gdalinfo Acidite2012_4326.tiff` (note qu'il existe ogrinfo pour les vector)

## le contenu des dossiers ##

### Le dossier leaflet ###

* [event_map.html](howTo_leaflet/event_map.html) 
