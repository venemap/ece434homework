### Blinking an LED
If you run the command 'make', the LED will start blinking on its own. To stop the PRU, you can use the 'make stop' command. 'make start' will restart the program.

When setting __delay_cycles() to 0, there was a decent amount of overshoot that was caused in the resulting square wave. This overshoot caused a relatively large amount of standard deviation from the norm, with a value of 41millivolts, but the voltage was actually quite consistent, so it was stable in that regard. 
The period looks to be fairly constant in the short term, but the oscilloscope says that there is a std deviation of 942microseconds, which doesnt sound like alot, but the mean value of the period is only 2.025milliseconds. So basically half of the average period shows up in the std deviation, so the period is actually quite inconsistent, though it is so fast that it is hard to see without taking a snapshot of an oscilloscope.


