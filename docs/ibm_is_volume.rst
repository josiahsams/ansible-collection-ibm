
ibm_is_volume -- Configure IBM Cloud 'ibm_is_volume' resource
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_volume' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.8.1
- Terraform v0.12.20



Parameters
----------

  profile (True, str, None)
    (Required for new resource) Vloume profile name


  iops (False, int, None)
    IOPS value for the Volume


  crn (False, str, None)
    CRN value for the volume instance


  resource_crn (False, str, None)
    The crn of the resource


  encryption_key (False, str, None)
    Volume encryption key info


  resource_group (False, str, None)
    Resource group name


  tags (False, list, None)
    Tags for the volume instance


  zone (True, str, None)
    (Required for new resource) Zone name


  capacity (False, int, 100)
    Vloume capacity value


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance


  resource_name (False, str, None)
    The name of the resource


  resource_status (False, str, None)
    The status of the resource


  name (True, str, None)
    (Required for new resource) Volume name


  status (False, str, None)
    Volume status


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, int, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

