# Week 4 — Postgres and RDS

## Provision an RDS instance

```
aws rds create-db-instance \
  --db-instance-identifier cruddur-db-instance \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --engine-version  14.6 \
  --master-username root \
  --master-user-password $PASSWORD \
  --allocated-storage 20 \
  --availability-zone us-east-1a \
  --backup-retention-period 0 \
  --port 5432 \
  --no-multi-az \
  --db-name cruddur \
  --storage-type gp2 \
  --publicly-accessible \
  --storage-encrypted \
  --enable-performance-insights \
  --performance-insights-retention-period 7 \
  --no-deletion-protection
```

![](images/01-provisioned-rds.png)

## Temporarily stop an RDS instance

![](images/02-temp-stop-rds.png)

## Remotely connect to RDS instance


## Create a schema SQL file by hand

The following is for Postgres to generate out UUIDs.


backend-flask/db/schema.sql
```sql
CREATE EXTENSION "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```

```
gitpod /workspace/aws-bootcamp-cruddur-2023 (week-4) $ psql cruddur < backend-flask/db/schema.sql -h localhost -U postgres
Password for user postgres: 
CREATE EXTENSION
NOTICE:  extension "uuid-ossp" already exists, skipping
CREATE EXTENSION
```

## Write several bash scripts for database operations

Created the following bash scripts:
* db-create
* db-drop
* db-schema-load
* db-sessions
* db-seed
* and db-setup (which executes the others)

![](images/03-bash-scripts.png)

## Implement a postgres client for python using a connection pool

Read from the postgres database for the Home Activities page.

![](images/04-postgres-driver.png)