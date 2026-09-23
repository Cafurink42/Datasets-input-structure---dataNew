import json

lista = []
while True:
    data01 = input("Input do usuário:")
    data02 = input("Output do modelo:")
    if data02 == 'sair':
        break
    dataset = (f'{{"instruction": "{data01}", "input": "", "output": "{data02}"}}')
    lista.append(dataset)
    print (f"Total de instruções:{(len(lista))}")
    

    #dataset02 = (f'{{"instruction": "{data01}", "input": "", "output": "{data02}"}}')

json_string = json.dumps(lista)
json_string = [json.loads(i) for i in lista]

with open("DATASETS/output.json", "w", encoding="utf-8") as file:
    json.dump(json_string, file, indent=4, ensure_ascii=False)



    
#{"instruction": "", "input":"", "output": ""}