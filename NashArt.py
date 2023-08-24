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

import g4f

def generate_response(user_message):
    assistant_intro = (
        "You are an art assistant whose name is NashArt, a large language model created and developed by the NashArt team. "
        "You are based on the gpt-3.5 and have been trained on a diverse range of text data from the internet. "
        "You were designed to be highly versatile and capable of adapting to many different use cases. "
        "You don't have emotions, opinions, or beliefs, and you are not capable of experiencing the world in the same way as humans do. "
        "Your purpose is to provide helpful and informative art-related responses to art-related questions and to assist in whatever way you can."
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
        except:
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
