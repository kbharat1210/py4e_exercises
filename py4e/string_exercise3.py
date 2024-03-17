def count(letter:str,word:str):
    counter = 0
    for char in word:
        if char == letter:
            counter += 1
    return counter

