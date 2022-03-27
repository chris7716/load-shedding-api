from domain import area_registry
from storage import area

def shed_load(area_id):
    # Total power to be removed
    shedding_amount = 100

    # This values should be picked from the database for the given area
    area_name = 'area-1'
    area_status = 'UP'

    # Total number of priority levels
    number_of_priority_levels = 10

    n = number_of_priority_levels

    priority_levels = []

    # A list of IDs of the priority levels that are going to be interrupted
    removed_levels = []

    # A list of IDs of the houses that are going to be interrupted.
    removed_houses = []

    area = area_registry.Area(area_id, area_name, area_status)

    removed_levels, shedding_amount, last_shedded_priority_level = area.calculate_load_shedding_priority_levels(priority_levels)

    # This are the households of the given area in the priority level of 
    # 'last_shedded_priority_level - 1' level
    house_holds = []

    removed_houses = area.calculate_load_sheddin_households(house_holds, shedding_amount)

    removed_elements = {
        'removed_levels': removed_levels,
        'removed_houses': removed_houses
    }

