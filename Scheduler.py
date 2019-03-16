import time
import os
#assume data is in the form of a 2d array
#schedule = alexa_data()
#schduler basicllay takes things from the schedule and does things
class Scheduler:
    categories = ["Homework", "Work", "Chores"]
    offline_categories = ["Chores"]
    schedule = []
    short_break_time = 5
    long_break_time = 20

    def setCategories(self, categorylist):
        self.categories = categorylist
    def addCategory(self, category):
        self.categories.append(category)

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
        cycles = 0
        minutes = scheduleitem.duration
        if not (scheduleitem.category in self.offline_categories):
            for a in range(minutes/25 + 1):
                if minutes >= 25:
                    time_end = time.time() + 60*25
                    cycles = cycles + 1
                else:
                    time_end = time.time() + 60*minutes
                    cycles = 0
                while time.time() < time_end:
                    #if user ends, break
                    ""
                #alert alexa
                #sound for end
                os.system("afplay ding.wav")
                if cycles < 4:
                    break_end = time.time() + 60*self.short_break_time
                else:
                    break_end = time.time() + 60*self.long_break_time
                    cycles = 0
                #sound for end
                os.system("afplay ding.wav")
        else:
            #alexa shit
            ""
