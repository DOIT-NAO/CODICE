from naoqi import ALProxy
def parla(messaggio, nao_ip, nao_port):
    tts = ALProxy("ALTextToSpeech", nao_ip, nao_port)
    tts.say(messaggio)