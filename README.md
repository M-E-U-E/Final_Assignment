
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
## Git Clone Instructions

To clone this project to your local machine, follow these steps:

1. **Open terminal (Command Prompt, PowerShell, or Terminal)**

2. **Clone the repository**:
   
         git clone https://github.com/M-E-U-E/Final_Assignment.git or git clone git@github.com:M-E-U-E/Final_Assignment.git
   
    Go to the Directory:
    ```bash
    cd Final_Assignment
    ```
4. **Set Up Virtual Environment**
   
    ```bash
    # Create virtual environment On macOS/Linux:
       python3 -m venv env
       source env/bin/activate

    # Activate virtual environment
    # Create virtual environment On Windows:
       python -m venv env
       venv\Scripts\activate
5. **Install Dependencies**
        pip install django
        pip install django-summernote
        pip install django-summernote pillow


python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
