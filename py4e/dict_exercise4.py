filename = input("Enter a File Name:")

fopen = open(filename)
email_dict = {}
for line in fopen:
    if line.startswith("From"):
        words = line.split()
        if len(words)>= 2:
            word = words[1]
            if word not in email_dict:
                email_dict[word] = 1
            else:
                email_dict[word] += 1
print(email_dict)
max = 0

for emails in email_dict:
    if email_dict[emails] >= max:
        max = email_dict[emails]
print(max)
