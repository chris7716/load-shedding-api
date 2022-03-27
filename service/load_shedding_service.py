def shed_load(area_id):
    # Total power to be removed
    shedding_amount = 100

    # Total number of priority levels
    number_of_priority_levels = 10

    n = number_of_priority_levels

    # A list of IDs of the priority levels that are going to be interrupted
    removed_levels = []

    # A list of IDs of the houses that are going to be interrupted.
    removed_houses = []

    while n > 0:

        # Total consumption of the nth priority level
        priority_level_consumption = 40

        if n == 0 or shedding_amount == 0:
            break
        if shedding_amount > priority_level_consumption:
            removed_levels.append(n)
            shedding_amount = shedding_amount - priority_level_consumption
        else:
            break
        n = n - 1

    if shedding_amount > 0:

        # Consumption of each household of the priority level k where
        # the total consumption of the kth priority level is less than
        # the shedding amount
        consumptions_of_huseholds = []

        sorted_consumptions_of_huseholds = consumptions_of_huseholds.sort()

        total_households = len(consumptions_of_huseholds)

        i = total_households
        k = 1
        started_index = 0

        while sorted_consumptions_of_huseholds[i - 1] > shedding_amount:
            i = i - 1
        
        started_index = i

        i = 0

        while i != started_index:
            # Add the house hold to the removed households
            removed_houses.append(i)

            shedding_amount = shedding_amount - sorted_consumptions_of_huseholds[i]

            i = i + 1

        if shedding_amount > 0:
            # Only removes the house at the started indexes
            removed_houses = [started_index]

    removed_elements = {
        "removed_levels": removed_levels,
        "removed_houses": removed_houses
    }

