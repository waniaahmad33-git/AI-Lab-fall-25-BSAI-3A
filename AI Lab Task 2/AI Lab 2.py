
class ClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):
        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "COOL"
        elif temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"

        if target_mode != self.previous_mode:
            send_command = True
        else:
            send_command = False

        self.previous_mode = target_mode

        return target_mode, send_command


agent = ClassroomAgent()

percepts = [
    (29, True),
    (29, True),
    (20, True),
    (26, True),
    (19, True),
    (29, False),
    (29, False)
]

for step, percept in enumerate(percepts, 1):
    previous_mode = agent.previous_mode

    temp, occupied = percept
    target_mode, send_command = agent.act(temp, occupied)

    if send_command:
        result = "SEND COMMAND"
    else:
        result = "NO COMMAND"

    print("Step:", step)
    print("Previous Mode:", previous_mode)
    print("Percept:", percept)
    print("Target Mode:", target_mode)
    print("Command Status:", result)
    print("-" * 35)
