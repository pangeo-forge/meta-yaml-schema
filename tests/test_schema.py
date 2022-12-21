import copy

import pytest
from jsonschema import ValidationError, validate

from meta_yaml_schema.schema import schema


def test_schema_valid(valid_meta_yaml):
    validate(valid_meta_yaml, schema=schema)


def test_schema_valid_dict_object(valid_meta_yaml_dict_object):
    validate(valid_meta_yaml_dict_object, schema=schema)


@pytest.mark.parametrize(
    "field",
    [
        "title",
        "description",
        "pangeo_forge_version",
        "pangeo_notebook_version",
        "recipes",
        "provenance",
        "maintainers",
        "bakery",
    ],
)
def test_missing_toplevel_field(valid_meta_yaml, field):
    invalid_meta_yaml = copy.deepcopy(valid_meta_yaml)
    del invalid_meta_yaml[field]
    with pytest.raises(ValidationError, match=f"'{field}' is a required property"):
        validate(invalid_meta_yaml, schema=schema)


@pytest.mark.parametrize(
    "subfield",
    [
        "id",
        "object",
    ],
)
def test_missing_recipes_subfield(valid_meta_yaml, subfield):
    invalid_meta_yaml = copy.deepcopy(valid_meta_yaml)
    del invalid_meta_yaml["recipes"][0][subfield]

    with pytest.raises(ValidationError, match=f"'{subfield}' is a required property"):
        validate(invalid_meta_yaml, schema=schema)


@pytest.mark.parametrize(
    "subfield",
    [
        "providers",
        "license",
    ],
)
def test_missing_provenance_subfield(valid_meta_yaml, subfield):
    invalid_meta_yaml = copy.deepcopy(valid_meta_yaml)
    del invalid_meta_yaml["provenance"][subfield]

    with pytest.raises(ValidationError, match=f"'{subfield}' is a required property"):
        validate(invalid_meta_yaml, schema=schema)


@pytest.mark.parametrize(
    "subfield",
    [
        "name",
        "description",
        "roles",
        "url",
    ],
)
def test_missing_providers_subfield(valid_meta_yaml, subfield):
    invalid_meta_yaml = copy.deepcopy(valid_meta_yaml)
    del invalid_meta_yaml["provenance"]["providers"][0][subfield]

    with pytest.raises(ValidationError, match=f"'{subfield}' is a required property"):
        validate(invalid_meta_yaml, schema=schema)


@pytest.mark.parametrize(
    "subfield",
    [
        "name",
        "orcid",
        "github",
    ],
)
def test_missing_maintainers_subfield(valid_meta_yaml, subfield):
    invalid_meta_yaml = copy.deepcopy(valid_meta_yaml)
    del invalid_meta_yaml["maintainers"][0][subfield]

    with pytest.raises(ValidationError, match=f"'{subfield}' is a required property"):
        validate(invalid_meta_yaml, schema=schema)


@pytest.mark.parametrize(
    "subfield",
    [
        "id",
    ],
)
def test_missing_bakery_subfield(valid_meta_yaml, subfield):
    invalid_meta_yaml = copy.deepcopy(valid_meta_yaml)
    del invalid_meta_yaml["bakery"][subfield]

    with pytest.raises(ValidationError, match=f"'{subfield}' is a required property"):
        validate(invalid_meta_yaml, schema=schema)
