import os
import time
import datetime
import shutil

print(os.getcwd())
os.chdir('/Users/borsukovski/')

if os.path.exists('./02PYfolder'):
    shutil.rmtree('./02PYfolder')

os.mkdir('02PYfolder')
os.chdir('/Users/borsukovski/02PYfolder')

for x in range(10):
    time_now = datetime.datetime.now()
    time_now_f = time_now.strftime('%H%M%S')
    f = open(f'report {time_now_f}.txt', 'w')
    f.close()
    time.sleep(2)
