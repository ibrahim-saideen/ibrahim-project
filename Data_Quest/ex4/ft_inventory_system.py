import sys


def max_value(equipment) -> str:
    mx = 0
    for key, value in equipment.items():
        if value > mx :
            mx = value
            kk = key
    return kk


def min_value(equipment) -> str:
    mn = 10000000
    for key, value in equipment.items():
        if value < mn :
            mn = value
            kk = key
    return kk


def handle_data() -> None | dict:
    if len(sys.argv) < 2:
        print('Enter some data 7abebe like this format ->  <item_name>:<quantity> ...')
        return
    equipment = {}
    data = []
    i = 1
    while i < len(sys.argv):
        data.append(sys.argv[i].strip())
        i += 1
    i = 0
    while i < len(data):
        if ':' not in data[i]:
            print(f'Error - invalid parameter ’{data[i]}’')
            i += 1
            continue
        try :
            splt = data[i].split(':')
            val = int(splt[1])
        except ValueError as e:
            print(f'Quantity error for  ’{splt[0]}’:  {e}')
            i += 1
            continue
        if splt[0] not in equipment:
            equipment.update({splt[0] : val})
        else:
            print(f'Redundant item ’{splt[0]}’ - discarding')
        i += 1
    return equipment
        

def main() -> None:
    print('=== Inventory System Analysis ===')
    equipment = handle_data()
    if equipment == None:
        return
    print(f'Got inventory:  {equipment}')
    print(f'Item list:  {equipment.keys()}')
    print(f'Total quantity of the {len(equipment)} items:'
          f'{sum(equipment.values())}')
    for key, value in equipment.items():
        rep = round((value / sum(equipment.values()) * 100),1)
        print(f'Item {key} represents {rep}%')
    print(f'Item most abundant:  {max_value(equipment)} with' 
          f' quantity {equipment[max_value(equipment)]}')
    print(f'Item least abundant:  {min_value(equipment)} with' 
          f' quantity {equipment[min_value(equipment)]}')
    equipment.update({'magic_item' : 1})
    print(f'Updated inventory:  {equipment}')


if __name__ == '__main__':
    main()
