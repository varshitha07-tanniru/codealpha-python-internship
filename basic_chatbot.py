def fun1():
    print("Hello")
def fun2():
    print("I'm fine, thanks!")
def fun3():
    print("GoodBye!!")
print("BASIC CHATBOX:")
print("Hello!! how can i help you")
print("Type 'hello', 'how are you', or 'bye' to chat.")
while True:
    user=input().lower()
    if user in ["hello", "hi", "hey"]:
        fun1()
    elif(user=="how are you"):
        fun2()
    elif(user=="bye"):
        fun3()
        break
    else:
        print("Sorry,I did'nt understand")

    


