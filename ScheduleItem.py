#A class that is the object for schedule items
class ScheduleItem:
    def __init__(self, name, category, duration):
        self.name = name
        self.category = category
        self.duration = duration

    def getName(self):
        return self.name
    def setName(self, name1):
        self.name = name1

    def getCategory(self):
        return self.category
    def setCategory(self, category1):
        self.category = category1

    def getDuration(self):
        return self.duration
    def setDuration(self, duration1):
        self.duration = duration1
