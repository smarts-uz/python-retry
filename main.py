import os
import time
from pprint import pprint

from retry import retry
import shutil

@retry((FileNotFoundError, IOError), delay=1, backoff=2, max_delay=10, tries=1000)
def attempt_to_move_file(fname, dest_path):
    # Your attempt to move file
    print(fname,os.path.exists(fname))
    print(dest_path,os.path.exists(dest_path))
    shutil.copy(fname, dest_path)
    print('file copied')
    time.sleep(5)

for file in os.listdir('o:/'):
    if os.path.isfile(os.path.join('o:/',file)):
        attempt_to_move_file(fname=os.path.join('o:/',file),dest_path='p:/')
        print('okey')



#
# @retry(exceptions=ZeroDivisionError, delay=0.5, backoff=2, max_delay=1, tries=2)
# def zero_v(num):
#     print(num)
#     print(0/num)
#
#
# zero_v(num=5)

