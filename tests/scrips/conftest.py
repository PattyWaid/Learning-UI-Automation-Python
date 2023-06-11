from common.common import common_utils


def pytest_configure(config):
    print("Initialzing properties file")
    common_utils.load_properties()