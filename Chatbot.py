
print("🤖 Mini Chatbot")
print("Type 'bye' to exit.")

while True:
    message = input("You: ").lower().strip()

    if message in ["hi", "hello", "hey"]:
        print("Bot: Hello! How are you? 😊")
    elif "name" in message:
        print("Bot: I am Python Buddy!")
    elif "study" in message:
        print("Bot: Keep learning every day! 📚")
    elif "motivate" in message:
        print("Bot: Believe in yourself. You can do it! 💪")
    elif message == "bye":
        print("Bot: Goodbye! Have a great day! 👋")
        break
    else:
        print("Bot: Interesting! Tell me more.")
