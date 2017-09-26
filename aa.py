
import requests
from bs4 import BeautifulSoup
from lxml import html

res = requests.get("http://127.0.0.1:4040/status")


soup = BeautifulSoup(res.content,'html.parser')
js_code = soup.find_all('script')
for x in js_code:
    print x
    if "window.data" in x:
        print x



