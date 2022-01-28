from .return_class import AbstractApiClass


class PredictionMetricVersion(AbstractApiClass):
    """
        A Prediction Metric version for a Prediction Metric job description.
    """

    def __init__(self, client, createdAt=None, error=None, featureGroupVersion=None, predictionMetricCompletedAt=None, predictionMetricConfig=None, predictionMetricId=None, predictionMetricStartedAt=None, predictionMetricVersion=None, status=None):
        super().__init__(client, predictionMetricVersion)
        self.created_at = createdAt
        self.error = error
        self.feature_group_version = featureGroupVersion
        self.prediction_metric_completed_at = predictionMetricCompletedAt
        self.prediction_metric_config = predictionMetricConfig
        self.prediction_metric_id = predictionMetricId
        self.prediction_metric_started_at = predictionMetricStartedAt
        self.prediction_metric_version = predictionMetricVersion
        self.status = status

    def __repr__(self):
        return f"PredictionMetricVersion(created_at={repr(self.created_at)},\n  error={repr(self.error)},\n  feature_group_version={repr(self.feature_group_version)},\n  prediction_metric_completed_at={repr(self.prediction_metric_completed_at)},\n  prediction_metric_config={repr(self.prediction_metric_config)},\n  prediction_metric_id={repr(self.prediction_metric_id)},\n  prediction_metric_started_at={repr(self.prediction_metric_started_at)},\n  prediction_metric_version={repr(self.prediction_metric_version)},\n  status={repr(self.status)})"

    def to_dict(self):
        return {'created_at': self.created_at, 'error': self.error, 'feature_group_version': self.feature_group_version, 'prediction_metric_completed_at': self.prediction_metric_completed_at, 'prediction_metric_config': self.prediction_metric_config, 'prediction_metric_id': self.prediction_metric_id, 'prediction_metric_started_at': self.prediction_metric_started_at, 'prediction_metric_version': self.prediction_metric_version, 'status': self.status}

    def wait_for_prediction_metric_version(self, timeout=1200):
        """
        A waiting call until the prediction metric version is ready.

        Args:
            timeout (int, optional): The waiting time given to the call to finish, if it doesn't finish by the allocated time, the call is said to be timed out. Default value given is 1200 milliseconds.

        Returns:
            None
        """
        return self.client._poll(self, {'PENDING', 'RUNNING'}, timeout=timeout)

    def get_status(self):
        """
        Get the lifecycle status of this version.

        Returns:
            Enum (string): An enum value of the lifecycle status of this version.
        """
        return self.describe().status
