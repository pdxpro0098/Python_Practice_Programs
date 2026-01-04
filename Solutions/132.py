# Dalip's Approach
def convertToSeconds(hours,minutes):
    totalSeconds = (hours * 3600) + (minutes *60)
    return totalSeconds

hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))

print("Total Seconds:",convertToSeconds(hours,minutes))
