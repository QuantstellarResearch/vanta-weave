import json
from geopy.distance import geodesic


def tinh_khoang_cach_bus(data, bus_id_1, bus_id_2):

    bus_1 = _find_bus_by_id(data.mapped["buses"], bus_id_1)
    bus_2 = _find_bus_by_id(data.mapped["buses"], bus_id_2)

    geo_1_str = _get_bus_geo(bus_1)
    geo_2_str = _get_bus_geo(bus_2)

    if not geo_1_str or not geo_2_str:
        print(f"Lỗi: Bus {bus_id_1} hoặc Bus {bus_id_2} không có dữ liệu geo.")
        return None

    geo_1 = json.loads(geo_1_str)
    geo_2 = json.loads(geo_2_str)

    lon1, lat1 = geo_1["coordinates"]
    lon2, lat2 = geo_2["coordinates"]

    toa_do_1 = (lat1, lon1)
    toa_do_2 = (lat2, lon2)

    distance = geodesic(toa_do_1, toa_do_2).kilometers

    return distance


def _find_bus_by_id(buses, bus_id):
    for bus in buses:
        if getattr(bus, "id", None) == bus_id:
            return bus
        if isinstance(bus, dict) and bus.get("id") == bus_id:
            return bus

    raise KeyError(f"Bus {bus_id} not found.")


def _get_bus_geo(bus):
    if isinstance(bus, dict):
        return bus.get("geo")
    return getattr(bus, "geo", None)
