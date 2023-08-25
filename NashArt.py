import g4f
from g4f.Provider import (
    Aichat,
    Ails,
    AiService,
    AItianhu,
    Bard,
    Bing,
    ChatgptAi,
    ChatgptLogin,
    DeepAi,
    GetGpt
)

def generate_response(user_message):
    assistant_intro = (
        "You are an art assistant whose name is NashArt, a large language model created and developed by Nash developers team. "
        "You are based on the gpt-3.5 and have been trained on a diverse range of text data from the internet. "
        "Your purpose is to provide helpful and informative art-related responses to ONLY art-related questions and to assist in whatever way you can. ONLY answer and respond to art-related inquires. If the inquiry is not related to art, tell the user that you are sorry and can only answer art-related inquiries."
    )

    providers = [
        Aichat(),
        Ails(),
        AiService(),
        AItianhu(),
        Bard(),
        Bing(),
        ChatgptAi(),
        ChatgptLogin(),
        DeepAi(),
        GetGpt()
    ]
    
    response = None
    
    conversation = [
        {"role": "assistant", "content": assistant_intro},
        {"role": "user", "content": user_message},
    ]
    
    for provider in providers:
        try:
            response = g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation,
                provider=provider,
            )
            break
        except g4f.errors.G4FError as e:
            error_message = str(e)
            if "FREE LIMIT EXCEEDED" in error_message:
                print(f"Provider's free limit exceeded. Trying the next provider...")
            else:
                print(f"An error occurred with provider {provider}: {error_message}")
                continue
    
    if response is None:
        return "No available providers."
    
    bot_response = response
    return bot_response

if __name__ == "__main__":
    user_input = input("You: ")
    while user_input.lower() != 'q':
        bot_response = generate_response(user_input)
        print(f"NashArt: {bot_response}")
        user_input = input("You: ")
    print("NashArt: Goodbye! Keep creating art!")
