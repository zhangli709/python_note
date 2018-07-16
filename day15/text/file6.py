import json

def main():
    mydict = {
        'name': '骆昊 ',
        'qq': 34654,
        'age': 38,
        'friends': [
            {'brand': 'Auto', 'max_speed': 123},
            {'brand': 'QQ', 'max_speed': 100},
            {'brand': 'Benz', 'max_speed': 90}
        ]
    }
    try:
        with open('date.json', 'r', encoding='utf-8') as fs:
            json.load(fs)

    except IOError as e:
        print(e)


if __name__ == '__main__':
    main()