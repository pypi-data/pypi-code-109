from checkov.common.models.enums import CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck


class MariaDBGeoBackupEnabled(BaseResourceValueCheck):
    def __init__(self) -> None:
        name = "Ensure that MariaDB server enables geo-redundant backups"
        id = "CKV_AZURE_129"
        supported_resources = ("azurerm_mariadb_server",)
        categories = (CheckCategories.BACKUP_AND_RECOVERY,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self) -> str:
        return "geo_redundant_backup_enabled"


check = MariaDBGeoBackupEnabled()
