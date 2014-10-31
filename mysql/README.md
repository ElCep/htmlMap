Pense pas bête mySql
====================

Pour donner l'accès depuis l'exterieur via une IP

        # mysql -u root -p
        mysql> GRANT ALL ON fooDatabase.* TO fooUser@'1.2.3.4' IDENTIFIED BY 'my_password';

POur tester l'accès a distance :

        mysql> GRANT ALL ON fooDatabase.* TO fooUser@'1.2.3.4' IDENTIFIED BY 'my_password';

source : [(http://www.rackspace.com/knowledge_center/article/mysql-connect-to-your-database-remotely)]

## mySQL et l'espace ##

Depuis sa version 4 mySql suporte quelques fonctions spatiales.


### creer une geom a partir d'un WKT###
MySQL peut embarquer des données spatiales. Imaginons que nos données sont dans
une base tests, et que la table qui nous intéresse s'appelle villes2.

        ALTER TABLE  tests.villes2 ADD  geom GEOMETRY NOT NULL; #construction du col GEOMETRY
        UPDATE tests.villes2 SET geom=GeomFromText(wkt_geom,'WGS84'); #copie des données de la col kht_geom dans geom

## Sources ##
* [importer des données depuis Qgis](http://dogeo.fr/index.php/web-carto/17-importer-une-couche-spatiale-dans-mysql)
