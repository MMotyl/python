import csv
from typing import IO, Iterator, List, Text, Union, Iterable

def row_iter(source: IO) -> Iterator[List[Text]]:
    return csv.reader(source, delimiter="\t")

def head_split_fixed(row_iter: Iterator[List[Text]]) -> Iterator[List[Text]]:
    title = next(row_iter)
    assert (len(title) == 1 and title[0] == "Anscombe's quartet")
    
    heading = next(row_iter)
    assert (len(heading) == 4 and heading == ['I', 'II', 'III', 'IV'])
    
    columns = next(row_iter)
    assert (len(columns) == 8 and columns == ['x','y', 'x','y', 'x','y', 'x','y'])
    
    return row_iter

path = 'D:\\Programowanie\\GIT_Python\\python\\testy\\test.csv'
with open(path) as source:
    print(list(head_split_fixed(row_iter(source))))