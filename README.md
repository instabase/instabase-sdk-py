# Instabase Apps SDK

Use this SDK to access apps on apps.instabase.com.


## Setup

You will need to set the following environment variables:
1. `IB_API_TOKEN` : Your API token from Instabase Apps website.
2. `IB_ROOT_URL` : Root URL of Instabase App website.

## Getting Started
Example below demonstrates usage of the SDK to extract contents of an image using Instabase's Bank Statements application (version 3.0.0):

```
from instabase.apps import Client

app_name, app_version = 'US Bank Statements', '3.0.0'
file_url = '<INPUT FILE URL HERE>'

client = Client()
resp = client.extract_from_input_url(file_url, app_name, app_version)
print(resp)
```

