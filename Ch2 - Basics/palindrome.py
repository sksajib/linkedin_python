import string
def palindrome(word):
    l1=[]
    for i in range(10):
        l1.append(i)
    l2=list(word.lower())
    l3=[]
    for j in l2:
        if j in l1 or list(string.ascii_lowercase):
            l3.append(j)
    del l1,l2
    l5=l3[::-1]
    l3="".join(l3)
    print(l3)
    
    l5="".join(l5)
    print(l5)
    if l3 == l5:
        print(True)
    else:
        print(False)
    del l3,l5
palindrome(input("Enter String to check palindrome: "))