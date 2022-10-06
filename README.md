# Django Blog Rest API
 Django Blog with Rest Api

cd library<br>
virtualenv -p python3 venv<br>
pip3 install -r requirements.txt<br>
python manage.py runserver<br>
python -m smtpd -n -c DebuggingServer localhost:1025<br>

Rest API Routes:

127.0.0.1:8000/api/books<br>
127.0.0.1:8000/api/books/{id}<br>

To be implemented:
Cache with redis
units tests
polished code
