#assume data is in the form of a 2d array
#schedule = alexa_data()
class Scheduler:
    categories = ["Homework", "Chores", "Work"]
    schedule = []

    def setCategories(self, categorylist):
        self.categories = categorylist
    def addCategory(self, category):
        self.categories.append(category)

    def setSchedule(self, scheduleitems):
        self.schedule = scheduleitems
    def addSchedule(self, scheduleitem):
        self.schedule.append(scheduleitem)
