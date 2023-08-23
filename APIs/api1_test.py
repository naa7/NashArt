import api1

chat = []

while True:
    prompt = input("You: ")
    
    response = api1.Completion.create(
        prompt  = prompt,
        chat    = chat)
    
    print("Bot:", response["response"])
    
    chat.append({"question": prompt, "answer": response["response"]})
