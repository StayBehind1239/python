def collatz(number):

        while number != 1:
                
                if number % 2 == 0:
                        number = number // 2
                        print(number)

                elif number % 2 == 1:
                        number = 3 * number + 1
                        print(number)
                        

try:
        print('the simplest impossible math problem... give me number and i will show you ^^')
        newnumber = int(input())
        collatz(newnumber)
except ValueError:
        print('Maybe you should use an integer ^^')
