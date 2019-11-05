#Jonathan Kelly, jonathan.kelly2@marist.edu
#prints out prime numbers under a certain cap

def main():
    x = int(input("What is the top number: "))
    numList = [0] * (x -1) 
    for i in range(x):
        numList[i-1] = i + 1
        
    while (len(numList) > 0):
        #removes prime numbers
        prime = numList[0]
        print(prime, "is prime")
        numList.remove(prime)
        
        #removes non-prime numbers
        for i in numList:
            if (i % prime == 0):
                numList.remove(i)
main()