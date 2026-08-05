
import math
import time 


from pymavlink import mavutil

from vehicle_states import VehicleState 


class MavlinkInterface:
    def __init__(self, connection_address, baud_rate=57600):
        self.connection_address = connection_address
        self.baud_rate = baud_rate

        self.connection = None 
        self.state = VehicleState()

        #heartbeat vars
        self.last_heartbeat_time = 0.0 
        self.heartbeat_timeout = 5.0 

    def connect(self):
                print(f"Connecting to MAVLINK at {self.connection_address}...")
    
                try:
                    self.connection = mavutil.mavlink_connection(
                        self.connection_address,
                        baud = self.baud_rate
                    )
    
                    print("Waiting for Pixhawk heartbeat...")
    
                    heartbeat = self.connection.wait_heartbeat(
                          timeout=10
                          )
    
                    if heartbeat is None:
                        print("Connection failed: no heartbeat received :(")
                        return False
    
                    self.state.connected = True
                    self.last_heartbeat_time = time.monotonic() #this might be the wrong time referencing

                    print("Pixhawk connected!")

                    return True

                except Exception as error: 
                    print(
                         f"MAVLink connection failed: {error} :("
                    )

                    return False

    def update(self):
        if self.connection is None:
            return
        message = self.connection.recv_match(
            blocking=True,
            timeout=0.2
        )

        if message is None:
            self.check_connection()
            return

        if message.get_type() == "BAD_DATA":
              return

        message_type = message.get_type()

        if message_type == "HEARTBEAT":
              self.update_heartbeat(message)

        elif message_type == "ATTITUDE":
              self.update_attitude(message)

        elif message_type == "BATTERY_STATUS":
             self.update_battery(message)

        # elif message_type == "GPS_RAW_INT": #noisy data
        #      self.update_gps(message)

        elif message_type == "GLOBAL_POSITION_INT": #EKF and Fused Data for GPS/IMU 
            self.update_position(message)

        def update_heartbeat(self, message):
            self.last_heartbeat_time = time.monotonic()    
            self.state.connected = True 

            armed_flag = (
                 mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED
            )

            self.state.armed = bool(
                 message.base_mode & armed_flag
            )

            self.state.flight_mode = (
                 self.connection.flightmode
            )

        def update_attitude(self, message):
             #MAVLink uses radians
             # Converting to degrees (for personal preference) 

            #IMU dofs 
            self.state.roll = math.degrees(message.roll)  
            self.state.pitch = math.degrees(message.pitch)
            self.state.yaw = math.degrees(message.yaw)

            #IMU rates 
            self.state.roll_rate = math.degrees(message.rollspeed)
            self.state.pitch_rate = math.degrees(message.pitchspeed)
            self.state.yaw_rate = math.degrees(message.yawspeed)

        def update_battery(self, message):
            # millivolts -> volts 
            self.state.battery_voltage = (
                 message.voltage_battery / 1000 #volt conversion factor
            )

            # centiamps -> amps 
            self.state.battery_current = (
                 message.current_battery / 100 
            )

            self.state.battery_remaining = ( 
                 message.battery_remaining
            )


        def update_posiiton(self, message):
             #degrees * 10^-7 -> degrees (mavlink is WEIRD!)
            self.state.latitude = (
                message.lat / 10000000
            )

            self.state.longitude = (
                message.lon / 10000000
            )

            self.state.altitude = (
                message.alt / 10000000
            )

        def check_connection(self):
            time_since_heartbeat = (
                 time.monotonic() - self.last_heartbeat_time
            )

            if time_since_heartbeat > self.heartbeat_timeout: #connection timed out condition
                 self.state.connected = False

                 print(
                      "Lost MAVLink connection :("
                 )
                 return False
            return True

        def close(self):
            if self.connection:
                  self.connection.close() 
                  self.connection = None 

            self.state.connected = False 
            print("MAVLink is disconnected.")

    
             





             
  

            

         
       