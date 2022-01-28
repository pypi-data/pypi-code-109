# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from github.com.metaprov.modelaapi.services.modelautobuilder.v1 import modelautobuilder_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2


class ModelAutobuilderServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListModelAutobuilders = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.modelautobuilder.v1.ModelAutobuilderService/ListModelAutobuilders',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.ListModelAutobuildersRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.ListModelAutobuildersResponse.FromString,
                )
        self.CreateModelAutobuilder = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.modelautobuilder.v1.ModelAutobuilderService/CreateModelAutobuilder',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.CreateModelAutobuilderRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.CreateModelAutobuilderResponse.FromString,
                )
        self.GetModelAutobuilder = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.modelautobuilder.v1.ModelAutobuilderService/GetModelAutobuilder',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.GetModelAutobuilderRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.GetModelAutobuilderResponse.FromString,
                )
        self.UpdateModelAutobuilder = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.modelautobuilder.v1.ModelAutobuilderService/UpdateModelAutobuilder',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.UpdateModelAutobuilderRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.UpdateModelAutobuilderResponse.FromString,
                )
        self.DeleteModelAutobuilder = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.modelautobuilder.v1.ModelAutobuilderService/DeleteModelAutobuilder',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.DeleteModelAutobuilderRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.DeleteModelAutobuilderResponse.FromString,
                )


class ModelAutobuilderServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListModelAutobuilders(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateModelAutobuilder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetModelAutobuilder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateModelAutobuilder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteModelAutobuilder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelAutobuilderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListModelAutobuilders': grpc.unary_unary_rpc_method_handler(
                    servicer.ListModelAutobuilders,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.ListModelAutobuildersRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.ListModelAutobuildersResponse.SerializeToString,
            ),
            'CreateModelAutobuilder': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateModelAutobuilder,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.CreateModelAutobuilderRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.CreateModelAutobuilderResponse.SerializeToString,
            ),
            'GetModelAutobuilder': grpc.unary_unary_rpc_method_handler(
                    servicer.GetModelAutobuilder,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.GetModelAutobuilderRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.GetModelAutobuilderResponse.SerializeToString,
            ),
            'UpdateModelAutobuilder': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateModelAutobuilder,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.UpdateModelAutobuilderRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.UpdateModelAutobuilderResponse.SerializeToString,
            ),
            'DeleteModelAutobuilder': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteModelAutobuilder,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.DeleteModelAutobuilderRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.DeleteModelAutobuilderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'github.com.metaprov.modelaapi.services.modelautobuilder.v1.ModelAutobuilderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ModelAutobuilderService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListModelAutobuilders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.modelautobuilder.v1.ModelAutobuilderService/ListModelAutobuilders',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.ListModelAutobuildersRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.ListModelAutobuildersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateModelAutobuilder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.modelautobuilder.v1.ModelAutobuilderService/CreateModelAutobuilder',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.CreateModelAutobuilderRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.CreateModelAutobuilderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetModelAutobuilder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.modelautobuilder.v1.ModelAutobuilderService/GetModelAutobuilder',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.GetModelAutobuilderRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.GetModelAutobuilderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateModelAutobuilder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.modelautobuilder.v1.ModelAutobuilderService/UpdateModelAutobuilder',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.UpdateModelAutobuilderRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.UpdateModelAutobuilderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteModelAutobuilder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.modelautobuilder.v1.ModelAutobuilderService/DeleteModelAutobuilder',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.DeleteModelAutobuilderRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_modelautobuilder_dot_v1_dot_modelautobuilder__pb2.DeleteModelAutobuilderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
