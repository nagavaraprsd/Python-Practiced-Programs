t=input("Enter the time in HH:MM Format\n")
t1=list(str(t))
if ":" not in t1:
    print("Invalid Format !! Re-Enter the Time in Correct Format ")
    exit()
hours,minutes=t.split(":")
hours=int(hours)
minutes=int(minutes)
if hours<=12 and minutes<=60:
    print("valid Time")
else:
    print("Invalid Time")