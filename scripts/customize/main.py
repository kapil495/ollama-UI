ollama_models = ["deepseek-coder:latest","llama3", "llama3:8b", "llama3:70b", "mistral", "mistral:7b", "gemma", "gemma:2b", "gemma:7b", "phi", "phi:3", "phi:3-mini", "llava", "llava:7b", "codellama", "codellama:7b", "starling", "starling:7b", "neural-chat", "neural-chat:7b", "moondream", "moondream:2", "solar", "solar:10.7b", "llama2-uncensored", "llama2-uncensored:7b"]

def customize_OLLAMA_UI():
    print("cutomize your OLLAMA UI")
    print("i am assuming that ollama is running locally in your device.")
    ollama_Port = ask_Port()
    model_Name = ask_Model_Name()

    print(f"ollama  {ollama_Port} : {model_Name}")
def ask_Port():
    try:
        port = int(input("port on which ollama in running? (default : 11434) >>> "))
    except ValueError:
        port = 11434
    return port
def ask_Model_Name():
    modelName = input("the model you wanna use ?(leave blank to get list of available models) >>> ")
    if modelName == "":
        print("available models are:")
        for model in ollama_models:
            print(model)
        input("any key to return")
        ask_Model_Name()
    elif modelName not in ollama_models:
        print("model not found")
        option = input("want to get list of available models ? (y/n)")
        if option == "y":
            print("available models are:")
            for model in ollama_models:
                print(model)
            ask_Model_Name()
        elif option == "n":
            ask_Model_Name()
    else :
        return modelName

customize_OLLAMA_UI()