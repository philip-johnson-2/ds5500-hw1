import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.offline as offline
from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


init_notebook_mode(connected=True)


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


scl = [[0.0, '#ffffff'],[0.2, '#ff9999'],[0.4, '#ff4d4d'], 
       [0.6, '#ff1a1a'],[0.8, '#cc0000'],[1.0, '#4d0000']] # reds	


### create empty list for data object:    

data_slider = []


#### I populate the data object

for year in df.Year.unique():


    # I select the year 
    df_year = df[df['Year']== year]

    
    ### create the dictionary with the data for the current year
    data_one_year = dict(
                        type='choropleth',
                        locations = df_year['Geo'],
                        z=df['GDP Per Capita'].astype(float),
                        locationmode='ISO-3',
                        colorscale = scl,
                        )

    data_slider.append(data_one_year)  # I add the dictionary to the list of dictionaries for the slider



##  I create the steps for the slider

steps = []

for i in range(len(data_slider)):
    step = dict(method='restyle',
                args=['visible', [False] * len(data_slider)],
                label='Year {}'.format(i + 1960)) # label to be displayed for each step (year)
    step['args'][1][i] = True
    steps.append(step)


	
##  I create the 'sliders' object from the 'steps' 

sliders = [dict(active=0, pad={"t": 1}, steps=steps)]  


# I set up the layout (including slider option)

layout = dict(sliders=sliders)


	
# I create the figure object:

fig = dict(data=data_slider, layout=layout) 



	
# to plot in the notebook

plotly.offline.iplot(fig)



	
