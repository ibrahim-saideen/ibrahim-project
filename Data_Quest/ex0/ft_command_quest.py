import sys


def main() -> None:
    print('=== Command Quest ===')
    len_argv = len(sys.argv)
    print(f'program name:  {sys.argv[0]}')
    if len(sys.argv) < 2:
        print('No arguments provided!')
        print(f'Total arguments:  {len_argv}')
    else:
        print(f'Arguments received:  {len_argv - 1}')
        i = 1
        while i < len(sys.argv):
            print(f'Argument {i}:  {sys.argv[i]}')
            i += 1
        print(f'Total arguments:  {len_argv}')


if __name__ == '__main__':
    main()
