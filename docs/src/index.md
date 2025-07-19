# Van Cooldown System

Welcome to the comprehensive documentation for the Van Cooldown system - an intelligent cooling solution for van life applications.

## Overview

The Van Cooldown system is a sophisticated cooling management solution that combines:

- **Smart Power Management**: Texas Instruments TPS25751 and BQ25798 for efficient charging
- **Wireless Communication**: Nordic nRF54H20 and nRF21540 for enhanced connectivity  
- **Environmental Monitoring**: Advanced sensor integration for weather-adaptive control
- **Real-time Dashboard**: Progressive Web App with live data visualization

## Quick Start

=== "Hardware Setup"

    1. Install the main PCB in your van's electrical panel
    2. Connect power cables from your 12V system
    3. Mount environmental sensors in optimal locations
    4. Connect cooling fans to the control outputs

=== "Software Setup"

    1. Power on the system and wait for BLE advertising
    2. Open the Van Cooldown web app on your device
    3. Connect via Bluetooth and complete initial setup
    4. Configure cooling preferences and schedules

=== "Development"

    1. Clone the monorepo: `git clone https://github.com/FabienMeyer/van-cooldown.git`
    2. Run setup script: `./tools/scripts/setup-dev-env.sh`
    3. Build all components: `pnpm run build`
    4. Start development servers: `pnpm run dev`

## System Architecture

```mermaid
graph TB
    subgraph "Power Management"
        TPS25751[TPS25751 USB-C PD Controller]
        BQ25798[BQ25798 Battery Charger]
        nPM1300[nPM1300 PMIC]
    end
    
    subgraph "Communication"
        nRF54H20[nRF54H20 Main MCU]
        nRF21540[nRF21540 RF Frontend]
        BLE[Bluetooth Low Energy]
    end
    
    subgraph "Sensors"
        SHT40[SHT40 Temp/Humidity]
        INA219[INA219 Power Monitor]
        BME280[BME280 Environmental]
    end
    
    subgraph "User Interface"
        PWA[React Progressive Web App]
        Dashboard[Real-time Dashboard]
        Mobile[Mobile Interface]
    end
    
    TPS25751 --> BQ25798
    BQ25798 --> nPM1300
    nPM1300 --> nRF54H20
    nRF54H20 --> nRF21540
    nRF21540 --> BLE
    BLE --> PWA
    SHT40 --> nRF54H20
    INA219 --> nRF54H20
    BME280 --> nRF54H20
    PWA --> Dashboard
    PWA --> Mobile