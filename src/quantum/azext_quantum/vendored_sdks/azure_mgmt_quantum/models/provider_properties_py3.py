# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ProviderProperties(Model):
    """Provider properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar description: A description about this provider.
    :vartype description: str
    :ivar provider_type: Provider type.
    :vartype provider_type: str
    :ivar company: Company name.
    :vartype company: str
    :ivar default_endpoint: Provider's default endpoint.
    :vartype default_endpoint: str
    :param aad: Azure Active Directory info.
    :type aad: ~azure.quantum.models.ProviderPropertiesAad
    :param managed_application: Provider's Managed-Application info
    :type managed_application:
     ~azure.quantum.models.ProviderPropertiesManagedApplication
    :param targets: The list of targets available from this provider.
    :type targets: list[~azure.quantum.models.TargetDescription]
    :param skus: The list of skus available from this provider.
    :type skus: list[~azure.quantum.models.SkuDescription]
    :param quota_dimensions: The list of quota dimensions from the provider.
    :type quota_dimensions: list[~azure.quantum.models.QuotaDimension]
    :param pricing_dimensions: The list of pricing dimensions from the
     provider.
    :type pricing_dimensions: list[~azure.quantum.models.PricingDimension]
    """

    _validation = {
        'description': {'readonly': True},
        'provider_type': {'readonly': True},
        'company': {'readonly': True},
        'default_endpoint': {'readonly': True},
    }

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'provider_type': {'key': 'providerType', 'type': 'str'},
        'company': {'key': 'company', 'type': 'str'},
        'default_endpoint': {'key': 'defaultEndpoint', 'type': 'str'},
        'aad': {'key': 'aad', 'type': 'ProviderPropertiesAad'},
        'managed_application': {'key': 'managedApplication', 'type': 'ProviderPropertiesManagedApplication'},
        'targets': {'key': 'targets', 'type': '[TargetDescription]'},
        'skus': {'key': 'skus', 'type': '[SkuDescription]'},
        'quota_dimensions': {'key': 'quotaDimensions', 'type': '[QuotaDimension]'},
        'pricing_dimensions': {'key': 'pricingDimensions', 'type': '[PricingDimension]'},
    }

    def __init__(self, *, aad=None, managed_application=None, targets=None, skus=None, quota_dimensions=None, pricing_dimensions=None, **kwargs) -> None:
        super(ProviderProperties, self).__init__(**kwargs)
        self.description = None
        self.provider_type = None
        self.company = None
        self.default_endpoint = None
        self.aad = aad
        self.managed_application = managed_application
        self.targets = targets
        self.skus = skus
        self.quota_dimensions = quota_dimensions
        self.pricing_dimensions = pricing_dimensions
