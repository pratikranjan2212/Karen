from Brain.AIBrain import ReplyBrain
from Brain.Qna import Qna
from Body.Listen import Listen
print(">> Starting Zane : Wait for a few moments")
from Body.Speak import Speak
'''from Features.Clap  import Tester''' 
print(">> Starting Zane : Wait for sometime")
from Main import MainTaskExecutor
def MainExecution():

    Speak("Allow me to introduce myself. I am Zane, a virtual personal assistant and I am here to assist you with a variety of tasks as best as I can.")
    Speak("24 hours a day. 7 days a week. Importing preferences from home interface.")
    Speak("Systems now fully operational!")
    while True:

        Data = Listen()
        Data = str(Data).replace('.','')
        ValueReturn = MainTaskExecutor(Data)
        if ValueReturn==True:
            pass
        elif 'what' in Data or "where" in Data or "Question" in Data or "answer" in Data:
            Reply = Qna(Data)
        else:
            Reply = ReplyBrain(Data)
        Speak(Reply)

'''
def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Clap Detected >>")
        print("")
        MainExecution()
    else:
        pass

ClapDetect()
'''
print(MainExecution())


