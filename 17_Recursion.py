import time
# def greet():
#     print('----------------------')
#     print("Hello, Programmers")
#     print('----------------------')
#     time.sleep(2)
#     greet()
# greet()
def connection_to_internet(signal:bool,delay:int) -> None:
    if delay >= 5:
        signal = True
    if signal:
        print("Connected....","this","what","wish",end='*****',sep=':',flush=True)
    else:
        print(f"Please wait Connection Failed Trying again for {delay}...")
        time.sleep(delay)
        connection_to_internet(False,delay+1)

connection_to_internet(False,0)
        
        