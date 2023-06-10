from typing import Dict, List
from typing import Tuple
from os.path import splitext

EXTENSIONS = ('yaml', 'yml', 'json')


def prepare_data(path_file: str) -> Tuple[str, str]:
    extension = splitext(path_file)[1][1:]
    if extension in EXTENSIONS:
        with open(path_file) as f:
            data = f.read()
            return data, extension
    raise ValueError(f"Unrecognized extension: {extension}")

def build_diff(parced_data1: Dict, parced_data2: Dict) -> List[Dict]:
    diff = list()
    sorted_keys = sorted(
        list(set(parced_data1.keys()) | set(parced_data2.keys()))
    )
    for key in sorted_keys:
        if key not in parced_data1:
            diff.append({
                'key': key,
                'operation': 'add',
                'new': parced_data2[key]
            })
        elif key not in parced_data2:
            diff.append({
                'key': key,
                'operation': 'removed',
                'old': parced_data1[key]
            })
        elif isinstance(parced_data1[key], dict) and isinstance(
                parced_data2[key], dict):
            child = build_diff(parced_data1[key], parced_data2[key])
            diff.append({
                'key': key,
                'operation': 'nested',
                'value': child
            })
        elif parced_data1[key] == parced_data2[key]:
            diff.append({
                'key': key,
                'operation': 'same',
                'value': parced_data1[key]
            })
        elif parced_data1[key] != parced_data2[key]:
            diff.append({
                'key': key,
                'operation': 'changed',
                'old': parced_data1[key],
                'new': parced_data2[key]
            })
    return diff
