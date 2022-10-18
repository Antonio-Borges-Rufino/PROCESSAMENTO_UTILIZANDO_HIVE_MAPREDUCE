# INSTRUÇÕES INICIAIS:
1. [OS DADOS UTILIZADOS ESTÃO AQUI](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/airports.csv)
2. PARA IMPORTAR OS DADOS PARA O HDFS UTILIZA-SE
```
hdfs dfs -put ~/airports.csv /user/RUFINO_CLUSTER/PROCESSO
```
3. PARA RODAR OS PROCESSOS MAPREDUCE PURO UTILIZEI O MAPRED PARA CONSTRUÇÃO DOS BLOCOS EM PYTHON
```
mapred streaming -input /user/RUFINO_CLUSTER/PROCESSO -output /user/RUFINO_CLUSTER/result_ -mapper /home/hadoop/map.py -reducer /home/hadoop/reduce.py
```
4. NO HIVE, FOI CRIADO UM DATABASE E UMA TABELA PRÓRPIA PARA COMPORTAR OS DADOS
```
hive/bin/hive
CREATE DATABASE airports;
USE airports;
CREATE TABLE info_airport (id_a INT,name STRING,city STRING,country STRING,iata STRING,icao STRING,latitude FLOAT,longitude FLOAT,altitude FLOAT,time_a STRING,dst STRING,tz STRING,type_a STRING,source_a STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY ','; 
```
5. APÓS ISSO, SÓ IMPORTAR OS DADOS DO HDFS PARA O HIVE
```
LOAD DATA INPATH '/user/RUFINO_CLUSTER/PROCESSO/airports.csv' OVERWRITE INTO TABLE info_airport;
```

# PERGUNTAS:
### Considerando o dataset airports.dat, qual a diferença de altitude entre os aeroportos Jorge Newbery Airpark e Altamira Airport?
1. HIVE CONSULTA:
```
SELECT Max(altitude)-Min(altitude) FROM info_airport WHERE name='"Altamira Airport"' or name ='"Jorge Newbery Airpark"';
```
2. [CÓDIGO MAP PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q7/map.py)
3. [CÓDIGO REDUCE PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q7/reduce.py)
4. [RESULTADO DO PROCESSAMENTO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/tree/main/q7/result_)
### Considerando o dataset airports.dat, quantos aeroportos existem na cidade de São Paulo? (no dataset não há acentos)
1. HIVE CONSULTA:
```
SELECT COUNT(*) FROM info_airport WHERE city='"Sao Paulo"'
```
2. [CÓDIGO MAP PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q8/map.py)
3. [CÓDIGO REDUCE PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q8/reduce.py)
4. [RESULTADO DO PROCESSAMENTO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/tree/main/q8/result_)
### Considerando o dataset airports.dat, quantos aeroportos o Brasil (está em inglês, Brazil) possui?
1. HIVE CONSULTA:
```
SELECT COUNT(*) FROM info_airport WHERE country='"Brazil"'
```
2. [CÓDIGO MAP PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q9/map.py)
3. [CÓDIGO REDUCE PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q9/reduce.py)
4. [RESULTADO DO PROCESSAMENTO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/tree/main/q9/result_)
### Considerando o dataset airports.dat, qual cidade apresenta a maior quantidade de aeroportos?
1. HIVE CONSULTA:
```
SELECT city, COUNT(*) as conta FROM info_airport GROUP BY city ORDER BY conta;
```
2. [CÓDIGO MAP PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q10/map.py)
3. [CÓDIGO REDUCE PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q10/reduce.py)
4. [RESULTADO DO PROCESSAMENTO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/tree/main/q10/result_)
### Considerando o dataset airports.dat, qual país apresenta a maior quantidade de aeroportos?
1. HIVE CONSULTA:
```
SELECT country, COUNT(*) as conta FROM info_airport GROUP BY country ORDER BY conta;
```
2. [CÓDIGO MAP PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q11/map.py)
3. [CÓDIGO REDUCE PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q11/reduce.py)
4. [RESULTADO DO PROCESSAMENTO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/tree/main/q11/result_)
### Considerando o dataset airports.dat, qual aeroporto apresenta a maior altitude?
1. HIVE CONSULTA:
```
SELECT name, altitude FROM info_airport ORDER BY altitude;
```
2. [CÓDIGO MAP PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q12/map.py)
3. [CÓDIGO REDUCE PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q12/reduce.py)
4. [RESULTADO DO PROCESSAMENTO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/tree/main/q12/result_)
### Considerando o dataset airports.dat, qual a média da altitude dos aeroportos do Brasil?
1. HIVE CONSULTA:
```
SELECT AVG(altitude) FROM info_airport WHERE country='"Brazil"';
```
2. [CÓDIGO MAP PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q13/map.py)
3. [CÓDIGO REDUCE PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q13/reduce.py)
4. [RESULTADO DO PROCESSAMENTO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/tree/main/q13/result_)
### Considerando o dataset airports.dat, quantos DST (faixas de horário de verão) existem? (Para essa resposta desconsidere aqueles que não possuem dados, representados por \N)
1. HIVE CONSULTA:
```
SELECT DISTINCT(dst) FROM info_airport;
```
2. [CÓDIGO MAP PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q14/map.py)
3. [CÓDIGO REDUCE PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q14/reduce.py)
4. [RESULTADO DO PROCESSAMENTO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/tree/main/q14/result_)
### Considerando o dataset airports.dat, quantos países possuem aeroportos?
1. HIVE CONSULTA:
```
SELECT COUNT(DISTINCT(country)) FROM info_airport WHERE type_a='"airport"';
```
2. [CÓDIGO MAP PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q15/map.py)
3. [CÓDIGO REDUCE PURO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/blob/main/q15/reduce.py)
4. [RESULTADO DO PROCESSAMENTO](https://github.com/Antonio-Borges-Rufino/PROCESSAMENTO_UTILIZANDO_HIVE_MAPREDUCE/tree/main/q15/result_)
