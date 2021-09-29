# Understanding Covid19 Impact

Analysis has been done on the covid data which has been collected through scraping API's of this [covid website](https://www.covid19india.org/) which contains day-to-day information about number of **Confirmed**,**recovered**,**deceased** cases and all other sorts of Information related to the country India.

 # Scraping Data
 
 * Scraping has been done using Scrapy library which provides tons of ways to extract the data out from the website. Data has been scraped using this [link](https://data.covid19india.org/v4/min/timeseries-DL.min.json) which returns a json object having everyday statistics of confirmed,recoverd, vaccinated and deceased cases for a single state. The above link belongs to Delhi.
 * Fields captured:
      * Confirmed
      * recovered
      * deceased
      * tested
      * vaccinated
      * population
      * state
      * date
    
    This data has been scraped for every single day for every state.

 * json response file has also been added for clear understanding of the response structure.
 * Attached numbers.py file has comments added for better clarity of the process and can be found in the directory as follows:
    * covid
      * covid
        * spiders
          * numbers.py

`Note :` The above scraped data can be directly downloaded from the above mentioned [Covid Website](https://www.covid19india.org).

 # Running Python Script
   
   1. Conda/pip install scrapy version listed in the `requirements.txt` and all the other dependencies to avoid problems while running.
   2. Now, move folder **covid** to your local machine.
   3. Activate the environment then move into `covid` folder from your terminal/cmd.
   4. Type `scrapy crawl numbers.py -o covid.csv` in your terminal
   5. This will generate a csv file named  ***covid*** in your main folder.

# Covid Data Analysis

This analysis project presents detailed analysis on the scraped covid19 data. This project project deals with missing values if any, analyses relationship between the 
features through plots, treats anamoly in the data when found , inspects current active cases and testing number by states and much more. Extra fields have been 
calculated for eg .**fatality ratio**, **percentage population affected** etc to see at what extent the lives of people from every state has been impacted by 
corona virus. Recovery rate of the country and impact of vaccination on active cases has also been studied. Pandas has been used for data manipulation where Seaborn 
and matplotlib is used for plots.  Please see `covid.ipynb` for more details and plots on the covid data.
