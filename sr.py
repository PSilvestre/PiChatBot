import speech_recognition as sr
#import json
#import urllib.request
import subprocess
from cleverwrap import CleverWrap

API_KEY = "CC49d2fqNiA_AF83O8oCfleyvxQ"
#URL = "https://www.cleverbot.com/getreply?key="
#URL_INPUT = "&input="
#URL_STATE = "&cs="



#def getCleverResponse(inputText, state):
	#with urllib.request.urlopen(URL + API_KEY + URL_INPUT + '"' + inputText + '"' + (URL_STATE + state if state != "" else "")) as url:
		#data = json.loads(url.read().decode())
		#return data["output"], data["cs"]
	
def main():
	mic_input = ""
	cs = ""
	cleverResponse = ""
	r = sr.Recognizer()
	r.dynamic_energy_threshold = True
	r.pause_threshold = 0.7
	cw = CleverWrap(API_KEY)
	print("------------------------------------------")
	print("		Welcome to CleverBot VoiceChat!")
	print("------------------------------------------")
	with sr.Microphone() as source:	
		while True:
			audio = r.listen(source)
			try:
				mic_input = r.recognize_google(audio)
				print("You: " + mic_input)
				cleverResponse = cw.say(mic_input)
				print("CleverBot: " + cleverResponse)
				subprocess.call(['espeak', '"' + cleverResponse + '"'])
			except sr.UnknownValueError:
				print("Cannot understand audio")
			except sr.RequestError:
				print("Provider error")
				
				
if __name__ == '__main__':
	main()
