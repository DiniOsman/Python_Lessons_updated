def ask_for_passcode(fun):
    def inner():
        print("what is your passcode: ")
        passcode = input()
        if passcode != '1234':
            print("wrong passcode: ")
        else:
            print("print access granted")
            fun()
            return inner()
@ask_for_passcode

def start():
    print("start has been started: ")
    
@ask_for_passcode
def end():
    print("server has been stopped: ")
    
        
    start()
    end()    
    