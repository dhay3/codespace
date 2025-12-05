import logging

# import grpc
# import json
# from collections import OrderedDict
import grpc_service_pb2, grpc_service_pb2_grpc
# import Syslog_pb2, Syslog_pb2_grpc
# import Ifmgr_pb2, Ifmgr_pb2_grpc


class Client:
    def __init__(self, username, password, channel):
        self.username = username
        self.password = password
        self.channel = channel
        self.__stub = grpc_service_pb2_grpc.GrpcServiceStub(channel)
        self.tokenid = ''

    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_value, traceback):
        if self.tokenid:
            self.Logout()

    def __str__(self):
        return '{username=%s, password=%s, tokenid=%s}' % (
            self.username,
            self.password,
            self.tokenid,
        )

    def metadata(self):
        return (('token_id', self.tokenid),)

    def Login(self):
        if self.tokenid:
            return self

        request = grpc_service_pb2.LoginRequest(
            user_name=self.username, password=self.password
        )
        reply = self.__stub.Login(request)
        self.tokenid = reply.token_id
        return self

    def Logout(self):
        if not self.tokenid:
            return
        request = grpc_service_pb2.LogoutRequest(token_id=self.tokenid)
        try:
            self.__stub.Logout(request)
        except Exception as e:
            logging.warning('Logout:' + e)
        self.tokenid = ''
        return


    # def SubscribeByStreamName(self, stream):
    #     request = grpc_service_pb2.SubscribeRequest(stream_name=stream)
    #     reply = self.__stub.SubscribeByStreamName(request, metadata=self.metadata())
    #     return reply.result

    # def GetEventReport(self):
    #     request = grpc_service_pb2.GetReportRequest(token_id=self.tokenid)
    #     yield from self.__stub.GetEventReport(request)

    # def sub(self, path):
    #     if path == 'SubscribeLOGEvent':
    #         request = Syslog_pb2.LOGEvent()
    #         RpcMethod = Syslog_pb2_grpc.SyslogServiceStub(self.channel)
    #         reply = RpcMethod.SubscribeLOGEvent(request, metadata=self.metadata())
    #     if path == 'SubscribeInterfaceEvent':
    #         request = Ifmgr_pb2.InterfaceEvent()
    #         RpcMethod = Ifmgr_pb2_grpc.IfmgrServiceStub(self.channel)
    #         reply = RpcMethod.SubscribeInterfaceEvent(request, metadata=self.metadata())
    #     return reply.result


# if __name__ == '__main__':

#     def format_json(jsonstr):
#         obj = json.loads(jsonstr, object_hook=OrderedDict)
#         return json.dumps(obj, ensure_ascii=False, indent=4)

#     def test():
#         channel = grpc.insecure_channel('192.168.254.6:50051')
#         client = Client('admin', 'Wlm@xwb9527', channel)
#         with client.Login():
#             print(client)
#             print(client.SubscribeByStreamName('SubscribeInterfaceEvent'))
#             for e in client.GetEventReport():
#                 print(e)
#                 print(format_json(e.json_text))

#     test()
