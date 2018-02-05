# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import tribune_tts_pb2 as tribune__tts__pb2


class TTSStub(object):
  """Service that implements Techmo TTS API
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Synthesize = channel.unary_stream(
        '/techmo.tribune.TTS/Synthesize',
        request_serializer=tribune__tts__pb2.SynthesizeRequest.SerializeToString,
        response_deserializer=tribune__tts__pb2.SynthesizeResponse.FromString,
        )


class TTSServicer(object):
  """Service that implements Techmo TTS API
  """

  def Synthesize(self, request, context):
    """Return speech using given text and optional configuration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TTSServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Synthesize': grpc.unary_stream_rpc_method_handler(
          servicer.Synthesize,
          request_deserializer=tribune__tts__pb2.SynthesizeRequest.FromString,
          response_serializer=tribune__tts__pb2.SynthesizeResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'techmo.tribune.TTS', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))