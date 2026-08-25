import random

def simple_chatbot():
    responses = {
        "hello": "Hi",
        "how are you":"I,m fine,Thanks",

        "bye": "Goodbye!"
    }

    print("🤖 PyBot: Hi! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "bye" in user_input:
            print("🤖 PyBot:",responses["bye"])
            break

        # Check if any keyword matches
        found = False
        for keyword in responses:
            if keyword in user_input:
                print("🤖 PyBot:", random.choice(responses[keyword]))
                found = True
                break

        if not found:
            print("🤖 PyBot: I don't understand. Type 'help'.")

simple_chatbot()