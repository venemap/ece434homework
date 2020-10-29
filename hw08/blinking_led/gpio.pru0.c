// This code accesses GPIO without using R30 and R31
#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

#define P9_31   (0x1<<14)
#define P2_05	(0x1<<30)			// Bit position tied to P2_05 on Pocket

volatile register uint32_t __R30;
volatile register uint32_t __R31;

void main(void)
{
	uint32_t *gpio3 = (uint32_t *)GPIO3;
	
	while(1) {
		gpio3[GPIO_SETDATAOUT]   = P9_31;
		__delay_cycles(0);
		gpio3[GPIO_CLEARDATAOUT] = P9_31;
		__delay_cycles(0);
	}
}
