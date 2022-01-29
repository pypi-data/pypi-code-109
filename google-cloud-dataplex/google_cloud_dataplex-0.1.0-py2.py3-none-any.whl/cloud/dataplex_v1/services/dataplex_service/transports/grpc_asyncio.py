# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import warnings
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import gapic_v1
from google.api_core import grpc_helpers_async
from google.api_core import operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.dataplex_v1.types import resources
from google.cloud.dataplex_v1.types import service
from google.cloud.dataplex_v1.types import tasks
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import empty_pb2  # type: ignore
from .base import DataplexServiceTransport, DEFAULT_CLIENT_INFO
from .grpc import DataplexServiceGrpcTransport


class DataplexServiceGrpcAsyncIOTransport(DataplexServiceTransport):
    """gRPC AsyncIO backend transport for DataplexService.

    Dataplex service provides data lakes as a service. The
    primary resources offered by this service are Lakes, Zones and
    Assets which collectively allow a data adminstrator to organize,
    manage, secure and catalog data across their organization
    located across cloud projects in a variety of storage systems
    including Cloud Storage and BigQuery.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "dataplex.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "dataplex.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: aio.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id=None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client: Optional[operations_v1.OperationsAsyncClient] = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsAsyncClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsAsyncClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def create_lake(
        self,
    ) -> Callable[[service.CreateLakeRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create lake method over gRPC.

        Creates a lake resource.

        Returns:
            Callable[[~.CreateLakeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_lake" not in self._stubs:
            self._stubs["create_lake"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/CreateLake",
                request_serializer=service.CreateLakeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_lake"]

    @property
    def update_lake(
        self,
    ) -> Callable[[service.UpdateLakeRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the update lake method over gRPC.

        Updates a lake resource.

        Returns:
            Callable[[~.UpdateLakeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_lake" not in self._stubs:
            self._stubs["update_lake"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/UpdateLake",
                request_serializer=service.UpdateLakeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_lake"]

    @property
    def delete_lake(
        self,
    ) -> Callable[[service.DeleteLakeRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete lake method over gRPC.

        Deletes a lake resource. All zones within the lake
        must be deleted before the lake can be deleted.

        Returns:
            Callable[[~.DeleteLakeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_lake" not in self._stubs:
            self._stubs["delete_lake"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/DeleteLake",
                request_serializer=service.DeleteLakeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_lake"]

    @property
    def list_lakes(
        self,
    ) -> Callable[[service.ListLakesRequest], Awaitable[service.ListLakesResponse]]:
        r"""Return a callable for the list lakes method over gRPC.

        Lists lake resources in a project and location.

        Returns:
            Callable[[~.ListLakesRequest],
                    Awaitable[~.ListLakesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_lakes" not in self._stubs:
            self._stubs["list_lakes"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/ListLakes",
                request_serializer=service.ListLakesRequest.serialize,
                response_deserializer=service.ListLakesResponse.deserialize,
            )
        return self._stubs["list_lakes"]

    @property
    def get_lake(self) -> Callable[[service.GetLakeRequest], Awaitable[resources.Lake]]:
        r"""Return a callable for the get lake method over gRPC.

        Retrieves a lake resource.

        Returns:
            Callable[[~.GetLakeRequest],
                    Awaitable[~.Lake]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_lake" not in self._stubs:
            self._stubs["get_lake"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/GetLake",
                request_serializer=service.GetLakeRequest.serialize,
                response_deserializer=resources.Lake.deserialize,
            )
        return self._stubs["get_lake"]

    @property
    def list_lake_actions(
        self,
    ) -> Callable[
        [service.ListLakeActionsRequest], Awaitable[service.ListActionsResponse]
    ]:
        r"""Return a callable for the list lake actions method over gRPC.

        Lists action resources in a lake.

        Returns:
            Callable[[~.ListLakeActionsRequest],
                    Awaitable[~.ListActionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_lake_actions" not in self._stubs:
            self._stubs["list_lake_actions"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/ListLakeActions",
                request_serializer=service.ListLakeActionsRequest.serialize,
                response_deserializer=service.ListActionsResponse.deserialize,
            )
        return self._stubs["list_lake_actions"]

    @property
    def create_zone(
        self,
    ) -> Callable[[service.CreateZoneRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create zone method over gRPC.

        Creates a zone resource within a lake.

        Returns:
            Callable[[~.CreateZoneRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_zone" not in self._stubs:
            self._stubs["create_zone"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/CreateZone",
                request_serializer=service.CreateZoneRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_zone"]

    @property
    def update_zone(
        self,
    ) -> Callable[[service.UpdateZoneRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the update zone method over gRPC.

        Updates a zone resource.

        Returns:
            Callable[[~.UpdateZoneRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_zone" not in self._stubs:
            self._stubs["update_zone"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/UpdateZone",
                request_serializer=service.UpdateZoneRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_zone"]

    @property
    def delete_zone(
        self,
    ) -> Callable[[service.DeleteZoneRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete zone method over gRPC.

        Deletes a zone resource. All assets within a zone
        must be deleted before the zone can be deleted.

        Returns:
            Callable[[~.DeleteZoneRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_zone" not in self._stubs:
            self._stubs["delete_zone"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/DeleteZone",
                request_serializer=service.DeleteZoneRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_zone"]

    @property
    def list_zones(
        self,
    ) -> Callable[[service.ListZonesRequest], Awaitable[service.ListZonesResponse]]:
        r"""Return a callable for the list zones method over gRPC.

        Lists zone resources in a lake.

        Returns:
            Callable[[~.ListZonesRequest],
                    Awaitable[~.ListZonesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_zones" not in self._stubs:
            self._stubs["list_zones"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/ListZones",
                request_serializer=service.ListZonesRequest.serialize,
                response_deserializer=service.ListZonesResponse.deserialize,
            )
        return self._stubs["list_zones"]

    @property
    def get_zone(self) -> Callable[[service.GetZoneRequest], Awaitable[resources.Zone]]:
        r"""Return a callable for the get zone method over gRPC.

        Retrieves a zone resource.

        Returns:
            Callable[[~.GetZoneRequest],
                    Awaitable[~.Zone]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_zone" not in self._stubs:
            self._stubs["get_zone"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/GetZone",
                request_serializer=service.GetZoneRequest.serialize,
                response_deserializer=resources.Zone.deserialize,
            )
        return self._stubs["get_zone"]

    @property
    def list_zone_actions(
        self,
    ) -> Callable[
        [service.ListZoneActionsRequest], Awaitable[service.ListActionsResponse]
    ]:
        r"""Return a callable for the list zone actions method over gRPC.

        Lists action resources in a zone.

        Returns:
            Callable[[~.ListZoneActionsRequest],
                    Awaitable[~.ListActionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_zone_actions" not in self._stubs:
            self._stubs["list_zone_actions"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/ListZoneActions",
                request_serializer=service.ListZoneActionsRequest.serialize,
                response_deserializer=service.ListActionsResponse.deserialize,
            )
        return self._stubs["list_zone_actions"]

    @property
    def create_asset(
        self,
    ) -> Callable[[service.CreateAssetRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create asset method over gRPC.

        Creates an asset resource.

        Returns:
            Callable[[~.CreateAssetRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_asset" not in self._stubs:
            self._stubs["create_asset"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/CreateAsset",
                request_serializer=service.CreateAssetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_asset"]

    @property
    def update_asset(
        self,
    ) -> Callable[[service.UpdateAssetRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the update asset method over gRPC.

        Updates an asset resource.

        Returns:
            Callable[[~.UpdateAssetRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_asset" not in self._stubs:
            self._stubs["update_asset"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/UpdateAsset",
                request_serializer=service.UpdateAssetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_asset"]

    @property
    def delete_asset(
        self,
    ) -> Callable[[service.DeleteAssetRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete asset method over gRPC.

        Deletes an asset resource. The referenced storage
        resource is detached (default) or deleted based on the
        associated Lifecycle policy.

        Returns:
            Callable[[~.DeleteAssetRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_asset" not in self._stubs:
            self._stubs["delete_asset"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/DeleteAsset",
                request_serializer=service.DeleteAssetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_asset"]

    @property
    def list_assets(
        self,
    ) -> Callable[[service.ListAssetsRequest], Awaitable[service.ListAssetsResponse]]:
        r"""Return a callable for the list assets method over gRPC.

        Lists asset resources in a zone.

        Returns:
            Callable[[~.ListAssetsRequest],
                    Awaitable[~.ListAssetsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_assets" not in self._stubs:
            self._stubs["list_assets"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/ListAssets",
                request_serializer=service.ListAssetsRequest.serialize,
                response_deserializer=service.ListAssetsResponse.deserialize,
            )
        return self._stubs["list_assets"]

    @property
    def get_asset(
        self,
    ) -> Callable[[service.GetAssetRequest], Awaitable[resources.Asset]]:
        r"""Return a callable for the get asset method over gRPC.

        Retrieves an asset resource.

        Returns:
            Callable[[~.GetAssetRequest],
                    Awaitable[~.Asset]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_asset" not in self._stubs:
            self._stubs["get_asset"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/GetAsset",
                request_serializer=service.GetAssetRequest.serialize,
                response_deserializer=resources.Asset.deserialize,
            )
        return self._stubs["get_asset"]

    @property
    def list_asset_actions(
        self,
    ) -> Callable[
        [service.ListAssetActionsRequest], Awaitable[service.ListActionsResponse]
    ]:
        r"""Return a callable for the list asset actions method over gRPC.

        Lists action resources in an asset.

        Returns:
            Callable[[~.ListAssetActionsRequest],
                    Awaitable[~.ListActionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_asset_actions" not in self._stubs:
            self._stubs["list_asset_actions"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/ListAssetActions",
                request_serializer=service.ListAssetActionsRequest.serialize,
                response_deserializer=service.ListActionsResponse.deserialize,
            )
        return self._stubs["list_asset_actions"]

    @property
    def create_task(
        self,
    ) -> Callable[[service.CreateTaskRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create task method over gRPC.

        Creates a task resource within a lake.

        Returns:
            Callable[[~.CreateTaskRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_task" not in self._stubs:
            self._stubs["create_task"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/CreateTask",
                request_serializer=service.CreateTaskRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_task"]

    @property
    def update_task(
        self,
    ) -> Callable[[service.UpdateTaskRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the update task method over gRPC.

        Update the task resource.

        Returns:
            Callable[[~.UpdateTaskRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_task" not in self._stubs:
            self._stubs["update_task"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/UpdateTask",
                request_serializer=service.UpdateTaskRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_task"]

    @property
    def delete_task(
        self,
    ) -> Callable[[service.DeleteTaskRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete task method over gRPC.

        Delete the task resource.

        Returns:
            Callable[[~.DeleteTaskRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_task" not in self._stubs:
            self._stubs["delete_task"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/DeleteTask",
                request_serializer=service.DeleteTaskRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_task"]

    @property
    def list_tasks(
        self,
    ) -> Callable[[service.ListTasksRequest], Awaitable[service.ListTasksResponse]]:
        r"""Return a callable for the list tasks method over gRPC.

        Lists tasks under the given lake.

        Returns:
            Callable[[~.ListTasksRequest],
                    Awaitable[~.ListTasksResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_tasks" not in self._stubs:
            self._stubs["list_tasks"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/ListTasks",
                request_serializer=service.ListTasksRequest.serialize,
                response_deserializer=service.ListTasksResponse.deserialize,
            )
        return self._stubs["list_tasks"]

    @property
    def get_task(self) -> Callable[[service.GetTaskRequest], Awaitable[tasks.Task]]:
        r"""Return a callable for the get task method over gRPC.

        Get task resource.

        Returns:
            Callable[[~.GetTaskRequest],
                    Awaitable[~.Task]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_task" not in self._stubs:
            self._stubs["get_task"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/GetTask",
                request_serializer=service.GetTaskRequest.serialize,
                response_deserializer=tasks.Task.deserialize,
            )
        return self._stubs["get_task"]

    @property
    def list_jobs(
        self,
    ) -> Callable[[service.ListJobsRequest], Awaitable[service.ListJobsResponse]]:
        r"""Return a callable for the list jobs method over gRPC.

        Lists Jobs under the given task.

        Returns:
            Callable[[~.ListJobsRequest],
                    Awaitable[~.ListJobsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_jobs" not in self._stubs:
            self._stubs["list_jobs"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/ListJobs",
                request_serializer=service.ListJobsRequest.serialize,
                response_deserializer=service.ListJobsResponse.deserialize,
            )
        return self._stubs["list_jobs"]

    @property
    def get_job(self) -> Callable[[service.GetJobRequest], Awaitable[tasks.Job]]:
        r"""Return a callable for the get job method over gRPC.

        Get job resource.

        Returns:
            Callable[[~.GetJobRequest],
                    Awaitable[~.Job]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_job" not in self._stubs:
            self._stubs["get_job"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/GetJob",
                request_serializer=service.GetJobRequest.serialize,
                response_deserializer=tasks.Job.deserialize,
            )
        return self._stubs["get_job"]

    @property
    def cancel_job(
        self,
    ) -> Callable[[service.CancelJobRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the cancel job method over gRPC.

        Cancel jobs running for the task resource.

        Returns:
            Callable[[~.CancelJobRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_job" not in self._stubs:
            self._stubs["cancel_job"] = self.grpc_channel.unary_unary(
                "/google.cloud.dataplex.v1.DataplexService/CancelJob",
                request_serializer=service.CancelJobRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["cancel_job"]

    def close(self):
        return self.grpc_channel.close()


__all__ = ("DataplexServiceGrpcAsyncIOTransport",)
