'''
# S3 Bucket Notifications Destinations

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This module includes integration classes for using Topics, Queues or Lambdas
as S3 Notification Destinations.

## Examples

The following example shows how to send a notification to an SNS
topic when an object is created in an S3 bucket:

```python
import aws_cdk.aws_sns as sns


bucket = s3.Bucket(self, "Bucket")
topic = sns.Topic(self, "Topic")

bucket.add_event_notification(s3.EventType.OBJECT_CREATED_PUT, s3n.SnsDestination(topic))
```

The following example shows how to send a notification to a Lambda function when an object is created in an S3 bucket:

```python
import aws_cdk.aws_lambda as lambda_


bucket = s3.Bucket(self, "Bucket")
fn = lambda_.Function(self, "MyFunction",
    runtime=lambda_.Runtime.NODEJS_12_X,
    handler="index.handler",
    code=lambda_.Code.from_asset(path.join(__dirname, "lambda-handler"))
)

bucket.add_event_notification(s3.EventType.OBJECT_CREATED, s3n.LambdaDestination(fn))
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.aws_lambda
import aws_cdk.aws_s3
import aws_cdk.aws_sns
import aws_cdk.aws_sqs
import aws_cdk.core


@jsii.implements(aws_cdk.aws_s3.IBucketNotificationDestination)
class LambdaDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-s3-notifications.LambdaDestination",
):
    '''Use a Lambda function as a bucket notification destination.

    :exampleMetadata: infused

    Example::

        # my_lambda: lambda.Function
        
        bucket = s3.Bucket.from_bucket_attributes(self, "ImportedBucket",
            bucket_arn="arn:aws:s3:::my-bucket"
        )
        
        # now you can just call methods on the bucket
        bucket.add_event_notification(s3.EventType.OBJECT_CREATED, s3n.LambdaDestination(my_lambda), prefix="home/myusername/*")
    '''

    def __init__(self, fn: aws_cdk.aws_lambda.IFunction) -> None:
        '''
        :param fn: -
        '''
        jsii.create(self.__class__, self, [fn])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: aws_cdk.core.Construct,
        bucket: aws_cdk.aws_s3.IBucket,
    ) -> aws_cdk.aws_s3.BucketNotificationDestinationConfig:
        '''Registers this resource to receive notifications for the specified bucket.

        This method will only be called once for each destination/bucket
        pair and the result will be cached, so there is no need to implement
        idempotency in each destination.

        :param _scope: -
        :param bucket: -
        '''
        return typing.cast(aws_cdk.aws_s3.BucketNotificationDestinationConfig, jsii.invoke(self, "bind", [_scope, bucket]))


@jsii.implements(aws_cdk.aws_s3.IBucketNotificationDestination)
class SnsDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-s3-notifications.SnsDestination",
):
    '''Use an SNS topic as a bucket notification destination.

    :exampleMetadata: infused

    Example::

        bucket = s3.Bucket(self, "MyBucket")
        topic = sns.Topic(self, "MyTopic")
        bucket.add_event_notification(s3.EventType.OBJECT_CREATED, s3n.SnsDestination(topic))
    '''

    def __init__(self, topic: aws_cdk.aws_sns.ITopic) -> None:
        '''
        :param topic: -
        '''
        jsii.create(self.__class__, self, [topic])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: aws_cdk.core.Construct,
        bucket: aws_cdk.aws_s3.IBucket,
    ) -> aws_cdk.aws_s3.BucketNotificationDestinationConfig:
        '''Registers this resource to receive notifications for the specified bucket.

        This method will only be called once for each destination/bucket
        pair and the result will be cached, so there is no need to implement
        idempotency in each destination.

        :param _scope: -
        :param bucket: -
        '''
        return typing.cast(aws_cdk.aws_s3.BucketNotificationDestinationConfig, jsii.invoke(self, "bind", [_scope, bucket]))


@jsii.implements(aws_cdk.aws_s3.IBucketNotificationDestination)
class SqsDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-s3-notifications.SqsDestination",
):
    '''Use an SQS queue as a bucket notification destination.

    :exampleMetadata: infused

    Example::

        # my_queue: sqs.Queue
        
        bucket = s3.Bucket(self, "MyBucket")
        bucket.add_event_notification(s3.EventType.OBJECT_REMOVED,
            s3n.SqsDestination(my_queue), prefix="foo/", suffix=".jpg")
    '''

    def __init__(self, queue: aws_cdk.aws_sqs.IQueue) -> None:
        '''
        :param queue: -
        '''
        jsii.create(self.__class__, self, [queue])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: aws_cdk.core.Construct,
        bucket: aws_cdk.aws_s3.IBucket,
    ) -> aws_cdk.aws_s3.BucketNotificationDestinationConfig:
        '''Allows using SQS queues as destinations for bucket notifications.

        Use ``bucket.onEvent(event, queue)`` to subscribe.

        :param _scope: -
        :param bucket: -
        '''
        return typing.cast(aws_cdk.aws_s3.BucketNotificationDestinationConfig, jsii.invoke(self, "bind", [_scope, bucket]))


__all__ = [
    "LambdaDestination",
    "SnsDestination",
    "SqsDestination",
]

publication.publish()
