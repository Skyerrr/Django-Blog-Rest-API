# Django Blog Rest API
 Django Blog with Rest Api

cd library
virtualenv -p python3 venv
pip3 install -r requirements.txt
python manage.py runserver
python -m smtpd -n -c DebuggingServer localhost:1025

Rest API Routes:

127.0.0.1:8000/api/books
127.0.0.1:8000/api/books/{id}

To be implemented:
Cache with redis
units tests
polished code
