from pynotifier import Notification
from .ims import IMS
from threading import Timer, Thread
import time
import pandas as pd

class Bot:
    def __init__(self, id, pw, interval = 5 * 60, alert_types = ['new']):
        self.ims = IMS(id, pw)
        self.interval = interval
        self.init_variables()
        self.alert_types = alert_types
    def init_variables(self):
        self.is_running_job = False
        self.is_start = False
        self.first_run = True
        self.previous_data = pd.DataFrame([])
        self.callback = self.send_noti
    def set_callback(self, callback):
        self.callback = callback
    def reset_callback(self):
        self.callback = self.send_noti
    def send_noti(self, changed, _type):
        # print(changed)
        Notification(
            title='(' + _type + ') ' + changed['Issue Number'],
            description=changed['Subject'],
            duration=5,
            urgency=Notification.URGENCY_CRITICAL
        ).send()
    def job(self):
        data = self.ims.fetch()
        if self.first_run:
            self.first_run = False
            self.previous_data = data

        # new test
        old = self.previous_data['Issue Number'].values.tolist()
        new = data['Issue Number'].values.tolist()

        if 'new' in self.alert_types:
            for issue_number in new:
                if issue_number not in old:
                    row = pd.DataFrame(data[data['Issue Number'].isin([issue_number])])
                    self.callback(row.iloc[0], 'new')

        # delete test
        if 'delete' in self.alert_types:
            for issue_number in old:
                if issue_number not in new:
                    row = pd.DataFrame(self.previous_data[self.previous_data['Issue Number'].isin([issue_number])])
                    self.callback(row.iloc[0], 'delete')

        self.previous_data = data
        # change test
        # compare = data.compare(self.previous_data)
        # if len(compare) > 0:
        #     changed_list = []
        #     for ind in compare.index:
        #         changed_list.append(data.iloc[ind])
        #     self.callback(changed_list)
    def run(self):
        self.is_running_job = True
        self.job()
        self.is_running_job = False

        if self.is_start:
            self.t = Timer(self.interval, self.run)
            self.t.start()
    def start(self):
        self.is_start = True
        self.run()
    def stop(self):
        if self.is_running_job:
            self.is_start = False
        else:
            self.t.cancel()
