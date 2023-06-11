# now_build_staticfiles.sh

# Install Python 3.6 since it is missing in the Now build environment
pip install -r requirements.txt

# make migrations
python3.9 manage.py migrate 
python3.9 manage.py migrate sessions
python3.9 manage.py collectstatic