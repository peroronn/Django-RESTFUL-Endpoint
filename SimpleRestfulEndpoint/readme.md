python -m venv SimpleRestfulEndpoint
.\SimpleRestfulEndpoint\Scripts\activate
pip install -r requirements.txt
cd carpark_system
python manage.py makemigrations carpark 
python manage.py migrate

### load csv filea
python manage.py load_data

### testing
python manage.py test

### Create super user
python manage.py createsuperuser

python manage.py runserver 


### Home 
http://127.0.0.1:8000/

### Admin
http://127.0.0.1:8000/

### Get - no parking
http://127.0.0.1:8000/api/carparks/no_parking/

### Get - night parking
http://127.0.0.1:8000/api/carparks/night_parking/

### Get - Height filter above 2.1
http://127.0.0.1:8000/api/carparks/gantry_height/2.1/

### Post - add carpark (CP001 as id when adding)
http://127.0.0.1:8000/api/carparks/add/

### Put - update carpark with id (CP001 is carparkid that added)
http://127.0.0.1:8000/api/carparks/update/CP001/

### Delete - delete carpark
http://127.0.0.1:8000/api/carparks/delete/CP001/

### for output_file.txt
python dump_sqlite.py
