#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import os
import struct


def write_opcode(f, opcode):
	opcode = struct.pack('>H', opcode)
	f.write(opcode)


def read_opcode(f):
	return struct.unpack('>H', f.read(2))[0]


def shell(file_in, file_out):
	print("(c)opy | (m)odify | (p)repend, 'q' to quit")
	file_in_size = os.fstat(file_in.fileno()).st_size
	while True:
		position = file_in.tell()
		if position == file_in_size:
			print 'Complete input file read, done.'
			break

		current_opcode = read_opcode(file_in)
		try:
			x = raw_input('[ +%i: %x ]> ' % (position, current_opcode)).split(' ')
		except (KeyboardInterrupt, EOFError):
			print("\nWarning: Exiting without saving.")
			sys.exit(1)
		
		cmd = x[0]
		if cmd == 'q':
			break

		if cmd == 'c':
			write_opcode(file_out, current_opcode)
		else:
			opcode_hex = x[1]
			opcode = int(opcode_hex, base=16)
			if cmd == 'm' or cmd == 'p':
				write_opcode(file_out, opcode)
			
			if cmd == 'p':	
				file_in.seek(-2, os.SEEK_CUR)


def main(args):
	file_in = open(args[1], 'rb')
	file_out = open(args[2], 'wb')

	shell(file_in, file_out)

	file_in.close()
	file_out.close()


if __name__ == '__main__':
	if len(sys.argv) < 3:
		print('Usage: python %s infile outfile' % sys.argv[0])
		sys.exit(1)
	main(sys.argv)
