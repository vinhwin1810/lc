def compareStrings(s1, s2):
    res1, res2 = "", ""
    
    for char in s1:
        if char != "#":
            res1 += char
        else:
            res1 = res1[:-1]
        print("res1", res1)
    for c in s2:
        if c != "#":
            res2 += c
        else:
            res2 = res2[:-1]
        print("res2", res2)
    return 1 if res1 == res2 else 0

print(compareStrings("r#a#n#k#", "###"))