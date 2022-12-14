from jsonschema import validate

from meta_yaml_schema.schema import schema


def test_schema_valid(valid_meta_yaml):
    validate(valid_meta_yaml, schema=schema)
