# KNR Drones simulation repository
This is KNR repository for simulation of drones based on ardupilot_gazebo plugin, based on official [ArduPilot/ardupilot_gazebo repo](https://github.com/ArduPilot/ardupilot_gazebo).
It allows users to simulate 3D enviroment while using Ardupilot in SITL.

## Prerequisites :
Ignition Fortress is supported on Ubuntu Bionic, Focal and Jammy. If you are running Ubuntu as a virtual machine you will need at least Ubuntu 20.04 (Focal) in order to have the OpenGL support required for the `ogre2` render engine.

Follow the instructions for a [binary install of ignition fortress](https://ignitionrobotics.org/docs/fortress/install) and verify that ignition gazebo is running correctly.

Set up an [ArduPilot development environment](https://ardupilot.org/dev/index.html). In the following it is assumed that you are able to
run ArduPilot SITL using the [MAVProxy GCS](https://ardupilot.org/mavproxy/index.html).

## Installation :

Install Ignition Gazebo Fortress development libs and rapidjson:
````
sudo apt install rapidjson-dev libignition-gazebo6-dev
````

Clone the repo and build with:
````bash
git clone https://github.com/qbaaa-0/drone_sim -b fortress
cd drone_sim
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo
make -j4
````

## Running :

Set the ignition environment variables in your `.bashrc` or `.zshrc` or in  the terminal used to run gazebo:

### In terminal
Assuming that you have clone the repository in `$HOME/drone_sim`:
```bash
source util/setup.bash
```

### In .bashrc
Assuming that you have clone the repository in `$HOME/drone_sim`:
```bash
echo 'export IGN_GAZEBO_SYSTEM_PLUGIN_PATH=$HOME/drone_sim/build:${IGN_GAZEBO_SYSTEM_PLUGIN_PATH}' >> ~/.bashrc
echo 'export IGN_GAZEBO_RESOURCE_PATH=$HOME/drone_sim/models:$HOME/drone_sim/worlds:${IGN_GAZEBO_RESOURCE_PATH}' >> ~/.bashrc
```

Reload your terminal with source ~/.bashrc

### Run Gazebo

```bash
ign gazebo -v 4 -r iris_runway.sdf
```

In order to display debug information, use `-v 4` parameter. 

### Run ArduPilot SITL
To run an ArduPilot simulation with Gazebo, the frame should have `gazebo-` in it and have `JSON` as model. Other commandline parameters are the same as usal on SITL.
```bash
sim_vehicle.py -v ArduCopter -f gazebo-iris --model JSON --map --console
```

### Arm and takeoff
In order to controll the drone one may use SITL terminal and MAVLink commands, eg.:

```bash
STABILIZE> mode guided
GUIDED> arm throttle
GUIDED> takeoff 5
GUIDED> mode auto
```