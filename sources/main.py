import subprocess
import re
from sources.some_class_file import APICalls
from sources.some_class_file import Connect


def function_over_traceroute_analysis(ip):
    out = traceroute_analysis(ip)
    # some computation over traceroute_analysis ip
    out = out[::-1]
    return out


def call_api_from_outside_class(url):
    obj = APICalls()
    out = obj.do_get(url)
    return out


def gather_mac(conn: Connect, ip: str):
    """
    Get the mac address for ip
    :param conn: conn session
    :param ip: ip of the host
    :return: str, mac address of the host
    """
    out = conn.send_command('sh ip arp ' + ip + ' vrf all | i Address n 1')
    out = out.split('\r\n')
    mac = out[1].split()[out[0].lower().split().index('mac')]
    return mac

