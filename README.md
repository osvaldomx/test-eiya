# Test Eiya!

Fleet Manager.

Features:
* Create, Edit and Delete vehicles.
* List all vehicles and current state.
* Create a trip and update vehicle features.

Technical Stack:
* Web app with Flask, HTML and Bootstrap.
* Backend in Flask and Python 3.9.
* DataBase in PostgreSQL.

## Instructions

For install the project, run:

```sh
> git clone git@github.com:osvaldomx/test-eiya.git myproject
> cd myproject
> pip install -r requirements.txt
> python app.py
```
for database conecction:
```sql
> CREATE DATABASE eiya;
```
and modify variable `SQLALCHEMY_DATABASE_URI` in `config.py` and `services/__init__.py`:
```python
SQLALCHEMY_DATABASE_URI = 'postgresql://<user>:<pass>@127.0.0.1:5432/eiya'
``` 

For access to app, the url:
`http://localhost:5000`

## Get started

### Web app

Once in `http://localhost:5000` see you a navbar with `Home` and `Admin` menu.

In Home you will see the three citys and vehicles in them.

In Admin you will see options for create, edit, delete and create trip for a vehicle. When you have created a trip, you will see a screen with trip and vehicle details updated. After, you only should click in Home button and in the index you will see the vehicles updated. 

### API

There is available an API. 

| endpoint          | url                                                     |
| ----------------- | ------------------------------------------------------- |
| Get All Vehicles  | `http://localhost:5000/api/vehiculos/all`               |
| Get Vehicle By ID | `http://localhost:5000/api/vehiculos/<int:id>`          |
| Create Vehicle    | `http://localhost:5000/api/vehiculos/crear`             |
| Edit Vehicle      | `http://localhost:5000/api/vehiculos/edit/<int:id>`     |
| Delete Vehicle    | `http://localhost:5000/api/vehiculos/eliminar/<int:id>` |
| Create Trip       | `http://localhost:5000/api/vehiculos/viaje`             |

Also, you can import http requests with `Test Eiya.postman_collection.json` form `Postman`.

#### Create vehicle parameters

```json
{
    "id": 13,
    "ubicacion": "CIUDAD A",
    "consumo": 2,
    "distancia": 123,
    "combustible": 2.5
}
```

#### Edit vehicle parameters

```json
{
    "ubicacion": "CIUDAD A",
    "consumo": 2,
    "distancia": 123,
    "combustible": 2.5
}
```

#### Create trip parameters
```json
{
    "id": 10,
    "origen": "CIUDAD A",
    "destino": "CIUDAD C"
}
```

## Contact

mail: [osvaldo.trujillo.ingenieria@gmail.com](mailto:osvaldo.trujillo.ingenieria@gmail.com)