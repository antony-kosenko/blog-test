Testing Guide
===============


Available API routes:
---------------------
### *Accounts* <br>
*Managing CustomUser instance CRUD.*<br>
Allowed http methods : (GET, POST, HEAD, OPTIONS)*:
1) GET (list) - `{HOST_NAME}/api/v1/accounts`
2) GET (retrieve) - `{HOST_NAME}/api/v1/accounts/(PK)`
3) POST (create) - `{HOST_NAME}/api/v1/accounts/`

   _Required fields_:
   - email;
   - username;
   - password;

    _Optional fields_:
    - Homepage;
    - Avatar;

4) PUT, PATCH (update) - `{HOST_NAME}/api/v1/accounts/(PK)`
5) DELETE (destroy) - `{HOST_NAME}/api/v1/accounts/(PK)`

### *Comments*
*Managing Comment instance CRUD.*<br>
Allowed http methods : (GET, POST, HEAD, OPTIONS)*:
1) GET (list) - `{HOST_NAME}/api/v1/comments`
2) GET (retrieve) - `{HOST_NAME}/api/v1/comments/(PK)`
3) POST (create) - `{HOST_NAME}/api/v1/comments/`

   _Required fields_:
   - user (data to be catched from the comment creation form which has to include all required fields from **Accounts**);
   - text;

    _Optional fields_:
   - parent (**id** of parent comment to be passed if comment being created is not a root comment);

4) PUT, PATCH (update) - `{HOST_NAME}/api/v1/comments/(PK)`
5) DELETE (destroy) - `{HOST_NAME}/api/v1/comments/(PK)`
6) POST (create / rate comment) - `{HOST_NAME}/api/v1/comments/(PK)/[option]`<br>

    _Options:_ 
    - like (increases comment rating)
    - dislike (decreases comment rating)

### *Rates*
*Managing Rates instance actions.*<br>
Allowed http methods : (POST, OPTIONS)*:

1) POST (create) - `{HOST_NAME}/api/v1/ratings/`
2) POST (update) - `{HOST_NAME}/api/v1/ratings/(PK)`

### Websockets:
Websockets testing available on root URL: `{HOST_NAME}/`

> ***API response parameters and ordering:***<br>
> Default comment sorting order: **LIFO**<br><br>
>**Valide filtering parameters:**<br>
> 1) `parent=` - returns child comments of parent comment (PK) provided;
> 2) `date_created_after==` - **after** which date comments to be listed;
> 3) `date_created_before==` - **before** which date comments to be listed; <br> **Note:** *Combination of `date_created_after` and `date_created_before` will list comments which were created between this two dates*.<br> *Date input format : **ISO 8601***. *Example: **[2024-05-14T08:57:43.919768Z]*** but even partial data provided is a valid request as backend will look for data that ***contains*** provided data;
> 4) `username=` - returns comments of the user with requested username;
> 5) `email=` - returns comments of the user with requested email;
> 6) `ordering=`<br> - if provided orders list of requested comments with requested ordering.<br>
>    Options:
>      - `username` - lits all comments ordering by username;
>      - `email` - lits all comments ordering by email;
>      - `date_created` - lits all comments ordering by date creation ;
>       > Defaul ordering for each parameter - `ascending`.
>       > To list by `descending` order - simpy add `-` before the ordering parameter.<br>
>    ***Example***: `{HOST_NAME}/api/v1/comments/?date_created_after=2024-05-14&ordering=-email`. Tthis API call will return all comments created after `2024-05-14` and all of them will be listed ordered by email value in descendent order;

Installation
---------------
As per task requirements hererepository has two ways for testing:

1) **Live server on hosting**;
2) **Running containerized app in Docker on local machine.**

## Hosting test

1) URL for API calls: **https://blog-test-iyxb.onrender.com**;

> **Note**: Hosting runs on free plan billing so innactivity causes server to stop until any activity observer. Please, wait for a minute after initial URL access to let server restart.

## Docker
Test task image available on publick repositor as well as local Dockerfile available to build image localy.
1) To pull image from public repository : `docker pull kosanko/testing-app:latest`
2) To build and run with docker-compose: `docker-compose up` from root project repository.

> **Note:** API url remains the same in case of run Docker only the `{HOST_NAME}=127.0.0.1`