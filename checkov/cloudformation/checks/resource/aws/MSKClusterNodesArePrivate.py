from typing import Any

from checkov.cloudformation.checks.resource.base_resource_negative_value_check import BaseResourceNegativeValueCheck
from checkov.common.models.enums import CheckCategories


class MSKClusterNodesArePrivate(BaseResourceNegativeValueCheck):
    def __init__(self) -> None:
        name = "Ensure MSK nodes are private"
        id = "CKV_AWS_291"
        supported_resources = ['AWS::MSK::Cluster']
        categories = [CheckCategories.NETWORKING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self) -> str:
        return 'Properties/BrokerNodeGroupInfo/ConnectivityInfo/PublicAccess/Type' # any multiple?

    def get_forbidden_values(self) -> list[Any]:
        return ["SERVICE_PROVIDED_EIPS"]


check = MSKClusterNodesArePrivate()
