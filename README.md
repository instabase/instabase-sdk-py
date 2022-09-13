# Instabase Apps SDK

Use this SDK to access apps on apps.instabase.com.


## Setup

You will need to set the following environment variables:
1. `IB_API_TOKEN` : Your API token from Instabase Apps website.
2. `IB_ROOT_URL` : Root URL of Instabase App website.

## Getting Started
Example below demonstrates usage of the SDK to extract contents of an image using Instabase's Bank Statements application (version 3.0.0):

```
from instabase import SDK

app_name, app_version = 'US Bank Statements', '3.0.0'
file_url = 'https://apps.instabase.com/static/assets/images/cloud-developers/us-bs/sample-us-bs-1.jpeg'

sdk = SDK()
resp = sdk.extract_from_input_url(file_url, app_name, app_version)
print(resp)
```

