filename = input("Enter an file name:")

try:
    fhand = open(filename)
except FileNotFoundError:
    exit()

hours_dic = {}

for lines in fhand:
    lines.rstrip()
    if lines.startswith("From"):
        words = lines.split()
        if len(words) > 6:  # Check if the line has at least 7 words
            full_time = words[5].split(':')  # Assuming the time is in the 6th word
            if len(full_time) >= 2:  # Check if the time has a valid format (HH:MM or HH:MM:SS)
                hours = full_time[0]
                hours_dic[hours] = hours_dic.get(hours, 0) + 1

print(hours_dic)

fhand.close()

hours_list = list(hours_dic.items())

hours_list.sort()

for key, value in hours_list:
    print(key,value)
