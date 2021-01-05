import bs4
import requests
import time
from pynotifier import Notification
import pandas as pd

LOGIN_URL = 'https://ims.tmaxsoft.com/tody/auth/login.do?tmaxsso_nsso=yes'

default_issue_list_url = 'https://ims.tmaxsoft.com/tody/ims/issue/issueList.do?listType=5&menuCode=issue_list&CRCheck=N'
default_header = ["Issue Number", "Subject", "Reporter", "Issued date", "handler", "status", "Version"]

class IMS:
    def __init__(self, id, pw, interval):
        self.id = id
        self.pw = pw
        self.session = requests.Session()
        self.interval = interval
        self.running = False
        self.issue_list = default_issue_list_url
        self.header = default_header
    def set_header(self, header):
        self.header = header
    def set_issue_list_url(self, url):
        self.issue_list = url
    def login(self):
        self.session.post(LOGIN_URL, { 'id': self.id, 'password': self.pw })
    # def run(self):
    #     while True:
    #         if self.running == False:
    #             break
    #         print(time.time())
    #         time.sleep(self.interval)
    # def start(self):
    #     self.running = True
    #     self.run()
    # def stop(self):
    #     self.running = False
    def fetch(self):
        self.login()
        response = self.session.get(self.issue_list, cookies={'pageSize': '500'})

        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        header_rows = soup.find_all('tr', {'class': 'title'})
        
        data = []
        
        if len(header_rows) == 1:
            header_indexes = []
            new_header = []
            data_rows = soup.find_all('tr', {'class': 'data'})

            header_tds = header_rows[0].find_all('td')
            
            for i in range(len(header_tds)):
                if header_tds[i].text.strip() in self.header:
                    header_indexes.append(i)
                    new_header.append(header_tds[i].text.strip())
            for row in data_rows:
                tds = row.find_all('td')
                d = []
                for index in header_indexes:
                    d.append(tds[index].text.strip())
                data.append(d)
            data = pd.DataFrame(data=data, columns=new_header)
            return data
        else:
            print('no issue')
            return pd.DataFrame()

# if first_run:
#     first_run = False
# else:
#     # compare data_list vs data
#     compare = data.compare(data_list)

#     if len(compare) > 0:
#         # NOTI
#         for label, content in compare.items():
#             Notification(
#                 title=str(label[0]),
#                 description=str(content[0]),
#                 duration=5,
#                 urgency=Notification.URGENCY_CRITICAL
#             ).send()
# data_list = data
