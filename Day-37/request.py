# Here I showing request module in python

import requests

url = "https://ctsolutionbd.com"
data = requests.get(url)

print(data.text)
print(data.status_code)
print(requests.get(url, timeout=2.50))

import requests

class WebChecker:

    def __init__(self, url):
        self.url = url

    def checker(self):
        try:
            response = requests.get(self.url, timeout=2.50)
            if response.status_code == 200:
                print("Website is reachable and responding with status 200 OK")
            else:
                print(f"Website returned status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error: {e}. Unable to reach the website.")

if __name__ == "__main__":
    input_url = "https://" + input("Enter Your Url: ")
    checker = WebChecker(input_url)
    checker.checker()




