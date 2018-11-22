from gtts import gTTS

tts_menu = gTTS("Welcome to Strans! A voice translator program from Sunsquare", lang='en')
tts_menu.save('svo_wc.mp3')
