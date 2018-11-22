import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound

# enter the name of usb microphone that you found
# using lsusb
# the following name is only used as an example
#mic_name = ""
# Sample rate is how often values are recorded
#sample_rate = 48000
# Chunk is like a buffer. It stores 2048 samples (bytes of data)
# here.
# it is advisable to use powers of 2 such as 1024 or 2048
#chunk_size = 2048
# Initialize the recognizer
r = sr.Recognizer()
tr = Translator()

def translation(text,lang):
    translatedText = tr.translate(text, dest=lang)
    print(translatedText.text)
    translatedSpeech = gTTS(translatedText.text, lang=lang)
    translatedSpeech.save("svo_output.mp3")
    playsound("svo_output.mp3")
    

# generate a list of all audio cards/microphones
#mic_list = sr.Microphone.list_microphone_names()

# the following loop aims to set the device ID of the mic that
# we specifically want to use to avoid ambiguity.
#for i, microphone_name in enumerate(mic_list):
#    if microphone_name == mic_name:
#        device_id = i

# use the microphone as source for input. Here, we also specify
# which device ID to specifically look for incase the microphone
# is not working, an error will pop up saying "device_id undefined"
playsound('svo_wc.mp3')
with sr.Microphone() as source:
    # wait for a second to let the recognizer adjust the
    # energy threshold based on the surrounding noise level
    r.adjust_for_ambient_noise(source)
    print ("Say Something...")
    # listens for the user's input
    audio = r.listen(source)
    lang_dict = {
    "English":"en",
    "Hindi":"hi",
    "Spanish":"es",
    "France":"fr"
    }

    try:
        text = r.recognize_google(audio)
        print ("You said: " + text)
        while text != 'close the program':
        	print("\n 1: English \n 2: Hindi \n 3: Spanish \n 4: French")
        	playsound('svo_select.mp3')
        	audio = r.listen(source)
        	sel_lang = r.recognize_google(audio)
        	if sel_lang in lang_dict:
        		dest_lang = lang_dict[sel_lang]
        		translation(text, dest_lang)
        	else:
        		print("\n\n Choose proper language.")
        	exit(0)
        exit(0)
    # error occurs when google could not understand what was said

    except sr.UnknownValueError:
        playsound('svo_lang_error.mp3')

    except sr.RequestError as e:
        playsound('svo_other_error.mp3')
        print(format(e))