hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here
hour_end = (hour + ((dura + mins) // 60)) % 24
mins_end = (mins + dura) % 60

print("It will end up at: " + str(hour_end) + ":" + str(mins_end))