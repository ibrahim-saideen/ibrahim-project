from abc import ABC, abstractmethod
from typing import Any , Protocol


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.lst: list[str] = []
        self.show_count = 0
        self.total = 0

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
            self.total += 1
        if isinstance(data, list):
            for item in data:
                self.lst.append(str(item))
                self.total += 1


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
            self.total += 1
        else:
            self.lst.extend(data)
            self.total += len(data)


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
                self.total += 1
                i += 2

        if isinstance(data, list):
            for dic in data:
                lst_val = list(dic.values())
                for i in range(len(lst_val) - 1):
                    self.lst.append(lst_val[i] + ': ' + lst_val[i + 1])
                    self.total += 1
                    i += 2


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass        


class DataStream():
    def __init__(self) -> None:
        self.processors:list[DataProcessor] = []


    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)


    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            x = 1
            for processor in self.processors:
                if processor.validate(item):
                    processor.ingest(item) 
                    x = 0
            if x :
                print(f'DataStream error - Can’t process element in stream: {item}')


    def print_processors_stats(self) -> None:
        print('\n== DataStream statistics ==')
        if self.processors == []:
            print('No processor found, no data\n')
            return
        for processor in self.processors:
            if isinstance(processor, NumericProcessor):
                print('Numeric Processor: ', end = '')
            elif isinstance(processor, TextProcessor):
                print('Text Processor: ', end = '')
            elif isinstance(processor, LogProcessor):
                print('Log Processor: ', end = '')
            print(f' total {processor.total} items processed , '
                  f'remaining {processor.total - processor.show_count} on processer')

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        lst_tbl: list[tuple[int, str]] = []
        for processor in self.processors:
            for i in range(nb):
                if processor.lst == []:
                    break
                lst_tbl.append(processor.output())
            plugin.process_output(lst_tbl)
            lst_tbl.clear()
    


class CSV():

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print('CSV Output:')
        for item in data:
            print(item[1],end=',')
        print('')


class JSON():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        dic = {}
        print('JSON Output:')
        for item in data:
            dic.update({f'item_{item[0]}':f'{item[1]}'})
            


def main() -> None:
   print('=== Code Nexus - Data Pipeline ===\n')
   stream = DataStream()
   stream.print_processors_stats()
   stream.register_processor(NumericProcessor())
   stream.register_processor(TextProcessor())
   stream.register_processor(LogProcessor())
   lst = [
          'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
            42,
            ['Hi', 'five']
        ]
   stream.process_stream(lst)
   stream.print_processors_stats()
   stream.output_pipeline(3, CSV())
   
    




if __name__ == '__main__':
    main()
