from PIL import ImageGrab
import keyboard as kb
import os
from send_image_email import email
BASE_PATH = "The path file to where you want the image to be saved, e.g C:\\Users\\Name\\Pictures\\"


def handler():
    img = ImageGrab.grabclipboard()
    if img is not None:
        counter = 0
        filename = "snippet"
        while os.path.isfile(f"{BASE_PATH}/{filename}{counter}.png"):
            counter += 1
        img.save(f"{BASE_PATH}/{filename}{counter}.png")
    else:
        print("No image in clipboard!")


def main():
    shortcut = "D+M+V" # create your custom keyboard shortcuts if you want
    send_email = "S+M"
    kb.add_hotkey(shortcut, handler, args=None)
    kb.add_hotkey(send_email, email, args=None)
    kb.wait("D+M+O")


if __name__ == "__main__":
    main()
