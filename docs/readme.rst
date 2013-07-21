.. code::

      _____ ___    _____  ______          _____  __  __ ______ 
     / ____/ _ \  |  __ \|  ____|   /\   |  __ \|  \/  |  ____|
    | |   | (_) | | |__) | |__     /  \  | |  | | \  / | |__   
    | |    > _ <  |  _  /|  __|   / /\ \ | |  | | |\/| |  __|  
    | |___| (_) | | | \ \| |____ / ____ \| |__| | |  | | |____ 
     \_____\___/  |_|  \_\______/_/    \_\_____/|_|  |_|______|


C8 Emulator Manual
~~~~~~~~~~~~~~~~~~

Basics
======

In order to fire up the C8 environment, open a workspace, enter `C8IDE new` and
then "do it". The development environment opens. Initially, the source code for
the presentation slides are shown. There are several options available through
the top-level buttons:

* **Compile and Run.** The currently entered assembly source is compiled and 
  executed. The emulation will open a new window.

* **Compile.** Only compile the assembly source. Potential errors are shown in
  the field below the source code input.

* **Load ROM.** You can load arbitrary binary ROMs and display their disassembly
  in the source code viewer. Note that load and run will work with any ROM, but
  their disassembly might not be accurate, especially when the authors included
  copyright notices in ASCII.

* **Load Source.** Simply load an assembly source file in the editor component
  in order to edit, compile, run and debug your ROM.

Running
=======

For playing a ROM that demands keyboard interaction, you can use the software
keyboard and alter the button states with a single mouse click. One click
triggers the pressed state; another one releases it. The hardware keyboard is
mapped to the  Morphic keyboard as follows:

* **1, 2, 3, 4** are 1, 2, 3, C on hex. Similarly
* **Q, W, E, R** are 4, 5, 6, D;
* **A, S, D, F** are 7, 8, 9, E; and
* **Y, X, C, V** are A, 0, B, F.

If you want to try the presentation ROM, you can press **1** for forward, **2**
for one slide back.

Debugging
=========

For debugging purposes, you can add a `BREAK` instruction in the assembly
source. The next instruction will be highlighted in red when executed. The
execution thread will halt when reaching the instruction. Alternatively, you
can pause the emulation at any time by pressing **Stop** on the emulator window.

In both cases, the register view will become visible and you can inspect their
values. Execute single instructions by clicking **Step** and watch their effect.
During stepping, note that the delay and sound timers run at normal speed.
Resume the execution thread by clicking **Start**.