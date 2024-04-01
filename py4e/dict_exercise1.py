with open("words.txt", "r") as file:
    contents = file.read()
    print(contents)
    count = {}
    words = contents.split()
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] = count[word] + 1

    while True:
        user_word = input("Enter a word (or 'q' to quit): ").strip().lower()
        if user_word == 'q':
            break
        if user_word in count:
            print(f"Word '{user_word}' is in the file. Count: {count[user_word]}")
        else:
            print(f"Word '{user_word}' is not in the file.")













