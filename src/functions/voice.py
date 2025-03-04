from naoqi import ALProxy
import time
sayParameters = []
commands = []

def init(ip, port):
    global sayParameters, commands
    sayParameters = [ip, port]
    commands = [
        {
            "requires": [["ciao", "buongiorno"]],
            "function": parla,
            "parameters": ["Ciao mondo!"] + sayParameters
        },
        {
            "requires": [["come"], ["stai", "va"]],
            "function": parla,
            "parameters": ["Stavo bene prima che mi parlassi"] + sayParameters
        }
    ]

def parla(messaggio, nao_ip, nao_port):
    tts = ALProxy("ALTextToSpeech", nao_ip, nao_port)
    tts.say(messaggio)

def getVocabulary():
    lista = []
    for command in commands:
        for alternatives in command["requires"]:
            for word in alternatives:
                if word not in lista:
                    lista.append(word)
    return lista


def executeCommand(words):
    for command in commands:
        foundAlternative = False
        for alternatives in command["requires"]:
            foundAlternative = False
            for word in alternatives: 
                if word in words:
                    foundAlternative = True
                    break
            if not foundAlternative: break
        if foundAlternative:
            commands[0]["function"](*commands[0]["parameters"])
            return


def registra():
    print("Inizializzazione...")
    audio_recorder = ALProxy("ALAudioRecorder",  *sayParameters)

    file_path = "/home/nao/4ci/audio.wav"

    channels = [1, 0, 0, 0]

    sample_rate = 16000  

    print("Inizio registrazione...")
    audio_recorder.startMicrophonesRecording(file_path, "wav", sample_rate, channels)

    time.sleep(20)
    audio_recorder.stopMicrophonesRecording()
    print("Registrazione completata! File salvato in: " + file_path)