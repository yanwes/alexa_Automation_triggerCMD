import time
import random
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()
time.sleep(10)  # Sleep for the amount of seconds generated
keyboard.press(Key.alt)
keyboard.press(Key.f12)
keyboard.release(Key.f12)
keyboard.release(Key.alt)

time.sleep(3)

def type_string_with_delay(string):
    for character in string:  # Loop over each character in the string
        keyboard.type(character)  # Type the character
         # Generate a random number between 0 and 10
         # Sleep for the amount of seconds generated

type_string_with_delay('COMMAND')
time.sleep(5)  #
keyboard.press(Key.enter)
