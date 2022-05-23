from pandas import DataFrame

format_table = lambda table: ' | '.join(table.keys()) + "\n" + '\n'.join(map(
    lambda data:' | '.join(data.values()),
    DataFrame(table).transpose().to_dict().values()
))