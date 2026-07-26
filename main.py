from space_network_lib import SpaceEntity, Packet,SpaceNetwork,TemporalInterferenceError,DataCorruptedError,LinkTerminatedError,OutOfRangeError

from time import sleep
class Satellite(SpaceEntity):
    def receive_signal(self, packet: Packet):
        print(f"[{self.name}]  Received: {packet}.")
class BrokenConnectionError:
    pass        
network = SpaceNetwork(level=3)
sat1 = Satellite("sat1",100)
sat2 = Satellite("sat2",200)        
massage = Packet("The satellite is excellent.",sat1,sat2)


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
try:
    transmission_attempt(massage)
except:
    print("failed Transmission") 
        