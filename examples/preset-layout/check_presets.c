#include "src/user/ctrl_settings.h"

/* Checks only configuration selection and units; no hardware is accessed. */
_Static_assert(APP_PWM_HZ == 20000UL, "Expected example PWM rate");
_Static_assert(APP_CONTROL_HZ == 10000UL, "Expected divided control rate");
_Static_assert(APP_CENTER_ALIGNED_PERIOD_COUNTS == 2500UL,
               "Expected center-aligned period");
_Static_assert(APP_ENCODER_COUNTS_PER_TURN == 4096UL,
               "Encoder counts use a mechanical-turn base");
_Static_assert(EXAMPLE_ENCODER_CAL_VALID == 0U,
               "Example calibration must not be treated as valid");

int main(void)
{
    return 0;
}
