# Auto generated from linkml_fitness_app.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-11-02T20:57:42
# Schema: fitness-app
#
# id: fitness-schema
# description: Schema for the fitness tracking platform
# license: https://creativecommons.org/publicdomain/zero/1.0/

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.metamodelcore import empty_list
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_int
from rdflib import URIRef

from linkml_runtime.utils.metamodelcore import XSDDate

metamodel_version = "1.7.0"
version = "0.0.1"

# Namespaces
DC = CurieNamespace("dc", "http://purl.org/dc/elements/1.1/")
DCTERMS = CurieNamespace("dcterms", "http://purl.org/dc/terms/")
FIT = CurieNamespace("fit", "https://example.org/fit/")
LINKML = CurieNamespace("linkml", "https://w3id.org/linkml/")
PROV = CurieNamespace("prov", "http://www.w3.org/ns/prov#")
RDF = CurieNamespace("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = CurieNamespace("rdfs", "http://www.w3.org/2000/01/rdf-schema#")
DEFAULT_ = FIT


# Types


# Class references
class ThingId(extended_int):
    pass


class UserId(ThingId):
    pass


class WorkoutId(ThingId):
    pass


class ExerciseId(ThingId):
    pass


@dataclass(repr=False)
class Thing(YAMLRoot):
    """
    The root class for all entities in the fitness app
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIT["Thing"]
    class_class_curie: ClassVar[str] = "fit:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = FIT.Thing

    id: Union[int, ThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThingId):
            self.id = ThingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class User(Thing):
    """
    A registered app user
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIT["User"]
    class_class_curie: ClassVar[str] = "fit:User"
    class_name: ClassVar[str] = "User"
    class_model_uri: ClassVar[URIRef] = FIT.User

    id: Union[int, UserId] = None
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    workouts: Optional[Union[Union[int, WorkoutId], list[Union[int, WorkoutId]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UserId):
            self.id = UserId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.age is not None and not isinstance(self.age, int):
            self.age = int(self.age)

        if not isinstance(self.workouts, list):
            self.workouts = [self.workouts] if self.workouts is not None else []
        self.workouts = [
            v if isinstance(v, WorkoutId) else WorkoutId(v) for v in self.workouts
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Workout(Thing):
    """
    A recorded workout session
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIT["Workout"]
    class_class_curie: ClassVar[str] = "fit:Workout"
    class_name: ClassVar[str] = "Workout"
    class_model_uri: ClassVar[URIRef] = FIT.Workout

    id: Union[int, WorkoutId] = None
    workout_date: Optional[Union[str, XSDDate]] = None
    duration: Optional[float] = None
    exercises: Optional[Union[Union[int, ExerciseId], list[Union[int, ExerciseId]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkoutId):
            self.id = WorkoutId(self.id)

        if self.workout_date is not None and not isinstance(self.workout_date, XSDDate):
            self.workout_date = XSDDate(self.workout_date)

        if self.duration is not None and not isinstance(self.duration, float):
            self.duration = float(self.duration)

        if not isinstance(self.exercises, list):
            self.exercises = [self.exercises] if self.exercises is not None else []
        self.exercises = [
            v if isinstance(v, ExerciseId) else ExerciseId(v) for v in self.exercises
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Exercise(Thing):
    """
    Individual exercise performed
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIT["Exercise"]
    class_class_curie: ClassVar[str] = "fit:Exercise"
    class_name: ClassVar[str] = "Exercise"
    class_model_uri: ClassVar[URIRef] = FIT.Exercise

    id: Union[int, ExerciseId] = None
    name: Optional[str] = None
    sets: Optional[int] = None
    reps: Optional[int] = None
    weight: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExerciseId):
            self.id = ExerciseId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.sets is not None and not isinstance(self.sets, int):
            self.sets = int(self.sets)

        if self.reps is not None and not isinstance(self.reps, int):
            self.reps = int(self.reps)

        if self.weight is not None and not isinstance(self.weight, float):
            self.weight = float(self.weight)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass


slots.id = Slot(
    uri=FIT.id,
    name="id",
    curie=FIT.curie("id"),
    model_uri=FIT.id,
    domain=None,
    range=URIRef,
)

slots.name = Slot(
    uri=FIT.name,
    name="name",
    curie=FIT.curie("name"),
    model_uri=FIT.name,
    domain=None,
    range=Optional[str],
)

slots.email = Slot(
    uri=FIT.email,
    name="email",
    curie=FIT.curie("email"),
    model_uri=FIT.email,
    domain=None,
    range=Optional[str],
)

slots.age = Slot(
    uri=FIT.age,
    name="age",
    curie=FIT.curie("age"),
    model_uri=FIT.age,
    domain=None,
    range=Optional[int],
)

slots.workout_date = Slot(
    uri=FIT.workout_date,
    name="workout_date",
    curie=FIT.curie("workout_date"),
    model_uri=FIT.workout_date,
    domain=None,
    range=Optional[Union[str, XSDDate]],
)

slots.duration = Slot(
    uri=FIT.duration,
    name="duration",
    curie=FIT.curie("duration"),
    model_uri=FIT.duration,
    domain=None,
    range=Optional[float],
)

slots.sets = Slot(
    uri=FIT.sets,
    name="sets",
    curie=FIT.curie("sets"),
    model_uri=FIT.sets,
    domain=None,
    range=Optional[int],
)

slots.reps = Slot(
    uri=FIT.reps,
    name="reps",
    curie=FIT.curie("reps"),
    model_uri=FIT.reps,
    domain=None,
    range=Optional[int],
)

slots.weight = Slot(
    uri=FIT.weight,
    name="weight",
    curie=FIT.curie("weight"),
    model_uri=FIT.weight,
    domain=None,
    range=Optional[float],
)

slots.exercises = Slot(
    uri=FIT.exercises,
    name="exercises",
    curie=FIT.curie("exercises"),
    model_uri=FIT.exercises,
    domain=None,
    range=Optional[Union[Union[int, ExerciseId], list[Union[int, ExerciseId]]]],
)

slots.workouts = Slot(
    uri=FIT.workouts,
    name="workouts",
    curie=FIT.curie("workouts"),
    model_uri=FIT.workouts,
    domain=None,
    range=Optional[Union[Union[int, WorkoutId], list[Union[int, WorkoutId]]]],
)
