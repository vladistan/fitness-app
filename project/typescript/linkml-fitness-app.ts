export type ThingId = string;
export type UserId = string;
export type WorkoutId = string;
export type ExerciseId = string;


/**
 * The root class for all entities in the fitness app
 */
export interface Thing {
    id: number,
}


/**
 * A registered app user
 */
export interface User extends Thing {
    name?: string,
    email?: string,
    age?: number,
    workouts?: WorkoutId[],
}


/**
 * A recorded workout session
 */
export interface Workout extends Thing {
    workout_date?: date,
    duration?: number,
    exercises?: ExerciseId[],
}


/**
 * Individual exercise performed
 */
export interface Exercise extends Thing {
    name?: string,
    sets?: number,
    reps?: number,
    weight?: number,
}
