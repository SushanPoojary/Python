import random
import urllib.request

def download_web_image(url):
    first = ("Sushan", "Sasha", "Sashu")
    second = ("Poojary", "Bhai")
    first_name = random.choice(first)
    second_name = random.choice(second)
    name = (first_name + " " + second_name)
    full_name = name + ".jpg"
    urllib.request.urlretrieve(url, full_name)
    print("Download Successful!")


download_web_image("https://bit.ly/2RmJryr")

