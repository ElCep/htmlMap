HOWTO mapfile
=============

Ce dossier contient un exemple de mapfile, le fichier de base nécessaire à la configuration
d'une solution de cartographie avec [mapserver](http://mapserver.org/fr/)

## Sous [Fedora](http://www.fedora-fr.org/) ##
Il faudra disposer d'un serveur [apache](http://httpd.apache.org/) correctement configuré,
Ce qui est le cas sur la plus part des saveurs de cette distribution. Celle utilisé pour
cette exemple est [scientifique fedora](https://spins.fedoraproject.org/fr/scientific-kde/)

Si le serveur est installé,  
        sudo systemctl start httpd.service

permet de lancer le serveur
<!-- Je ne suis pas sur qu'il y en ait besoin
##les mode
getenforce
setenforce Permissive -->

##l'install mapserver sur fedora
          sudo yum gdal gdal-devel  geos geos-devel libtiff libtiff-devel libgeotiff libgeotiff-devel libpng12-devel libjpeg-turbo libjpeg-turbo-devel curl-devel httpd-devel fcgi spawn-fcgi php php-devel php-mysql php-pecl-memcache php-pgsql

sudo yum install freetype libpng libjpeg proj libcurl mapserver
