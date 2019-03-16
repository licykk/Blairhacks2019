import time
#assume data is in the form of a 2d array
#schedule = alexa_data()
class Scheduler:
    categories = ["Homework", "Work", "Chores"]
    offline_categories = ["Chores"]
    schedule = []

    def setCategories(self, categorylist):
        self.categories = categorylist
    def addCategory(self, category):
        self.categories.append(category)

    def setSchedule(self, scheduleitems):
        self.schedule = scheduleitems
    def addSchedule(self, scheduleitem):
        self.schedule.append(scheduleitem)

    # Cycles through 25 min block, 5 min break
    def cycle(self, scheduleitem):
        cycles = 0
        minutes = scheduleitem.duration
        if not (scheduleitem.category in offline_categories):
            for a in range(minutes/25 + 1):
                if minutes >= 25:
                    time_end = time.time() + 60*25
                else:
                    time_end = time.time() + 60*minutes
                
