from space_network_lib import SpaceEntity, Packet,SpaceNetwork,TemporalInterferenceError,DataCorruptedError,LinkTerminatedError,OutOfRangeError

from time import sleep
class Satellite(SpaceEntity):
    def receive_signal(self, packet: Packet):
        if isinstance(packet,RelayPacket):
            print(f"Unwrapping and forwarding to {packet.receiver}")
            inner_packet = packet.data
            transmission_attempt(inner_packet)
        else:
            print(f"Final destination reached: {packet.data}")
class BrokenConnectionError:
    pass        
class Earth(SpaceEntity):
    def receive_signal(self, packet: Packet):
        pass
class RelayPacket(Packet):
    def __init__(self, packet_to_relay, sender, proxy):
        super().__init__(packet_to_relay, sender, proxy) 
    def __repr__(self):
        return f"RelayPacket(Relaying [{self.data}] to {self.receiver} from {self.sender})"        


def transmission_attempt(packet):
    status = True

    while status == True:
        try:
            network.send(packet)
            status = False

        except TemporalInterferenceError:
            print("waiting ,Interference...")
            sleep(2)
          
        except DataCorruptedError:
            print("Data retrying ,corrupted...")
        except LinkTerminatedError:
            raise BrokenConnectionError("link lost")
        except OutOfRangeError:
            raise BrokenConnectionError("Target out of range")

network = SpaceNetwork(level=5)
sat1 = Satellite("sat1",100)
sat2 = Satellite("sat2",200)
sat3 = Satellite("sat3",300)
sat4 = Satellite("sat4",400)
earth = Earth("earth",0)     
p_final= Packet("hello from earth!!!",sat3,sat4)
p_sat2_to_sat3 = RelayPacket(p_final,sat2,sat3)
p_sat1_to_sat2 = RelayPacket(p_sat2_to_sat3,sat1,sat2)
p_earth_to_sat1 = RelayPacket(p_sat1_to_sat2,earth,sat1)

try:
    transmission_attempt(p_earth_to_sat1)
except:
    print("failed Transmission")
