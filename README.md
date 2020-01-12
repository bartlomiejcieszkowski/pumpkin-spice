# PumpkinSpice

## What is PumpkinSpice?

This project aims to help with provisioning embedded devices.

## Why?

I had few devices on which I've been trying different firmwares, I've been using some releays to power off the device, short the pins for reset, and even for switching serial ports. Of course this helps a lot, but you end up writing little scripts for each function, gluing it together, and wrapping it around so you could with a single command compile, flash, and boot new firmware. As you change the setup, even switch gpio around, this gets hard to mantain - hence the idea for PumpkinSpice

## How?

Idea is simple, define a file with a given schema that will satisfy requirements.

Target is to declare connections and how to do actions, and as a result be able to run simple commands like:

```
pmps mydevice compile
pmps mydevice burn
pmps mydevice monitor
pmps mydevice all
```

