# Intro:
- This directory will be for explore data visualization through Python.
- Data Visualization: exploring data through visual representations
    - Data mining: using code to explore patterns and connections in a data set.
        - data set: can be a small list of numbers up to gigabytes of data.
- More than just pretty pictures
    - Helps see patterns and significance in data sets.
- We'll be analyzing data online in two common formats: CSV and JSON
    - CSV: comma separated values, tricky for humans to read, but easy to process and extract data from 
- **Note: for all who reads this README, for things like Install matplotlib, please refer to Google-senpai for assistance. Also, most content is from Python Crash Course**

## Installations to start:
- Install matplotlib first.
    - a mathematical plotting library.
    - matplotlib gallery at: http://matplotlib.org/
- Install Pygal next
    - Python visualization package which produces scalable vector graphic files.
    - helps scale to fit users screens
    - mac/linux: pip install --user pygal
    - pygal gallery at: http://www.pygal.org

## Useful Links
- you can donwload weather data at: https://www.wunderground.com/history/
    - Seems like you need to use their API to provide the weather data and historical records through HTTP requests
- More data sets can be obtained from: http://frictionlessdata.io/
- Gross Domestic Product: http://data.okfn.org/data/core/gdp
    - it seems like the data goes up to 2014 so far
- http://data.worldbank.org/indicator/
    - contains many data sets that are broken down for info on each country worldwide
- sample of what an API call looks like:
    -  https://api.github.com/search/repositories?q=language:python&sort=stars  
    - first part: up to the .com/ directs request to part of github website that responds to API calls
    - search/repositories tell API conduct a search through all rep on site
    - ? after rep signals about to pass an argument
    - q stands for query
    - = allows to begin specifying a query
    - language:python indicate we want info in git that has python as main
    - &sort=stars, sorts byy number stars given
    - NOTE: there's a limit to how many requests you can make in a certain amount of time
        - https://api.github.com/rate_limit
        - obtaining API keys usually raise the limits you can do 