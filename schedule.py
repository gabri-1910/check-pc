import sched, time
import updates
def check_pc():
    print("This is my scheduled task.")
    updates.updates()

s = sched.scheduler(time.time, time.sleep)

# Schedule your task to run at 11 AM every day
s.enterabs(time.mktime(time.strptime("2023-04-16 11:00:00", "%Y-%m-%d %H:%M:%S")), 1, check_pc, ())

# Schedule your task to run at 17 PM every day
s.enterabs(time.mktime(time.strptime("2023-04-16 17:00:00", "%Y-%m-%d %H:%M:%S")), 1, check_pc, ())

# Run the scheduler
s.run()
