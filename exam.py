from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
import string
find_me = [a+b for a in string.ascii_lowercase for b in string.ascii_lowercase]

for pswd in find_me:
   password = pswd + 'bcmpda'
   if unzip_with_7z(zip_file_path, dest_path, password):
      print(f'Successfull {password}')
      break