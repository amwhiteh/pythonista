from __future__ import print_function
ply_url = 'https://pypi.python.org/packages/source/p/ply/ply-3.4.tar.gz'
slimit_url = 'https://pypi.python.org/packages/source/s/slimit/slimit-0.8.1.zip'

print('Downloading SlimIt...')
from urllib import urlretrieve
import tarfile
import zipfile
import shutil
import os
try:
	shutil.rmtree('ply')
	shutil.rmtree('slimit')
except OSError:
	pass
urlretrieve(ply_url, 'ply.tar.gz')
urlretrieve(slimit_url, 'slimit.zip')

print('Installing...')
with tarfile.open('ply.tar.gz', 'r') as t:
def is_within_directory(directory, target):
	
	abs_directory = os.path.abspath(directory)
	abs_target = os.path.abspath(target)

	prefix = os.path.commonprefix([abs_directory, abs_target])
	
	return prefix == abs_directory

def safe_extract(tar, path=".", members=None, *, numeric_owner=False):

	for member in tar.getmembers():
		member_path = os.path.join(path, member.name)
		if not is_within_directory(path, member_path):
			raise Exception("Attempted Path Traversal in Tar File")

	tar.extractall(path, members, numeric_owner) 
	

safe_extract(t)

shutil.move('ply-3.4/ply', '.')
shutil.rmtree('ply-3.4')
os.remove('ply.tar.gz')

with zipfile.ZipFile('slimit.zip', 'r') as z:
	z.extractall()
shutil.move('slimit-0.8.1/src/slimit', '.')
shutil.rmtree('slimit-0.8.1')
os.remove('slimit.zip')
print('Done.')

print('Testing...')
from slimit import minify

text = '''var foo = function( obj ) {
    for (var name in obj ) {
        return false;
    }

return true;};'''

print('=' * 40)
print(text)
print('=' * 40)
print('Minified:')
print('=' * 40)
print(minify(text, mangle=True, mangle_toplevel=True))
print('=' * 40)
