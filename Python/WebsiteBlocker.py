import time
from datetime import datetime as dt

hosts_file=r"C:\Users\Administrator\Documents\Hackathon Stuffs\BlairHacks2019\Python\hosts.txt"
local="10.72.74.213"
website_list=["www.facebook.com","facebook.com","www.twitter.com","twitter.com"]



"""
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        with open(hosts_file,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(local+" "+ website+"\n")
    else:
        with open(hosts_file,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(120)
"""
