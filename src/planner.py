def generate_itinerary(selected_places, days, daily_hours=8):
    """
    Distributes selected places over the given number of days.
    """
    plan = {f"Day {i+1}": [] for i in range(days)}
    day = 0
    hours_left = daily_hours

    for row in selected_places:
        time_needed = row['time_needed_to_visit_in_hrs']
        if time_needed <= hours_left:
            plan[f"Day {day+1}"].append(row)
            hours_left -= time_needed
        else:
            day += 1
            if day >= days:
                break
            plan[f"Day {day+1}"].append(row)
            hours_left = daily_hours - time_needed

    return plan
