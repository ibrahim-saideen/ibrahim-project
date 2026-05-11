import sys


def average(lst) -> float:
    av = sum(lst) / len(lst)
    return av


def main() -> None:
    print('=== Player Score Analytics ===')
    if len(sys.argv) < 2:
        print('No scores provided. Usage:'
              ' python3 ft_score_analytics.py <score1> <score2> ...')
        return
    lst = []
    i = 1
    while i < len(sys.argv):
        try:
            if sys.argv[i].isnumeric():
                lst.append(int(sys.argv[i]))
            else:
                raise ValueError(f'Invalid parameter:  ’{sys.argv[i]}’')
        except ValueError as e:
            print(e)
        i+=1
    if len(lst) < 1:
        print('No scores provided. Usage:'
              ' python3 ft_score_analytics.py <score1> <score2> ...')
    else:
        print(f'Scores processed:  {lst}')
        print(f'Total players:  {len(lst)}')
        print(f'Total score:  {sum(lst)}')
        print(f'Average score:  {average(lst)}')
        print(f'High score:  {max(lst)}')
        print(f'Low score:  {min(lst)}')
        print(f'Score range:  {max(lst) - min(lst)}')







if __name__ == '__main__':
    main()