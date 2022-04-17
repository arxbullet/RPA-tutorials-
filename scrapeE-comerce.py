#install beutifull soup : pip install bs4
#install request 
#install pandas

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

"""
______________________________________ SINGLE PAGE SCRAPPING ____________________________________________
"""

#                 HTTP REQUEST 

# Store website in a variable
website = 'httpblabla'
# Get request
response = requests.get(website)
# Http status
response.status_code
# Soup object
soup = bs(response.content, 'html.parser')
# Results
products = soup.find_all("a", {"class":"exampleclass"})
# Count results
len(products) 
# Target necessary data
"""
ej : 
-product name
-product id
-product quantity
"""

#                        DATAFRAME

# Formating python dataframe
dataframe = {
    'productName' : [],
    'productId': [],
    'productQuantity' : []
}

for result in products:
    try:
        name = result.find("a", {"class":"examplename"}).get_text()
        id = result.find("a", {"class":"exampleid"}).get_text()
        quantity = result.find("a", {"class":"examplequantity"}).get_text()
        dataframe['productName'].append(name)
        dataframe['productName'].append(id)
        dataframe['productName'].append(quantity)
    except:
        dataframe['productName'].append('notfind')
        dataframe['productName'].append('notfind')
        dataframe['productName'].append('notfind')

# Also we can create a panda dataframe
panda_dataframe = pd.DataFrame(dataframe)

# Export to excel 
panda_dataframe.to_excel('resultsproducts.elxs', index=False)


"""
______________________________________ MULTI PAGE SCRAPPING ____________________________________________
"""
# quantity of pages 
pagination = result.find("div", {"class":"div_paginacion"}).get_text()
# max value of page
pages = pagination.max()
#in case query params start at second page
first_page_website = requests.get('http:fistpage')
#for the first page the next steps can be the steps for a single page scrapping

for i in range(2, pages):
    multiwebsite = requests.get('http:first//page=' + str(i))
    results = soup.find_all("a", {"class":"exampleclass"})

    # for inside a for 
    for result in products:
        try:
            name = result.find("a", {"class":"examplename"}).get_text()
            id = result.find("a", {"class":"exampleid"}).get_text()
            quantity = result.find("a", {"class":"examplequantity"}).get_text()
            dataframe['productName'].append(name)
            dataframe['productName'].append(id)
            dataframe['productName'].append(quantity)
        except:
            dataframe['productName'].append('notfind')
            dataframe['productName'].append('notfind')
            dataframe['productName'].append('notfind')
