import requests,bs4,time, re
res = requests.get("https://www.ufc.com/events")
res.raise_for_status
next_event = bs4.BeautifulSoup(res.text,"html.parser")
event_fight = next_event.select(".view-display-id-upcoming > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > article:nth-child(2) > div:nth-child(3) > h3:nth-child(1) > a:nth-child(1)")
event_time = next_event.select(".view-display-id-upcoming > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > article:nth-child(2) > div:nth-child(3) > div:nth-child(2) > a:nth-child(1)")

#Regex looking for fighters based on pattern: Name vs Name
fighters = re.compile(r'[A-Z][a-z]+\svs\s[A-Z][a-z]+')

next_fighters = str(event_fight)
next_vs = []

for match in fighters.findall(next_fighters):
    next_vs.append(match)

#Regex looking for date patterns based on: month-dd-yyyy
date = re.compile(r'january\W\d{2}\W\d{4}|february\W\d{2}\W\d{4}|march\W\d{2}\W\d{4}|april\W\d{2}\W\d{4}|may\W\d{2}\W\d{4}|june\W\d{2}\W\d{4}|july\W\d{2}\W\d{4}|august\W\d{2}\W\d{4}|september\W\d{2}\W\d{4}|october\W\d{2}\W\d{4}|november\W\d{2}\W\d{4}|december\W\d{2}\W\d{4}')

event_fight = str(event_fight)
next_date = []

for match in date.findall(event_fight):
    next_date.append(match)
    
#Regex looking for time patterns
clock = re.compile(r'\d[:punct:]\d{2}\s\D{2}\s\D{3}|\d{2}[:punct:]\d{2}\s\D{2}\s\D{3}')

event_time = str(event_time)
next_time = []

for match in clock.findall(event_time):
    next_time.append(match)
    
print("The next event is " + str(next_vs) + " on " + str(next_date) + " at " + str(next_time))
time.sleep(10)
