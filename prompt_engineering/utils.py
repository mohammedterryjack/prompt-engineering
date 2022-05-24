from typing import List
from csv import DictWriter, DictReader
from io import StringIO 

def to_csv(data:List[dict], column_names:List[str], delimiter:str=",") -> str:
    output = StringIO() 
    writer = DictWriter(
        output, 
        fieldnames=[] if column_names is None else column_names,
        delimiter=delimiter
    )
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()

def from_csv(lines:List[str], delimiter:str=",") -> List[dict]:
    return list(DictReader(lines,delimiter=delimiter))