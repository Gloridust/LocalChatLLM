import ollama

def response_text(message):
    # modelname = 'gemma-7b'
    modelname = 'qwen:14b'
    response = ollama.chat(
        model = modelname, 
        messages = message,
        stream = False,
        )
    output_text = response['message']['content']
    message_list = response['message']
    # Parse model output
    return (output_text,message_list)
    # for chunk in response_text:
    #     yield chunk['message']['content']

message_lists = []
while True:
    user_input_text = input("Input:")
    message = {'role': 'user', 'content': user_input_text}
    message_lists.append(message)
    output_text, message_list = response_text(message_lists)
    message_lists.append(message_list)
    print(output_text)
    print(message_lists)
