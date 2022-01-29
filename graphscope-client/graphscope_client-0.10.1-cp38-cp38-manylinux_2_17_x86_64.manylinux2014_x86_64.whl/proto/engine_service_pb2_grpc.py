# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from graphscope.proto import message_pb2 as graphscope_dot_proto_dot_message__pb2


class EngineServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RunStep = channel.unary_unary(
                '/gs.rpc.EngineService/RunStep',
                request_serializer=graphscope_dot_proto_dot_message__pb2.RunStepRequest.SerializeToString,
                response_deserializer=graphscope_dot_proto_dot_message__pb2.RunStepResponse.FromString,
                )
        self.HeartBeat = channel.unary_unary(
                '/gs.rpc.EngineService/HeartBeat',
                request_serializer=graphscope_dot_proto_dot_message__pb2.HeartBeatRequest.SerializeToString,
                response_deserializer=graphscope_dot_proto_dot_message__pb2.HeartBeatResponse.FromString,
                )


class EngineServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RunStep(self, request, context):
        """Drives the graph computation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HeartBeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EngineServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RunStep': grpc.unary_unary_rpc_method_handler(
                    servicer.RunStep,
                    request_deserializer=graphscope_dot_proto_dot_message__pb2.RunStepRequest.FromString,
                    response_serializer=graphscope_dot_proto_dot_message__pb2.RunStepResponse.SerializeToString,
            ),
            'HeartBeat': grpc.unary_unary_rpc_method_handler(
                    servicer.HeartBeat,
                    request_deserializer=graphscope_dot_proto_dot_message__pb2.HeartBeatRequest.FromString,
                    response_serializer=graphscope_dot_proto_dot_message__pb2.HeartBeatResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gs.rpc.EngineService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EngineService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RunStep(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gs.rpc.EngineService/RunStep',
            graphscope_dot_proto_dot_message__pb2.RunStepRequest.SerializeToString,
            graphscope_dot_proto_dot_message__pb2.RunStepResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HeartBeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gs.rpc.EngineService/HeartBeat',
            graphscope_dot_proto_dot_message__pb2.HeartBeatRequest.SerializeToString,
            graphscope_dot_proto_dot_message__pb2.HeartBeatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
