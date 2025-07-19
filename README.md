# Van Cooldown Project

This project aims to provide an efficient and versatile cooling solution for a van, ensuring comfortable temperatures overnight through intelligent fan control.
Project Overview

The "Van Cooldown" system is designed to manage four PWM fans, offering flexible power options and multiple control methods. It integrates a temperature sensor for automated fan speed adjustments and provides both physical hardware controls and a modern React-based application for user interaction.

## Features

### 4-Channel PWM Fan Control:

Independently control the speed of up to four Pulse Width Modulation (PWM) fans.

### Flexible Power Input

* Battery Power: Compatible with Lipo or LiFePO4 batteries, designed to power the system reliably overnight.

* 12V Cigarette Lighter Socket: Seamless integration with standard vehicle power outlets.

* USB-C: Convenient power option for various scenarios.

### Hybrid Control System

* React Application: A modern web-based interface for intuitive fan speed control and monitoring with direct Bluetooth Low Energy communication to the nRF54H20 controller.

* Hardware Trimmers: Physical potentiometers for manual, fine-grained fan speed adjustments.

* Hardware Switches: Physical switches for quick on/off control or mode selection.

* Automated Temperature Regulation: Advanced environmental control system that utilizes multiple temperature and humidity sensors to automatically adjust fan speeds based on weather conditions (temperature, humidity, heat index), maintaining optimal comfort and energy efficiency with predictive algorithms.

## Hardware Components

The core hardware components for this project include:

* Microcontroller/SBC: Nordic nRF54H20 multiprotocol wireless SoC with multiple Arm Cortex-M33 processors (up to 320MHz), 2MB flash, 1MB RAM, supporting Bluetooth LE, Thread, Matter, and Zigbee with advanced security features.

* RF Front-End Module: Nordic nRF21540 for extended wireless range (+20dBm TX power, 13dB RX gain) providing 6.3-10x range improvement for reliable communication. 

* PWM Fan Controller Module: To drive the four PWM fans efficiently.

* Temperature Sensor: Multiple high-precision sensors for comprehensive environmental monitoring:
  - Interior/exterior temperature and humidity (SHT40 sensors)
  - Component temperature monitoring (MCP9808 sensors)
  - Backup environmental sensing (BME280 sensor)

* Power Monitoring System: Comprehensive power analytics featuring:
  - System-wide power consumption monitoring (INA219 sensors)
  - Individual fan power tracking and health monitoring
  - Real-time efficiency calculations and battery analytics
  - Predictive runtime estimation and energy optimization

* Power Management Module: Comprehensive charging and power management system featuring:
  - Nordic nPM1300 PMIC with integrated fuel gauging and system management
  - TPS25751DREFR USB-C Power Delivery Controller (up to 100W)
  - BQ25798RQMR Battery Charger IC for 4S LiFePO4 batteries
  - Intelligent power source switching and priority management
  - Real-time monitoring via I2C interface

* DC-DC Converters: Multiple regulated output rails:
  - 12V @ 3A for PWM fans
  - 5V @ 1A for logic circuits and sensors  
  - 3.3V @ 0.5A for microcontroller and I2C devices

* PWM Fans: Four 12V PWM-controlled fans.

* Potentiometers (Trimmers): For manual fan speed control.

* Switches: For various control functions.

* Connectors: For power input and fan connections.

## Software Components

### Firmware: Code running on the Nordic nRF54H20:

* Read temperature sensor data and environmental conditions.

* Control PWM fan speeds based on sensor input, user commands, and automated algorithms.

* Communicate with the React application via Bluetooth Low Energy with optional Thread/Matter support for smart home integration.

* Read input from hardware trimmers and switches for manual override control.

* Manage power systems via I2C communication with nPM1300 PMIC and charging controllers.

* Provide real-time monitoring data including battery status, power consumption, and system health.

### React Application: A web-based user interface with Bluetooth connectivity and offline capabilities

* Connecting directly to the nRF54H20 via Web Bluetooth API for real-time communication.

* **Real-Time Graphics Dashboard**: Power-aware live visualizations featuring:
  - High-frequency updates (1Hz) when on external power (12V/USB)
  - Battery-conserving updates (0.2Hz) when on battery power
  - Live temperature, power consumption, and system performance charts
  - Real-time fan status monitoring with visual indicators
  - Interactive system metrics with efficiency scoring

* **Offline-First Design**: Progressive Web App (PWA) with comprehensive offline data storage and synchronization.

* **Local Data Storage**: IndexedDB for statistics, sensor data, events, and historical trends.

* Displaying current temperature, battery level, charging status, and comprehensive system analytics.

* Manually adjusting individual fan speeds with real-time feedback and automatic weather-based control.

* Selecting operation modes (automatic temperature control, manual override, sleep mode, eco mode).

* Monitoring comprehensive system status including power consumption, efficiency metrics, and wireless connectivity.

* Configuring advanced features like scheduling, temperature thresholds, smart home integration, and data retention policies.

* **Data Synchronization**: Automatic cloud sync when connectivity is available with intelligent conflict resolution.

### Power Delivery Strategy

The system is designed with a robust power delivery strategy to ensure continuous operation:

* Primary Power (Overnight): Lipo or LiFePO4 battery pack with sufficient capacity to power all components and fans for an entire night. A Battery Management System (BMS) is recommended for battery protection.

* Auxiliary Power (Vehicle): 12V cigarette lighter socket input for charging the battery or directly powering the system when the vehicle is running.

* Convenience Power: USB-C input for low-power operation or charging smaller components.

* Automatic Power Switching: A mechanism (e.g., power multiplexer, relays) to seamlessly switch between power sources based on availability and priority.