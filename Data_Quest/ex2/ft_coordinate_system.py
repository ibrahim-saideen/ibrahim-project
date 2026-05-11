import math


def calc_destance(tbl1,tbl2=(0,0,0)) -> float:
    val1 = tbl1[0] - tbl2[0]
    val2 = tbl1[1] - tbl2[1]
    val3 = tbl1[2] - tbl2[2]
    sum = val1**2 + val2**2 + val3**2
    return round(math.sqrt(sum),4)


def check_input(inpt) -> bool:
    lst = inpt.split(',')
    i = 0
    while i < len(lst):
        lst[i] = lst[i].strip()
        try:
            float(lst[i])
        except ValueError:
            print('Invalid syntax')
            return True
        i+=1
    return False


def get_player_pos():
    inpt = input('Enter new coordinates as floats in format ’x,y,z’: ')
    while check_input(inpt):
        inpt = input('Enter new coordinates as floats in format ’x,y,z’: ')
    lst = inpt.split(',')
    coordinates = tuple(float(x) for x in lst)
    return coordinates    


def main() -> None:
    print('=== Game Coordinate System ===\n')
    print('Get a first set of coordinates')
    coordinates = get_player_pos()
    print(f'Got a first tuple:  {coordinates}')
    print(f'It includes:  X={coordinates[0]},'
          f'Y={coordinates[1]}, Z={coordinates[2]}')
    print(f'Distance to center:  {calc_destance(coordinates)}\n')
    print('Get a second set of coordinates')
    coordinates2 = get_player_pos()


if __name__ == '__main__' :
    main()