
# FITNESS-APP


**metamodel version:** 1.7.0

**version:** 0.0.1


Schema for the fitness tracking platform


## Class Diagram

```mermaid
classDiagram
Thing <|-- Exercise
Thing <|-- User
Thing <|-- Workout
```

## ERD Diagram

```mermaid
erDiagram
Exercise {
    integer id  
    string name  
    integer reps  
    integer sets  
    float weight  
}
User {
    integer id  
    string name  
    integer age  
    string email  
}
Workout {
    integer id  
    float duration  
    date workout_date  
}

User ||--}o Workout : "workouts"
Workout ||--}o Exercise : "exercises"

```

## Base Classes


Foundational classes in the hierarchy (root classes and direct children of Thing):

| Class | Description |
| --- | --- |
| [Exercise](#exercise) | Individual exercise performed |
| [Thing](#thing) | The root class for all entities in the fitness app |
| [User](#user) | A registered app user |
| [Workout](#workout) | A recorded workout session |

## Classes


### Exercise

Individual exercise performed

```mermaid
erDiagram
Exercise {

}
Workout {

}

Workout ||--}o Exercise : "exercises"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>0..1</sub> | integer |  |
| **[name](#name)** | <sub>0..1</sub> | string |  |
| **[reps](#reps)** | <sub>0..1</sub> | integer |  |
| **[sets](#sets)** | <sub>0..1</sub> | integer |  |
| **[weight](#weight)** | <sub>0..1</sub> | float |  |

#### Parents

 * [Thing](#thing) - The root class for all entities in the fitness app

#### Referenced by:

 *  **[Workout](#workout)** : exercises  <sub>0..\*</sub> 




### Thing

The root class for all entities in the fitness app


#### Local class diagram

```mermaid
classDiagram
Thing <|-- Exercise
Thing <|-- User
Thing <|-- Workout
```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>1..1</sub> | integer |  |

#### Children

 * [Exercise](#exercise) - Individual exercise performed
 * [User](#user) - A registered app user
 * [Workout](#workout) - A recorded workout session




### User

A registered app user

```mermaid
erDiagram
User {

}
Workout {

}

User ||--}o Workout : "workouts"
Workout ||--}o Exercise : "exercises"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>1..1</sub> | integer |  |
| **[name](#name)** | <sub>0..1</sub> | string |  |
| **[age](#age)** | <sub>0..1</sub> | integer |  |
| **[email](#email)** | <sub>0..1</sub> | string |  |
| **[workouts](#workouts)** | <sub>0..\*</sub> | [Workout](#workout) |  |

#### Parents

 * [Thing](#thing) - The root class for all entities in the fitness app




### Workout

A recorded workout session

```mermaid
erDiagram
Exercise {

}
User {

}
Workout {

}

User ||--}o Workout : "workouts"
Workout ||--}o Exercise : "exercises"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[id](#id)** | <sub>1..1</sub> | integer |  |
| **[duration](#duration)** | <sub>0..1</sub> | float |  |
| **[exercises](#exercises)** | <sub>0..\*</sub> | [Exercise](#exercise) |  |
| **[workout_date](#workout_date)** | <sub>0..1</sub> | date |  |

#### Parents

 * [Thing](#thing) - The root class for all entities in the fitness app

#### Referenced by:

 *  **[User](#user)** : workouts  <sub>0..\*</sub> 




## Slots

| Name | Cardinality/Range | Used By |
| --- | --- | --- |
| <a id="id"></a>**id** | <sub>1..1</sub><br/>integer | [Exercise](#exercise), [Thing](#thing), [User](#user), [Workout](#workout) |
| <a id="name"></a>**name** | <sub>0..1</sub><br/>string | [Exercise](#exercise), [User](#user) |
| <a id="age"></a>**age** | <sub>0..1</sub><br/>integer | [User](#user) |
| <a id="duration"></a>**duration** | <sub>0..1</sub><br/>float | [Workout](#workout) |
| <a id="email"></a>**email** | <sub>0..1</sub><br/>string | [User](#user) |
| <a id="exercises"></a>**exercises** | <sub>0..\*</sub><br/>[Exercise](#exercise) | [Workout](#workout) |
| <a id="reps"></a>**reps** | <sub>0..1</sub><br/>integer | [Exercise](#exercise) |
| <a id="sets"></a>**sets** | <sub>0..1</sub><br/>integer | [Exercise](#exercise) |
| <a id="weight"></a>**weight** | <sub>0..1</sub><br/>float | [Exercise](#exercise) |
| <a id="workout_date"></a>**workout_date** | <sub>0..1</sub><br/>date | [Workout](#workout) |
| <a id="workouts"></a>**workouts** | <sub>0..\*</sub><br/>[Workout](#workout) | [User](#user) |

