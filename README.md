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


## Querying the database

This will query zipcodes_one and output the last 10 rows

```
SELECT * FROM zipcodes_one.zipcodes_one LIMIT 9990,10;
```

```
+---------+-------------+----------------+-------+--------------+-----------+------------+-------------------------+---------------+-----------------+---------------------+------------+
| Zipcode | ZipCodeType | City           | State | LocationType | Coord_Lat | Coord_Long | Location                | Decommisioned | TaxReturnsFiled | EstimatedPopulation | TotalWages |
+---------+-------------+----------------+-------+--------------+-----------+------------+-------------------------+---------------+-----------------+---------------------+------------+
|   40843 | STANDARD    | HOLMES MILL    | KY    | PRIMARY      | 36.86     | -83        | NA-US-KY-HOLMES MILL    | FALSE         |                 |                     |            |
|   41425 | STANDARD    | EZEL           | KY    | PRIMARY      | 37.89     | -83.44     | NA-US-KY-EZEL           | FALSE         | 390             | 801                 | 10204009   |
|   40118 | STANDARD    | FAIRDALE       | KY    | PRIMARY      | 38.11     | -85.75     | NA-US-KY-FAIRDALE       | FALSE         | 4398            | 7635                | 122449930  |
|   40020 | PO BOX      | FAIRFIELD      | KY    | PRIMARY      | 37.93     | -85.38     | NA-US-KY-FAIRFIELD      | FALSE         |                 |                     |            |
|   42221 | PO BOX      | FAIRVIEW       | KY    | PRIMARY      | 36.84     | -87.31     | NA-US-KY-FAIRVIEW       | FALSE         |                 |                     |            |
|   41426 | PO BOX      | FALCON         | KY    | PRIMARY      | 37.78     | -83        | NA-US-KY-FALCON         | FALSE         |                 |                     |            |
|   40932 | PO BOX      | FALL ROCK      | KY    | PRIMARY      | 37.22     | -83.78     | NA-US-KY-FALL ROCK      | FALSE         |                 |                     |            |
|   40119 | STANDARD    | FALLS OF ROUGH | KY    | PRIMARY      | 37.6      | -86.55     | NA-US-KY-FALLS OF ROUGH | FALSE         | 760             | 1468                | 20771670   |
|   42039 | STANDARD    | FANCY FARM     | KY    | PRIMARY      | 36.75     | -88.79     | NA-US-KY-FANCY FARM     | FALSE         | 696             | 1317                | 20643485   |
|   40319 | PO BOX      | FARMERS        | KY    | PRIMARY      | 38.14     | -83.54     | NA-US-KY-FARMERS        | FALSE         |                 |                     |            |
+---------+-------------+----------------+-------+--------------+-----------+------------+-------------------------+---------------+-----------------+---------------------+------------+
10 rows in set (0.004 sec)
```

This will query zipcodes_two and output the first 10 rows

```
SELECT * FROM zipcodes_two.zipcodes_two LIMIT 10;
```

```
+---------+-------------+-------------+-------+--------------+-----------+------------+----------------------+---------------+-----------------+---------------------+------------+
| Zipcode | ZipCodeType | City        | State | LocationType | Coord_Lat | Coord_Long | Location             | Decommisioned | TaxReturnsFiled | EstimatedPopulation | TotalWages |
+---------+-------------+-------------+-------+--------------+-----------+------------+----------------------+---------------+-----------------+---------------------+------------+
|   42040 | STANDARD    | FARMINGTON  | KY    | PRIMARY      | 36.67     | -88.53     | NA-US-KY-FARMINGTON  | FALSE         | 465             | 896                 | 11562973   |
|   41524 | STANDARD    | FEDSCREEK   | KY    | PRIMARY      | 37.4      | -82.24     | NA-US-KY-FEDSCREEK   | FALSE         |                 |                     |            |
|   42533 | STANDARD    | FERGUSON    | KY    | PRIMARY      | 37.06     | -84.59     | NA-US-KY-FERGUSON    | FALSE         | 429             | 761                 | 9555412    |
|   40022 | STANDARD    | FINCHVILLE  | KY    | PRIMARY      | 38.15     | -85.31     | NA-US-KY-FINCHVILLE  | FALSE         | 437             | 839                 | 19909942   |
|   40023 | STANDARD    | FISHERVILLE | KY    | PRIMARY      | 38.16     | -85.42     | NA-US-KY-FISHERVILLE | FALSE         | 1884            | 3733                | 113020684  |
|   41743 | PO BOX      | FISTY       | KY    | PRIMARY      | 37.33     | -83.1      | NA-US-KY-FISTY       | FALSE         |                 |                     |            |
|   41219 | STANDARD    | FLATGAP     | KY    | PRIMARY      | 37.93     | -82.88     | NA-US-KY-FLATGAP     | FALSE         | 708             | 1397                | 20395667   |
|   40935 | STANDARD    | FLAT LICK   | KY    | PRIMARY      | 36.82     | -83.76     | NA-US-KY-FLAT LICK   | FALSE         | 752             | 1477                | 14267237   |
|   40997 | STANDARD    | WALKER      | KY    | PRIMARY      | 36.88     | -83.71     | NA-US-KY-WALKER      | FALSE         |                 |                     |            |
|   41139 | STANDARD    | FLATWOODS   | KY    | PRIMARY      | 38.51     | -82.72     | NA-US-KY-FLATWOODS   | FALSE         | 3692            | 6748                | 121902277  |
+---------+-------------+-------------+-------+--------------+-----------+------------+----------------------+---------------+-----------------+---------------------+------------+
10 rows in set (0.001 sec)
```

This will query zipcodes_one and output the largest zipcode

```
SELECT * FROM zipcodes_one.zipcodes_one ORDER BY zipcode DESC LIMIT 1;
```

```
+---------+-------------+------------+-------+--------------+-----------+------------+---------------------+---------------+-----------------+---------------------+------------+
| Zipcode | ZipCodeType | City       | State | LocationType | Coord_Lat | Coord_Long | Location            | Decommisioned | TaxReturnsFiled | EstimatedPopulation | TotalWages |
+---------+-------------+------------+-------+--------------+-----------+------------+---------------------+---------------+-----------------+---------------------+------------+
|   47750 | UNIQUE      | EVANSVILLE | IN    | PRIMARY      | 37.98     | -87.54     | NA-US-IN-EVANSVILLE | FALSE         |                 |                     |            |
+---------+-------------+------------+-------+--------------+-----------+------------+---------------------+---------------+-----------------+---------------------+------------+
```

This will query zipcodes_two and output the smallest zipcode

```
SELECT * FROM zipcodes_two.zipcodes_two ORDER BY zipcode LIMIT 1;
```

```
+---------+-------------+--------------+-------+--------------+-----------+------------+-----------------------+---------------+-----------------+---------------------+------------+
| Zipcode | ZipCodeType | City         | State | LocationType | Coord_Lat | Coord_Long | Location              | Decommisioned | TaxReturnsFiled | EstimatedPopulation | TotalWages |
+---------+-------------+--------------+-------+--------------+-----------+------------+-----------------------+---------------+-----------------+---------------------+------------+
|   38257 | STANDARD    | SOUTH FULTON | TN    | PRIMARY      | 36.49     | -88.88     | NA-US-TN-SOUTH FULTON | FALSE         | 2066            | 3778                | 63816233   |
+---------+-------------+--------------+-------+--------------+-----------+------------+-----------------------+---------------+-----------------+---------------------+------------+
1 row in set (0.024 sec)
```

## Querying the database with the python script

The python script will query both tables in the database and will output last 10 rows of zipcodes_one, first 10 rows of zipcodes_two, largest zipcode in zipcodes_one, and smallest zipcode in zipcodes_two.
Run the query python script

```
./query.py
```

Results

```
The last 10 rows from zipcodes_one
(40843, 'STANDARD', 'HOLMES MILL', 'KY', 'PRIMARY', '36.86', '-83', 'NA-US-KY-HOLMES MILL', 'FALSE', '', '', '')
(41425, 'STANDARD', 'EZEL', 'KY', 'PRIMARY', '37.89', '-83.44', 'NA-US-KY-EZEL', 'FALSE', '390', '801', '10204009')
(40118, 'STANDARD', 'FAIRDALE', 'KY', 'PRIMARY', '38.11', '-85.75', 'NA-US-KY-FAIRDALE', 'FALSE', '4398', '7635', '122449930')
(40020, 'PO BOX', 'FAIRFIELD', 'KY', 'PRIMARY', '37.93', '-85.38', 'NA-US-KY-FAIRFIELD', 'FALSE', '', '', '')
(42221, 'PO BOX', 'FAIRVIEW', 'KY', 'PRIMARY', '36.84', '-87.31', 'NA-US-KY-FAIRVIEW', 'FALSE', '', '', '')
(41426, 'PO BOX', 'FALCON', 'KY', 'PRIMARY', '37.78', '-83', 'NA-US-KY-FALCON', 'FALSE', '', '', '')
(40932, 'PO BOX', 'FALL ROCK', 'KY', 'PRIMARY', '37.22', '-83.78', 'NA-US-KY-FALL ROCK', 'FALSE', '', '', '')
(40119, 'STANDARD', 'FALLS OF ROUGH', 'KY', 'PRIMARY', '37.6', '-86.55', 'NA-US-KY-FALLS OF ROUGH', 'FALSE', '760', '1468', '20771670')
(42039, 'STANDARD', 'FANCY FARM', 'KY', 'PRIMARY', '36.75', '-88.79', 'NA-US-KY-FANCY FARM', 'FALSE', '696', '1317', '20643485')
(40319, 'PO BOX', 'FARMERS', 'KY', 'PRIMARY', '38.14', '-83.54', 'NA-US-KY-FARMERS', 'FALSE', '', '', '')
The first 10 rows from zipcodes_two
(42040, 'STANDARD', 'FARMINGTON', 'KY', 'PRIMARY', '36.67', '-88.53', 'NA-US-KY-FARMINGTON', 'FALSE', '465', '896', '11562973')
(41524, 'STANDARD', 'FEDSCREEK', 'KY', 'PRIMARY', '37.4', '-82.24', 'NA-US-KY-FEDSCREEK', 'FALSE', '', '', '')
(42533, 'STANDARD', 'FERGUSON', 'KY', 'PRIMARY', '37.06', '-84.59', 'NA-US-KY-FERGUSON', 'FALSE', '429', '761', '9555412')
(40022, 'STANDARD', 'FINCHVILLE', 'KY', 'PRIMARY', '38.15', '-85.31', 'NA-US-KY-FINCHVILLE', 'FALSE', '437', '839', '19909942')
(40023, 'STANDARD', 'FISHERVILLE', 'KY', 'PRIMARY', '38.16', '-85.42', 'NA-US-KY-FISHERVILLE', 'FALSE', '1884', '3733', '113020684')
(41743, 'PO BOX', 'FISTY', 'KY', 'PRIMARY', '37.33', '-83.1', 'NA-US-KY-FISTY', 'FALSE', '', '', '')
(41219, 'STANDARD', 'FLATGAP', 'KY', 'PRIMARY', '37.93', '-82.88', 'NA-US-KY-FLATGAP', 'FALSE', '708', '1397', '20395667')
(40935, 'STANDARD', 'FLAT LICK', 'KY', 'PRIMARY', '36.82', '-83.76', 'NA-US-KY-FLAT LICK', 'FALSE', '752', '1477', '14267237')
(40997, 'STANDARD', 'WALKER', 'KY', 'PRIMARY', '36.88', '-83.71', 'NA-US-KY-WALKER', 'FALSE', '', '', '')
(41139, 'STANDARD', 'FLATWOODS', 'KY', 'PRIMARY', '38.51', '-82.72', 'NA-US-KY-FLATWOODS', 'FALSE', '3692', '6748', '121902277')
The largest zipcode from zipcodes_one
[(47750, 'UNIQUE', 'EVANSVILLE', 'IN', 'PRIMARY', '37.98', '-87.54', 'NA-US-IN-EVANSVILLE', 'FALSE', '', '', '')]
The smallest zipcode from zipcodes_two
[(38257, 'STANDARD', 'SOUTH FULTON', 'TN', 'PRIMARY', '36.49', '-88.88', 'NA-US-TN-SOUTH FULTON', 'FALSE', '2066', '3778', '63816233')]
```

## Shutting down the docker containers

To shut down the docker container

```
docker-compose down -v
```
