import time
import os
from block import block
import threading

#assume data is in the form of a 2d array
#schedule = alexa_data()
#schduler basicllay takes things from the schedule and does things
class Scheduler:
    categories = ["Homework", "Work", "Chores"]
    offline_categories = ["Chores"]
    short_break_time = 5
    long_break_time = 20

    def setCategories(self, categorylist):
        self.categories = categorylist
    def addCategory(self, category):
        self.categories.append(category)
    def getCategories(self):
        return self.categories

    def setSchedule(self, scheduleitems):
        self.schedule = scheduleitems
    def addSchedule(self, scheduleitem):
        self.schedule.append(scheduleitem)

    def setShortBreak(self, shorttime):
        self.short_break_time = shorttime

    def setLongBreak(self, longtime):
        self.long_break_time = longtime;

    # Cycles through 25 min block, 5 min break, for one given scheduleitem
    def cycle(self, scheduleitem):
        print("ckp")
        cycles = 0
        minutes = scheduleitem.duration
        if not (scheduleitem.category in self.offline_categories):
            for a in range(int(minutes)/25 + 1):
                print("ckpt3")
                block("websites.txt")
                if minutes >= 25:
                    cycles = cycles + 1
                    minutes = minutes - 25

                    time.sleep(60*25)
                else:
                    print("ckpt")
                    cycles = 0

                    time.sleep(60*minutes)
                print("end first timer")
                block("emptyfile.txt")
                #alert alexa
                #sound for end
                os.system("afplay ding.wav")
                if scheduleitem.duration < 15:
                    break_end = time.time()
                    print("ckpt2")
                else:
                    if cycles < 4:
                        time.sleep(60*self.short_break_time)
                    else:
                        time.sleep(60*self.long_break_time)
                        cycles = 0
                #sound for end
                os.system("afplay ding.wav")
        else:
            #alexa shit
            ""
