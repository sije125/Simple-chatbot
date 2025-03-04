import re  # Importing the regular expression library for pattern matching

# Dictionary of predefined responses based on user input keywords
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! How can I assist you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I am a chatbot created to assist you. But you can call me Heny!",
    "help": "Sure, I'm here to help you. What do you need assistance with?",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! I'm happy to help",
    "default": "I'm not sure I understand. Could you please rephrase?"
}

# Function to generate a response based on user input
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for case-insensitive matching
    for keyword in responses:
        if re.search(keyword, user_input):  # Check if any keyword is present in user input
            return responses[keyword]  # Return the matching response
    
    return responses["default"]  # Return default response if no match is found

# Function to run the chatbot interaction
def chatbot():
    print("Welcome! How can I assist you today? (Type 'bye' to exit)")
    while True:
        user_input = input("You: ")  # Get user input
        if user_input.lower() == "bye":  # Exit condition
            print("Chatbot: Goodbye! Have a great day!")
            break  # Exit the loop

        response = chatbot_response(user_input)  # Get chatbot response
        print(f"Chatbot: {response}")  # Display chatbot response

chatbot()  # Start the chatbot
