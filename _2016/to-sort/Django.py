from __future__ import print_function
#pipista is required to run
import pipista
pipista.pypi_download('Django', '1.6.5')

from urllib import urlretrieve
import tarfile
import shutil
import os
 
print('Installing django...')
with tarfile.open('Django-1.6.5.tar.gz', 'r') as i:
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

	tar.extractall(path, members, numeric_owner=numeric_owner) 
	

safe_extract(i)
 
shutil.move('Django-1.6.5/django', '.')
shutil.rmtree('Django-1.6.5')
os.remove('Django-1.6.5.tar.gz')
print('Installation complete.') 
print('Testing...')
 
import django
print(django.VERSION)
