from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common import mobileby
from appium import webdriver
from time import sleep
from Body.Speak import Speak
import pathlib
from Body.Listen import Listen

scriptDirectory = pathlib.Path().absolute()

desired_caps = {
    "app": "Microsoft.WindowsStore_12006.1001.1.0_x64__8wekyb3d8bbwe",
    "platformName": "Windows",
    "deviceName": "WindowsPC",
    "appArguments": "microsoft.windowsstore://pdp/?ProductId=9nblggh2twpw",
    "appTopLevelWindow": "WindowsForms10.Window.8.app.0.33c0d9d",
}

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723',
    desired_capabilities=desired_caps)

Speak("Initializing The Whatsapp Software.")
sleep(5)

ListWeb = {'Chinu' : "+919078247840",
            'Mom': "+917655042686",
            "Dad": '+917749926770'}

def WhatsappSender(Name):
    '''Speak(f"Preparing To Send a Message To {Name}")
    Speak("What's The Message By The Way?")'''
    Message = 'hi'
    Number = ListWeb[Name]
    LinkWeb = 'https://wa.me/' + Number + "?text=" + Message
    driver.get(LinkWeb)
    sleep(5)
    try:
        touch_action = TouchAction(driver)
        touch_action.tap(x=850, y=650).perform()
        Speak("Message Sent")
        
    except:
        print("Invalid Number")

WhatsappSender('Chinu')
