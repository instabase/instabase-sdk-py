#  Extract information from solution name=US Bank Statements version=3.0.0 for given file_url
import base64
import json
import os
import requests
import urllib
import validators

from .enums import KEY_API_TOKEN, KEY_ROOT_URL
from ._utils import get_env_var, build_headers


class SDK:

    def __init__(self):
        """Initialize the SDK using environment config."""
        self.token = get_env_var(KEY_API_TOKEN)
        self.root_url = get_env_var(KEY_ROOT_URL)


    def _build_run_url(self, version='v1'):
        return urllib.parse.urljoin(self.root_url,'api/')+version+'/solution/run_developers_portal'


    def extract_from_input_bytes(self, bytes_content, file_name, app_name, app_version):
        """ Extract information from an input file represented by bytes_content and file_name."""
        
        if not bytes_content:
            raise Exception('No bytes content found in input')
        if not file_name:
            raise Exception('file_name cannot be None')
        if not app_name or not app_version:
            raise Exception('app_name or app_version cannot be None') 


        url = self._build_run_url()
        headers = build_headers(self.token)
        # We need to base64 encode the file and send it to the API
        resp = requests.post(
            url,
            headers=headers,
            data=json.dumps({
                'input_file_content':
                base64.b64encode(bytes_content).decode('ascii'),
                'input_file_name':
                file_name,
                'name': app_name,
                'settings': {
                    'output_has_run_id': True,
                    'use_flow_batch_mode': True
                },
                'version': app_version
            }))

        return resp.json()


    def extract_from_input_url(self, file_url, app_name, app_version):
        """ Extract information from an input file located at file_url."""
        if not file_url or not validators.url(file_url):
            raise Exception('{} is an invalid file_url'.format(file_url))
        if not app_name or not app_version:
            raise Exception('app_name or app_version cannot be None')

        _fileresp = requests.get(file_url)
        _fileresp = requests.get(file_url)
        _, file_name = os.path.split(file_url)
        content = _fileresp.content

        return self.extract_from_input_bytes(content, file_name, app_name, app_version)
        