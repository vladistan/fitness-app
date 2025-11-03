from __future__ import annotations

from datetime import date
from typing import Any, ClassVar, Optional

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    model_serializer,
)


metamodel_version = "None"
version = "0.0.1"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias=True,
        validate_by_name=True,
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        arbitrary_types_allowed=True,
        use_enum_values=True,
        strict=False,
    )

    @model_serializer(mode="wrap", when_used="unless-none")
    def treat_empty_lists_as_none(
        self, handler: SerializerFunctionWrapHandler, info: SerializationInfo
    ) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not (field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)


class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key: str):
        return getattr(self.root, key)

    def __getitem__(self, key: str):
        return self.root[key]

    def __setitem__(self, key: str, value):
        self.root[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta(
    {
        "default_prefix": "fit",
        "description": "Schema for the fitness tracking platform",
        "id": "fitness-schema",
        "imports": ["linkml:types"],
        "name": "fitness-app",
        "prefixes": {
            "dc": {
                "prefix_prefix": "dc",
                "prefix_reference": "http://purl.org/dc/elements/1.1/",
            },
            "dcterms": {
                "prefix_prefix": "dcterms",
                "prefix_reference": "http://purl.org/dc/terms/",
            },
            "fit": {
                "prefix_prefix": "fit",
                "prefix_reference": "https://example.org/fit/",
            },
            "linkml": {
                "prefix_prefix": "linkml",
                "prefix_reference": "https://w3id.org/linkml/",
            },
            "prov": {
                "prefix_prefix": "prov",
                "prefix_reference": "http://www.w3.org/ns/prov#",
            },
            "rdf": {
                "prefix_prefix": "rdf",
                "prefix_reference": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            },
            "rdfs": {
                "prefix_prefix": "rdfs",
                "prefix_reference": "http://www.w3.org/2000/01/rdf-schema#",
            },
        },
        "source_file": "src/linkml_fitness_app/schema/linkml_fitness_app.yaml",
    }
)


class Thing(ConfiguredBaseModel):
    """
    The root class for all entities in the fitness app
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "fitness-schema"})

    id: int = Field(
        default=..., json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}}
    )


class User(Thing):
    """
    A registered app user
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "fitness-schema"})

    name: Optional[str] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"domain_of": ["User", "Exercise"]}},
    )
    email: Optional[str] = Field(
        default=None, json_schema_extra={"linkml_meta": {"domain_of": ["User"]}}
    )
    age: Optional[int] = Field(
        default=None, json_schema_extra={"linkml_meta": {"domain_of": ["User"]}}
    )
    workouts: Optional[list[int]] = Field(
        default=[], json_schema_extra={"linkml_meta": {"domain_of": ["User"]}}
    )
    id: int = Field(
        default=..., json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}}
    )


class Workout(Thing):
    """
    A recorded workout session
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "fitness-schema"})

    workout_date: Optional[date] = Field(
        default=None, json_schema_extra={"linkml_meta": {"domain_of": ["Workout"]}}
    )
    duration: Optional[float] = Field(
        default=None, json_schema_extra={"linkml_meta": {"domain_of": ["Workout"]}}
    )
    exercises: Optional[list[int]] = Field(
        default=[], json_schema_extra={"linkml_meta": {"domain_of": ["Workout"]}}
    )
    id: int = Field(
        default=..., json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}}
    )


class Exercise(Thing):
    """
    Individual exercise performed
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({"from_schema": "fitness-schema"})

    name: Optional[str] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"domain_of": ["User", "Exercise"]}},
    )
    sets: Optional[int] = Field(
        default=None, json_schema_extra={"linkml_meta": {"domain_of": ["Exercise"]}}
    )
    reps: Optional[int] = Field(
        default=None, json_schema_extra={"linkml_meta": {"domain_of": ["Exercise"]}}
    )
    weight: Optional[float] = Field(
        default=None, json_schema_extra={"linkml_meta": {"domain_of": ["Exercise"]}}
    )
    id: int = Field(
        default=..., json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}}
    )


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Thing.model_rebuild()
User.model_rebuild()
Workout.model_rebuild()
Exercise.model_rebuild()
