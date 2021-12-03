# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import prediction_service_pb2 as prediction__service__pb2


class PredictionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Predict = channel.unary_unary(
                '/prediction.PredictionService/Predict',
                request_serializer=prediction__service__pb2.PredictRequest.SerializeToString,
                response_deserializer=prediction__service__pb2.PredictResponse.FromString,
                )
        self.RegisterPredictor = channel.unary_unary(
                '/prediction.PredictionService/RegisterPredictor',
                request_serializer=prediction__service__pb2.RegisterPredictorRequest.SerializeToString,
                response_deserializer=prediction__service__pb2.RegisterPredictorResponse.FromString,
                )


class PredictionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Predict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterPredictor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PredictionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Predict': grpc.unary_unary_rpc_method_handler(
                    servicer.Predict,
                    request_deserializer=prediction__service__pb2.PredictRequest.FromString,
                    response_serializer=prediction__service__pb2.PredictResponse.SerializeToString,
            ),
            'RegisterPredictor': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterPredictor,
                    request_deserializer=prediction__service__pb2.RegisterPredictorRequest.FromString,
                    response_serializer=prediction__service__pb2.RegisterPredictorResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'prediction.PredictionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PredictionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Predict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prediction.PredictionService/Predict',
            prediction__service__pb2.PredictRequest.SerializeToString,
            prediction__service__pb2.PredictResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterPredictor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prediction.PredictionService/RegisterPredictor',
            prediction__service__pb2.RegisterPredictorRequest.SerializeToString,
            prediction__service__pb2.RegisterPredictorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class PredictorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PredictorPredict = channel.unary_unary(
                '/prediction.Predictor/PredictorPredict',
                request_serializer=prediction__service__pb2.PredictorPredictRequest.SerializeToString,
                response_deserializer=prediction__service__pb2.PredictorPredictResponse.FromString,
                )


class PredictorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PredictorPredict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PredictorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PredictorPredict': grpc.unary_unary_rpc_method_handler(
                    servicer.PredictorPredict,
                    request_deserializer=prediction__service__pb2.PredictorPredictRequest.FromString,
                    response_serializer=prediction__service__pb2.PredictorPredictResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'prediction.Predictor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Predictor(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PredictorPredict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prediction.Predictor/PredictorPredict',
            prediction__service__pb2.PredictorPredictRequest.SerializeToString,
            prediction__service__pb2.PredictorPredictResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
