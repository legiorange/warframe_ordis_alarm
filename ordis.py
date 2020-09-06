 #播放mp3音频文件
from playsound import playsound
import random
# cont
from apscheduler.schedulers.blocking import BlockingScheduler


#randomnum=random.randint(0,9)
#print(randomnum)

def num_to_string(num):
    numbers = {
        0 : 'audio\Ordis - Alarm (Are you Awake).mp3',
        1 : 'audio\Ordis - Alarm (Emergency).mp3',
        2 : 'audio\Ordis - Alarm (Good Morning).mp3',
        3 : 'audio\Ordis - Alarm (Wake Up).mp3',
        4 : 'audio\Ordis - Alarm (System in Need).mp3',
        5 :'audio\Ordis - Alarm 1.mp3',
        6 :'audio\Ordis - Alarm 2.mp3',
        7 :'audio\Ordis - Alarm 3.mp3',
        8 :'audio\Ordis - Alarm 4.mp3',
        9 :'audio\Ordis - Alarm 5.mp3'
        
    }
    return numbers.get(num, None)

 

# sound ='audio\Ordis - Alarm (Are you Awake).mp3'
# sound ='audio\Ordis - Alarm (Emergency).mp3'
# sound ='audio\Ordis - Alarm (Good Morning).mp3'
# sound ='audio\Ordis - Alarm (System in Need).mp3'
# sound ='audio\Ordis - Alarm (Wake Up).mp3'
# sound ='audio\Ordis - Alarm 1.mp3'
# sound ='audio\Ordis - Alarm 2.mp3'
# sound ='audio\Ordis - Alarm 3.mp3'
# sound ='audio\Ordis - Alarm 4.mp3'
# sound ='audio\Ordis - Alarm 5.mp3'
# sound ='audio\OrdisIsItTalking.mp3'
# sound ='audio\OrdisIsItTalking.mp3'
# sound ='audio\OrdisIsItTalking.mp3'


scheduler = BlockingScheduler()
# @scheduler.scheduled_job('interval', seconds=9)
@scheduler.scheduled_job('cron', id= 'job_0',day_of_week='0-4',hour='6',minute='30')
# @scheduler.scheduled_job('cron', id= 'job_0',second='9')

def job_0():
        randomnum=random.randint(1,4)
        sound = num_to_string(randomnum)
        playsound(sound)
        print('Ordis Alarm実行完了')

print('Ordis init.....      done')
scheduler.start()


