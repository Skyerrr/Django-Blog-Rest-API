# Django Blog Rest API
 Django Blog with Rest Api
 
Linux only because redis<br>

Install:<br>

cd library<br>
virtualenv -p python3 venv<br>
pip3 install -r requirements.txt<br>
sudo apt install redis-server # if you already have redis skip<br>
sudo service redis-server start #<br>
python manage.py runserver<br>
python -m smtpd -n -c DebuggingServer localhost:1025 # Temporary test for email send confirmation not necessary<br>

Rest API Routes:

127.0.0.1:8000/api/books<br>
127.0.0.1:8000/api/books/{id}<br>

admin login:<br>
User: admin<br>
Pass: admin<br>

To be implemented:<br>
units tests<br>
polished code<br>
