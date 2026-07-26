from space_network_lib import SpaceEntity, Packet
class Satellite(SpaceEntity):
    def receive_signal(self, packet: Packet):
        return f"[{self.name}]  Received: {packet}."
    