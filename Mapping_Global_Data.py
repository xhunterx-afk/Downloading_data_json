import json
from  plotly.graph_objects import Scattergeo, Layout
from plotly import offline


# Opening file

with open("eq_data_1_day_m1.json")as f:
    all_eq_data=json.load(f)

# accessing all data

all_eq_dicts=all_eq_data['features']

# Setting a title so if the the file change sthe title dosent

title="Global Earthquake"
# Looping through the information and storing it in the empty list

mag=[dicts["properties"]["mag"] for dicts in all_eq_dicts]
lang=[dicts["geometry"]["coordinates"][0] for dicts in all_eq_dicts]
lat=[dicts["geometry"]["coordinates"][1] for dicts in all_eq_dicts]

# Using a map as a type, lon and lat where the coordination,
# Making as the bigger the magnitude the bigger the point where the EQ is,
# Making a scaling color as bigger the magnitude it takes a specific color,
# Naming the color scale

data=[{"type": "scattergeo",
       "lon": lang,
       "lat": lat,
       "marker": {
       "size": [3*mags for mags in mag],
       "color":mag,
       "colorscale": "Viridis",
       "reversescale":True,
       "colorbar":{"title":"Magnitude"}}}]

# Giving the graph a title and putting it in the middle with some modification text type and text size

my_layout=Layout(title={"text": title ,
                        "y": 0.96,
                        "x": 0.5,
                        "xanchor": "center",
                        "yanchor": "top"},
                        font=dict
                        (family="Courier New, monospace",
                        size=25))

# Saving the graph and running the data and the layout

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="Global_Earthquake.html")
