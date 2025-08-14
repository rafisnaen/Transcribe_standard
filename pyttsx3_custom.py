import pyttsx3
engine = pyttsx3.init() # object creation

rate = engine.getProperty('rate')   
print (rate)                        
engine.setProperty('rate', 135)

volume = engine.getProperty('volume')   
print (volume)                         
engine.setProperty('volume',1.0)       

engine.setProperty('voice', engine.getProperty('voices')[1].id)

text_response = "In 2025, the dominant trend in gaming will be the fusion of unprecedented scale and AI-driven dynamism, epitomized by blockbuster releases like *Grand Theft Auto VI*. The expectation is for vast, photorealistic open worlds, powered by engines like Unreal Engine 5, that are not merely static backdrops but living ecosystems. We will see a significant leap in procedural generation and AI, creating more believable NPC behaviors, emergent gameplay scenarios, and quests that feel reactive and less scripted. This means the world itself becomes a core character, constantly offering unique and unscripted moments that make each player's journey feel distinct, moving beyond graphical fidelity into an era of true environmental and social simulation."
engine.say(text_response)
engine.runAndWait()
engine.stop()