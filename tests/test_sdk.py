from sdk import SDK


app_name = 'US Bank Statements'
app_version = '3.0.0'
file_url = 'https://apps.instabase.com/static/assets/images/cloud-developers/us-bs/sample-us-bs-1.jpeg'

sdk = SDK()
resp = sdk.extract_from_input_url(file_url, app_name, app_version)
print(resp)