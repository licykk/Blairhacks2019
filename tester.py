from Scheduler import Scheduler
from ScheduleItem import ScheduleItem

schedulethings = [["Math", "Homework", 35], ["Shower", "Chores", 20], ["Cooking", "Chores", 40]]

schedule = []

for a in schedulethings:
    ScheduleItem(a[0], a[1], a[2])
    schedule.append(ScheduleItem(a[0], a[1], a[2]))

scheduler = Scheduler()
scheduler.setSchedule(schedule)
print(scheduler.schedule[0].duration)
