# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# assign github URLs
country_url = 'https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--entities--geo--country.csv'
gdp_url = 'https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--datapoints--gdppercapita_us_inflation_adjusted--by--geo--time.csv'
infant_mortaility_url = 'https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--datapoints--infant_mortality_rate_per_1000_births--by--geo--time.csv'
life_expectancy_url = 'https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--datapoints--life_expectancy_years--by--geo--time.csv'


# Data
# read dataset
country_df = pd.read_csv(country_url)
gdp_df = pd.read_csv(gdp_url, skiprows=1, names=['Geo','Year','gdp_per_capita'])
infant_mortality_df = pd.read_csv(infant_mortaility_url, skiprows=1, names=['Geo','Year','mortality_rate'])
life_expectancy_df = pd.read_csv(life_expectancy_url, skiprows=1, names=['Geo','Year','life_expectancy'])


# add country information 
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


gdp_by_year = pd.DataFrame(df.groupby(['Year','world_4region']).gdp_per_capita.mean()).reset_index()
mortality_by_year = pd.DataFrame(df.groupby(['Year','world_4region']).mortality_rate.mean()).reset_index()
life_expectancy_by_year = pd.DataFrame(df.groupby(['Year','world_4region']).life_expectancy.mean()).reset_index()



# multiple line plot
import seaborn as sns                  
sns.lineplot('Year', 'gdp_per_capita', data=gdp_by_year, hue='world_4region')
sns.lineplot('Year', 'mortality_rate', data=mortality_by_year, hue='world_4region')
sns.lineplot('Year', 'life_expectancy', data=life_expectancy_by_year, hue='world_4region')
