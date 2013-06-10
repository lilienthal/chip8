

User Stories
~~~~~~~~~~~~
Points per week: 10

OPEN
====

Story IV : Keypad usage
-----------------------
**Points:** 5

**Motivation:** Enable user interaction

**Description:** Users can enter numbers via the keypad. The value is shown on the Transcript.

------------------

Story V : RAM access
--------------------
**Points:** 5

**Motivation:** *Core functionality*

**Description:** As a user I want to address the RAM, read and write its value. 

------------------

Story VI : LOAD RAM
-------------------
**Points:** 7

**Dependecies**: V

**Motivation:** Enable execution of arbitrary external programs

**Description:** As a user I want to load a ROM from the filesystem into the RAM.

------------------

Story VII : CPU execution cycle
------------------------------- 
**Points:** 3

**Motivation:** Allowing sequential execution of multiple instructions.

**Description:** The cpu fetches the next instruction and executes it.

------------------

Story VIII: CPU supports subroutines
------------------------------------
**Points:** 3

**Motivation:** Allowing more complex programs

**Description:** As a user i can use the `jump to subroutine`-opcode and return from it.

------------------

Story IX : Display
------------------
**Points:** 15

**Motivation:** User interaction

**Description:** Sprites can be displayed. As an example the `HPI`-logo is displayed on the scren.

Example:

.. code-block:: smalltalk

    g := C8Graphics new.
    C8Display newFor: g.
    hpi := #(#[16r00 16r00 16r00 16r00 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F 16r7F] #[16rFF 16rFF 16rFF 16rFF 16r00 16r00 16r00 16r09 16r09 16r0F 16r09 16r09 16r00 16r00 16r00 16r00 16r00 16r00 16r00 16r00 16r00 16rFF 16rFF 16rFF 16rFF 16rFF 16rFF 16rFF] #[16rFF 16rFF 16rFF 16rFF 16r00 16r00 16r00 16r74 16r54 16r74 16r44 16r44 16r00 16r00 16r00 16r00 16r00 16r00 16r00 16r00 16r00 16rFF 16rFF 16rFF 16rFF 16rFF 16rFF 16rFF] #[16rF8 16rF8 16rF8 16rF8 16r78 16r78 16r78 16r78 16r78 16r78 16r78 16r78 16r78 16r78 16r78 16r78 16r78 16r78 16r78 16r78 16r78 16r80 16r80 16r80 16r80 16r80 16r80 16r80]).
    x := 17.
    hpi do: [ :sprite |
        g draw: sprite to: x @ 2.
        x := x + 8 ]


------------------

Story X: OpCodeDispatcher
-------------------------

**Points:** 8.5

**Motivation:** Execution of RAM values

**Description**: Support execution of all opcodes.

------------------



DONE
====

Story I : Register access
-------------------------

As a user I can create a register object and access its value. Also I can apply a new value to the register.

**Motivation:** Core functionality of the chip


Solution
........

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

Solution
........

.. code-block:: smalltalk

    "
    create a new cpu,
    set register 7 to 111
    and add 123 to id
    "
    cpu := C8CPU new.
    cpu ldVx: 7 byte: 111.
    cpu addVx: 7 byte: 123.
    (cpu register: 7) bits. "=> 234"

------------------

Story III : CPU opcode add Value to Register
--------------------------------------------

.. code-block:: smalltalk
    
    "load input A in register 1"
    cpu execute: 16rF10A
    
    "load input B in register 2"
    cpu execute: 16rF20A

    "add B to A (register 2 to 1)"
    cpu execute: 16r8124

