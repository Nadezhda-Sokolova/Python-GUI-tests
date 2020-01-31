import pytest

from fixture.application import Application

@pytest.fixture(scope="session")
def app(request):
    fixture = Application("D:\\PythonTraining\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.distroy)
    return fixture

