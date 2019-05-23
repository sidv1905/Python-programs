import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,"html.parser")

for story_heading in soup.find_all(class=="css-8uvv5f esl82me2"):
    if story_heading.h2:
        print(story_heading.h2.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())
