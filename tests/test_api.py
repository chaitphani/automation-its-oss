import pytest

from its import constants
from its.exceptions import (
    InvalidCFSDetailException,
    InvalidDeviceNameException,
    InvalidDomainNameException,
    InvalidServiceIdException,
)
from its.json_extractor import inject_test_data
from its.utils import get_data


class TestOSSAPI:
    test_data = inject_test_data(file=constants.FILE_PATH)

    @pytest.mark.parametrize("input", test_data.happy_path)
    def test_happy_path(self, input):
        response = get_data(
            input['Service_ID'], input['Domain_Name'], input['OLT_Device_Name'], input['CFS_Detail']
        )
        assert response.status_code == 201

    @pytest.mark.parametrize("input", test_data.invalid_service_id)
    def test_invaild_service_id(self, input):
        with pytest.raises(InvalidServiceIdException):
            get_data(
                input['Service_ID'],
                input['Domain_Name'],
                input['OLT_Device_Name'],
                input['CFS_Detail'],
            )

    @pytest.mark.parametrize("input", test_data.invalid_device_name)
    def test_invaild_device_name(self, input):
        with pytest.raises(InvalidDeviceNameException):
            get_data(
                input['Service_ID'],
                input['Domain_Name'],
                input['OLT_Device_Name'],
                input['CFS_Detail'],
            )

    @pytest.mark.parametrize("input", test_data.invalid_domain_name)
    def test_invaild_domain_name(self, input):
        with pytest.raises(InvalidDomainNameException):
            get_data(
                input['Service_ID'],
                input['Domain_Name'],
                input['OLT_Device_Name'],
                input['CFS_Detail'],
            )

    @pytest.mark.parametrize("input", test_data.invalid_cfs_detail)
    def test_invaild_cfs_details(self, input):
        with pytest.raises(InvalidCFSDetailException):
            get_data(
                input['Service_ID'],
                input['Domain_Name'],
                input['OLT_Device_Name'],
                input['CFS_Detail'],
            )
