from typing import Any, Dict, List
import json as json_global

def render_json(diff: List[Dict[str, Any]]) -> str:
    return json_global.dumps(diff)
