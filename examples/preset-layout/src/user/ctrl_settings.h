#ifndef EXAMPLE_CTRL_SETTINGS_H
#define EXAMPLE_CTRL_SETTINGS_H

#include "../preset/board/example_board.h"
#include "../preset/power_device/example_power_device.h"
#include "../preset/motor/example_motor.h"

/* An explicit build selection takes precedence over the manual default. */
#ifdef APP_CONTROL_PRESET_FILE
#include APP_CONTROL_PRESET_FILE
#else
#include "../preset/control/example_control.h"
#endif

/* Example application names, not GMP API macros. */
#define APP_PWM_HZ EXAMPLE_BOARD_PWM_HZ
#define APP_CONTROL_HZ (APP_PWM_HZ / EXAMPLE_CONTROL_DIVIDER)
#define APP_CENTER_ALIGNED_PERIOD_COUNTS \
    (EXAMPLE_BOARD_PWM_CLOCK_HZ / (2UL * APP_PWM_HZ))
#define APP_MOTOR_POLE_PAIRS EXAMPLE_MOTOR_POLE_PAIRS
#define APP_ENCODER_COUNTS_PER_TURN EXAMPLE_ENCODER_COUNTS_PER_MECH_TURN

#if EXAMPLE_BOARD_PWM_HZ == 0 || EXAMPLE_CONTROL_DIVIDER == 0
#error "PWM frequency and control divider must be positive"
#else
#if EXAMPLE_BOARD_PWM_CLOCK_HZ % (2UL * APP_PWM_HZ) != 0
#error "PWM period must be an integer number of clock ticks"
#endif
#if APP_PWM_HZ % EXAMPLE_CONTROL_DIVIDER != 0
#error "Control update frequency must divide the base frequency exactly"
#endif
#endif

#if EXAMPLE_ENCODER_CAL_VALID != 0 && EXAMPLE_ENCODER_CAL_VALID != 1
#error "Calibration validity must be 0 or 1"
#endif

#endif
