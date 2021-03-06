#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_resource_quota_info
short_description: Retrieve IBM Cloud 'ibm_resource_quota' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_resource_quota' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.8.1
    - Terraform v0.12.20

options:
    vsi_limit:
        description:
            - Defines the VSI limit.
        required: False
        type: int
    name:
        description:
            - Resource quota name, for example Trial Quota
        required: True
        type: str
    type:
        description:
            - Type of the quota.
        required: False
        type: str
    max_apps:
        description:
            - Defines the total app limit.
        required: False
        type: int
    max_instances_per_app:
        description:
            - Defines the total instances limit per app.
        required: False
        type: int
    max_app_instance_memory:
        description:
            - Defines the total memory of app instance.
        required: False
        type: str
    total_app_memory:
        description:
            - Defines the total memory for app.
        required: False
        type: str
    max_service_instances:
        description:
            - Defines the total service instances limit.
        required: False
        type: int
    iaas_classic_username:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'vsi_limit',
    'name',
    'type',
    'max_apps',
    'max_instances_per_app',
    'max_app_instance_memory',
    'total_app_memory',
    'max_service_instances',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    vsi_limit=dict(
        required=False,
        type='int'),
    name=dict(
        required=True,
        type='str'),
    type=dict(
        required=False,
        type='str'),
    max_apps=dict(
        required=False,
        type='int'),
    max_instances_per_app=dict(
        required=False,
        type='int'),
    max_app_instance_memory=dict(
        required=False,
        type='str'),
    total_app_memory=dict(
        required=False,
        type='str'),
    max_service_instances=dict(
        required=False,
        type='int'),
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    result = ibmcloud_terraform(
        resource_type='ibm_resource_quota',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.8.1',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
