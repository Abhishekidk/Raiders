def get_response(intents_list, intents_json):
    tag=intents_list[0]['intent']
    list_of_intents=intents_json['intents']
    for i in list_of_intents:
        if i['tag']==tag:
            result=random.choice(i['responses'])
            break
        return result

print("GO! Bot is running")

while True:
    message=input("")
    ints=predict_class(message)
    res=get_response(ints, intents)
    print(res)