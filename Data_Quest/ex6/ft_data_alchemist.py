import random


def main() -> None:
    print('=== Game Data Alchemist ===\n')
    name_lst = ['Alice', 'bob', 'Charlie', 'dylan',
                'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f'Initial list of players:  {name_lst}')
    full_capitalize_name = [name.capitalize() for name in name_lst]
    print('New list with all names '
          f'capitalized:  {full_capitalize_name}'
          )
    capitalize_name_only = [
                name
                for name in name_lst
                if name.capitalize() == name
            ]
    print(f'New list of capitalized names only:  {capitalize_name_only}')
    first_dict = {
        x: random.randint(0, 1000)
        for x in full_capitalize_name
        }
    print(f'Score dict:  {first_dict}')
    averag = sum(first_dict.values()) / len(first_dict)
    print(f'Score average is {round(averag, 2)}')
    second_dict = {
        x: random.randint(int(averag), 1000)
        for x in full_capitalize_name
        }
    print(f'High scores:  {second_dict}')


if __name__ == '__main__':
    main()
