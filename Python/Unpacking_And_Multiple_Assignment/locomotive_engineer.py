"""Functions which helps the locomotive engineer to keep track of the train."""
def get_list_of_wagons(*wagon_ids):
    """Return a list of wagons.
 
    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagon_ids)
def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.
 
    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    a,b,c,*old_wagons=each_wagons_id
    *wagons,=c,*missing_wagons,*old_wagons,a,b
    return wagons
def add_missing_stops(routing, **kwargs):
    """Add missing stops to route dict.
 
    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops = list(kwargs.values())
    routing["stops"] = stops
    return routing
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.
 
    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    finfo={**route,**more_route_information}
    return finfo
def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.
 
    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    return [list(column) for column in zip(*wagons_rows)]
