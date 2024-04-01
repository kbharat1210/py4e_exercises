
with open("mbox_short.txt","r") as file:
    date_dict = {}
    for line in file:
        if line.startswith("From"):
            words = line.split()
            if len(words) >= 3:
                date = words[2]
                if date not in date_dict:
                    date_dict[date] = 1
                else:
                    date_dict[date] += 1
    print(date_dict)

