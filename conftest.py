import pytest

from fixture.application import Application

@pytest.fixture(scope="session")
def app(request):
    fixture = Application("D:\\Python training\\FreeAddressBookPortable\\AddressBook")
    request.addfinalizer(fixture.distroy)
    return fixture

