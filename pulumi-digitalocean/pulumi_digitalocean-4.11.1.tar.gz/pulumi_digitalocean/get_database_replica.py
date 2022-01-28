# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetDatabaseReplicaResult',
    'AwaitableGetDatabaseReplicaResult',
    'get_database_replica',
    'get_database_replica_output',
]

@pulumi.output_type
class GetDatabaseReplicaResult:
    """
    A collection of values returned by getDatabaseReplica.
    """
    def __init__(__self__, cluster_id=None, database=None, host=None, id=None, name=None, password=None, port=None, private_host=None, private_network_uuid=None, private_uri=None, region=None, tags=None, uri=None, user=None):
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if database and not isinstance(database, str):
            raise TypeError("Expected argument 'database' to be a str")
        pulumi.set(__self__, "database", database)
        if host and not isinstance(host, str):
            raise TypeError("Expected argument 'host' to be a str")
        pulumi.set(__self__, "host", host)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if password and not isinstance(password, str):
            raise TypeError("Expected argument 'password' to be a str")
        pulumi.set(__self__, "password", password)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if private_host and not isinstance(private_host, str):
            raise TypeError("Expected argument 'private_host' to be a str")
        pulumi.set(__self__, "private_host", private_host)
        if private_network_uuid and not isinstance(private_network_uuid, str):
            raise TypeError("Expected argument 'private_network_uuid' to be a str")
        pulumi.set(__self__, "private_network_uuid", private_network_uuid)
        if private_uri and not isinstance(private_uri, str):
            raise TypeError("Expected argument 'private_uri' to be a str")
        pulumi.set(__self__, "private_uri", private_uri)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if uri and not isinstance(uri, str):
            raise TypeError("Expected argument 'uri' to be a str")
        pulumi.set(__self__, "uri", uri)
        if user and not isinstance(user, str):
            raise TypeError("Expected argument 'user' to be a str")
        pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def database(self) -> str:
        """
        Name of the replica's default database.
        """
        return pulumi.get(self, "database")

    @property
    @pulumi.getter
    def host(self) -> str:
        """
        Database replica's hostname.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> str:
        """
        Password for the replica's default user.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        Network port that the database replica is listening on.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="privateHost")
    def private_host(self) -> str:
        """
        Same as `host`, but only accessible from resources within the account and in the same region.
        """
        return pulumi.get(self, "private_host")

    @property
    @pulumi.getter(name="privateNetworkUuid")
    def private_network_uuid(self) -> str:
        return pulumi.get(self, "private_network_uuid")

    @property
    @pulumi.getter(name="privateUri")
    def private_uri(self) -> str:
        """
        Same as `uri`, but only accessible from resources within the account and in the same region.
        """
        return pulumi.get(self, "private_uri")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[str]]:
        """
        A list of tag names to be applied to the database replica.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def uri(self) -> str:
        """
        The full URI for connecting to the database replica.
        """
        return pulumi.get(self, "uri")

    @property
    @pulumi.getter
    def user(self) -> str:
        """
        Username for the replica's default user.
        """
        return pulumi.get(self, "user")


class AwaitableGetDatabaseReplicaResult(GetDatabaseReplicaResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseReplicaResult(
            cluster_id=self.cluster_id,
            database=self.database,
            host=self.host,
            id=self.id,
            name=self.name,
            password=self.password,
            port=self.port,
            private_host=self.private_host,
            private_network_uuid=self.private_network_uuid,
            private_uri=self.private_uri,
            region=self.region,
            tags=self.tags,
            uri=self.uri,
            user=self.user)


def get_database_replica(cluster_id: Optional[str] = None,
                         name: Optional[str] = None,
                         tags: Optional[Sequence[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseReplicaResult:
    """
    Provides information on a DigitalOcean database replica.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example = digitalocean.get_database_cluster(name="example-cluster")
    read_only = digitalocean.get_database_replica(cluster_id=example.id,
        name="terra-test-ro")
    pulumi.export("replicaOutput", read_only.uri)
    ```


    :param str cluster_id: The ID of the original source database cluster.
    :param str name: The name for the database replica.
    :param Sequence[str] tags: A list of tag names to be applied to the database replica.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['name'] = name
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('digitalocean:index/getDatabaseReplica:getDatabaseReplica', __args__, opts=opts, typ=GetDatabaseReplicaResult).value

    return AwaitableGetDatabaseReplicaResult(
        cluster_id=__ret__.cluster_id,
        database=__ret__.database,
        host=__ret__.host,
        id=__ret__.id,
        name=__ret__.name,
        password=__ret__.password,
        port=__ret__.port,
        private_host=__ret__.private_host,
        private_network_uuid=__ret__.private_network_uuid,
        private_uri=__ret__.private_uri,
        region=__ret__.region,
        tags=__ret__.tags,
        uri=__ret__.uri,
        user=__ret__.user)


@_utilities.lift_output_func(get_database_replica)
def get_database_replica_output(cluster_id: Optional[pulumi.Input[str]] = None,
                                name: Optional[pulumi.Input[str]] = None,
                                tags: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseReplicaResult]:
    """
    Provides information on a DigitalOcean database replica.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example = digitalocean.get_database_cluster(name="example-cluster")
    read_only = digitalocean.get_database_replica(cluster_id=example.id,
        name="terra-test-ro")
    pulumi.export("replicaOutput", read_only.uri)
    ```


    :param str cluster_id: The ID of the original source database cluster.
    :param str name: The name for the database replica.
    :param Sequence[str] tags: A list of tag names to be applied to the database replica.
    """
    ...
