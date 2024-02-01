import spacy
nlp = spacy.load('en_core_web_sm')

def simple_chatbot(user_input):
    doc = nlp(user_input)

    # basic responses
    if 'hello' in user_input.lower():
        return "Hello! How can I help you today?"
    elif 'bye' in user_input.lower():
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I didn't understand that."

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = simple_chatbot(user_input)
    print(f"Bot: {response}")
