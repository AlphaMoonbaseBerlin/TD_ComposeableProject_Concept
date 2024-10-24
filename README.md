# Composeable Project Concept
This repository is a project that highlights the idea of DODE. Develop Once, Deploy Everyhwere for TouchDesigner. 
The idea is that, especially for distributed systems, we do not want to develop certain aspects seperate from on another as this tends to result in repetition for functionality and harder debugging.
The following approach sees components as Plugins. Elements to a project that can be plugged in to the logic, but are not hard coded and needed. This results in us being able to dynamicly describe the project using a config-file and activating and deactivating elements resulting in a flexible setup.

## The Config
The Config is a pretty important part of the concept and utilisies the JsonConfig-Component, which generates the Schema based on dynamic callbacks.
We can make use of this by creating the schema in runtime and using customParameters as our definition.
You can finde them in /project/Configs
Right now we are setting the values from the config once on startup, but this is something that could be done dynamicly, even with binding to allow fer fast paced setup.
Also, the way this is setup is pretty barebones as we do not have a proper parsing of the parameters, so it will only work with strings and numbers for now.

## Init Procedure
The InitProcedure is tun by the InitEmitter in root. It has 4 Steps, Startup, where nothing should happen, InitPlugins where the internal processes are run like loading data/configs etc and FinalizePlugins where Components start running, for example opening the playback video.
To react to the events use the eventListener Component.

## Store
The idea of the OP-Store is pretty streight forward. Defining a single Place where we define important OPs. This is our single source of truth. Do not use global OP shortcuts or global iOPs. The store is the only place to define the refference.
