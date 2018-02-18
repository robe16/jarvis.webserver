from jsonschema import validate
import json
import os


def validate_tv_lg_netcast(inpt):
    schema = _get_schema('tv_lg_netcast')
    return _validate_schema(inpt, schema)


def validate_virginmedia_tivo(inpt):
    schema = _get_schema('virginmedia_tivo')
    return _validate_schema(inpt, schema)


def validate_nest(inpt):
    schema = _get_schema('nest')
    return _validate_schema(inpt, schema)


def _validate_schema(inpt, schema):
    try:
        validate(inpt, schema)
        return True
    except Exception as e:
        return False


def _get_schema(filename):
    #
    filename = '{filename}.schema.json'.format(filename=filename)
    #
    with open(os.path.join(os.path.dirname(__file__), 'schemas', filename), 'r') as data_file:
        return json.load(data_file)
