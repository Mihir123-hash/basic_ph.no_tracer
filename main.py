import phonenumbers
from number import  number

from phonenumbers import  geocoder  # Geocoder is a built in function for  finding phone numbers location
ch_num = phonenumbers.parse(number, "CH") #CH stands for coountry history
print(geocoder.description_for_number(ch_num, "en")) # en is the language

from phonenumbers import carrier # carrier is used for finding service provider
service_num = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_num, "en"))