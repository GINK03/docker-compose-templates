import schedule
import time
import os
import base64
from pathlib import Path

def job():
        Path('./tricks').mkdir(exist_ok=True)
        print('try to predict')
        #os.system('python3 ./10-make_source_csv.py')
        #os.system('python3 ./30-make_user_csv.py')
        #os.system('python3 ./40-make_train_dataset.py')
        Path('./source.csv').unlink()
        Path('./user.csv').unlink()
        #os.system('python3 ./50-prediction.py')


schedule.every(60*24).minutes.do(job)
job()
while True:
        schedule.run_pending()  
        time.sleep(1)
