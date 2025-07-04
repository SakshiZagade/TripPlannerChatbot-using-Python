from src import chatbot
from src.recommender import load_data, recommend_places
from src.planner import generate_itinerary

if __name__ == "__main__":
    trip_type, days, location = chatbot.get_user_inputs()
    df = load_data()

    total_hours = days * 8  # assuming 8 hours/day
    selected = recommend_places(df, trip_type, location, total_hours)

    if selected:
        itinerary = generate_itinerary(selected, days)
        chatbot.show_itinerary(itinerary)
    else:
        print(" Sorry, no places match your criteria. Try different inputs.")
