
# ✨ Trip Planner Chatbot

A **Trip Planner Chatbot** that recommends the best places to visit in India based on:

* trip type (`solo`, `family`, `couple`, `friends`),
* number of days available,
* and the desired state/location.

It uses a real-world dataset of tourist destinations and suggests places to visit, estimated time to explore, best times to visit, and a daily itinerary.
This is a **Big Data mini-project**, built with **Python & Pandas**, and can run in CLI or can be extended to Streamlit/Web UI.

---

## 📂 Project Structure

```
TripPlannerChatbot/
├── app.py                       # Entry point: runs the chatbot
├── data/
│   └── enhanced_places_dataset.csv   # processed dataset
├── src/
│   ├── preprocess.py            # preprocesses raw dataset & generates enhanced CSV
│   ├── chatbot.py               # handles user inputs & outputs
│   ├── recommender.py           # recommendation logic
│   └── planner.py               # itinerary planner
├── raw_data/
│   └── raw_places_dataset.csv   # original dataset (optional)
└── README.md                    # this file
```

---

## 🗝️ Features

✅ User-friendly CLI chatbot
✅ Takes into account trip type, duration, and location
✅ Recommends best places to visit sorted by popularity & reviews
✅ Provides estimated time per place & best time to visit
✅ Generates a suggested day-wise itinerary
✅ Uses a real dataset of Indian tourist attractions

---

## 🚀 How to Run

### 1️⃣ Install Dependencies

Make sure you have Python ≥ 3.8 installed.
Install `pandas`:

```bash
pip install pandas
```

### 2️⃣ Preprocess the dataset

Ensure your `raw_places_dataset.csv` is available in the `raw_data/` folder.
Run the preprocessing script to generate `enhanced_places_dataset.csv`:

```bash
cd src
python preprocess.py
```

### 3️⃣ Run the chatbot

Go back to project root & start:

```bash
cd ..
python app.py
```

Then follow the on-screen prompts:

```
Enter trip type (solo / family / couple / friends): family
Enter number of days: 3
Enter state to visit: Rajasthan
```

---

## 📊 Dataset

The dataset (`enhanced_places_dataset.csv`) contains \~325 rows & 17 columns, including:

* `zone`: Region of India
* `state`: State name
* `city`: City name
* `name`: Place name
* `type`: Type of attraction (temple, fort, etc.)
* `establishment_year`
* `time_to_visit`: Estimated hours needed
* `google_review_rating`
* `entrance_fee`
* `airport_nearby`
* `weekly_off`
* `description`: Significance
* `dslr_allowed`
* `number_of_reviews`
* `best_time`: Best time of day
* `tags`: Derived tags for trip types

---

## 💡 Example Output

```
✨ Welcome to the Trip Planner Chatbot ✨
Enter trip type (solo / family / couple / friends): family
Enter number of days: 2
Enter state to visit: Rajasthan

✅ Recommended Places:
1️⃣ Amber Fort — 3 hours — Best Time: Morning — Rating: 4.7 ⭐
2️⃣ City Palace — 2 hours — Best Time: Afternoon — Rating: 4.6 ⭐
...

📅 Suggested Itinerary:
Day 1:
 - Amber Fort (3 hrs)
 - City Palace (2 hrs)
Day 2:
 - Hawa Mahal (2 hrs)
 - Jantar Mantar (1.5 hrs)
```

---

## 📌 Future Enhancements

* Add a Streamlit or web-based UI
* Use NLP to understand free-text queries
* Integrate with live weather & traffic APIs
* Support more countries & datasets

---
