# *******************************************************************************************************************************************
#                                   USES PYTTSX3 FOR TTS AND SPEECH RECOGNITION (CHIPMUNK AHH)

# import speech_recognition as sr
# import pyttsx3

# # Initialize recognizer and TTS engine
# recognizer = sr.Recognizer()
# tts_engine = pyttsx3.init()

# # Set voice to a more natural one
# voices = tts_engine.getProperty('voices')

# # Choose a female voice (you can change the index to experiment with different voices)
# tts_engine.setProperty('voice', voices[1].id)  # Index 1 is typically a female voice, you can adjust as needed

# # Optional: Adjust rate and volume for more natural speech
# tts_engine.setProperty('rate', 190)  # Speed of speech
# tts_engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# def speak(text):
#     """Convert text to speech."""
#     print("Pal2 (speaking):", text)
#     tts_engine.say(text)
#     tts_engine.runAndWait()

# def listen():
#     """Capture voice input and convert to text."""
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source, duration=0.5)
#         audio = recognizer.listen(source)

#     try:
#         query = recognizer.recognize_google(audio)
#         print("You (said):", query)
#         return query
#     except sr.UnknownValueError:
#         speak("Sorry, I didn't catch that. Please try again.")
#         return None
#     except sr.RequestError:
#         speak("Sorry, there's a problem with the speech service.")
#         return None

# ***************************************************************************************************************************************
#                                          THIS ONE SAVES THE RESPONSES TO A WAV FILE

# import speech_recognition as sr
# from TTS.api import TTS
# import soundfile as sf

# # Initialize recognizer and TTS engine
# recognizer = sr.Recognizer()

# # Initialize TTS with the specific model
# synthesizer = TTS(
#     model_name="tts_models/en/jenny/jenny",
#     progress_bar=True,
#     gpu=True
# )

# # Function to convert text to speech
# def speak(text):
#     """Convert text to speech."""
#     print("Pal2 (speaking):", text)
#     waveform = synthesizer.tts(text)
#     sample_rate = 48000  # You can adjust the sample rate if needed
#     sf.write('output.wav', waveform, sample_rate)
#     print("Generated speech saved as 'output.wav'")

# # Function to listen to voice input
# def listen():
#     """Capture voice input and convert to text."""
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source, duration=0.5)
#         audio = recognizer.listen(source)

#     try:
#         query = recognizer.recognize_google(audio)
#         print("You (said):", query)
#         return query
#     except sr.UnknownValueError:
#         speak("Sorry, I didn't catch that. Please try again.")
#         return None
#     except sr.RequestError:
#         speak("Sorry, there's a problem with the speech service.")
#         return None

# ***************************************************************************************************************************************
#                                                   DOABLE BUT STILL WORK IN PROGRESS

# SPEECH RECOGNITION AND TTS USING COQUI TTS
import speech_recognition as sr
from TTS.api import TTS
import sounddevice as sd
import numpy as np

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()

# Initialize TTS with the specific model
synthesizer = TTS(
    model_name="tts_models/en/jenny/jenny",
    progress_bar=True,
    gpu=True
)

# Function to convert text to speech
def speak(text):
    """Convert text to speech and play instantly."""
    print("Pal2 (speaking):", text)
    waveform = synthesizer.tts(text)
    waveform_np = np.array(waveform, dtype=np.float32)
    sd.play(waveform_np, samplerate=48000)
    sd.wait()

# FUNCTION TO LISTEN TO VOICE INPUT
def listen(retries=1):
    """Capture voice input with retry mechanism if not understood."""
    with sr.Microphone() as source:
        print("Pal2: Adjusting for background noise... (Stay quiet)")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        for attempt in range(retries + 1):
            print("Pal2: Listening...")
            speak("I am listening...")
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            except sr.WaitTimeoutError:
                print("Pal2: Listening timed out while waiting for phrase.")
                return None

            try:
                query = recognizer.recognize_google(audio)
                print(f"You (said): {query}")
                return query

            except sr.UnknownValueError:
                if attempt < retries:
                    print("Pal2: I didn't catch that. Please repeat...")
                    continue
                else:
                    print("Pal2: Still couldn't understand. Moving on.")
                    return None

            except sr.RequestError as e:
                print(f"Pal2: Could not request results; {e}")
                return None

# ***************************************************************************************************************************************