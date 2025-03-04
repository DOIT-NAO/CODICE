from naoqi import ALProxy

# Set NAO's IP and port
NAO_IP = "172.32.44.92"  # Replace with your robot's IP address
NAO_PORT = 9559

# Connect to NAOqi modules
speech_recognition = ALProxy("ALSpeechRecognition", NAO_IP, NAO_PORT)
memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)

# Define the words NAO should recognize
vocabulary = ["hello", "yes", "no", "goodbye", "NAO"]
speech_recognition.setVocabulary(vocabulary, False)

# Subscribe to the speech recognition event
def speech_callback(value):
    if isinstance(value, list) and len(value) > 0:
        print("Recognized speech:", value[0])

# Subscribe to "WordRecognized" event
memory.subscribeToEvent("WordRecognized", "speech_callback")

# Enable speech recognition
speech_recognition.setAudioExpression(True)
speech_recognition.setVisualExpression(True)
speech_recognition.subscribe("SpeechTest")

print("NAO is listening...")

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nStopping speech recognition.")
    speech_recognition.unsubscribe("SpeechTest")
