from .return_class import AbstractApiClass


class FeatureGroupExport(AbstractApiClass):
    """
        A feature Group Export Job
    """

    def __init__(self, client, featureGroupExportId=None, featureGroupVersion=None, connectorType=None, outputLocation=None, fileFormat=None, databaseConnectorId=None, objectName=None, writeMode=None, databaseFeatureMapping=None, idColumn=None, status=None, createdAt=None, exportCompletedAt=None):
        super().__init__(client, featureGroupExportId)
        self.feature_group_export_id = featureGroupExportId
        self.feature_group_version = featureGroupVersion
        self.connector_type = connectorType
        self.output_location = outputLocation
        self.file_format = fileFormat
        self.database_connector_id = databaseConnectorId
        self.object_name = objectName
        self.write_mode = writeMode
        self.database_feature_mapping = databaseFeatureMapping
        self.id_column = idColumn
        self.status = status
        self.created_at = createdAt
        self.export_completed_at = exportCompletedAt

    def __repr__(self):
        return f"FeatureGroupExport(feature_group_export_id={repr(self.feature_group_export_id)},\n  feature_group_version={repr(self.feature_group_version)},\n  connector_type={repr(self.connector_type)},\n  output_location={repr(self.output_location)},\n  file_format={repr(self.file_format)},\n  database_connector_id={repr(self.database_connector_id)},\n  object_name={repr(self.object_name)},\n  write_mode={repr(self.write_mode)},\n  database_feature_mapping={repr(self.database_feature_mapping)},\n  id_column={repr(self.id_column)},\n  status={repr(self.status)},\n  created_at={repr(self.created_at)},\n  export_completed_at={repr(self.export_completed_at)})"

    def to_dict(self):
        return {'feature_group_export_id': self.feature_group_export_id, 'feature_group_version': self.feature_group_version, 'connector_type': self.connector_type, 'output_location': self.output_location, 'file_format': self.file_format, 'database_connector_id': self.database_connector_id, 'object_name': self.object_name, 'write_mode': self.write_mode, 'database_feature_mapping': self.database_feature_mapping, 'id_column': self.id_column, 'status': self.status, 'created_at': self.created_at, 'export_completed_at': self.export_completed_at}

    def refresh(self):
        """Calls describe and refreshes the current object's fields"""
        self.__dict__.update(self.describe().__dict__)
        return self

    def describe(self):
        """A feature group export"""
        return self.client.describe_feature_group_export(self.feature_group_export_id)

    def wait_for_results(self, timeout=3600):
        """
        A waiting call until feature group export is created.

        Args:
            timeout (int, optional): The waiting time given to the call to finish, if it doesn't finish by the allocated time, the call is said to be timed out. Default value given is 3600 milliseconds.

        Returns:
            None
        """
        return self.client._poll(self, {'PENDING', 'EXPORTING'}, timeout=timeout)

    def get_status(self):
        """
        Gets the status of the feature group export.

        Returns:
            Enum (string): A string describing the status of a feature group export (pending, complete, etc.).
        """
        return self.describe().status

    # to be deleted
    def get_results(self):
        return self.client.get_export_result(self.feature_group_export_id)
