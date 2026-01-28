# 🪴 ECE 2021 – Automatic Plant Wellness System

This project was developed as part of the **ECE 2021** course at UNB. This project implements an automated plant watering and monitoring system using environmental sensors and the UNB Dev Board.

## Overview
The system continuously monitors:
- Soil moisture (plant)
- Water reservoir level
- Ambient temperature
- Ambient light level

Based on sensor readings, the system automatically controls a water pump and provides real-time visuals through LEDs and audio feedback using a speaker to indicate system status.

## Features
- Automatic plant watering based on soil moisture thresholds
- Safety check to prevent pump operation when the water reservoir is low
- LED indicators for light, temperature, plant moisture, and reservoir status
- Audio alert when the reservoir is empty

## Hardware
- UNB development board (Rev 4.1)
- Soil moisture sensors (plant and reservoir)
- Water pump controlled via digital output
- LEDs and speaker for system feedback

Hardware schematics are provided in the `schematics/` directory for reference.

## Software
The firmware is written in Python and runs in a continuous loop, periodically reading sensor values and applying threshold-based control logic to determine pump activation and feedback behavior.

Source code is located in the `firmware/` directory.
