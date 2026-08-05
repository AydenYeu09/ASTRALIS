#stores all relevant information to the drone (hence, a vehicle state)

#8/4 - disabling GPS for now.
class VehicleState:
    def __init__(self):
        #Connection Status 
        self.connected = False
        self.armed = False 
        self.flight_mode = "UNKNOWN"

        #IMU
        self.roll = 0.0 
        self.pitch = 0.0
        self.yaw = 0.0 

        #IMU Derivatives 
        self.roll_rate = 0.0
        self.pitch_rate = 0.0 
        self.yaw_rate = 0.0

        #Battery 
        self.battery_voltage = 0.0
        self.battery_current = 0.0 
        self.battery_remaining = 0.0

        #GPS 
        # self.latitude = 0.0
        # self.longitude = 0.0
        # self.altitude = 0.0

        # self.ground_speed = 0.0
        # self.heading = 0.0 

    def print_status(self): 
        print(f"Connected: {self.connected}")
        print(f"Mode: {self.flight_mode}")
        print(f"Armed: {self.armed}")


        print(f"Roll: {self.roll:.2f}")
        print(f"Pitch: {self.pitch:.2f}")
        print(f"Yaw: {self.yaw:.2f}")

        # print(f"Latitude: {self.latitude:.3f}")
        # print(f"Longitude: {self.longitude:.3f}")
        # print(f"Altitude: {self.altitude:.2f} m")

        print(f"Battery: {self.battery_voltage:.2f}V")
              

