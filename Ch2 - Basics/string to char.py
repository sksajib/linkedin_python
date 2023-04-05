ab="I am S'jib"
b=list(ab)
print(b)
l=1
c=b[:l:-1]
print("".join(b))
print(len(b))
for i in range(2,10):
    print(i)
print(c)
def inc(a,b=1):
     return(a+b)
a=inc(1)
a=inc(a,a)
print(a)
try:
    x=int("five")
except ValueError:
    print("There is a value error.")
finally:
    print("Something went wrong.")
var="0123456789"
print(var[1:6:2])
