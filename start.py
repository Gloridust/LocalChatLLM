import ollama

def get_response(message):
    model_name = 'qwen:14b'
    response = ollama.chat(
        model=model_name, 
        messages=message,
        stream=False,
    )
    output_text = response['message']['content']
    received_message = response['message']
    return output_text, received_message

message_history = []
while True:
    user_input_text = input("Input:")
    message = {'role': 'user', 'content': user_input_text}
    message_history.append(message)
    output_text, received_message = get_response(message_history)
    message_history.append(received_message)
    print(output_text)
    # print(message_history)
