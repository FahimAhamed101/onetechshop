# now_build_staticfiles.sh

# Install Python 3.6 since it is missing in the Now build environment
yum install -y https://centos6.iuscommunity.org/ius-release.rpm
yum install -y python39u

# Install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py

# Install project requirements
pip install -r requirements.txt

# Build staticfiles
python3.9 manage.py collectstatic
python3.9 manage.py makemigrations
python3.9 manage.py migrate --run-syncdb
