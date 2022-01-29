# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from graphscope.proto import ddl_service_pb2 as graphscope_dot_proto_dot_ddl__service__pb2


class ClientDdlStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.batchSubmit = channel.unary_unary(
                '/gs.rpc.ddl_service.v1.ClientDdl/batchSubmit',
                request_serializer=graphscope_dot_proto_dot_ddl__service__pb2.BatchSubmitRequest.SerializeToString,
                response_deserializer=graphscope_dot_proto_dot_ddl__service__pb2.BatchSubmitResponse.FromString,
                )
        self.getGraphDef = channel.unary_unary(
                '/gs.rpc.ddl_service.v1.ClientDdl/getGraphDef',
                request_serializer=graphscope_dot_proto_dot_ddl__service__pb2.GetGraphDefRequest.SerializeToString,
                response_deserializer=graphscope_dot_proto_dot_ddl__service__pb2.GetGraphDefResponse.FromString,
                )


class ClientDdlServicer(object):
    """Missing associated documentation comment in .proto file."""

    def batchSubmit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getGraphDef(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClientDdlServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'batchSubmit': grpc.unary_unary_rpc_method_handler(
                    servicer.batchSubmit,
                    request_deserializer=graphscope_dot_proto_dot_ddl__service__pb2.BatchSubmitRequest.FromString,
                    response_serializer=graphscope_dot_proto_dot_ddl__service__pb2.BatchSubmitResponse.SerializeToString,
            ),
            'getGraphDef': grpc.unary_unary_rpc_method_handler(
                    servicer.getGraphDef,
                    request_deserializer=graphscope_dot_proto_dot_ddl__service__pb2.GetGraphDefRequest.FromString,
                    response_serializer=graphscope_dot_proto_dot_ddl__service__pb2.GetGraphDefResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gs.rpc.ddl_service.v1.ClientDdl', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClientDdl(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def batchSubmit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gs.rpc.ddl_service.v1.ClientDdl/batchSubmit',
            graphscope_dot_proto_dot_ddl__service__pb2.BatchSubmitRequest.SerializeToString,
            graphscope_dot_proto_dot_ddl__service__pb2.BatchSubmitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getGraphDef(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gs.rpc.ddl_service.v1.ClientDdl/getGraphDef',
            graphscope_dot_proto_dot_ddl__service__pb2.GetGraphDefRequest.SerializeToString,
            graphscope_dot_proto_dot_ddl__service__pb2.GetGraphDefResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
