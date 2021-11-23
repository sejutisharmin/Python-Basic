import random
def main():
#write a code to get the random number between 11-22(including)    
    rand = random.randrange(11,22)
 #write a code to determine if the number is even or odd   
    if rand % 2 == 0:
        print(f'{rand} is an even number')
    else:
         print(f'{rand} is an odd number')   

main()

