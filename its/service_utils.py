from django.http import HttpResponse

from .exceptions import (
    InvalidCFSDetailException,
    InvalidDeviceNameException,
    InvalidDomainNameException,
    InvalidServiceIdException,
)


def api_validator(func):
    def _processor(service_id, domain_name, olt_device_name, cfs_detail):
        validate_service_id(service_id)
        validate_domain_name(domain_name)
        validate_device_name(olt_device_name)
        validate_CFS_detail(cfs_detail)
        return func(service_id, domain_name, olt_device_name, cfs_detail)
    return _processor


@api_validator
def get_data(service_id: int, domain_name: str, olt_device_name: str, cfs_detail: str):
    print("Service ID: ", service_id)
    print("Domain Name: ", domain_name)
    print("OLT Device Name: ", olt_device_name)
    print("CFS Detail: ", cfs_detail)
    return HttpResponse(status=201)


def validate_service_id(service_id):
    if not isinstance(service_id, int) or service_id is None or service_id == "":
        raise InvalidServiceIdException(f"service id: {service_id} is not a valid service id")


def validate_domain_name(domain_name):
    if domain_name is None or domain_name == "":
        raise InvalidDomainNameException(f"domain name: {domain_name} is not a valid domain name")


def validate_device_name(device_name):
    if device_name is None or device_name == "":
        raise InvalidDeviceNameException(f"device name: {device_name} is not a valid device name")


def validate_CFS_detail(cfs_detail):
    if cfs_detail is None or cfs_detail == "":
        raise InvalidCFSDetailException(f"CFS detail: {cfs_detail} is not a valid CFS detail")
