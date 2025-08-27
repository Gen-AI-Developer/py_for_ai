import time
def connect()->None:
    print("Establishing connection...")
    time.sleep(2)
    print("Connection established.")

if __name__=="__main__":
    connect()