import json
def access_file_function():
    with open('file.json','r') as file:
        syn_dict = json.load(file)
    return syn_dict

syn_dict = access_file_function()

