# now_build_staticfiles.sh

# Install Python 3.6 since it is missing in the Now build environment
pip install -r requirements.txt

# make migrations
python3.9 manage.py migrate 
python3.9 manage.py migrate sessions
python3.9 manage.py collectstatic
DJANGO_SUPERUSER_PASSWORD=12345 DJANGO_SUPERUSER_USERNAME=pacho DJANGO_SUPERUSER_EMAIL=pacho@gmail.com DJANGO_SUPERUSER_FIRST_NAME=fahim DJANGO_SUPERUSER_LAST_NAME=fahim python3.9 manage.py createsuperuser --noinput