from domain import area_registry
from storage import area
from storage import priority_level
from storage import temp_customer
from storage import temp_data

def shed_load(area_id, consumptions):

    max_allowed_power = sum(consumptions)

    priority_levels = priority_level.PriorityLevel.all()

    # Total power to be removed
    sheddings = temp_data.TempData.all()
    shedding_amount = sheddings[0].amount
    # maxmium_supply = get_maximum_supply()
    # shedding_amount = power_consumptions - maxmium_supply

    max_allowed_power -= shedding_amount 

    # Total number of priority levels
    number_of_priority_levels = len(priority_levels)

    n = number_of_priority_levels

    # A list of IDs of the priority levels that are going to be interrupted
    removed_levels = []

    # A list of IDs of the houses that are going to be interrupted.
    removed_houses = []
    consumptions_of_removed_houses = []

    while n > 0:

        # Total consumption of the nth priority level
        priority_level_consumption = priority_levels[n-1].consumption
        print(priority_level_consumption)

        if n == 0 or shedding_amount == 0:
            break
        if shedding_amount > priority_level_consumption:
            removed_levels.append(n)
            shedding_amount = shedding_amount - priority_level_consumption
        else:
            break
        n = n - 1

    if shedding_amount > 0:

        all_households = temp_customer.TempCustomer.all()
        households = []

        for house in all_households:
            if house.priority == n:
                households.append(house)

        # Consumption of each household of the priority level k where
        # the total consumption of the kth priority level is less than
        # the shedding amount
        consumptions_of_huseholds = []
        households.sort(key=lambda x: x.amount, reverse=False)

        total_households = len(households)

        i = total_households
        started_index = 0

        while households[i - 1].amount >= shedding_amount:
            i = i - 1
            if i == 1:
                break

        started_index = i - 1
        removed_houses.append(households[started_index].id)
        consumptions_of_removed_houses.append(households[started_index].amount)
        shedding_amount -= households[started_index].amount

        i = 0

        while i != started_index:
            # Add the house hold to the removed households
            removed_houses.append(households[i].id)
            consumptions_of_removed_houses.append(households[i].amount)

            shedding_amount = shedding_amount - households[i].amount
            if shedding_amount <= 0:
                if len(households) > started_index + 1:
                    if sum(consumptions_of_removed_houses) > households[started_index + 1].amount:
                        removed_houses = [households[started_index + 1].id]
                break

            i = i + 1

        if shedding_amount > 0:
            # Only removes the house at the started indexes
            removed_houses = [households[started_index + 1].id]
            max_allowed_power -= households[started_index].amount  # REMOVE

    max_allowed_power_per_user = max_allowed_power / (len(removed_levels) + len(removed_houses))
    removed_elements = {
        "removed_levels": removed_levels,
        "removed_houses": removed_houses,
        "max_allowed_power_per_user": max_allowed_power_per_user
    }

    return removed_elements

