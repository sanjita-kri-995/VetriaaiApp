import json

from sqlalchemy.inspection import inspect

def serialize_model(obj):
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

def serialize_list(obj_list):
    return [serialize_model(obj) for obj in obj_list]

def list_to_json(obj_list):
    return json.dumps(serialize_list(obj_list), indent=2)

def obj_to_json(obj):
    return json.dumps(serialize_model(obj), indent=2)
