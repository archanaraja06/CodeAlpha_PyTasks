#Simple chatbot

def chatbot():
    print("Hello!I'm Chatbot!")
    print("Type Bye to exit")

    while True:
        user_query=input(f"Me : ").lower().strip()
        
        if user_query == "hello":
            print(f"Bot : Hey there !")
            
        elif user_query == "how are you?":
            print(f"Bot : I'm fine,thanks")

        elif user_query == "bye":
            print(f"Bot : GoodBye!")
            break
        
        else:
            print("Sorry,I don't understand that")

chatbot()

        
        
