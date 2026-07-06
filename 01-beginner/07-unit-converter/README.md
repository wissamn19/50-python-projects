# Unit Converter / Calculator

> OOP, custom exceptions, error handling

## Overview
A menu unit converter that handles 7 conversion types across distance,
temperature, weight, volume, data, speed, and pressure. Built with a clean OOP.
Structure and custom exceptions that enforce real physical limits like absolute zero for temperature and zero for pressure.

## Concepts Practiced
- OOP : `UnitConverter` class with one method per conversion
- Custom exceptions : `OutOfRangeError` for physically impossible inputs
- Error handling : `try/except` for both `ValueError` and custom exceptions
- Interactive menu with `input()` and a `while True` loop
- Physical constants : absolute zero (-273.15°C), perfect vacuum (0 Pa)

## How to Run
```bash
# from this folder
python main.py
```

## Supported Conversions

| # | Conversion | Physical Limit |
|---|-----------|----------------|
| 1 | Kilometers → Miles | Cannot be negative |
| 2 | Celsius → Fahrenheit | Cannot be below -273.15°C (absolute zero) |
| 3 | Kilograms → Pounds | Cannot be negative |
| 4 | Liters → Gallons | Cannot be negative |
| 5 | Gigabytes → Terabytes | Cannot be negative |
| 6 | Meters/Second → KM/Hour | Cannot be negative |
| 7 | Pascals → Atmospheres | Cannot drop below 0 Pa (perfect vacuum) |

## What I Learned

The main challenge was understanding how to create custom exceptions, I knew Python had `try/except` but I didn't know you could define your own exception classes. Once I saw that it's just a class that inherits from `Exception`, it clicked immediately. You define it once and raise it anywhere with a meaningful message.

The physical limits themselves were straightforward, if you know that
temperature can't go below -273.15°C or pressure can't drop below 0 Pa, the condition to raise the error writes itself. The hard part was the concept, not the physics.

What I'd do differently: create a base `ConverterError` class and have
`OutOfRangeError` inherit from it, that way if I add more custom exceptions later, they all share a common parent I can catch in one place.

---
[← Back to main repo](../../README.md)