#!/bin/bash

script_path=`readlink -f “${BASH_SOURCE:-$0}”`
DIR_PATH=`dirname $script_path`
SIM_PATH=`dirname $DIR_PATH`

export IGN_GAZEBO_RESOURCE_PATH=$SIM_PATH/models:$SIM_PATH/worlds:$IGN_GAZEBO_RESOURCE_PATH
export IGN_GAZEBO_SYSTEM_PLUGIN_PATH=$SIM_PATH/build:$IGN_GAZEBO_SYSTEM_PLUGIN_PATH