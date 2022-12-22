import http, json, pytest, requests

from its import constants
from its.helper import json_file_reader
from its.utils import header_with_token_generator

BAD_REQUEST = http.HTTPStatus.BAD_REQUEST


class TestOSSAPI:

    data = json_file_reader(file=constants.API_FILE_PATH)
    headers = header_with_token_generator()

    def generic_method(self, data):
        request_url_data = requests.post(url=constants.API_URL, data=json.dumps(data), headers=self.headers)
        return request_url_data

    ### testcase for invalid method provided.
    @pytest.mark.parametrize("input_data", data['happy_path'])
    @pytest.mark.parametrize("resp_msg", data['response_message'])
    def test_wrong_method(self, input_data, resp_msg):
        response = requests.get(url=constants.API_URL, data=json.dumps(input_data), headers=self.headers)
        resp_content = json.loads(response.content.decode('utf-8'))
        assert response.status_code == http.HTTPStatus.METHOD_NOT_ALLOWED
        assert resp_content["error"] == resp_msg['wrong_method']

    ### testcase for happy path provided.
    @pytest.mark.parametrize("input_data", data['happy_path'])
    @pytest.mark.parametrize("resp_msg", data['response_message'])
    def test_happy_path_201(self, input_data, resp_msg):
        response = self.generic_method(input_data)
        assert response.status_code == http.HTTPStatus.CREATED
        assert response.content.decode('utf-8') == resp_msg['success']

    ### testcase for invalid service Id provided.
    @pytest.mark.parametrize("input_data", data['service_id_validation'])
    @pytest.mark.parametrize("resp_msg", data['response_message'])
    def test_wrong_service_id_400(self, input_data, resp_msg):
        response = self.generic_method(input_data)
        assert response.status_code == BAD_REQUEST
        assert response.content.decode('utf-8') == resp_msg['bad_service_id']

    ### testcase for invalid domain name provided.
    @pytest.mark.parametrize("input_data", data['domain_name_validation'])
    @pytest.mark.parametrize("resp_msg", data['response_message'])
    def test_wrong_domain_name_400(self, input_data, resp_msg):
        response = self.generic_method(input_data)
        assert response.status_code == BAD_REQUEST
        assert response.content.decode('utf-8') == resp_msg['bad_domain_name']

    ### testcase for invalid device name provided.
    @pytest.mark.parametrize("input_data", data['device_name_validation'])
    @pytest.mark.parametrize("resp_msg", data['response_message'])
    def test_wrong_device_name_400(self, input_data, resp_msg):
        response = self.generic_method(input_data)
        assert response.status_code == BAD_REQUEST
        assert response.content.decode('utf-8') == resp_msg['bad_device_name']

    ### testcase for invalid CFS detail provided.
    @pytest.mark.parametrize("input_data", data['cfs_detail_validation'])
    @pytest.mark.parametrize("resp_msg", data['response_message'])
    def test_wrong_olt_device_detail_400(self, input_data, resp_msg):
        response = self.generic_method(input_data)
        assert response.status_code == BAD_REQUEST
        assert response.content.decode('utf-8') == resp_msg['bad_cfs_details']
