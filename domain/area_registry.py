
class PriorityLevel:
    def __init__(self, id, consumption, level):
        self.id = id
        self.consumption = consumption
        self.level = level

class Household:
    def __init__(self, id, consumption):
        self.id = id
        self.consumption = consumption

class Area:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def calculate_load_shedding_priority_levels(priority_levels, shedding_amount):
        n = len(priority_levels)

        removed_levels = []

        for i in reversed(range(n - 1)):
            # Total consumption of the nth priority level
            priority_level_consumption = priority_levels[i].consupmtion

            if i == 0 or shedding_amount == 0:
                break
            if shedding_amount > priority_level_consumption:
                removed_levels.append(n)
                shedding_amount = shedding_amount - priority_level_consumption
            else:
                break

        return removed_levels, shedding_amount, priority_levels[i].level

    def calculate_load_sheddin_households(households, shedding_amount):
        removed_houses = []
        if shedding_amount > 0:

            # Consumption of each household of the priority level k where
            # the total consumption of the kth priority level is less than
            # the shedding amount
            households.sort(key=lambda x: x.consumption, reverse=True)

            total_households = len(households)

            i = total_households
            k = 1
            started_index = 0

            while households[i - 1].consumption > shedding_amount:
                i = i - 1
            
            started_index = i

            i = 0

            while i != started_index:
                # Add the house hold to the removed households
                removed_houses.append(households[i])

                shedding_amount = shedding_amount - households[i].consumption

                i = i + 1

            if shedding_amount > 0:
                # Only removes the house at the started indexes
                removed_houses = [households[started_index]]
        
        return removed_houses