#ifndef EXAMPLE_MOTOR_H
#define EXAMPLE_MOTOR_H

/* Fictional motor and installation values, never hardware calibration. */
#ifdef APP_MOTOR_PRESET_SELECTED
#error "Select exactly one motor preset"
#endif
#define APP_MOTOR_PRESET_SELECTED 1
#define EXAMPLE_MOTOR_POLE_PAIRS 4U
#define EXAMPLE_MOTOR_RS_OHM 0.2f
#define EXAMPLE_MOTOR_LD_H 0.001f
#define EXAMPLE_MOTOR_LQ_H 0.001f
#define EXAMPLE_ENCODER_COUNTS_PER_MECH_TURN 4096UL
#define EXAMPLE_ENCODER_OFFSET_COUNTS 0L
#define EXAMPLE_ENCODER_CAL_VALID 0U

#endif
