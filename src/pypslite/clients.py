import grpc
from pypslite import pslite_pb2, pslite_pb2_grpc

class Client(object):
    def __init__(self, endpoint="localhost:10111", default_topic_name="testtopic"):
        self.endpoint = endpoint
        self.default_topic_name = default_topic_name
        self.channel = grpc.insecure_channel(self.endpoint)
        self.pslite_svc_stub = pslite_pb2_grpc.PSLiteServiceStub(self.channel)

    def ensure_topic(self, topic_name, folder):
        req = pslite_pb2.OpenTopicRequest(name = topic_name,
                records_path = os.path.join(folder, "RECORDS"),
                index_path = os.path.join(folder, "INDEX"))
        return self.pslite_svc_stub.OpenTopic(req)

    def pub(self, data, topic_name=None):
        topic_name = topic_name or self.default_topic_name
        req = pslite_pb2.PublishRequest(
                topic_name = topic_name,
                content = pslite_pb2.PublishRequest_ContentBytes(
                    content_bytes = data
                )
              )
        return self.pslite_svc_stub.Publish(req)

    def sub(self, offset = 0, end_offset = -1, topic_name=None):
        topic_name = topic_name or self.default_topic_name
        req = pslite_pb2.SubscribeRequest(
                topic_name = topic_name,
                offset = offset,
                end_offset = end_offset)
        return self.pslite_svc_stub.Subscribe(req)
