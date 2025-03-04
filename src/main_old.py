import sys
sys.path.append("functions")
from naoqi import ALProxy
import voice
import time
#import motionFunc

nao_ip = "172.32.44.92"
nao_port = 9559
voice.init(nao_ip, nao_port)

memory = ALProxy("ALMemory", nao_ip, nao_port)
speech_recognition = ALProxy("ALSpeechRecognition", nao_ip, nao_port)
speech_recognition.pause(True) 
speech_recognition.setLanguage("Italian")

speech_recognition.setVocabulary(voice.getVocabulary(), False)
speech_recognition.pause(False) 

def stampa(value):
    print("AJSDKASJD",value)

print("Inizio")
memory.subscriber("ALSpeechRecognised/WordRecognized").signal.connect(stampa)
speech_recognition.subscribe("Test_ASR")
time.sleep(10)  # Listen for 10 seconds
speech_recognition.unsubscribe("Test_ASR")