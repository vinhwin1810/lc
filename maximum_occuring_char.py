def maximumOccuringCharacter(text):
    counter = {}

    for char in text:
        if char not in counter:
            counter[char] = 1
        else:
            counter[char] +=1

    maxVal = max(counter.values())

    for char, val in counter.items():
        if val == maxVal:
            return char

