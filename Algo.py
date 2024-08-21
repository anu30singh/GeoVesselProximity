import pandas as pd
from geopy.distance import geodesic
import matplotlib.pyplot as plt
import plotly.express as px

def haversine_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

def detect_proximity(data, distance_threshold):
    proximity_events = []
    data_sorted = data.sort_values(by='timestamp')  # Ensure data is sorted by time

    for i, vessel1 in data_sorted.iterrows():
        interactions = []
        for j, vessel2 in data_sorted.iterrows():
            if vessel1['mmsi'] != vessel2['mmsi']:
                distance = haversine_distance(
                    (vessel1['lat'], vessel1['lon']),
                    (vessel2['lat'], vessel2['lon'])
                )
                if distance <= distance_threshold:
                    interactions.append(vessel2['mmsi'])
        if interactions:
            proximity_events.append({
                'mmsi': vessel1['mmsi'],
                'vessel_proximity': interactions,
                'timestamp': vessel1['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
            })
    return pd.DataFrame(proximity_events)

data = pd.read_csv('sample_data.csv')


data['timestamp'] = pd.to_datetime(data['timestamp'])
data['lat'] = data['lat'].astype(float)
data['lon'] = data['lon'].astype(float)


print(data.head())
print(data.dtypes)

# Detect proximity events
distance_threshold = 0.5  # Example distance threshold in kilometers
proximity_events_df = detect_proximity(data, distance_threshold)

# Print proximity events to check results
print(proximity_events_df)

# Visualization
def plot_proximity_events(events_df):
    plt.figure(figsize=(10, 6))
    for _, event in events_df.iterrows():
        plt.scatter(event['timestamp'], event['mmsi'], label=f'Proximity with: {event["vessel_proximity"]}')
    plt.xlabel('Timestamp')
    plt.ylabel('MMSI')
    plt.title('Vessel Proximity Events')
    plt.legend()
    plt.show()

def plot_proximity_events_plotly(events_df):
    fig = px.scatter(events_df, x='timestamp', y='mmsi', color='vessel_proximity',
                     title='Vessel Proximity Events',
                     labels={'timestamp': 'Timestamp', 'mmsi': 'MMSI'})
    fig.show()

# Call the functions to plot
plot_proximity_events(proximity_events_df)
# Or
# plot_proximity_events_plotly(proximity_events_df)
