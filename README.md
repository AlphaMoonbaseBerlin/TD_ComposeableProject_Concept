### Composable Project Concept

This repository showcases the concept of **DODE: Develop Once, Deploy Everywhere** for TouchDesigner. The goal is to avoid developing certain aspects of distributed systems separately, as this often leads to redundant functionality and more challenging debugging. In this approach, components function as plugins—modular elements that can be integrated into the project logic without being hard-coded as essential elements. This allows for a dynamic project structure, defined through a configuration file, where elements can be activated or deactivated as needed, resulting in a flexible setup.

### The Config

The configuration file plays a key role in this concept, utilizing the `JsonConfig` component, which generates a schema based on dynamic callbacks. By defining the schema at runtime and using custom parameters, the configuration can be highly adaptable. These configurations can be found in `/project/Configs`. Currently, values from the configuration are set once on startup, though this could be done dynamically, potentially with binding, to allow for rapid setup adjustments. As it stands, this setup is somewhat basic and lacks robust parameter parsing, so it currently supports only string and number data types.

### Init Procedure

The initialization process is managed by the `InitEmitter` component in the root directory and consists of three stages:

1. **Startup:** Where no processes occur.
2. **InitPlugins:** Where internal processes, such as loading data and configurations, are executed.
3. **FinalizePlugins:** Where components begin functioning, such as initiating video playback.

To respond to these events, use the `eventListener` component.

### Store

The concept of the **OP Store** is straightforward: it serves as a single, centralized location to define important OPs, acting as a single source of truth. Avoid using global OP shortcuts or global iOPs. The store should be the only place where OP references are defined.
