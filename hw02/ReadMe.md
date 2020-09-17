## Measuring a GPIO pin on an Oscilloscope

# Shell

1 - Min voltage = 0V, Max = 3.48V
2 - Period = 120ms
3 - It is about 20ms off
4 - They likely differ due to this shell script being interrupted by other processing running in the computer
5 - I was using abuot 1.3% of my processor according to htop
6 - |Period||
7 - The period seemed to be a bit reliant on what the computer was doing. When opening a more intensive program, I believe I saw the period become less consistent, though I was unable to capture this in the oscilloscope readings. 
8 - Period looked to fluctuate slightly
9 - The period stayed about the same, with the same delay of about 20ms when trying to generate a period of 100ms
10 - Period was the same using bash vs sh
11 - Shortest period I tried was a 3.3ms period. The oscilloscope reading told me that it was actually giving me a 26.5ms period, but by this point the waveform began to show signs of overshooting, so I decided to stop the experiment there. It seemed like the delay between expected and actual period was getting worse, and the max and min values of the output were getting more out of control, so I said that this as the shortest period I could get that still looked like a standard waveform.

# Python
1 - Min voltage = 0V, Max = 3.40V
2 - Period = 100ms exactly
3 - It looked to be exactly 100ms
4 - They didnt differ at all in my case
5 - I was using about 4.6% cpu according to htop
6 - 
7 - Period looked to be very stable
8 - When launching different tasks, the period appeared to stay very constant
9 - No change
10 - N/A
11 - Shortest period I could get was 1ms period

# C

## GPIOD
The fastest I could get python to toggle a bit and still look like a normal waveform was with a period of 0.3ms