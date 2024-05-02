import json

def parse_arr(arr):
    category = arr.pop(0)
    json_data = {}
    json_data['category'] = category.strip()
    json_data['attributes'] = {}
    for i in range(0, len(arr), 2):
        key = arr[i].strip()
        value = arr[i + 1]
        json_data['attributes'][key] = value
    return json_data

def create_json_file(json_data, file_name):
    with open(f'{file_name}.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)