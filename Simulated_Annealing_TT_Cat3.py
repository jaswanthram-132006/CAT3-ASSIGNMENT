import random
import math

DAYS = ["Tue", "Wed", "Thu", "Fri", "Sat"]
TIME_SLOTS = ["8-9", "9-10", "10-11", "11-12", "1-2", "2-3", "3-4", "4-5"]
SLOTS = [(day, time) for day in DAYS for time in TIME_SLOTS]
ROOMS = ["R1", "R2"]

events = [
    {"name": "Principles of AI",     "teacher": "T1", "group": "G1"},
    {"name": "Discrete Mathematics", "teacher": "T2", "group": "G1"},
    {"name": "DAA",                  "teacher": "T3", "group": "G1"},
    {"name": "EVS",                  "teacher": "T4", "group": "G1"},
    {"name": "Java-OOPs",            "teacher": "T5", "group": "G1"},
    {"name": "DBMS",                 "teacher": "T6", "group": "G1"},
]

def random_state():
    return [(random.choice(SLOTS), random.choice(ROOMS)) for _ in events]

def cost(state):
    violations = 0
    for i in range(len(events)):
        slot_i, room_i = state[i]
        for j in range(i + 1, len(events)):
            slot_j, room_j = state[j]
            if slot_i == slot_j:                      
                if room_i == room_j:
                    violations += 1                    
                if events[i]["teacher"] == events[j]["teacher"]:
                    violations += 1                    
                if events[i]["group"] == events[j]["group"]:
                    violations += 1                    
    return violations

def make_neighbor(state):
    new_state = state[:]
    i = random.randrange(len(events))
    new_state[i] = (random.choice(SLOTS), random.choice(ROOMS))
    return new_state

def run_sa():
    T = 10.0
    alpha = 0.95
    min_T = 0.01
    iterations_per_temp = 200

    current = random_state()
    current_cost = cost(current)
    best, best_cost = current[:], current_cost

    while T > min_T:
        for _ in range(iterations_per_temp):
            candidate = make_neighbor(current)
            candidate_cost = cost(candidate)
            delta = candidate_cost - current_cost

            if delta < 0 or random.random() < math.exp(-delta / T):
                current, current_cost = candidate, candidate_cost
                if current_cost < best_cost:
                    best, best_cost = current[:], current_cost

        T *= alpha

    return best, best_cost

best_state, best_cost = run_sa()

print(f"Best cost found: {best_cost} (0 = no clashes)\n")
for event, ((day, time), room) in zip(events, best_state):
    print(f"{event['name']:22s} | {day} {time} | Room {room} | Teacher {event['teacher']}")
    
