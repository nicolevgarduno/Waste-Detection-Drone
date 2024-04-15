import djitellopy as tello
from multiprocessing import Process

drone = tello.Tello()
drone.connect()

def test(drone):
    drone.streamon()

p1 = Process(target=test, args=(drone,))
p1.start()
p1.join()