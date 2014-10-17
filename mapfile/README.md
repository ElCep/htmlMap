HOWTO mapfile
=============

Ce dossier contient un exemple de mapfile, le fichier de base nécessaire à la configuration
d'une solution de cartographie avec [mapserver](http://mapserver.org/fr/)

## Sous [Fedora](http://www.fedora-fr.org/) ##

Il faudra disposer d'un serveur [apache](http://httpd.apache.org/) correctement configuré,
Ce qui est le cas sur la plus part des saveurs de cette distribution. Celle utilisé pour
cette exemple est [scientifique fedora](https://spins.fedoraproject.org/fr/scientific-kde/)

Si le serveur est installé, il faut le lancer avec :

        sudo systemctl start httpd.service

<!-- Je ne suis pas sur qu'il y en ait besoin
##les mode
getenforce
setenforce Permissive -->

##l'install mapserver sur fedora ##

Un certain nombre de packages sont [recommandé](http://mapserver.org/fr/installation/unix.html)
pour l'installation de mapserver :

        sudo yum gdal gdal-devel  geos geos-devel libtiff libtiff-devel
        libgeotiff libgeotiff-devel libpng12-devel libjpeg-turbo libjpeg-turbo-devel
        curl-devel httpd-devel fcgi spawn-fcgi php php-devel
        php-mysql php-pecl-memcache php-pgsql freetype libpng libjpeg proj libcurl

Vous pouvez ensuite utiliser le packages proposer par la distribution  :

        sudo yum install mapserver

Mais vous pouvez aussi le complier depuis les [sources](http://mapserver.org/fr/download.html).

## utilisation ##

Si vous avez installé le package de la distribution [vous trouverez mapserver là](http://lists.osgeo.org/pipermail/mapserver-users/2014-July/076712.html) :

        /usr/libexec/mapserver

Il vous faudra copier l'executable dans le fichier cgi créer à l'installation de `fcgi` :

        /var/www/cgi-bin/

Et le renomer en mapserv

        sudo cp /usr/libexec/mapserver /var/www/cgi-bin/
        sudo mv /var/www/cgi-bin/mapserver /var/www/cgi-bin/mapserv
