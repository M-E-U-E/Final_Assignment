
git clone git@github.com:M-E-U-E/Final_Assignment.git
cd Final_Assignment


python3 -m venv env
source env/bin/activate

pip install django
pip install django-summernote
pip install django-summernote pillow


python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
