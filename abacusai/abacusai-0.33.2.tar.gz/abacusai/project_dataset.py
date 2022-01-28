from .data_filter import DataFilter
from .return_class import AbstractApiClass


class ProjectDataset(AbstractApiClass):
    """
        The description of how a dataset is used in a project
    """

    def __init__(self, client, name=None, datasetType=None, datasetId=None, streaming=None, dataFilters={}):
        super().__init__(client, None)
        self.name = name
        self.dataset_type = datasetType
        self.dataset_id = datasetId
        self.streaming = streaming
        self.data_filters = client._build_class(DataFilter, dataFilters)

    def __repr__(self):
        return f"ProjectDataset(name={repr(self.name)},\n  dataset_type={repr(self.dataset_type)},\n  dataset_id={repr(self.dataset_id)},\n  streaming={repr(self.streaming)},\n  data_filters={repr(self.data_filters)})"

    def to_dict(self):
        return {'name': self.name, 'dataset_type': self.dataset_type, 'dataset_id': self.dataset_id, 'streaming': self.streaming, 'data_filters': self._get_attribute_as_dict(self.data_filters)}
