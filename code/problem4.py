'''
Problem 4

For this problem, I wanted to look and see if their is a relationship between 
healthcare spending per capita and long term unemployment. 
'''
import pandas as pd
import seaborn as sns

country_url = 'https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--entities--geo--country.csv'
health_spending_url = 'https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--datapoints--government_health_spending_per_person_international_dollar--by--geo--time.csv'
long_term_unemplyment_url = 'https://raw.githubusercontent.com/open-numbers/ddf--gapminder--systema_globalis/master/ddf--datapoints--long_term_unemployment_rate_percent--by--geo--time.csv'


# read dataset
country_df = pd.read_csv(country_url)
health_spending_df = pd.read_csv(health_spending_url, skiprows=1, names=['Geo','Year','health_spending'])
long_term_unemplyment_df = pd.read_csv(long_term_unemplyment_url, skiprows=1, names=['Geo','Year','long_term_unemployement'])



# add country information 
df = pd.merge(health_spending_df,
            country_df[['country','name','latitude','longitude', 'world_4region']],
            left_on = 'Geo', 
            right_on = 'country',
            how = 'left')
            

df = pd.merge(df,
            long_term_unemplyment_df[['Geo','Year','long_term_unemployement']],
            left_on = ['Geo','Year'], 
            right_on = ['Geo','Year'],
            how = 'left')

df = df.dropna()
df['log_health_spend'] = np.log10(df['health_spending'])
df.rename(columns={'world_4region':'Continent'}, inplace=True)



# create pairplot
sns.pairplot(df, 
             vars = ['long_term_unemployement', 'log_health_spend'], 
             hue = 'Continent', diag_kind = 'kde', 
             plot_kws = {'alpha': 0.6, 's': 80, 'edgecolor': 'k'},
             size = 4);