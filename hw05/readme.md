Basic readme for homework05

### Cross-Compiling results
venemap@venemap-Precision-5520:~/Desktop/exercises$ ssh bone ./a.out
Warning: Permanently added 'bone,192.168.7.2' (ECDSA) to the list of known hosts.
Debian GNU/Linux 10

BeagleBoard.org Debian Buster IoT Image 2020-08-31

Support: https://bbb.io/debian

default username:password is [debian:temppwd]

Hello, World! Main is executing at 0x4755ad
This address (0xbec0ac20) is in our stack frame
This address (0x486010) is in our bss section
This address (0x486008) is in our data section
venemap@venemap-Precision-5520:~/Desktop/exercises$ file a.out
a.out: ELF 32-bit LSB shared object, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux-armhf.so.3, BuildID[sha1]=537d8366dbc02d0860edb54b2fb931390cc20db7, for GNU/Linux 3.2.0, not stripped
