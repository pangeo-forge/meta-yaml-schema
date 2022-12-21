from typing import Dict, List, Optional, Union

from pydantic import BaseModel, HttpUrl


class RecipeObject(BaseModel):
    id: str  # TODO: require to be unique within meta.yaml namespace
    object: str  # TODO: require format '{module_name}:{recipe_instance_name}'


class RecipeDictObject(BaseModel):
    dict_object: str  # TODO: require format '{module_name}:{dict_instance_name}'


class Provider(BaseModel):
    name: str
    description: str
    roles: List[str]  # TODO: enum choices e.g. Roles.producer, Roles.licensor
    url: HttpUrl


class Provenance(BaseModel):
    providers: List[Provider]
    license: str  # TODO: enum choices e.g. Licenses.cc_by_40 = "CC-BY-4.0" etc.


class Maintainer(BaseModel):
    name: str
    orcid: str  # TODO: format requirement
    github: str  # TODO: allowable characters


class Bakery(BaseModel):
    id: str  # TODO: exists in database


class GithubDependency(BaseModel):
    repo: str
    ref: str


class MetaYaml(BaseModel):
    title: str
    description: str
    pangeo_forge_recipes: Union[str, GithubDependency]
    pangeo_notebook_version: str
    recipes: Union[List[RecipeObject], RecipeDictObject]
    provenance: Provenance
    maintainers: List[Maintainer]
    bakery: Bakery
    extras_require: Optional[Dict[str, Union[str, GithubDependency]]] = None


schema = MetaYaml.schema()
