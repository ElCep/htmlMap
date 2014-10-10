htmlMap
=======

## Quelques outils ##
### GDAL/OGR ####
* _gdalwrap_ reprojetter des raster `gdalwarp -s_srs EPSG:2154 -t_srs EPSG:4326 Acidite2012.tiff Acidite2012_4326.tiff`
* _gdalinfo_ pour obtenir les bbox d'un raster `gdalinfo Acidite2012_4326.tiff` (note qu'il existe ogrinfo pour les vector)

## CGI , mapserver et Qgis-mapserver ##

###  la configuration de CGI ###
des p'tites modification sont à apporter à apache

`nano /etc/httpd/conf/httpd.conf`

### Le mapfile ###


### Test Mapserver ###
Dans un browser :

http://localhost/cgi-bin/mapserv?map=/var/www/html/mapfiles/cadastre/banyuls4326.map&version=1.1.0&layer=acidity-2012&requet=GetMap&template=openLayers
