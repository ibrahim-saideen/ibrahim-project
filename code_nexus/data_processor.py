from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.lst: list[str] = []
        self.show_count = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        num = 0
        data = str(self.lst[num])
        self.lst.pop(num)
        num = self.show_count
        self.show_count += 1
        return (num, data)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        try:
            if not self.validate(data):
                raise ValueError('Got exception: Improper numeric data')
        except ValueError as e:
            print(e)
            return
        if isinstance(data, (int, float)):
            self.lst.append(str(data))
        if isinstance(data, list):
            for item in data:
                self.lst.append(str(item))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (str)):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (str)):
                    return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        try:
            if not self.validate(data):
                raise ValueError('Got exception: Improper numeric data')
        except ValueError as e:
            print(e)
            return
        if isinstance(data, str):
            self.lst.append(str(data))
        else:
            self.lst.extend(data)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str):
                    return False
                if not isinstance(value, str):
                    return False
        elif isinstance(data, list):
            for dic in data:
                if not isinstance(dic, dict):
                    return False
            for dic in data:
                for key, value in dic.items():
                    if not isinstance(key, str):
                        return False
                    if not isinstance(value, str):
                        return False
        else:
            return False
        return True

    def ingest(self, data: Any) -> None:
        try:
            if not self.validate(data):
                raise ValueError('Got exception: Improper numeric data')
        except ValueError as e:
            print(e)
            return

        if isinstance(data, dict):
            lst_val = list(data.values())
            for i in range(len(lst_val) - 1):
                self.lst.append(lst_val[i] + ': ' + lst_val[i + 1])
                i += 2

        if isinstance(data, list):
            for dic in data:
                lst_val = list(dic.values())
                for i in range(len(lst_val) - 1):
                    self.lst.append(lst_val[i] + ': ' + lst_val[i + 1])
                    i += 2


def main() -> None:
    print('=== Code Nexus - Data Processor ===')
    print('Testing Numeric Processor...')
    ob_num = NumericProcessor()
    print(f'Trying to validate input ’42’: {ob_num.validate(42)}')
    print(f'Trying to validate input ’Hello’: {ob_num.validate('Hello')}')
    print('Test invalid ingestion of string '
          '’foo’ without prior validation:')
    ob_num.ingest('foo')
    lst_num = [1, 2, 3, 4, 5]
    print(f'Processing data: {lst_num}')
    ob_num.ingest(lst_num)
    print('Extracting 3 values...')

    for i in range(3):
        tbl = ob_num.output()
        print(f'Numeric value {tbl[0]}: {tbl[1]}')
    print('')
    print('Testing Text Processor...')
    ob_txt = TextProcessor()
    print(f'Trying to validate input ’42’: {ob_txt.validate(42)}')
    lst_txt = ['Hello', 'Nexus', 'World']
    ob_txt.ingest(lst_txt)

    print('Extracting 1 value...')
    for i in range(1):
        tbl = ob_txt.output()
        print(f'Text value {tbl[0]}, {tbl[1]}')

    print('')
    ob_log = LogProcessor()
    print('Testing Log Processor...')
    print(f'Trying to validate input ’Hello’: {ob_log.validate('Hello')}')
    dic = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
           {'log_level': 'ERROR', '’log_message’': 'Unauthorized access!!'}]
    ob_log.ingest(dic)
    print('Extracting 2 values...')
    for i in range(2):
        tbl = ob_log.output()
        print(f'Log entry {tbl[0]}: {tbl[1]}')
    print('')

if __name__ == '__main__':
    main()
