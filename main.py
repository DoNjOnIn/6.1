import random

def filter(b,i):
    if b[i]%2==1 and b[i]%3==0:
        b.remove(b[i])
    if i < len(b)-1:
        return filter(b, i + 1)
    else:
        return b

def main():
    b=[]
    for i in range(21):
        b.append(random.randint(10,90))
    print(b)
    filter(b,0)
    print(b)


if __name__=='__main__':
    main()