class Task:
    def __init__(self, name, start_time, end_time, duration, priority, satellite=None):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.priority = priority  # priority from 3 to 1 = from high to low
        self.satellite = satellite


class Satellite:
    def __init__(self, name, activity_window):
        self.name = name
        self.activity_window = activity_window
        self.schedule = []  # list of ((#task_name, actual_start_time, real_end_time))


satellites = [Satellite('S1', (0, 23)), Satellite('S2', (0, 23)), Satellite('S3', (0, 23)),
              Satellite('S4', (0, 23)), Satellite('S5', (0, 23))]

tasks = [
    Task("Task1", start_time=0, end_time=3, duration=3, priority=4, satellite=satellites[0]),
    Task("Task2", start_time=2, end_time=7, duration=5, priority=2),
    Task("Task3", start_time=5, end_time=7, duration=2, priority=1),
    Task("Task4", start_time=8, end_time=12, duration=4, priority=4),
    Task("Task5", start_time=1, end_time=5, duration=4, priority=4),
    Task("Task6", start_time=6, end_time=10, duration=4, priority=3),
    Task("Task7", start_time=2, end_time=6, duration=4, priority=2),
    Task("Task8", start_time=4, end_time=9, duration=5, priority=1),
    Task("Task9", start_time=9, end_time=12, duration=3, priority=4),
    Task("Task10", start_time=1, end_time=4, duration=3, priority=3),
    Task("Task11", start_time=5, end_time=9, duration=4, priority=2),
    Task("Task12", start_time=3, end_time=8, duration=5, priority=1),
    Task("Task13", start_time=7, end_time=11, duration=4, priority=4),
    Task("Task14", start_time=10, end_time=15, duration=5, priority=4),
    Task("Task15", start_time=2, end_time=5, duration=3, priority=3),
    Task("Task16", start_time=6, end_time=9, duration=3, priority=2),
    Task("Task17", start_time=4, end_time=7, duration=3, priority=1),
    Task("Task18", start_time=8, end_time=11, duration=3, priority=4),
    Task("Task19", start_time=1, end_time=5, duration=4, priority=4),
    Task("Task20", start_time=3, end_time=8, duration=5, priority=3),
]

import random

# Define the fitness function
def fitness(schedule):
    total = 0
    for task in schedule:
        if task is not None:
            if task.priority == 4:
                total += 50**3
            elif task.priority == 3:
                total += 50**2
            elif task.priority == 2:
                total += 50
            else:
                total += 1
    return total

# Define the mutation function
def mutate(schedule):
    for i in range(len(schedule)):
        if schedule[i] is not None:
            # Change the start time of the task within the allowed window
            new_start_time = random.randint(schedule[i].start_time, schedule[i].end_time - schedule[i].duration)
            schedule[i].start_time = new_start_time

# Define the crossover function
def crossover(schedule1, schedule2):
    if len(schedule1) > 2:
        index = random.randint(1, len(schedule1) - 2)
        new_schedule1 = schedule1[:index] + schedule2[index:]
        new_schedule2 = schedule2[:index] + schedule1[index:]
        return new_schedule1, new_schedule2
    else:
        return schedule1, schedule2

# Initialize the population
population = []
unassigned_tasks = tasks.copy()
satellite_schedules = {satellite.name: [] for satellite in satellites}

for _ in range(100): #population
    random.shuffle(unassigned_tasks)
    newly_assigned_tasks = []

    for task in unassigned_tasks:
        assigned_satellite = None

        for satellite in satellites:
            # Check if the task's time conflicts with the times of tasks already in the schedule
            if all(
                not (task.start_time < t.end_time and t.start_time < task.end_time)
                for t in satellite_schedules[satellite.name] if t is not None
            ):
                assigned_satellite = satellite.name
                break

        if assigned_satellite is not None:
            satellite_schedules[assigned_satellite].append(task)
            newly_assigned_tasks.append(task)

    # Remove newly assigned tasks from unassigned_tasks
    unassigned_tasks = [task for task in unassigned_tasks if task not in newly_assigned_tasks]

    # Check if all tasks are assigned, break if yes
    if not unassigned_tasks:
        break

def print_schedule_info(unassigned_tasks, satellite_schedules):
    print("Unassigned Tasks:")
    for task in unassigned_tasks:
        print(f"Task {task.name}")

    # Print satellite schedules
    for satellite, schedule in satellite_schedules.items():
        print(f"\nSatellite {satellite} Schedule:")
        for task in schedule:
            print(f"Task {task.name} from {task.start_time} to {task.end_time}")




# Run the genetic algorithm
for _ in range(0,200): #Generations
    if random.random() < 0.5:
        # Mutation
        if population:
            schedule = random.choice(population)[:]
            mutate(schedule)
            population.append(schedule)
        else:
            # If the population is empty, generate a new random schedule
            new_schedule = []
            for satellite in satellites:
                possible_tasks = [task for task in tasks if
                                  (task.satellite is None or task.satellite.name == satellite.name)]
                random.shuffle(possible_tasks)
                new_schedule.extend(possible_tasks[:50])
            population.append(new_schedule)
    else:
        # Crossover
        if len(population) >= 2:
            schedule1, schedule2 = random.sample(population, 2)
            offspring1, offspring2 = crossover(schedule1, schedule2)
            population.append(offspring1)
            population.append(offspring2)

    # Select the top 100 schedules based on fitness for the next generation
    population = sorted(population, key=fitness, reverse=True)[:100]


# Print schedule information
print_schedule_info(unassigned_tasks, satellite_schedules)
