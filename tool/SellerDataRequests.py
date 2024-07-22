import requests

url = "http://10.158.161.136:30584/supplier/com.dhgate.supplier.api.SupplierInfoService/getSystemUserBase?supplierId=ff80808179fb11a2017a0e96be37000c"

payload = {}
headers = {
    'dh_test_union': '1'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)