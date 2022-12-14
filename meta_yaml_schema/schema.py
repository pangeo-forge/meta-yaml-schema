schema = {
    "type": "object",
    "required": [
        "title",
        "description",
        "pangeo_forge_version",
        "pangeo_notebook_version",
        "recipes",
        "provenance",
        "maintainers",
        "bakery",
    ],
    "properties": {
        "title": {"type": "string"},
        "description": {"type": "string"},
        # TODO: semantic version format
        "pangeo_forge_version": {"type": "string"},
        # TODO: convert to image tag
        "pangeo_notebook_version": {"type": "string"},
        "recipes": {
            # TODO: can also be dict_object, doing array first
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "id",
                    "object",
                ],
                "properties": {
                    "id": {"type": "string"},
                    "object": {
                        "type": "string"
                    },  # TODO: format as, e.g., 'recipe:recipe'
                },
            },
        },
        "provenance": {
            "type": "object",
            "required": [
                "providers",
                "license",
            ],
            "properties": {
                "providers": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": [
                            "name",
                            "description",
                            "roles",
                            "url",
                        ],
                        "properties": {
                            "name": {"type": "string"},
                            "description": {"type": "string"},
                            "roles": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },  # TODO: one of 'producer', 'licensor', etc.
                            },
                            "url": {"type": "string"},  # TODO: http url format
                        },
                    },
                },
                "license": {
                    "type": "string"
                },  # TODO: one of valid list, or custom object
            },
        },
        "maintainers": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "name",
                    "orcid",
                    "github",
                ],
                "properties": {
                    "name": {"type": "string"},
                    "orcid": {"type": "string"},  # TODO: orcid ID format
                    "github": {"type": "string"},
                },
            },
        },
        "bakery": {
            "type": "object",
            "required": [
                "id",
            ],
            "properties": {"id": {"type": "string"}},
        },
    },
}
