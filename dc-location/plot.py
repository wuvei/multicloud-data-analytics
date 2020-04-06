import plotly.express as px
import pandas as pd
px.set_mapbox_access_token('pk.eyJ1IjoienljMTk5NzAwIiwiYSI6ImNrOGswdTZqZzAyem0zbW54Y3g3ZTFzOHEifQ.dn5LAHxO-O95GCQd8FJctg')
df = pd.read_csv('locat.csv', header = 0)
print(df)
fig = px.scatter_mapbox(df, lat=df['Latitude'], lon="Longitude", color="Vendor", size=[1]*len (df.index), text = "Location", color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=1)
fig.show()