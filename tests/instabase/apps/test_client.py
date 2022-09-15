from instabase.apps import Client
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))


def test_extract_from_input_bytes():
	app_name = 'US Bank Statements'
	app_version = '3.0.0'
	file_url = 'https://www.commercebank.com/-/media/cb/pdf/personal/bank/statement_sample1.pdf'

	client = Client()
	test_data_file_name = 'test_data_bank_statement.pdf'
	with open(os.path.join(dir_path,'data/'+test_data_file_name),'rb') as f:
		resp = client.extract_from_input_bytes(f.read(), test_data_file_name, app_name, app_version)
		assert resp!=None
		expected_resp_fields = ['input_file_name', 'records', 'error', 'api_version']
		for field in expected_resp_fields:
			assert field in resp
		assert resp['error'] == None
		assert resp['api_version'] == 'v1'

	
