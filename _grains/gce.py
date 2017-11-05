"""Get info from gce metadata and put it into grains store."""
from __future__ import print_function
from __future__ import unicode_literals

import json

import six


def _decode_list(data):
    """Decode list items from unicode to normal strings."""
    ret = []
    for item in data:
        if isinstance(item, six.text_type):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        ret.append(item)
    return ret


def _decode_dict(data):
    """Decode dictionary keys and values from unicode to normal strings."""
    ret = {}
    for key, value in data.items():
        if isinstance(key, six.text_type):
            key = key.encode('utf-8')
        if isinstance(value, six.text_type):
            value = value.encode('utf-8')
        if isinstance(key, six.binary_type):
            key = key.decode('utf-8')
        if isinstance(value, six.binary_type):
            value = value.decode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        ret[key] = value
    return ret


def gce_metadata():
    """
    Fetch all metadata from GCE.

    Also fills in some legacy grain data
    """
    ret = {}
    http = six.moves.http_client.HTTPConnection('metadata.google.internal')
    http.request('GET', '/computeMetadata/v1/instance/?recursive=true', None,
                 {'Metadata-Flavor': 'Google'})
    resp = http.getresponse()
    json_str = resp.read().decode('utf-8')
    metadata = json.loads(json_str, object_hook=_decode_dict)

    ipv4 = metadata['networkInterfaces'][0]['accessConfigs'][0]['externalIp']
    ret['pub_fqdn_ipv4'] = ret['external_ip'] = ipv4
    ret['tags'] = ret['roles'] = metadata['tags']
    ret['zone'] = metadata['zone']
    ret['gce'] = metadata

    return ret


if __name__ == '__main__':
    print(gce_metadata())
