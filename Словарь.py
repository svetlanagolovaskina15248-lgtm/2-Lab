import xml.etree.ElementTree as ET

def parse_currency_data(currency_file):
    currency_file.seek(0)
    
    content = currency_file.read()
    content = content.decode('windows-1251')
    root = ET.fromstring(content) # Преобразуем текстовую строку в XML структуру
    
    currency_dict = {}  # результат
    
    for valute in root.findall('Valute'):
        name = valute.find('Name').text
        value_str = valute.find('Value').text
        
        value = float(value_str.replace(',', '.'))  # Преобразуем строку с курсом в формат для Python
        
        currency_dict[name] = value
    
    return currency_dict

if __name__ == '__main__':
    with open("currency.xml", 'rb') as currency_file:
        currency_data = parse_currency_data(currency_file)
        
        print("Словарь 'Name - Value':")
        for name, value in currency_data.items():   # Проходим по всем элементам словаря
            print(f"{name}: {value}")
        
        print(f"\nВсего валют: {len(currency_data)}")
