from abc import ABC, abstractmethod
from typing import Generator

class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: any) -> None:
        pass

    def output(self) -> Generator[tuple[int, str], None, None]:
        if self.ll == True:
            i = 0
            while i < len(self.lst):
                yield (i,self.lst[i])
                i += 1
        else:
            yield (0,self.strng)

class NumericProcessor(DataProcessor):
    def validate(self, data: any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        return False


    def ingest(self, data: any) -> None:
        try:
            if not self.validate(data):
                raise ValueError('Got exception: Improper numeric data')
        except ValueError as e:
            print(e)
            return
        if isinstance(data, (int, float)):
            self.strng = str(data)
            self.ll = False
        else:
            self.ll = True
        if isinstance(data, list):
            self.lst = []
            for item in data:
                self.lst.append(str(item))


class TextProcessor(DataProcessor):
    def validate(self, data: any) -> bool:
        if isinstance(data, (str)):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (str)):
                    return False
            return True
        return False


    def ingest(self, data: any) -> None:
        try:
            if not self.validate(data):
                raise ValueError('Got exception: Improper numeric data')
        except ValueError as e:
            print(e)
            return
        if isinstance(data, str):
            self.strng = data
            self.ll = False
        else:
            self.ll = True
        if isinstance(data, list):
            self.lst = data




class LogProcessor(DataProcessor):
    pass


def main() -> None:
    print('=== Code Nexus - Data Processor ===')
    print('Testing Numeric Processor...')
    ob = NumericProcessor()
    print(f'Trying to validate input ’42’: {ob.validate(42)}')
    print(f'Trying to validate input ’Hello’: {ob.validate('hello')}')
    print('Test invalid ingestion of string ’foo’ without prior validation: ')
    ob.ingest('foo')
    print(f'Processing data: {[1, 2, 3, 4, 5]}')
    ob.ingest([1, 2, 3, 4, 5])
    x = ob.output()
    print('Extracting 3 values...')
    for i in range(3):
        tbl = next(x)
        print(f'Numeric value {tbl[0]}:  {tbl[1]}')
    print('\nTesting Text Processor...')
    ob = TextProcessor()
    print(f'Trying to validate input ’42’: {ob.validate(42)}')
    lst = ['Hello', 'Nexus', 'World']
    print(f'Processing data:  {lst}')
    ob.ingest(lst)
    print('Extracting 1 value...')
    x = ob.output()
    for i in range(1):
        tbl = next(x)
        print(f'Text value {tbl[0]}:  {tbl[1]}')




if __name__ == '__main__':
    main()
