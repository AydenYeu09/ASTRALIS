# ASTRALIS

**ASTRALIS** is a thrust-vectoring aerial manipulation research quadcopter designed to investigate how independently vectored thrust can compensate for disturbances induced by the movement of an onboard robotic arm. 

<img width="600" height="451" alt="ASTRALISv2_2026-Aug-08_04-18-19AM-000_CustomizedView49024496437" src="https://github.com/user-attachments/assets/80fb7207-555f-460f-a466-44f3cd1af280" />


## Research Goals
Aerial manipulators, while adding functionality and expanding the applicable scope of a quadcopter, introduce a major problem to multirotor flight: moving an arm and payload changes the vehicle's mass distribution and produces additional forces and moments on the aircraft. 
Conventional quadcopter s attempt to compensate for these disturbances primarily by changing the thrust produced by each motor. ASTRALIS adds another control input by allowing the motors themselves to tilt and change the direction of their thrust. 
The primary question I want to investigate is:
> **To what extent can independently vectored thrust reduced attitude disturbances caused by the movement of an aerial manipulator and its payload?**
ASTRALIS is designed specifically as a testbed to investigate this question through repeatable arm-disturbance experiments during flight.
---
## Design
ASTRALIS consists of three main subsystems: 
- A custom quadcopter airframe (carbon fiber machined top and bottom plates + cf nylon frame pieces)
- Four independently tilting motor pods
- A multi-jointed robotic manipulator

A **Pixhawk 6C Mini** handles flight control and stabilization, while a **Raspberry Pi 4 Model B** acts as the companion computer for running and logging experimental routines, telemetry collection, and future software uses.

### Thrust-Vectoring Pods
Each motor is mounted to a tilting pod actuated by a servo and pushrod linkage. This allows the direction of each motor's thrust to be changed independently. The current design establishes the pod pivot, servo type and location, and general linkage architecture. The final linkage dimensions, ball-end selection, and mechanical advantage calculations will be determined through physical prototyping. 

<img width="400" height="300" alt="ASTRALISv2_2026-Aug-09_10-05-22PM-000_CustomizedView5219588414" src="https://github.com/user-attachments/assets/2be46a3b-3384-487f-8562-b3bf9a9ac8f7" />
<img width="400" height="300" alt="ASTRALISv2_2026-Aug-09_10-07-08PM-000_CustomizedView10570838011_png" src="https://github.com/user-attachments/assets/11fa67a6-9540-4ca7-adc2-f3f96e66acf8" />

The design includes a dual flange-bearing supported pivot and shoulder bolt, mechanically linked by a threaded rod to a servo horn. This was chosen because the turning drone's motors during thrust action will induce gyroscopic force, and I want to ensure that the system is structurally sound. The mounts will be printed out of Nylon CF as it is the strongest available filament in my collection. 

### Aerial Manipulator 
ASTRALIS uses a multi-jointed robotic arm to manipulate payloads and generate controlled disturbances during flight. The arm is designed to use **Waveshare ST3215 serial bus servos**, allowing multiple joints to be controlled through the same communication bus. 
The arm was originally designed around DYNAMIXEL servos but was redesigned around the ST3215 to increase available torque while reducing the overall costs of the actuator and control system. 

>**Note: The arm will be 3D printed out of PLA**

<img width="800" height="600" alt="ASTRALISv2_2026-Aug-09_10-07-26PM-000_CustomizedView5861968826_png" src="https://github.com/user-attachments/assets/f7cb2f0c-3b15-4ec7-af02-296fea9c5da4" />

Payload capacity is being estimated by calculating the torque produced by each arm component and payload about its respective joints.

<img width="876" height="650" alt="image" src="https://github.com/user-attachments/assets/a24bca83-3b65-4061-9a7a-2b9333a19f15" />

The calculated payload limits will be estimated once hardware is confirmed. 

---
## Electronics

<img width="1165" height="904" alt="image" src="https://github.com/user-attachments/assets/c12c041a-78ba-4978-b2bf-f0517c53a1cd" />


The electronics are spread across flight control and experiment control. 

| Component | Details |
|---|---|
| Pixhawk 6C Mini | Main flight controller |
| Raspberry Pi 5 | Companion computer used for experimental control |
| M10 GPS  | Vehicle positioning |
| Pi Camera | Used for object pickup and capturing on-board footage |
| ST3215 Servos | Used for Robotic Arm  |
| PCA9685 | Tilt Servo Driver Board | 
| DS3230 | High Torque Tilt Servos (picked to handle gyroscopic forces from tilting the motors) |
| Hobbywing XRotor 3110 900KV | Thrust Motors |
| Blueson A2 4in1 65A ESC | ESC for XRotor 3110s|

---
## Software (derived from discontinued Urban-Gust-Optimized UAV) 
Software development is currently focused on establishing basic communication between the Raspberry Pi and the Pixhawk and building the framework required for arm-disturbance experiments. Once I have the hardware confirmed, I will delve into system-
Current code includes: 
- MAVLink initialization
- Heartbeat monitoring
- Vehicle State tracking
- Attitude and angular-rate data
- Battery telemetry
- GPS telemetry

Several of the modules are still under development and will be implemented as the corresponding hardware becomes available/confirmed for purchase.

---
## Experimental Plan
>**The following experiment is the current plan, but is subject to subtle changes as hardware is confirmed for purchase or rejected**

The initial experiment will measure the aircraft's response to repeatable robotic-arm movements. A standardized payload will be picked up by the manipulator and moved through a predetermined trajectory while vehicle telemetry is recorded.
Tests will eventually be performed for both **with and without thrust-vectoring compensation**.

After the results of this experiment, I will develop a prediction-based model in MATLAB that will account for non-predetermined arm movements. 

## Future Plans 
After determining the impact of thrust-vectoring vehicle stability, I plan to add more software capabilities to the drone, making it a fully fledged UAV. I want to explore more into computer vision driven tasks with the manipulator.

Measurements will include:
- Peak roll and pitch deviation
- RMS attitude error
- Angular velocity
- Settling time 
- Response across different payload masses 

This will allow the performance of the thrust-vectoring system to be compared against the aircraft's baseline performance. 
