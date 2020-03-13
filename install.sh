rm -rf build
rm -rf dist
rm -rf mindsdb.egg-info

pip install --upgrade pip
pip3 install wheel
python3 setup.py sdist bdist_wheel
pip install -e ./
