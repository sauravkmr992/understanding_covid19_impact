# -*- coding: utf-8 -*-
import scrapy
import json

class NumbersSpider(scrapy.Spider):
    name = 'numbers'
    allowed_domains = ['data.covid19india.org']
    
    # this is the first request we are sending and response is sent back to the parse method just below
    start_urls = ['https://data.covid19india.org/v4/min/data.min.json']

    """parse method is looping through every state extracting each state's population and sending a request to the state's API 
       address which in turn sends the response to parsenum function along with the state population"""
       
    def parse(self, response):

        dict=json.loads(response.body)
        for x in dict:
            population= dict.get(x).get('meta').get('population')
            yield scrapy.Request(url=f'https://data.covid19india.org/v4/min/timeseries-{x}.min.json',callback=self.parsenum,meta={'state':x,'population':population})
     
    """ Parsenum function is extracting all the required information from the json response for eg. "confirmed cases",
    "recovered cases" etc. and returning it at the end. """    
            
    def parsenum(self,response):
            dic=json.loads(response.body)
            place=response.request.meta['state']
            population=response.request.meta['population']         # Extracting population and state name out of the response  
                                                                   # that was passed by parse func while sending the request 
            
            
            # getting dates out of the response
            dates=dic.get(place).get('dates')
            for date in dates:              # iterating through every date
                layer=dates.get(date)       # extracting the data for this particular date and storing it into variable "layer"
                
            # PLEASE GO THROUGH JSON STRUCTURE FILE TO UNDERSTAND THE DATA EXTRACTION DONE IN THIS SCRIPT.
            
            # for every "date" dictionary we have a "delta" key which contains daily data for "confirmed","recovered","deceased" cases.  
                
                if layer.get('delta'):      #checking if it has key named "delta".
                    confirmed=layer.get('delta').get('confirmed',0)
                    deceased=layer.get('delta').get('deceased',0)
                    tested=layer.get('delta').get('tested',0)
                    recovered=layer.get('delta').get('recovered',0)
                    vaccinated=layer.get('delta').get('vaccinated1',0)+layer.get('delta').get('vaccinated2',0)
                else:
                    confirmed=0
                    deceased=0
                    tested=0
                    recovered=0
                    vaccinated=0
                
                #yielding all the concerned fields
                
                yield {
                    'dates':date,
                    'state':place,
                    'confirmed':confirmed,
                    'tested':tested,
                    'deceased':deceased,
                    'recovered':recovered,
                    'vaccinated':vaccinated,
                    'population':population
                    }    