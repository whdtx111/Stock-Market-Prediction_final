import requests

url = "http://data.eastmoney.com/DataCenter_V3/gdhs/GetList.ashx"

querystring = {"reportdate":"","market":"","changerate":"=","range":"=","pagesize":"50","page":"1","sortRule":"-1","js":"var%20gpcgYIJv","param":"","rt":"51526418"}

payload = "{\n    \"uploads\": [\n        {\n            \"src_id\": 38,\n            \"ad_server\": \"bilibili\",\n            \"is_ad\": 0,\n            \"area\": 1,\n            \"ad_cb\": \"\",\n            \"event\": \"show\",\n            \"is_visible\": 1,\n            \"idx\": 4,\n            \"mid\": \"\",\n            \"client_version\": \"\",\n            \"ts\": 1544797263533,\n            \"resource_id\": 34,\n            \"load_ts\": 1544797261233,\n            \"server_type\": 0,\n            \"id\": 188319\n        }\n    ]\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "2f1d1c55-ba72-4f17-925e-17fce7eb8ba0"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
