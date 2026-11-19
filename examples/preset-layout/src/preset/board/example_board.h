#ifndef EXAMPLE_BOARD_H
#define EXAMPLE_BOARD_H

/* Fictional values for configuration structure only. */
#ifdef APP_BOARD_PRESET_SELECTED
#error "Select exactly one board preset"
#endif
#define APP_BOARD_PRESET_SELECTED 1
#define EXAMPLE_BOARD_PWM_CLOCK_HZ 100000000UL
#define EXAMPLE_BOARD_PWM_HZ 20000UL
#define EXAMPLE_BOARD_ADC_BITS 12U
#define EXAMPLE_BOARD_ADC_REFERENCE_V 3.3f

#endif
