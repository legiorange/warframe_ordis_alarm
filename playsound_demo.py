 #播放mp3音频文件
from playsound import playsound
import random

randomnum=random.randint(1,4)
print(randomnum)

def num_to_string(num):
    numbers = {
        # 0 : 'audio\Ordis - Alarm (Are you Awake).mp3',
        1 : 'audio\Ordis - Alarm (Emergency).mp3',
        2 : 'audio\Ordis - Alarm (Good Morning).mp3',
        3 : 'audio\Ordis - Alarm (Wake Up).mp3',
        # 4 : 'audio\Ordis - Alarm (System in Need).mp3',
        # 5 :'audio\Ordis - Alarm 1.mp3',
        # 6 :'audio\Ordis - Alarm 2.mp3',
        # 7 :'audio\Ordis - Alarm 3.mp3',
        # 8 :'audio\Ordis - Alarm 4.mp3',
        # 9 :'audio\Ordis - Alarm 5.mp3'
        
    }
    return numbers.get(num, None)

 
sound = num_to_string(randomnum)

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


playsound(sound)
