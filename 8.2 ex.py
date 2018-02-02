prefixes = "JKLMNOPQ"
suffix = "ack"

for l in prefixes:
    if l== "O" or l == "Q":
        print(l+"u"+suffix)
    else:
        print(l + suffix)


#prob 3
def count_letters(word,letter):
    count = 0
    for char in word:
        if char == letter
            count +=1
    return count

print(count_letters("eiojfos","o"))