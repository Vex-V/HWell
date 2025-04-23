from shapely.geometry import LineString, Polygon

# Airport coordinates
jfk = (-94.0, 41.0)  # (lon, lat)
lax = (-90.5, 43.0)

# SIGMET polygon (note: shapely uses (lon, lat) as (x, y))

sigmet_coords = [
    {'lat': 42.7333, 'lon': -92.8457},
    {'lat': 42.6346, 'lon': -91.0295},
    {'lat': 41.2845, 'lon': -91.9228},
    {'lat': 41.1328, 'lon': -93.4811},
    {'lat': 42.7333, 'lon': -92.8457}
]

# Convert to shapely-friendly format
shapely_coords = [(point['lon'], point['lat']) for point in sigmet_coords]

# Now you can use it to create a Polygon


sigmet_polygon = Polygon(shapely_coords)

print(sigmet_polygon)


# Create geometry
flight_path = LineString([jfk, lax])

# Check intersection
intersects = flight_path.intersects(sigmet_polygon)

print("Flight path crosses SIGMET polygon:", intersects)
