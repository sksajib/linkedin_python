def main():
    a=0
    b=1
    c=a
    d=b
    n=int(input("Enter how many numbers should be in the series: "))
    n=n-2
    
    fibo(c,d,n)
def fibo(c,d,n):
    print(c,d,end=' ')
    for i in range(n):
        total=c+d
        
        print(total,end=' ')
        c=d
        d=total
if __name__=="__main__":
    main()
