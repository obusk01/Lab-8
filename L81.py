# The Authors are Olivia Busk and Krista Dockery

def total_length(x):
    sum=0
    for y in x:
        sum=len(y)+sum
    return sum

print(total_length(["Olivia", "Busk", "Krista", "Dockery"]))
