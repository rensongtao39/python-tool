import http.client

def getSystemUserBase():

    # conn = http.client.HTTPSConnection("10.158.161.136", 30584)
    conn = http.client.HTTPConnection("10.158.161.136", 30584)
    payload = ''
    headers = {
        'dh_test_union': '1'
    }
    conn.request("POST", "/supplier/com.dhgate.supplier.api.SupplierInfoService/getSystemUserBase?supplierId=ff80808179fb11a2017a0e96be37000c", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))



if __name__ == '__main__':
    getSystemUserBase()