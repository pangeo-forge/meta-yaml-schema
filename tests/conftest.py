from textwrap import dedent

import pytest
import yaml


@pytest.fixture
def valid_meta_yaml():
    valid_meta_yaml = dedent(
        """\
    title: 'AWS NOAA WHOI SST'
    description: 'Analysis-ready datasets derived from AWS NOAA WHOI NetCDF'
    pangeo_forge_version: '0.9.2'
    pangeo_notebook_version: '2021.07.17'
    recipes:
      - id: aws-noaa-sea-surface-temp-whoi
        object: 'recipe:recipe'
    provenance:
      providers:
        - name: 'AWS NOAA Oceanic CDR'
          description: 'Registry of Open Data on AWS National Oceanographic & Atmospheric Administration National Centers for Environmental Information'
          roles:
            - producer
            - licensor
          url: s3://noaa-cdr-sea-surface-temp-whoi-pds/
      license: 'Open Data'
    maintainers:
      - name: 'Jo Contributor'
        orcid: '0000-0000-0000-0000'
        github: jocontributor123
    bakery:
      id: 'pangeo-ldeo-nsf-earthcube'
    """  # noqa: E501
    )
    return yaml.safe_load(valid_meta_yaml)
