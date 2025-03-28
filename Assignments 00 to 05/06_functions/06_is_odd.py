# Problem Statement
# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

def main():
    
    for i in range(10, 20):
        if i % 2 == 0:
            print("Even", i)
        else:
            print("odd",i)

if __name__ == '__main__':
    main()