word = "APPLE"
for i in range(1,len(word)+1):
    print(" " * (len(word) - i), end="")
    print(" ".join(word[:i]))

# join function defines
# word = ["V","I","S","H","W","A"]    
# result = " ".join(word)
# print(result)
