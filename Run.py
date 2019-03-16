from Scheduler import Scheduler
import threading

print("a1")
def run_gui():
    import Main
    return Main.scheduleitems
print("a2")
def run_cycles(scheduleitems1):
    s = Scheduler()
    for i in scheduleitems1:
        s.cycle(i)

t1 = threading.Thread(target=run_gui, args=())


a = t1.start()
t1.join()

t2 = threading.Thread(target=run_cycles, args=(a,))

t2.start()
t2.join()
