command=""
is_started=False
while True:
    command=input("Enter a command (help for details)  \n >>>>>").lower()
    
    if command=="start":
        if is_started:
            print("car is already started, try another command")
        else:print("car started. enjoy your ride.....")
        is_started=True
                
    elif command =="stop":
        if not is_started:
            print("car is already stopped, try another command")
        else:is_started=False
           
    elif command=="help":
        print(
    """"
    start- To start the car
    stop- To stopped the car
    quit- To terminate the program
    """
        )
        command=input("Enter a command (help for details)  \n >>>>>").lower()
        if command =="help":
              print("select from the above options.")

        
    elif command=="quit":
        break
    else:
        print("i dont understand your command!")
        