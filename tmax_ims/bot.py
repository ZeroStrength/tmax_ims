from pynotifier import Notification
from .ims import IMS
from threading import Timer
import time

class Bot:
    def __init__(self, id, pw, interval = 5 * 60):
        self.ims = IMS(id, pw)
        self.interval = interval
        self.is_running_job = False
        self.is_start = False
        self.previous_data = []
    def init():
        pass
    def test_desktop_noti(self):
        Notification(
            title=str('test'),
            description=str('test'),
            duration=5,
            urgency=Notification.URGENCY_CRITICAL
        ).send()
    def job(self):
        self.test_desktop_noti()
    def run(self):
        self.is_running_job = True
        self.job()
        self.is_running_job = False

        if self.is_start:
            self.t = Timer(self.interval, self.job)
            self.t.start()
    def start(self):
        self.is_start = True
        self.run()
    def stop(self):
        if self.is_running_job:
            self.is_start = False
        else:
            self.t.cancel()

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
