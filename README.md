# Homework 1

All code for the assignment is in the source_code folder on github. Each file can be run executed upon opening. The files pull the data needed for each question directly from the GitHub Gapminder repository so no need for changing working directory or downlaoding data.

## Question 1

I received a score of 69% on the GapMinder test. Two of the questions that surprised me the most were the question that asked about percent of the world population with access to electicity as well as the question about vaccination rates. In both cases, I underestimated how high the percentages were. For both statistics, the world is at 80% coverage. This is quite a bit higher than I excpected. 

For the question, I choose to look at the question in the survey that asked about comparing the poverty rate from 20 years ago to today:

"In the last 20 years the proportion of people living in extreme poverty worldwide, has...? "

So I set out to look at historical poverty rates to see try and see how far the world has come at pulling people out of extreme poverty.

First I looked at the extreme poverty rate year over year to look at the trend as a whole. 


![Screenshot](poverty_rate_by_year.png)



## Question 2


## Question 3

For question 3, we are looking at the relationship between GDP Per Capita, Life Expectancy, and Mortality Rate over time. To do this, I leveraged multiple line charts plotting by year to look at how each of these variables changed over time. I then looked at a pairwise plot between the 3 variables to see if I could identify any strong correlation between the variables.

![Screenshot](dual_plot.png)
![Screenshot](gdp_per_year.png)

Looking at these charts, it would be fairly easy to draw a conclusion that all of these variables are related to each. It makes sense there is a strong relationship between GDP Per Capita rising with a rise in Life Expectancy and a decrease in Mortality Rate. However, it is also clear that GDP Per Capita has risen much slower than life expectancy and the mortality rate has decreases at a slower clip than the rise in GDP, leading me to believe their are other factors that have a strong impact on these rates. Much of the improvement in Life Expectancy and Mortality Rates likely has to do with improvements in medicine and access to clean water/sanitation more so than the GDP Per Capita.

