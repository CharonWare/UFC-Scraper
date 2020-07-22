import requests,bs4,time,re
res = requests.get("https://www.ufc.com/events")
res.raise_for_status
next_event = bs4.BeautifulSoup(res.text,"html.parser")
event_fight = next_event.select(".view-display-id-upcoming > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > article:nth-child(2) > div:nth-child(3) > h3:nth-child(1) > a:nth-child(1)")
event_time = next_event.select(".view-display-id-upcoming > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > article:nth-child(2) > div:nth-child(3) > div:nth-child(2) > a:nth-child(1)")


print("The next event is " + str(event_fight) + " on " + str(event_time))
time.sleep(1)
input("Press return/enter to exit.\n")

# TODO experiment with regex to parse cleaner strings

#fighter_regex = re.compile(r'''(
#    [a-zA-Z-]+ #name
#     vs 
#    [a-zA-Z-]+ #opponent
#)''')

#str(fighter_regex.findall(event_fight))
