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

## Sous [Debian](https://www.debian.org/index.fr.html) ##

Il est possible d'installer Mapserver sur debian depuis les packages de la distribution,
mais aussi de compiler le programme [depuis les sources](http://mapserver.org/fr/installation/unix.html)
C'est ce que nous proposons ici.


### installation depuis le repo ###

Si les dernières avancer de mapserver ne sont pas cruciale, on peut se contenter des
binaire dans les dépots. En l'occurance, le binaire dans les dépôts n'est pas fonctionnelle!

        apt-get install mapserver-bin cgi-mapserver

### Complilation depuis les sources ###

On aura besoin de quelques lib

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

#### Installer posgresql ####

Il faut ajouter un depot a debian, on trouvera [les infos là](http://www.postgresql.org/download/linux/debian/) :

        nano /etc/apt/sources.list.d/pgdg.list

Ce qui ouvre un fichier dans lequel on copie l'adresse du depot

        deb http://apt.postgresql.org/pub/repos/apt/ wheezy-pgdg main

On importe la clef public du depot et prépare les MAJ

        wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
        apt-get update

On peut maintenant installer postgresql et postgis

        apt-get install postgresql-9.3 postgresql-contrib-9.3 postgis

*Configuration du serveur de base de données*
On doit permettre aux IP du reseau de se connecter :

        nano /etc/postgresql/9.3/main/pg_hba.conf

On ajoute une ligne à la configue :

        # TYPE  DATABASE        USER            ADDRESS                 METHOD
          host    all             all          164.81.168.0/24            md5

Ce qui devrait permettre à toutes les IP 164.81.168.X de se connecter.

Il faut ensuite modifier `/etc/postgresql/9.3/main/postgresql.conf` pour permettre à postgreSQL d'écouter tout les réseau :

        listen_addresses='*'

Enfin, pour que les modifications soit prisent en compte :

        service postgresql restart

#### Configurer postgreSQL et postGIS ####

La marche a suivre est [disponible sur e trac de l'OSGeo](http://trac.osgeo.org/postgis/wiki/UsersWikiPostGIS21UbuntuPGSQL93Apt) :



#### Compiler mapServer ####

On aura besoin d'un minimum d'outils de construction

        apt-get install build-essential

Il faut télécharger les sources de mapserver qui sont disponible sur [cette page](download.osgeo.org/mapserver/mapserver-6.4.1.tar.gz)

        wget download.osgeo.org/mapserver/mapserver-6.4.1.tar.gz

On procède ensuite à l'installation

        tar -xvzf mapserver-6.4.1.tar.gz #décompression
        cd mapserver-6.4.1  
        mkdir build                      #creation d'un dossier build
        cd build/

Une fois les petits préparatifs effectué, il faut configurer l'environnement

        cmake -DCMAKE_INSTALL_PREFIX=/opt \
        -DCMAKE_PREFIX_PATH=/etc/postgresql/9.3:/etc/python2.7:/usr/bin:/usr/include:/opt \
        -DWITH_FRIBIDI=0 \
        -DWITH_CLIENT_WFS=ON \
        -DWITH_CLIENT_WMS=ON \
        -DWITH_CURL=ON \
        -DWITH_SOS=ON \
        -DWITH_PHP=OFF \
        -DWITH_PYTHON=OFF \
        -DWITH_MSSQL2008=OFF .. >../configure.out.txt

Ce qui permet de produire le makefile il ne reste plus qu'a compiler et installer

        make
        make install

On peut creer un fichier `cgi-bin` dans `/var/www/`

        mkdir /var/www/cgi-bin

avec un petit `find / -name mapserv` vous optenez :

        /opt/bin/mapserv


Il faut alors copier le binaire `/opt/bin/mapserv` dans `/var/www/cgi-bin/`

        cp /opt/bin/mapserv /var/www/cgi-bin/

### Configurer cgi ###

Il faut réorienter la configuration d'apache pour cgi

        nano /etc/apache2/sites-available/default

et intégré quelque chose comme ça en remplacant user par l'utilisateur.

        ScriptAlias /cgi-bin/ /var/www/cgi-bin/
        <Directory "/var/www/cgi-bin/">
                AllowOverride None
                Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
                Order allow,deny
                Allow from all
        </Directory>

Puis passer les site available en enable

        a2ensite

POur tester que cela fonctionne :

        http://myDomain.fr/cgi-bin/mapserv

## Le mapfile ##

Il faut que le fichier soit lisible par [apache](http://httpd.apache.org/)

        chown -R yourname:www-data mydirectory #donne les droits recursifs
        chmod -R g+s mydirectory #conservera les droits dans ce dossier pour le groupe


## Test Mapserver ##
###Dans un browser : ###

On peut tester un flux *WMS* sur la base de l'exemple :
          http://localhost/cgi-bin/mapserv?map=/var/www/html/mapfiles/cadastre/banyuls4326.map&version=1.1.0&layer=acidity-2012&requet=GetMap&template=openLayers
Ce qui à pour effet de produir une carte avec un template ol

Dans le même esprit on peut tester un flux *WFS* sur la base de

          http://164.81.15.10/cgi-bin/mapserv?map=/var/www/ms_monsatR/monastR_wfs.map&SERVICE=WFS&VERSION=1.0.0&REQUEST=GetCapabilities
ce qui à pour effet de produire un flux XML


### Dans [Qgis](http://www.qgis.org/fr/site/) ###

[Qgis](http://www.qgis.org/fr/site/) semble une manière particulièrement addapter aux tests
des mapFiles !

Il vous suffirat de passer l'URL de votre serveur locale ou distant dans les fonctions
"ajouter une couche WMS" ou "ajouter une couche WFS"selon la manière dont vous avez
construit le mapfile. Par exemple :

        http://164.81.15.10/cgi-bin/mapserv?map=/var/www/ms_monsatR/monastR_wms.map
