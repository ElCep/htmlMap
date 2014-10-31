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

### utilisation ###

Si vous avez installé le package de la distribution [vous trouverez mapserver là](http://lists.osgeo.org/pipermail/mapserver-users/2014-July/076712.html) :

        /usr/libexec/mapserver

Il vous faudra copier l'executable dans le fichier cgi créer à l'installation de `fcgi` :

        /var/www/cgi-bin/

Et le renomer en mapserv

        sudo cp /usr/libexec/mapserver /var/www/cgi-bin/
        sudo mv /var/www/cgi-bin/mapserver /var/www/cgi-bin/mapserv

###  la configuration de CGI ###
des p'tites modification sont à apporter à apache

`nano /etc/httpd/conf/httpd.conf`

  <Directory "/var/www/cgi-bin">
    SetHandler fcgid-script
    Options +ExecCGI

    # Customize the next two directives for your requirements.
    Order allow,deny
    Allow from all
  </Directory>

## Sous debian ##

Il est possible d'installer Mapserver sur debian depuis les packages de la distribution,
mais aussi de compiler le programme [depuis les sources](http://mapserver.org/fr/installation/unix.html)
C'est ce que nous proposons ici.

### compilation depuis les sources ###
En nous raportant à la [page dediée](http://mapserver.org/fr/installation/unix.html#compiling),
 nous constatons qu'il y a quelques dépendences à satisfaire pour pouvoir compiler mapserver.

        #verifier les MAJ
        apt-get update && apt-get upgrade
        #installer un serveur web et cgi
        apt-get install apache2 libfcgi-dev php5-cgi
        #ajouter cgi a apache2
        a2enmod cgi
        #dependences de developpement
        apt-get install gcc gpp g++ libc-dev make automake autoconf flex bison perl libreadline5 libreadline-gplv2-dev
        #dependences mapserver
        apt-get install libjpeg8 libjpeg-dev libjpeg-dev libpng12-0 libpng12-dev libfreetype6 libfreetype6-dev proj-bin libcurl4-gnutls-dev fontconfig libtiff4 libtiff4-dev libxpm4 libcairo2-dev libgd-tools
        #install de geos
        apt-get install libgeos-c1 libgeos-dev
        #install proj4
        apt-get install libproj0 libproj-dev
        #install geotiff
        apt-get install geotiff-bin
        #install gdal
        apt-get install gdal-bin libgdal-dev
        #install postgreSQL (9.1) et postGIS (1.5)
        apt-get install postgresql postgis

On peut ensuite télécharger les sources :

        wget

### installation depuis le repo ###

Si les dernières avancer de mapserver ne sont pas cruciale, on peut se contenter des
binaire dans les dépots

        apt-get install mapserver-bin cgi-mapserver

### Configurer cgi ###

En suivant la [routine proposé par debian](https://wiki.debian.org/fr/Lamp)
 pour l'installation d'apache j'ai créé un dossier /home/flsh/public_html qui
 contiendra les sites et un dossier cgi-bin

Il faut donc réorienter la configuration d'apache pour cgi 

        nano /etc/apache2/sites-available/default

et intégré quelque chose comme ça en remplacant user par l'utilisateur.

        ScriptAlias /cgi-bin/ /home/user/public_html/cgi-bin/
        <Directory "/home/flsh/public_html/cgi-bin/">
                AllowOverride None
                Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
                Order allow,deny
                Allow from all
        </Directory>

POur tester que cela fonctionne :

        http://myDomain.fr/cgi-bin/mapserv

## Le mapfile ##

## Test Mapserver ##
Dans un browser :

http://localhost/cgi-bin/mapserv?map=/var/www/html/mapfiles/cadastre/banyuls4326.map&version=1.1.0&layer=acidity-2012&requet=GetMap&template=openLayers
