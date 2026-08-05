import time 
from flight.mavlink_interface import MavlinkInterface

def main():

    pixhawk = MavlinkInterface(
    "/dev/serial0" #change based on UART 
    )