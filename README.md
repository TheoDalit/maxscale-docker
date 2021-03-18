# MariaDB MaxScale Docker image

This Docker image runs the latest 2.4 version of MariaDB MaxScale.

-	[Travis CI:  
	![build status badge](https://img.shields.io/travis/mariadb-corporation/maxscale-docker/master.svg)](https://travis-ci.org/mariadb-corporation/maxscale-docker/branches)


## Building

Run the following command in this directory to build the image.

```
make build-image
```

## Running
Start the docker 

```
docker-compose up -d
```

Once it is up and running connect to MariaDB

```
mariadb -umaxuser -pmaxpwd -h 127.0.0.1 -P 4000
```

Databases `zipcodes_one` and `zipcodes_two` will be created. You can confirm the databases are created with `show databases;`.

```
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| zipcodes_one       |
| zipcodes_two       |
+--------------------+
5 rows in set (0.001 sec)
```

Quit MariDB by typing `quit;`.

## Querying the database with the python script

Run the query python script

```
./query.py
```

Results

```

```
