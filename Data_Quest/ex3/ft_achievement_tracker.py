import random


def gen_player_achievements() -> set:
    achievements = ('Crafting Genius', 'Strategist', 'World Savior',
                        'Speed Runner', 'Survivor', 'Master Explorer', 
                        'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme',
                        'Untouchable', 'Sharp Mind', 'Boss Slayer','Hidden Path Finder')
    Alice = set() 
    Bob = set()
    Charlie = set()
    Dylan = set()
    items = random.sample(achievements, 7)
    Alice.update(items)
    items.clear()
    items = random.sample(achievements, 7)
    Bob.update(items)
    items.clear()
    items = random.sample(achievements, 10)
    Charlie.update(items)
    items.clear()
    items = random.sample(achievements, 5)
    Dylan.update(items)
    items.clear()
    return Alice, Bob, Charlie, Dylan


def main() -> None:
    print('=== Achievement Tracker System ===\n')
    achievements_tbl = ('Crafting Genius', 'Strategist', 'World Savior',
                        'Speed Runner', 'Survivor', 'Master Explorer', 
                        'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme',
                        'Untouchable', 'Sharp Mind', 'Boss Slayer','Hidden Path Finder')
    achievements = set()
    achievements.update(achievements_tbl)
    Alice = set() 
    Bob = set()
    Charlie = set()
    Dylan = set()
    Alice ,Bob, Charlie, Dylan = gen_player_achievements()
    print(f'Player Alice:  {Alice}')
    print(f'Player Bob:  {Bob}')
    print(f'Player Charlie:  {Charlie}')
    print(f'Player Dylan:  {Dylan}\n')
    distinct = Alice | Bob | Charlie | Dylan
    print(f'All distinct achievements:  {distinct}')
    common = Alice & Bob & Charlie & Dylan
    print(f'Common achievements:  {common}')
    print(f'Only Alice has:  {Alice - Bob - Charlie - Dylan}')
    print(f'Only Bob has:   {Bob - Alice - Charlie - Dylan}')
    print(f'Only Charlie has:  {Charlie - Bob - Alice - Dylan}')
    print(f'Only Dylan has:  {Dylan.difference(Alice ,Bob, Charlie)}\n')
    print(f'Alice is missing:  {achievements - Alice}')
    print(f'Bob is missing:  {achievements - Bob}')
    print(f'Charlie is missing:  {achievements - Charlie}')
    print(f'Dylan is missing:  {achievements - Dylan}')





if __name__ == '__main__':
    main()