#ifndef EXAMPLE_POWER_DEVICE_H
#define EXAMPLE_POWER_DEVICE_H

/* Fictional values; no driver or device compatibility is implied. */
#ifdef APP_POWER_PRESET_SELECTED
#error "Select exactly one power-device preset"
#endif
#define APP_POWER_PRESET_SELECTED 1
#define EXAMPLE_POWER_DEADTIME_NS 1000UL
#define EXAMPLE_POWER_BUS_MIN_V 24.0f
#define EXAMPLE_POWER_BUS_MAX_V 48.0f

#endif
