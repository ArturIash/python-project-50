import json
import yaml


def parse(data: str, format: str) -> dict:
    if format in ('yml', 'yaml'):
        return yaml.safe_load(data)
    if format == 'json':
        return json.loads(data)
    raise ValueError(f"Unrecognized extension: {format}")


def build_diff(parced_data1: dict, parced_data2: dict) -> list[dict]:
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