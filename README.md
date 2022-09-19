# Instabase Apps SDK

Use this SDK to access apps on apps.instabase.com.


## Setup

You will need to set the following environment variables:
1. `IB_API_TOKEN` : Your API token from Instabase Apps website.
2. `IB_ROOT_URL` : Root URL of Instabase App website.

## Getting Started
Example below demonstrates usage of the SDK to extract contents of an input file using Instabase's Bank Statements application (version 3.0.0):

### Input file represented by remote URL

```
from instabase.apps import Client

app_name, app_version = 'US Bank Statements', '3.0.0'
file_url = '<INPUT FILE URL HERE>'

client = Client()
resp = client.extract_from_input_url(file_url, app_name, app_version)
print(resp)
```


### Input file represented by file path

```
from instabase.apps import Client

app_name, app_version = 'US Bank Statements', '3.0.0'
with open(<FILE_PATH_HERE>,'rb') as f:
	resp = client.extract_from_input_bytes(f.read(), <FILE_NAME>, app_name, app_version)
	print(resp)
```