from src.recommender import load_data, recommend_places
from src.planner import generate_itinerary

def get_user_inputs():
    print(" Welcome to the Trip Planner Chatbot ")
    trip_type = input("Enter trip type (solo / family / couple / friends): ").strip().lower()
    days = int(input("Enter number of days: ").strip())
    location = input("Enter state to visit: ").strip()
    return trip_type, days, location

def show_itinerary(itinerary):
    for day, places in itinerary.items():
        print(f"\n {day}:")
        if not places:
            print("No places planned.")
            continue
        for row in places:
            print(f" {row['name']} ({row['city']})")
            print(f"   - Time Needed: {row['time_needed_to_visit_in_hrs']} hrs")
            print(f"   - Best Time to Visit: {row['best_time_to_visit']}")
            print(f"   - Description: {row['significance']}")
            print(f"   - Rating: {row['google_review_rating']} ")
            print()
