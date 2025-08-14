import pyttsx3
engine = pyttsx3.init() # object creation

rate = engine.getProperty('rate')   
print (rate)                        
engine.setProperty('rate', 125)

volume = engine.getProperty('volume')   
print (volume)                         
engine.setProperty('volume',1.0)       

engine.setProperty('voice', engine.getProperty('voices')[1].id)
engine.say('Hello World')
engine.runAndWait()
engine.stop()