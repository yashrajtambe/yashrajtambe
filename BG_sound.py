from pygame import mixer
from pydub import AudioSegment
import time
sound = AudioSegment.from_mp3("health_new2.mp3")
sound.export("health.wav", format="wav")

sound = AudioSegment.from_mp3("have a nice day.mp3")
sound.export("have_a_nice_day.wav", format="wav")
def intro():
    mixer.init()
    mixer.music.load("health.wav")
    mixer.music.set_volume(0.9)
    mixer.music.play()
    time.sleep(3.4)
    mixer.music.stop()

def end():
    mixer.init()
    mixer.music.load("have_a_nice_day.wav")
    mixer.music.set_volume(0.9)
    mixer.music.play()
    time.sleep(2)
    mixer.music.stop()
