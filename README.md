# Vessel Proximity Detection

## Overview

This script analyzes vessel proximity events using data from a CSV file. It calculates when vessels come within a specified distance threshold and visualizes the results using Matplotlib and Plotly.

## Dependencies

- `pandas`: For data manipulation.
- `geopy`: For calculating geographical distances.
- `matplotlib`: For plotting with Matplotlib.
- `plotly`: For interactive plotting.

## Input Data

The input is a CSV file with the following columns:
- `mmsi`: Maritime Mobile Service Identity (9-digit vessel ID)
- `timestamp`: Timestamp of the vessel position
- `lat`: Latitude of the vessel
- `lon`: Longitude of the vessel

## Setup

1. **Install Dependencies**

   Ensure you have the necessary Python packages installed. You can install them using pip:

   ```bash
   pip install pandas geopy matplotlib plotly

## Haversine Distance Formula:

The Haversine formula calculates the distance between two points on the surface of a sphere using their latitudinal and longitudinal coordinates. It accounts for the spherical shape of the Earth to provide an accurate distance measurement.