'''
Problem 2:

Compare the GDP per capita today to 20 years ago
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plotly
import plotly.graph_objects as go

# assign github URLs
country_url = 'https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--entities--geo--country.csv'
gdp_url = 'https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--datapoints--gdppercapita_us_inflation_adjusted--by--geo--time.csv'

# read dataset
country_df = pd.read_csv(country_url)
gdp_df = pd.read_csv(gdp_url, skiprows=1, names=['Geo','Year','GDP Per Capita'])

# add country information 
data = pd.merge(gdp_df,
            country_df[['country','name','latitude','longitude']],
            left_on = 'Geo', 
            right_on = 'country',
            how = 'left')

# remove any NA values for lat/long
data = data.dropna()

#years = ['1980','1990','2000','2010']
years = ['2010']

df = data[data.Year.isin(years)]
df['Geo'] = df['Geo'].str.upper()

# plot maps
fig = go.Figure(data=go.Choropleth(
    locations = df['Geo'],
    z = round(df['GDP Per Capita'],2),
    text = df['name'],
    colorscale = 'Blues',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix = '$',
    colorbar_title = 'GDP Per Capita$',
))

fig.update_layout(
    title_text='2000 Global GDP',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        showarrow = False
    )]
)

fig.show()
