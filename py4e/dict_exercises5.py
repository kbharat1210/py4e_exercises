filename = input("Enter a file name:")

fopen = open(filename)

domain_dict = {}

for line in fopen:
    if line.startswith("Received:"):
        words = line.split()
        if len(words) >= 4:
            word = words[2]
            if words[2] == "murder":
                word = words[3]
            if word not in domain_dict:
                domain_dict[word] = 1
            else:
                domain_dict[word] += 1

updated_domain_dict = {}
for key,value in domain_dict.items():
    new_key = key.lstrip('([')

    updated_domain_dict[new_key] = value

print(updated_domain_dict)



