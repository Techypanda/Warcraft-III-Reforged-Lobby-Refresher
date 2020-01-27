import pywinauto
import pyautogui
import time
import keyboard
from pynput.keyboard import Key, Controller

################################################################################
#   PURPOSE: This function will type the inputted word through a keyboard.
#   IMPORT: inWord - String
#   EXPORT: NONE
################################################################################
def type(inWord):
    fakekeyboard = Controller()
    for i in range(len(inWord)):
        fakekeyboard.press(inWord[i])
        fakekeyboard.release(inWord[i])
    keyboard.press_and_release('enter')

################################################################################
#   PURPOSE: This function will execute one alt tab.
#   IMPORT: None
#   EXPORT: None
################################################################################
def altTab():
    fakekeyboard = Controller()
    fakekeyboard.press(Key.alt)
    fakekeyboard.press(Key.tab)
    fakekeyboard.release(Key.tab)
    fakekeyboard.release(Key.alt)

################################################################################
#   PURPOSE: This function will simply find the Warcraft Client and tab into it.
#   IMPORT: None
#   EXPORT: None
################################################################################
def getIntoWC():
    app = pywinauto.Application().connect(title="Warcraft III Beta")
    app_dialog = app.top_window()
    app_dialog.set_focus()
    pyautogui.click(1800, 1400)

################################################################################
#   PURPOSE: RefreshLobby will execute !closeall !openall to update the warcraft
#   lobby.
#   IMPORT: None
#   EXPORT: None
################################################################################
def refreshLobby():
    type("!closeall")
    type("!openall")
    altTab()

################################################################################
#   PURPOSE: Init will loop through eternally until you end the script.
#   IMPORT: None
#   EXPORT: None
################################################################################
def init():
    while 2 == 2:
        try:
            getIntoWC()
        except:
            print("Could Not Locate WC3 Client")
            break;
        refreshLobby()
        time.sleep(60)

init()
