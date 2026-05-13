import random
import typing


def consume_event(lst_of_tbls):
    tbl = ()
    len_lst = len(lst_of_tbls)
    for _ in range(len_lst):
        tbl = random.choice(lst_of_tbls)
        yield tbl


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
    tt = gen_event()
    lst_of_tbls = []
    for _ in range(10):
        tbl = next(tt)
        lst_of_tbls.append(tbl)
    print(f'Built list of 10 events:  {lst_of_tbls}')
    consume = consume_event(lst_of_tbls)
    len_lst = len(lst_of_tbls)
    for _ in range(len_lst):
        tbll = next(consume)
        print(f'Got event from list:  {tbll}')
        lst_of_tbls.remove(tbll)
        print(f'Remains in list:  {lst_of_tbls}')


if __name__ == '__main__':
    main()