from gendiff.difference import build_diff, prepare_data
from gendiff.parser import parse
from gendiff.formaters import get_formatter


def generate_diff(path_file1: str, path_file2: str,
                  formater: str = 'stylish') -> str:
    data1, format1 = prepare_data(path_file1)
    data2, format2 = prepare_data(path_file2)
    parced_data1 = parse(data1, format1)
    parced_data2 = parse(data2, format2)
    diff = build_diff(parced_data1, parced_data2)
    return get_formatter(formater)(diff)
