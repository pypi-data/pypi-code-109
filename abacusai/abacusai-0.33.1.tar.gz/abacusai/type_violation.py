from .return_class import AbstractApiClass


class TypeViolation(AbstractApiClass):
    """
        Summary of important type mismatches for a feature discovered by a model monitoring instance
    """

    def __init__(self, client, name=None, trainingDataType=None, predictionDataType=None):
        super().__init__(client, None)
        self.name = name
        self.training_data_type = trainingDataType
        self.prediction_data_type = predictionDataType

    def __repr__(self):
        return f"TypeViolation(name={repr(self.name)},\n  training_data_type={repr(self.training_data_type)},\n  prediction_data_type={repr(self.prediction_data_type)})"

    def to_dict(self):
        return {'name': self.name, 'training_data_type': self.training_data_type, 'prediction_data_type': self.prediction_data_type}
