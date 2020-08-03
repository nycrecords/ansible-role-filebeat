import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")

def test_package_is_installed(host):
    filebeat = host.package("filebeat")

    assert filebeat.is_installed
    assert filebeat.version.startswith("7")


def test_service_is_running_and_enabled(host):
    filebeat = host.service("filebeat")

    assert filebeat.is_running
    assert filebeat.is_enabled
