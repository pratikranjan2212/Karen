import pywhatkit
from Body.Speak import Speak
from Body.Listen import Listen

ListWeb = {'Chinu' : "+919078247840",
            'Mom': "+917655042686",
            "Dad": '+917749926770'}

def WhatsappSender(Name):
    '''Speak(f"Preparing To Send a Message To {Name}")
    Speak("What's The Message By The Way?")'''
    Message = 'hi'
    Number = ListWeb[Name]
    pywhatkit.sendwhatmsg(Number, Message, 0, 0, 0)
    Speak("Message Sent")

WhatsappSender('Chinu')
