User Stories - Done
~~~~~~~~~~~~~~~~~~~

Story I : Register access
-------------------------

As a user I can create a register object and access its value. Also I can apply a new value to the register.

**Motivation:** Core functionality of the chip


Demo
....

.. code-block:: smalltalk
    
    "Register creation"
    register := C8Register new.
    register bits: 8.

    "accessing it's value"
    register bits. "=> 8"

    "values >255 are cropped to fit 8 bits"
    register bits: 1337.
    register bits. "=> 57"

------------------

Story II : CPU opcode load register
-----------------------------------

Users can load a byte into a register using the ldVx opcode and execute the addVx opcode to add a number.

Demo
....

.. code-block:: smalltalk 
    
    cpu := C8CPU new.
    cpu ldVx: 7 byte: 111.
    cpu addVx: 7 byte: 123.
    (cpu register: 7) bits. "=> 234"

------------------

Story III : CPU opcode add Value to Register
--------------------------------------------

.. code-block:: smalltalk
    
    cpu := C8CPU new.

    "load input A in register 1"
    cpu execute: 16r610A.
    
    "load input B in register 2"
    cpu execute: 16r620B.

    "add B to A (register 2 to 1)"
    cpu execute: 16r8124; inspect

------------------

Story IV : Keypad usage
-----------------------
**Points:** 5

**Motivation:** Enable user interaction

**Description:** Users can enter numbers via the keypad. The value is shown on the Transcript.

Demo
....

.. code-block:: smalltalk

    "Show the last key on the transcript until a character other than
    0 is pressed"
    Transcript clear.
    kb := C8Keyboard new.
    [
        [ kb lastKey = 0 ] whileFalse:
            [Transcript show: 'Last Key: '; show: (kb lastKey ); cr.
            (Delay forSeconds: 3) wait. ]
    ] fork.


    "Second example - ldK opcode"
    [ chip := C8Chip new.
    chip cpu ldK: 0.
    Transcript show: (chip cpu register: 0) bits; cr.] fork.

------------------

Story V : RAM access
--------------------
**Points:** 5

**Motivation:** *Core functionality*

**Description:** As a user I want to address the RAM, read and write its value.

Demo
....

.. code-block:: smalltalk
    
    mem := C8Memory new.

    mem write: 16r4 to: 1000.
    mem readAt: 1000.

    two := #[16re 16rf].
    mem writeMany: two to: 4000.
    mem read: 2 at: 4000.

------------------

Story VI : LOAD ROM
-------------------
**Points:** 7

**Dependecies**: V

**Motivation:** Enable execution of arbitrary external programs

**Description:** As a user I want to load a ROM from the filesystem into the RAM.

Demo
....

.. code-block:: smalltalk

    chip := C8Chip new.
    chip loadROM: '/home/falco/c8games/BLINKY'.
    chip ram inspect.

------------------

Story VII : CPU execution cycle
------------------------------- 
**Points:** 3

**Motivation:** Allowing sequential execution of multiple instructions.

**Description:** The cpu fetches the next instruction and executes it.

Demo
....

.. code-block:: smalltalk

    chip := C8Chip new.
    chip cpu
        pc;
        doCycle;
        pc.

------------------

Story IX : Display
------------------
**Points:** 15

**Motivation:** User interaction

**Description:** Sprites can be displayed. As an example the `HPI`-logo is displayed on the scren.

Example:

.. code-block:: smalltalk

    "HPI Logo: 2 sprite version"
    g := C8Graphics new.
    (C8Display newFor: g) openInWorld; scaleFactor: 10.
    top := #(
    #[16r00 16r00 16r00 16r00 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F]
    #[16rFF 16rFF 16rFF 16rFF 16r00 16r00 16r00 16r09 16r09 16r0F 16r09 16r09 16r00 16r00]
    #[16rFF 16rFF 16rFF 16rFF 16r00 16r00 16r00 16r74 16r54 16r74 16r44 16r44 16r00 16r00]
    #[16rF8 16rF8 16rF8 16rF8 16r78 16r78 16r78 16r78 16r78 16r78 16r78 16r78 16r78 16r78]).
    bottom := #(
    #[16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F]
    #[16r00 16r00 16r00 16r00 16r00 16r00 16r00 16rFF 16rFF 16rFF 16rFF 16rFF 16rFF 16rFF]
    #[16r00 16r00 16r00 16r00 16r00 16r00 16r00 16rFF 16rFF 16rFF 16rFF 16rFF 16rFF 16rFF]
    #[16r78 16r78 16r78 16r78 16r78 16r78 16r78 16r80 16r80 16r80 16r80 16r80 16r80 16r80]).
    x := 17.
    top do: [ :sprite |
        g draw: sprite to: x @ 2.
        x := x + 8 ].
    x := 17.
    bottom do: [ :sprite |
        g draw: sprite to: x @ 16.
        x := x + 8 ]


    "C8 Logo"
    g := C8Graphics new.
    (C8Display newFor: g) openInWorld; scaleFactor: 10.
    g draw: #[2r01100110 2r10001001 2r10001001 2r10000110 2r10001001 2r10001001 2r01100110] to: 28@12.

------------------

Story X: Opcode Dispatcher
--------------------------

**Points:** 8.5

**Motivation:** Execution of RAM values

**Description**: Support execution of all opcodes.

Demo
....

.. code-block:: smalltalk

    [ self halt. C8CPU new dispatcher dispatch: 16rA111 ] value.

------------------

Story VIII: CPU supports subroutines
------------------------------------
**Points:** 3

**Motivation:** Allowing more complex programs

**Description:** As a user i can use the `jump to subroutine`-opcode and return from it.

Demo
....

.. code-block:: smalltalk

    chip := C8Chip new.
    chip cpu
    call: C8Chip startAddress + 20;
    pc;
    ret;
    pc.

------------------

Story XI: MAZE+
---------------

**Points:** 5

**Motivation:** Integration test.

**Description:** Execute the first ROM: MAZE. Prepend opcode "waiting for key
press" to demo user input.

Demo
....

.. code-block:: smalltalk

    chip := C8Chip new.
    C8Window newWithChip: chip.
    chip loadROM: '/home/falco/c8games/MAZE'.
    chip start.

    cpu stop.

------------------

Story XII: Symbolic Disassbembler
---------------------------------

**Points:** 8

**Motivation:** Faster ROM analysis.

**Description:** Enhance the current disassembler prototype and enable the user
to retrieve opcode and parameter descriptions from a binary ROM.

Demo
....

.. code-block:: smalltalk
    
    Transcript clear.
    d := C8SymbolicDisassembler new.
    d runOn: '/home/falco/c8games/MAZE'

------------------

Story XIII: Keyboard GUI
------------------------

**Points:** 6

**Motivation:** User Interaction.

**Description:** Enable the user to simulate keystrokes by clicking a corresponding
button.

Demo
....

.. code-block:: smalltalk

    chip := C8Window new.