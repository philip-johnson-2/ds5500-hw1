# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pylab import rcParams
import seaborn as sns 

# assign github URLs
country_url = 'https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--entities--geo--country.csv'
gdp_url = 'https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--datapoints--gdppercapita_us_inflation_adjusted--by--geo--time.csv'
infant_mortaility_url = 'https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--datapoints--infant_mortality_rate_per_1000_births--by--geo--time.csv'
life_expectancy_url = 'https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--datapoints--life_expectancy_years--by--geo--time.csv'



# read dataset
country_df = pd.read_csv(country_url)
gdp_df = pd.read_csv(gdp_url, skiprows=1, names=['Geo','Year','gdp_per_capita'])
infant_mortality_df = pd.read_csv(infant_mortaility_url, skiprows=1, names=['Geo','Year','mortality_rate'])
life_expectancy_df = pd.read_csv(life_expectancy_url, skiprows=1, names=['Geo','Year','life_expectancy'])


# add country information and merge datasets
df = pd.merge(gdp_df,
            country_df[['country','name','latitude','longitude', 'world_4region']],
            left_on = 'Geo', 
            right_on = 'country',
            how = 'left')
            
df = pd.merge(df,
            infant_mortality_df[['Geo','Year','mortality_rate']],
            left_on = ['Geo','Year'], 
            right_on = ['Geo','Year'],
            how = 'left')

df = pd.merge(df,
            life_expectancy_df[['Geo','Year','life_expectancy']],
            left_on = ['Geo','Year'], 
            right_on = ['Geo','Year'],
            how = 'left')

df.rename(columns={'world_4region':'Continent'}, inplace=True)

gdp_by_year = pd.DataFrame(df.groupby(['Year','Continent']).gdp_per_capita.mean()).reset_index()
mortality_by_year = pd.DataFrame(df.groupby(['Year','Continent']).mortality_rate.mean()).reset_index()
life_expectancy_by_year = pd.DataFrame(df.groupby(['Year','Continent']).life_expectancy.mean()).reset_index()



# set image size
#uncomment when running mutlichart
#rcParams['figure.figsize'] = 10, 5

# create mutlichart plot with gdp by year and poverty rate by year
# uncomment to run mutlichart plot
'''
fig, ax = plt.subplots(1,2)
sns.lineplot('Year', 'life_expectancy', data=life_expectancy_by_year, hue='Continent', ax=ax[0]).set(ylabel='Life Expectancy in Years', title='Life Expectancy by Year')
sns.lineplot('Year', 'mortality_rate', data=mortality_by_year, hue='Continent', ax=ax[1]).set( ylabel='Mortality Rate', title='Mortality Rate by Year')
fig.show()
'''

# plot life expectancy by year
# uncomment to run GDP Capita plot
#sns.lineplot('Year', 'gdp_per_capita', data=gdp_by_year, hue='Continent').set( ylabel='GDP Per Capita', title='GDP Per Capita by Year')



# Create the default pairplot
sns.pairplot(df, 
             vars = ['gdp_per_capita', 'mortality_rate','life_expectancy'], 
             hue = 'Continent', diag_kind = 'kde', 
             plot_kws = {'alpha': 0.6, 's': 80, 'edgecolor': 'k'},
             size = 4);
