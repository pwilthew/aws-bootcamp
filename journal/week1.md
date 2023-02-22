# Week 1 — App Containerization

* Wrote a Docker file for the backend and the frontend

    * [../backend-flask/Dockerfile](../backend-flask/Dockerfile)
    * [../frontend-react-js/Dockerfile](../frontend-react-js/Dockerfile)

* Wrote a Docker Compose file

    * [../docker-compose.yml](../docker-compose.yml)

* Documented the new API endpoint, Notifications, in OpenAPI

    * [../backend-flask/openapi-3.0.yml](../backend-flask/openapi-3.0.yml)

    ```
      /api/activities/notifications:
    get:
      description: 'Return a feed of activity for accounts I follow'
      tags:
        - activities
      responses: 
        '200':
          description: 'Returns an array of activities'
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Activity'

    ```

* Created a service that returns fake notifications

    * [../backend-flask/services/notifications_activities.py](../backend-flask/services/notifications_activities.py)

* Took care of all the compiler warnings in the front end

    * https://github.com/pwilthew/aws-bootcamp-cruddur-2023/commit/e8bafe195450d524d6ef4e26b8f8cea0671d9c85

* Verified the front-end and the back-end are working well together for *Notifications*

    ![](images/notifications-front.png)

* Added config to gitpod.yml to install psql at boot time
  * [../gitpod.yml](../gitpod.yml)

```
  - name: postgres
    init: |
      curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
      echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
      sudo apt update
      sudo apt install -y postgresql-client-13 libpq-dev
```

* Tried DynamoDB locally
  ```
  aws dynamodb create-table \
    --endpoint-url http://localhost:8000 \
    --table-name Music \
    --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
    --key-schema AttributeName=Artist,KeyType=HASH AttributeName=SongTitle,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --table-class STANDARD

  aws dynamodb list-tables --endpoint-url http://localhost:8000

  aws dynamodb scan --table-name Music --query "Items" --endpoint-url http://localhost:8000
  ```
  
  ![](images/dynamodb.png)

* Tried Postgres locally

`psql -h localhost -U postgres`

  ![](images/postgresql.png)