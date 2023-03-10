def get_file_name(items: list) -> str:
    longest_item = max(items, key=len)
    file_name_length = len(longest_item)
    unique_symbols = _get_unique_symbols(longest_item)
    count_ = file_name_length - len(unique_symbols)
    return unique_symbols + count_*'_'


def _get_unique_symbols(name:str) ->  str:
    unique_symbols = []
    for symbol in name:
        if symbol not in unique_symbols:
            unique_symbols.append(symbol)
    return ''.join(unique_symbols)
