# The Authors are Olivia Busk and Krista Dockery

# index=0
# s="Mind the Gap!"
# while index<len(s) and s[index] !=" ":
#     index+=1
# print(s[:index])

def until_dot(x):
    index=0
    while index<len(x) and x[index] !=".":
        index+=1
    print(x[:index])

until_dot("Hello. Olivia")


# def no_repeating():
#     words=[]
#     while True:
#         word=input("Tell me a word:")
#         if word in words:
#             print("You told me that word already!")
#             break
#         words.append(word)
#     return words
