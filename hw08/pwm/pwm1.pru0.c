#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

#define PRU0_DRAM    0x0000

volatile register uint32_t __R30;
volatile register uint32_t __R31;

void main(void)
{
	uint32_t gpio = P9_31;	// Select which pin to toggle.;

	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;
	
	volatile unsigned int *pru0_dram = PRU0_DRAM;

	while(1) {
		__R30 |= gpio;		// Set the GPIO pin to 1
		__delay_cycles(0);
		__R30 &= ~gpio;		// Clear the GPIO pin
		__delay_cycles(0);
		
	}
}
