import random

def create(b,low,high,i):
    if i<20:
        b.append(random.randint(low,high))
        create(b,low,high,i+1)

def filter(b,i):
    if i==len(b):
        return b
    if b[i]%2!=1 or b[i]%3!=0:
        return filter(b, i + 1)
    if i < len(b)-1:
        b[i]=0
        return filter(b, i + 1)


def main():
    b=[]
    create(b,10,90,0)
    print(b)
    filter(b,0)
    print(b)


if __name__=='__main__':
    main()