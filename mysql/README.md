Pense pas bête mySql
====================

Pour donner l'accès depuis l'exterieur via une IP

        # mysql -u root -p
Donner tous les accès

        mysql> GRANT ALL ON fooDatabase.* TO fooUser@'1.2.3.4' IDENTIFIED BY 'my_password';

Ou donner l'accès seulement en lecture

        mysql> GRANT SELECT, SHOW DATABASE ON fooDatabase.* TO fooUser@'1.2.3.4' IDENTIFIED BY 'my_password';
Pour tester l'accès a distance via mySQl:

        # mysql -u fooUser -p -h 44.55.66.77 database_name

source : http://www.rackspace.com/knowledge_center/article/mysql-connect-to-your-database-remotely

> ATTENTION ; il faudra bien donner les droits à chaque creations de base de données!

## mySQL et l'espace ##

Depuis sa version 4 mySql suporte quelques fonctions spatiales.

### Si vous avez dejà une tables spatiale ###

On peut utiliser gdal/ogr pour tester les connections au serveur

        #ogrinfo MYSQL:tests,host=164.81.15.10,port=3306,user=Foouser,password=p4ssw0rD

Si tout fonctionne on doit obtenir

        INFO: Open of `MYSQL:tests,host=164.81.15.10,port=3306,user=Foouser,password=p4ssw0rD'
        using driver `MySQL' successful.
        1: blablbla (None)
        2: villes
        3: villes2

On peut ensuite optenir des infos utilise à la configuration du mapFile avec

        #ogrinfo MYSQL:tests,host=164.81.15.10,port=3306,user=Foouser,password=p4ssw0rD villes -summary

Qui renvois :

        INFO: Open of `MYSQL:tests,host=164.81.15.10,port=3306,user=Foouser,password=p4ssw0rD'
        using driver `MySQL' successful.

        Layer name: villes
        Geometry: Unknown (any)
        Feature Count: 747
        Extent: (0.689483, 44.929308) - (2.562495, 46.421369)
        Layer SRS WKT:
        (unknown)
        FID Column = id
        Geometry Column = geom
        wkt_geom: String (47.0)


### Table spatiale : creer une geom a partir d'un WKT###
MySQL peut embarquer des données spatiales. Imaginons que nos données sont dans
une base tests, et que la table qui nous intéresse s'appelle villes2.

        ALTER TABLE  tests.villes2 ADD  geom GEOMETRY NOT NULL; #construction du col GEOMETRY
        UPDATE tests.villes2 SET geom=GeomFromText(wkt_geom,3857); #copie des données de la col kht_geom dans geom

On peut spécifier que ce sont des pts

        ALTER TABLE  monastR.villes ADD  geom GEOMETRY NOT NULL;# 747 lignes affectées.
        UPDATE monastR.villes SET geom=PointFromText(wkt_geom,900913);# 747 lignes affectées.

## Sources ##
* [importer des données depuis Qgis](http://dogeo.fr/index.php/web-carto/17-importer-une-couche-spatiale-dans-mysql)
* [connection mySql et mapServer](http://mapserver.org/fr/input/vector/mysql.html#mysql)
