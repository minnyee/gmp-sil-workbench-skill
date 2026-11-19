#ifndef EXAMPLE_CONTROL_H
#define EXAMPLE_CONTROL_H

/* Execution timing only: this example defines no control algorithm. */
#ifdef APP_CONTROL_PRESET_SELECTED
#error "Select exactly one control preset"
#endif
#define APP_CONTROL_PRESET_SELECTED 1
#define EXAMPLE_CONTROL_DIVIDER 2UL

#endif
