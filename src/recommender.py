import pandas as pd

def load_data(path="C:/Users/Sakshi/OneDrive/Desktop/My Project/TripPlannerChatbot/data/enhanced_places_dataset.csv"):
    df = pd.read_csv(path)
    return df

def recommend_places(df, trip_type, location, available_hours):
    """
    Filters places by trip_type (solo/family/etc), location (state), and time.
    """
    # filter by tags & location
    df_filtered = df[
        df['tags'].str.contains(trip_type, case=False, na=False) &
        df['state'].str.contains(location, case=False, na=False)
    ]

    if df_filtered.empty:
        print("⚠️ No places found for this trip type & location.")
        return []

    # sort by rating & reviews (optional)
    df_filtered = df_filtered.sort_values(by=['google_review_rating', 'number_of_google_review_in_lakhs'], ascending=False)

    # select places that fit within available_hours
    total_time = 0
    selected = []
    for _, row in df_filtered.iterrows():
        if total_time + row['time_needed_to_visit_in_hrs'] <= available_hours:
            selected.append(row)
            total_time += row['time_needed_to_visit_in_hrs']

    if not selected:
        print("⚠️ Not enough time for any recommended place.")
    return selected
