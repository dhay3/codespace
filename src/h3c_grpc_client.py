from h3c_client import Client
import gnmi_pb2
import gnmi_pb2_grpc
import grpc
import time


class GnmiClient(Client):
    @staticmethod
    def get_mode(s: str):
        mapping = {
            'stream': gnmi_pb2.SubscriptionList.Mode.STREAM,
            'once': gnmi_pb2.SubscriptionList.Mode.ONCE,
            'poll': gnmi_pb2.SubscriptionList.Mode.POLL,
            'target_defined': gnmi_pb2.TARGET_DEFINED,
            'on_change': gnmi_pb2.ON_CHANGE,
            'sample': gnmi_pb2.SAMPLE,
        }
        return mapping[s.lower()]

    def __init__(
        self,
        username,
        password,
        channel,
    ):
        super().__init__(username, password, channel)
        self.__stub = gnmi_pb2_grpc.gNMIStub(channel)
        return

    def Subscribe(self, req):
        return self.__stub.Subscribe(req, metadata=self.metadata())

    def make_sub_obj(self,interval:int):

        pass


    def make_sub_obj(self, interval):
        path_obj = gnmi_pb2.Path()
        ele = path_obj.elem.add()
        ele.name = 'Device'
        ele1 = path_obj.elem.add()
        ele1.name = 'Boards'
        mode = self.get_mode('sample')
        sample_interval = interval
        return gnmi_pb2.Subscription(
            path=path_obj, mode=mode, sample_interval=sample_interval
        )

    def make_sub_eventobj(self, interval, mode='on_change'):
        path_obj = gnmi_pb2.Path()
        ele = path_obj.elem.add()
        ele.name = 'Ifmgr'
        ele1 = path_obj.elem.add()
        ele1.name = 'InterfaceEvent'
        mode = self.get_mode('on_change')
        sample_interval = interval
        return gnmi_pb2.Subscription(
            path=path_obj, mode=mode, sample_interval=sample_interval
        )

    def make_poll_req(self):
            return gnmi_pb2.SubscribeRequest(poll=gnmi_pb2.Poll())

    def make_sub_req(
        self, sample_interval, mode, type='sample', qos=0, updates_only=False
    ):
        kwargs = {}
        kwargs['prefix'] = gnmi_pb2.Path()
        kwargs['qos'] = gnmi_pb2.QOSMarking(marking=qos)
        kwargs['mode'] = self.get_mode(mode)
        kwargs['encoding'] = gnmi_pb2.JSON
        kwargs['subscription'] = []
        if type == 'sample':
            kwargs['subscription'].append(self.make_sub_obj(sample_interval))
        else:
            kwargs['subscription'].append(self.make_sub_eventobj(sample_interval))
            kwargs['updates_only'] = updates_only
        subscribeList = gnmi_pb2.SubscriptionList(**kwargs)
        return gnmi_pb2.SubscribeRequest(subscribe=subscribeList)


def test_sub(client: GnmiClient):
    def poll_generator(n):
        req = client.make_sub_req(2000000000, mode='poll')
        yield req
        for _ in range(n):
            time.sleep(2)
        yield client.make_poll_req()
        return

    def sample_generator(t, sample_interval=2000000000, mode='stream'):
        req = client.make_sub_req(sample_interval, mode)
        yield req
        time.sleep(t)
        return

    def event_generator(t):
        req = client.make_sub_req(type='event', sample_interval=10000000, mode='stream')
        yield req
        time.sleep(t)
        return

    return sample_generator(300)


if __name__ == '__main__':
    channel = grpc.insecure_channel('192.168.254.6:50051')
    client = GnmiClient('admin', 'Wlm@xwb9527', channel)
    with client.Login():
        print(client)
        replies = client.Subscribe(test_sub(client))
        for reply in replies:
            print(reply)
