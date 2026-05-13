import random
import typing


def gen_event():
    rand_names  = ['alice', 'bob', 'charlie', 'dylan']
    rand_actions = ['run', 'sleep', 'move', 'grab', 'climp', 'swim', 'eat', 'release']
    for _ in range(1000):
        tbl=(
          random.choice(rand_names),
          random.choice(rand_actions)
        )
        yield tbl


def main() ->None :
    events = gen_event()
    for i in range(1000):
        tbl = next(events)
        print(f'Event {i}:  ',end='')
        print(f'Player {tbl[0]} did action {tbl[1]}')
    



if __name__ == '__main__':
    main()