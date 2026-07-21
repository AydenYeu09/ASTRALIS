# Astralis: An Overactuated Aerial Manipulation Quadcopter

> **Note:** Built for Hack Club's Stardance Program and intended to serve as an MIT Maker Portfolio project.

---

# 2026-06-29 — Project Initialization

### Derived from the Urban Gust Optimized UAV Project

**Astralis** originated from my previous **Urban Gust Optimized UAV (UGOUAV)** project. The following resources were carried over:

- Top and bottom plate CAD
- Initial arm design
- Onshape CAD document
- Notion workspace
- Bill of Materials (BOM)

Although the projects share a common starting point, they have completely different objectives. **UGOUAV** has been officially retired and will no longer receive updates.

---

# 2026-06-30 — Devlog 1: Battery Holder V1 & Electronics Diagram

### Battery Holder V1

Designed the first iteration of the battery holder.

Features:
- Intended to be 3D printed in PLA.
- Battery slides into a dedicated slot.
- Future revision will include a retaining mechanism to securely hold the LiPo during flight.

### Electronics Diagram

Created the first draft of the electronics architecture using **Lucidchart** for compatibility with Notion.

This diagram outlines the major onboard components and serves as the foundation for future wiring and power distribution planning.

**Time Spent:** **2.5 hours**

### Images
<img width="700" alt="image" src="https://github.com/user-attachments/assets/4baa60f2-5494-49d4-af86-5ff25415f695" />
<img width="700" alt="image" src="https://github.com/user-attachments/assets/831be675-8335-432d-854d-96bdd96d4477" />


---

# 2026-07-01 — Devlog 2: Servo Pod Research & Implementation

Focused primarily on designing the **servo pod**, a 3D printed component that mounts the tilt servo parallel to each thrust-vectoring pod.

The current design is inspired by the clamping mechanism presented in the following research paper:

> https://www.mdpi.com/2218-6581/7/4/65

The pod uses a shaft-collar style clamp that grips the carbon fiber arm while providing a rigid mounting point for the servo.

Future iterations will incorporate a pushrod linkage connecting the servo horn to the tilting motor pod.

### Next Steps

- [ ] Begin designing the aerial manipulator subsystem.
- [ ] Implement the pushrod linkage in CAD.
- [ ] Continue refining the thrust-vectoring mechanism.

**Time Spent:** **2 hours**

### Images
<img width="700" alt="image" src="https://github.com/user-attachments/assets/e048cd60-7e50-4e60-9277-2c14150d705f" />

---

# 2026-07-04 — Devlog 3: *Aerial Manipulator CAD*!

Today, I completed the **body frame** of the drone with the addition of a Pi Camera Module 2 mount; I also worked on improving the battery holder design, this time ensuring it can be added and removed without extreme disassembly.

## Cool Things:

- I tinkered around with the “Convex Polyhedron” OnShape featurescript to make the drone’s body have a low poly aesthetic
- Added Colors!

## Main Things:

- I developed the **Pi Camera Mount**, having the mount protrude outwards from the X-wing configuration and angle thirty degrees downward.
  - The Pi Camera was added because it provides future upgrade possibilities regarding software decisions, as well as gives the opportunity to get some footage of the drone (I also had two Pi Cams in my stash)
  - There was lots of experimentation regarding this part. I tried using lofts to make the camera mount first and then loft outwards, but frustratingly I was not able to get the geometry to work (too tight of geometry to be lofting like that!)
  - I ended up using the Convex Polyhedron Featurescript, which allowed me to select a few points and enclose an area with a low-poly extruded body, which I then hollowed out to create more overflow space for wiring
  - I finally added some material pockets, mainly for aesthetics. I will need to evaluate the printability of this part and the pockets will be the first thing to be edited if it bars printability.
- The **battery holder** received minor improvements regarding tolerances and the addition of the closer arm, which is mounted by two screws on each side
  - I added more space for the battery
- The spacing between the **top and bottom plates** received an update, increasing 10mm so that a Dynamixel XL430 can fit within the drone’s frame (for the design of the manipulator)
  - This also resulted in the arm tube clamp being changed

## Next Things to Do:

- [ ] Start Arm/Manipulator Development
- [ ] Finish Tilt Pods (add m2 push rods)
- [ ] Update the BOM

**Time Spent:** **4 hours**

### Images 
<img width="700" alt="image" src="https://github.com/user-attachments/assets/9bffee92-0b94-4181-90a4-a78d04894299" />
<img width="700" alt="image" src="https://github.com/user-attachments/assets/ce8a3444-7de8-4876-9e5d-785cd810438b" />
<img width="700" alt="image" src="https://github.com/user-attachments/assets/5df173df-6034-46c0-a260-f1511d08f01b" />
<img width="700" alt="image" src="https://github.com/user-attachments/assets/93eee287-5090-4a41-af3a-7cc012ac2a03" />

---

# 2026-07-10 — Devlog 4: Aerial Manipulator Design

Over the past couple of days, I completed the **aerial manipulator** — the robot arm — for the drone. The current design assumes the use of **DYNAMIXEL XL430 and XL330 servos**, though the final servo mounting is not fully finalized in CAD yet.

## Cool Things

- The arm is **animated in CAD**
- The full manipulator is now integrated into the drone assembly
- I designed and compared **two different gripper concepts**

## The Arm

The arm uses **DYNAMIXEL smart servos** because they provide positional feedback and include many features that may be useful later.

The current manipulator is a **4-DOF robotic arm with a gripper**:

- **Base rotation** about the Z-axis
- **Shoulder rotation** about the X-axis
- **Elbow rotation** about the X-axis
- **Wrist rotation** about the X-axis
- **Servo-driven gripper** as the end effector

The arm is intended to be **fully 3D printed**, allowing for fast iteration and easier replacement of parts if the design changes.

## The Gripper

The bulk of the time was spent on the gripper, partly because I designed two different models:

1. A **linkage gripper**
2. A **standard parallel gripper**, inspired by this guide: [3D Printed Parallel Gripper for Robotic Arms](https://www.instructables.com/3D-Printed-Parallel-Gripper-for-Robotics-Arms/)

### Linkages…

The linkage gripper was designed with compactness in mind. It used a gear-driven linkage system and was intended to use **TPU fingers** to grip rigid payloads.

However, maintaining printing tolerances and designing around the linkage geometry made the CAD extremely messy. The mechanism had too many small pivot points, tolerance-sensitive parts, and potential failure points. Because of that, I could not justify printing and prototyping this version.

The main focus of the project is not the gripper itself. The focus is on testing how the drone handles **disturbances induced by arm movement and held payloads**. Because of this, I need full confidence that the gripper will work reliably without spending too much project time reprinting and redesigning it.

### Parallel Gripper!

Following the Instructables guide, I designed a simpler parallel gripper using a similar bearing, rod, and rack-and-pinion layout.

This gripper uses:

- A 3D-printed main body
- Rigid 3D-printed fingers instead of TPU fingers
- Two identical gear racks
- A central pinion gear
- Linear rods for jaw guidance

The CAD design was much simpler, and I am more confident that this version will produce reliable performance. The parallel gripper should be easier to print, easier to assemble, and easier to debug than the linkage gripper.

## Next Things to Do

- [ ] Add push/pull rods in CAD to the tilting pods
- [ ] Finalize internal electronics mounting
- [ ] Evaluate costs for plates and add weights in CAD
- [ ] Bias the center of gravity toward the ideal location
- [ ] Research and add drone motors and propellers to the BOM
- [ ] Add the DYNAMIXEL XL330 mount in the arm

**Time Spent:** **6 hours, 45 minutes**

### Images
<img width="700" alt="image" src="https://github.com/user-attachments/assets/ee660d00-3430-46d1-9960-833e2e556ba5" />
<img width="700" alt="image" src="https://github.com/user-attachments/assets/05eb4b2a-c2ff-412a-9a6e-325d9bd2a80f" />
<img width="400" alt="image" src="https://github.com/user-attachments/assets/33f69b7e-a02b-49e3-9ef3-57f8ff39a925" />
<img width="700" alt="image" src="https://github.com/user-attachments/assets/b5c1c383-0ccb-48bd-9eb0-071af108e7e9" />

---

# 2026-07-21 — Devlog 5: *Aerial Manipulator Finalized, Tilt Pods Finished, and Frame Finished*

Over the past few days, I finalized the overall airframe, completed the aerial manipulator, and finished the design of the thrust-vectoring tilt pods. This was probably one of the toughest and most detailed-focus stages of the project so far (definitely stayed up super late fixing it sometimes!), prompting several redesigns to accommodate the Dynamixel XL330-M288-T servos while also standardizing hardware throughout the drone.

> **Note:** I have another CAD timelapse recorded in Lookout that I'm still trying to transfer into Stardance.

---

## General Design Updates

A major focus during this stage was reducing complexity and improving ease of assembly.

- Standardized as many fasteners as possible across the drone.
- Reused hardware from previous combat robotics and robotics projects whenever practical.
- Organized the CAD assembly by separating self-tapping screws into dedicated **PLASTITES** folders while leaving machine screws in the default folders to simplify the assembly process.

---

## Landing Gear

The landing gear went through two complete design iterations.

The original concept used a dedicated clamp that attached independently to the carbon fiber arms. After evaluating the design, I integrated the landing gear directly into the arm end cap instead.

This redesign:

- Reduced the total number of printed components.
- Increased the distance between the landing feet, improving stability.
- Maximizes operating space of arm.
- Minimized interference with the thrust-vectoring pod geometry.

Each landing gear assembly consists of three printed components, including TPU feet intended to improve grip and absorb landing impacts.

---

## Tilt Pods

The thrust-vectoring pods are now mechanically complete.

The largest addition during this stage was designing the pushrod linkage connecting each servo horn to its corresponding tilt pod. 
At the moment:

- The linkage geometry has been finalized.
- The linkage components will be 3D printed and prototyped.
- Mechanical advantage calculations and linkage calibration still need to be completed before the CAD animation accurately reflects the pod motion.

---

## Aerial Manipulator

The aerial manipulator has now been finalized (closed book, finally done!).

One of the largest changes was redesigning the arm to properly mount the Dynamixel XL330-M288-T servos internally instead of externally.

Benefits of the redesign include:

- Cleaner overall appearance.
- More compact packaging.

The servos will be mounted using the provided M2 self-tapping screws directly into the printed components.

---

## Battery Holder V2

The battery mounting system also received a significant redesign.

Originally, the battery was positioned underneath the frame because I assumed lowering the center of gravity would improve stability. After learning more about quadcopter dynamics, I realized this configuration introduces a pendulum effect that complicates flight control.

The updated design mounts the battery on top of the frame using a PLA battery cradle secured with four M4 machine screws and a Velcro strap.

This redesign also frees the entire underside of the frame for the aerial manipulator, allowing the arm to rotate through a full **360°** without the battery obstructing its workspace.

---

## Next Steps
- [ ] Assign materials to all CAD components and calculate the drone's center of gravity.
- [ ] Finalize the complete electrical component placement within the body and wiring diagram.
- [ ] Characterize the thrust-vectoring linkage and determine its mechanical advantage.
- [ ] Begin firmware development and hardware testing routines.
- [ ] Write assembly documentation and build guides.
- [ ] Begin printing and validating mechanical prototypes.

**Time Spent:** **6 hours, 45 minutes**

### Images
<img width="650" alt="image" src="https://github.com/user-attachments/assets/a8ba1836-08c9-456c-a16f-481df47e7f2d" />
<img width="700" alt="image" src="https://github.com/user-attachments/assets/3387aa51-2dcd-40f4-81eb-e57e33e98703" />
<img width="400" alt="image" src="https://github.com/user-attachments/assets/39946b0c-e5ae-4656-91ab-16a7fcb8be5d" />
<img width="700" alt="image" src="https://github.com/user-attachments/assets/0dac1b93-55e6-4f94-8dd0-63abaaafb8bd" />

---
