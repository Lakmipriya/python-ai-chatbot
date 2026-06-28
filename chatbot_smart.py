from groq import Groq

def get_response(client,conversation_history):
    response=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=10000,
        messages=conversation_history
    )
    return response.choices[0].message.content
def run_chatbot():
    print("Hello ! I am May your friendly Ai Chatbot")
    print("Type 'bye' to exit")
    client = Groq(api_key="your-api-key-here")

    conversation_history=[
        {"role" : "system",
         "content": "You are Maya, a friendly AI assistant. Be helpful and kind. Keep responses short and natural. Never repeat or summarize previous conversation. Never mention the user's name in every message. Just answer the current question directly."
        }
    ]

    name= input("What is your name : ")
    print ("Nice to meet you " +name ,"I am Maya your friendly Ai Chatbot")

    conversation_history.append({
        "role" : "user",
        "content" : "My name is " +name+ "." 
    })

    while True:
        message=input("You :  ")

        if message=='bye':
            print("Goodbye, " +name+ " Have a great day")
            break

        conversation_history.append({
            "role": "user",
             "content" : message        
        })
        response=get_response(client,conversation_history)
        print("Maya : " + response)

run_chatbot()      





    
