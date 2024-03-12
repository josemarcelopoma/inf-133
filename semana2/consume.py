from zeep import Client
Client = Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
)
result = Client.service.NumberToWords(5)
print(result)
resultado= Client.service.NumberToDollars(9)
print(resultado)