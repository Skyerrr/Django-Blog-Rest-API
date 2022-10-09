# Django Blog Rest API
 Django Blog with Rest Api
 
Linux only because redis<br>

Install:<br>

cd library<br>
virtualenv -p python3 venv<br>
pip3 install -r requirements.txt<br>
sudo apt install redis-server # if you already have redis skip<br>
sudo service redis-server start<br>
python3 manage.py runserver<br>
python3 -m smtpd -n -c DebuggingServer localhost:1025<br>


[API Documentation](https://documenter.getpostman.com/view/21693015/2s83ziMiYR) <br>

admin login:<br>
User: admin<br>
Pass: admin<br>

To be implemented:<br>
units tests<br>
