def hospital_chatbot():
    print("Welcome to our Hospital Chatbot!")
    print("Here are some questions you might ask:")
    print("1. How do I book an appointment?")
    print("2. What are your operating hours?")
    print("3. Where are you located?")
    print("Type the number of your question or type 'quit' to end the chat.")
    
    while True:
        user_message = input("You: ")
        if user_message.lower() == "quit":
            break
        elif user_message == "1":
            print("Bot: To book an appointment, please call our hotline at 123-456-7890.")
        elif user_message == "2":
            print("Bot: We are open from 8:00 AM to 5:00 PM from Monday to Friday.")
        elif user_message == "3":
            print("Bot: We are located at 123 Hospital Street.")
        else:
            print("Bot: Sorry, I didn't understand that. Can you please choose a number from the list?")

if __name__ == "__main__":
    hospital_chatbot()
