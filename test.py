from __future__ import print_function
import time
import stylelens_search
from stylelens_search.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_search.SearchApi()
file = '/Users/bok95/Desktop/img.jpg'

try:
  # Query to search images
  api_response = api_instance.search_image(file=file)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling SearchApi->search_image: %s\n" % e)
