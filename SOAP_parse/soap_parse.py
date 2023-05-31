import requests
import xml.etree.ElementTree as ET

#user to input celsius
celsius = int(input("Enter Celsius: "))
#url of soap api from w3schools
url = 'https://www.w3schools.com/xml/tempconvert.asmx?op=CelsiusToFahrenheit'
#soap xml
SOAPEnvelope = f"""
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
    <CelsiusToFahrenheit xmlns="https://www.w3schools.com/xml/">
    <Celsius>{celsius}</Celsius>
    </CelsiusToFahrenheit>
</soap:Body>
</soap:Envelope>
"""
#specify type
options = {
    "Content-Type": "text/xml; charset=utf-8"
}
#enable response using request.post()
response = requests.post(url, data = SOAPEnvelope, headers = options)

#assign the response as a variable
root = ET.fromstring(response.text)

#get the results
for child in root.iter("{https://www.w3schools.com/xml/}CelsiusToFahrenheitResult"):
    print(child.text, "Fahrenheit")