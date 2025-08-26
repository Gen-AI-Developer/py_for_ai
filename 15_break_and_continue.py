import time
number : int = 14
while number > 0:
    if number == 2:
        print('Statement is going to break')
        time.sleep(2)
        break
    else:
        print(number)
    number -= 1
    
while number > 0:
    if number == 10:
        print("Skipping 10.")
        # time.sleep(2)
        continue
    print(number)
    number -= 1