import requests
from bs4 import BeautifulSoup
import time, random, re
from datetime import datetime

def parse_url(url):
    # Step 1: Send request to the website
    response = requests.get(url)
    html = response.text

    # Step 2: Parse HTML
    soup = BeautifulSoup(html, "html.parser")

    # Step 3: Extract the desired field (e.g., <span class="price">)
    price_tag = soup.find_all("label", class_="control-label date-time")
    if len(price_tag) != 2:
        return None
    available = price_tag[1].text.strip()
    return re.search(r'([A-Z][a-z]+ \d{2}, \d{4})',available).group(1)

dmvs = {
    "bayonne":"https://telegov.njportal.com/njmvc/AppointmentWizard/15/187",
    "elizabeth":"https://telegov.njportal.com/njmvc/AppointmentWizard/15/264",
    "edison":"https://telegov.njportal.com/njmvc/AppointmentWizard/15/194",
    "newark":"https://telegov.njportal.com/njmvc/AppointmentWizard/15/200",
    "bergen":"https://telegov.njportal.com/njmvc/AppointmentWizard/15/201",
    "paterson":"https://telegov.njportal.com/njmvc/AppointmentWizard/15/204",
    "rahway":"https://telegov.njportal.com/njmvc/AppointmentWizard/15/206",
    "wayne":"https://telegov.njportal.com/njmvc/AppointmentWizard/15/202"
}
print(datetime.now())
for dmv,url in dmvs.items():
    text = parse_url(url)
    if text == None:
        continue
    available = parse_url(url)
    print(f" {dmv} --> {available}")
    time.sleep(random.uniform(1,3))


print("*****************************************")
