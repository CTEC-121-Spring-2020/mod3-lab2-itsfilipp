# MyLibrary.py

def function1():
    print("___name___:", __name__)
    print("Function 1")

def function2(inValue):
    print("___name___:", __name__)
    print("Function 2")
    if inValue > 10:
        print("invalid")
    else:
        print("inValue:", inValue)
    

def unitTest():
    print("unit test")
    function1()
    function2(5)
    function2(10)
    function2(11)

if __name__ == "__main__":
    unitTest()