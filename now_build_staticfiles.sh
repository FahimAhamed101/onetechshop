# now_build_staticfiles.sh

# Install Python 3.6 since it is missing in the Now build environment

# Install project requirements
pip install -r requirements.txt

# Build staticfiles
python3.10 manage.py collectstatic
python3.10 manage.py makemigrations
python3.10 manage.py migrate --run-syncdb
python3.10 manage.py makemigrations sessions
python3.10 manage.py migrate sessions
