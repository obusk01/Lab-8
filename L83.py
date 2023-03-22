# The Authors are Olivia Busk and Krista Dockery

def count_character(string, letter):
    count=0
    for char in string:
        if char == letter:
            count += 1
    return count

print(count_character("banana","a"))
