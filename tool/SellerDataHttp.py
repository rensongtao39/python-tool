import http.client
import re
import requests
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


def encode_data(data):
    url = 'http://172.21.70.77/coder.php'
    params = {
        'type': 'encode',
        'auth': 'jvs1243',
        'text': data
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.text.strip()  # 假设返回的编码数据在响应体中
    else:
        raise Exception(f"请求失败，状态码: {response.status_code}")

def replace_encode_strings(sql):
    pattern = re.compile(r"encode\((.*?)\)")

    def encode_and_replace(match):
        data_to_encode = match.group(1)
        encoded_data = encode_data(data_to_encode)
        return f"{encoded_data}"

    return pattern.sub(encode_and_replace, sql)


# 处理SQL文件
def dealSql():
    # 打开输入文件用于读取
    with open("D:\Workspace\python\python-tool-seller\\tool\sql.txt", 'r', encoding='utf-8') as input_file:
        # 打开输出文件用于写入
        with open("sql_result.txt", 'w', encoding='utf-8') as output_file:
            # 逐行读取输入文件
            for sql in input_file:
                # 去除行尾换行符并添加字符串
                updated_sql = replace_encode_strings(sql)
                # 将修改后的行写入输出文件
                output_file.write(updated_sql)




if __name__ == "__main__":
    dealSql()