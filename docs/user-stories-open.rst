

User Stories - Open
~~~~~~~~~~~~~~~~~~~

Points per week: 10


Story VIII: CPU supports subroutines
------------------------------------
**Points:** 3

**Motivation:** Allowing more complex programs

**Description:** As a user i can use the `jump to subroutine`-opcode and return from it.

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

	cpu := C8CPU new.
	cpu ram loadROM: '/home/falco/c8games/MAZE2'.
	cpu display: C8Display new.
	cpu start.

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