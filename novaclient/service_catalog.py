# Copyright 2011 OpenStack LLC.
# Copyright 2011, Piston Cloud Computing, Inc.
#
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import novaclient.exceptions


class ServiceCatalog(object):
    """Helper methods for dealing with a Keystone Service Catalog."""

    def __init__(self, resource_dict):
        self.catalog = resource_dict

    def get_token(self):
        return self.catalog['access']['token']['id']

    def url_for(self, service=None, admin=None, attr=None, filter_value=None):
        """Fetch the public URL from the Compute service for
        a particular endpoint attribute. If none given, return
        the first. See tests for sample service catalog."""
        catalog = self.catalog['access']['serviceCatalog']

        for service in catalog:
            if service['type'] != 'compute' and service['type'] != service:
                continue

            print service['endpoints']
            endpoints = service['endpoints']
            for endpoint in endpoints:
                if filter_value == None or endpoint[attr] == filter_value:
                    if admin == 'admin':
                        return endpoint['adminURL']
                    else:
                        return endpoint['publicURL']

        raise novaclient.exceptions.EndpointNotFound()
