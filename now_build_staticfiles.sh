# now_build_staticfiles.sh

# Install Python 3.6 since it is missing in the Now build environment

# Install project requirements
pip install -r requirements.txt

# Build staticfiles
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py makemigrations sessions
python manage.py migrate sessions
