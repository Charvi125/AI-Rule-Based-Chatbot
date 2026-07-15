print(" AI Chatbot")
print("Type 'exit' to end the chat.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you?")

    elif user == "how are you":
        print("Bot: I am doing great. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: My name is RuleBot.")

    elif user == "who created you":
        print("Bot: I was created using Python and if-else statements.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "what can you do":
        print("Bot: I can answer simple predefined questions.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    elif user == "exit":
        print("Bot: Chat ended.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")

sample output
🤖 AI Chatbot
Type 'exit' to end the chat.

You: Hello
Bot: Hello! How can I help you?

You: What is AI
Bot: AI stands for Artificial Intelligence.

You: How are you
Bot: I am doing great. Thanks for asking!

You: What is your name
Bot: My name is RuleBot.

You: Bye
Bot: Goodbye! Have a nice day.
