import schedule
import subprocess 
import time

def job():
    #subprocess.call('aplay /home/pi/alarm.wav', shell=true)
    print("doing job")
    
#schedule.every().day.at('7:00').do(job)
a = schedule.every().minute.at(":17").do(job)

while(1):
    schedule.run_pending()
    time.sleep(1)
    
    
    