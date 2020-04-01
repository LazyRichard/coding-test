from typing import List, Dict

def solution(bridge_length:int, weight:int, truck_weights:List[int]) -> int:
    total_trucks:int = len(truck_weights)
    remain_trucks:List[int] = truck_weights
    finished_trucks:List[int] = []
    time_passed:int = 0

    bridge_trucks:List[Dict[str, int]] = []
    on_bridge_weight:int = 0
    while len(finished_trucks) != total_trucks:
        time_passed += 1

        new_truck:List[Dict[str, int]] = []
        new_weight:int = 0
        for truck in bridge_trucks:
            truck["TTL"] = truck["TTL"] - 1

            if truck["TTL"] > 0:
                new_truck.append(truck)
                new_weight += truck["weight"]
            else:
                finished_trucks.append(truck["weight"])

        bridge_trucks = new_truck
        on_bridge_weight = new_weight

        if len(remain_trucks) < 1:
            continue
        elif on_bridge_weight + remain_trucks[0] <= weight:
            truck_weight = remain_trucks.pop(0)
            truck_info:Dict[str, int] = {
                "weight": truck_weight,
                "TTL": bridge_length
            }
            bridge_trucks.append(truck_info)

    return time_passed
