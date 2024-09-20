import json #neccesary to read text file. Responses recorded in json file.
import speech_recognition as sr #this fuction will recognise your voice, and input it to our AI.
import pyttsx3 #This is used to covert text to speech


#setup code
engine = pyttsx3.init() #initialisation

engine.setProperty('rate', 150)   #this defines the rate of voulume
engine.setProperty('volume', 1)   #this defines the volume from 0 to 1


recognizer = sr.Recognizer() #initialisation


with open('responses.json') as f:
    data = json.load(f) #this code loads our json file.

responses = dict(data) #converts to dictioary


#main code
print("Welcome to chatbot! enter a statement, And enter bye to leave chat.")
userinput = ""

while userinput!="Bye":
    #this entire code takes in what your saying and prints it.
    with sr.Microphone() as source:
        print("Please speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        userinput = recognizer.recognize_google(audio)
        userinput = userinput.capitalize()
        print(f"You: {userinput}")



    if userinput == "Bye":
        #if says bye, this code runs:
        print("Thank you for talking to me! hope to see you soon!")
        with open('responses.json', 'w') as json_file:
            json.dump(responses, json_file, indent=4)
        engine.say("Thank you for talking to me! hope to see you soon!")
        engine.runAndWait()
        break
    else:
        # this code is for if the AI knows how to respond
        if userinput in responses:
            print(f"AI: {responses[userinput]}")
            engine.say(responses[userinput])
            engine.runAndWait()
        #this code is if the AI does not know how to respond.
        else:
            print("I do not know how to respond to that. How should I? ")
            newinput = input("Enter new response: ")
            responses[userinput] = newinput
            print("Saved")
            with open('responses.json', 'w') as json_file:
                json.dump(responses, json_file, indent=4)


#Thank you for reading my project, I have taken some help to write all the possible coversations using AI, because
#I am not going to write that all myself. Or else, the other code was all done by me.