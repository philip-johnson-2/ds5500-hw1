
'''
Problem 1:
In the last 20 years the proportion of people living in extreme poverty worldwide, has...? 

Below the extreme poverty dataset from the GapMinder github account will be used 
to look at the difference between the proportion of people living in poverty 
now compared to 20 years ago
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plotly
import plotly.graph_objects as go


# assign github URLs
country_url = 'https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--entities--geo--country.csv'
poverty_url = 'https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--datapoints--alternative_poverty_percent_below_nationally_defined_poverty--by--geo--time.csv'

# read dataset
country_df = pd.read_csv(country_url)
poverty_df = pd.read_csv(poverty_url, skiprows=1, names=['Geo','Year','Poverty Rate'])


# add country information 
df = pd.merge(poverty_df,
            country_df[['country','name']],
            left_on = 'Geo', 
            right_on = 'country',
            how = 'left')
df.rename(columns={'Poverty Rate':'povertyrate'}, inplace=True)


# check unique geo locations by year
print(df.groupby('Year').Geo.nunique())
'''
These counts can be used to identify which years are the 
best for comparison to try and have as clean a representation
across the globe as possible

Based on the years in which we have data, I am going to use 2002
and 2016 as the years in which we can compare average poverty 
rate across the country.
'''



#create data for visualization
poverty_by_year = pd.DataFrame(df.groupby('Year').povertyrate.mean()).reset_index()



# create data for line chart
x = poverty_by_year['Year']
y = poverty_by_year['povertyrate']
 
# Change the color and its transparency
plt.fill_between( x, y, color="skyblue", alpha=0.2)
plt.plot(x, y, color="Slateblue", alpha=0.6)
plt.title('Avg Extreme Poverty Rate By Year')
plt.xlabel('Year')
plt.ylabel('Extreme Poverty Rate')
plt.show()






# create radial chart to show comparisons
'''
ax = plt.subplot(projection='polar')
ax.barh(0, math.radians(150))
ax.barh(1, math.radians(300))
ax.barh(2, math.radians(270))
ax.barh(3, math.radians(320))
'''

