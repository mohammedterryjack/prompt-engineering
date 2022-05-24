from typing import List
from csv import DictWriter 
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
