schema = {
    "type": "object",
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
            "properties": {
                "providers": {
                    "type": "array",
                    "items": {
                        "type": "object",
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
                "properties": {
                    "name": {"type": "string"},
                    "orcid": {"type": "string"},  # TODO: orcid ID format
                    "github": {"type": "string"},
                },
            },
        },
        "bakery": {"type": "object", "properties": {"id": {"type": "string"}}},
    },
}
