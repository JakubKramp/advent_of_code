"""
--- Day 23: Opening the Turing Lock ---
Little Jane Marie just got her very first computer for Christmas from some unknown benefactor. It comes with instructions and an example program, but the computer itself seems to be malfunctioning. She's curious what the program does, and would like you to help her run it.

The manual explains that the computer supports two registers and six instructions (truly, it goes on to remind the reader, a state-of-the-art technology). The registers are named a and b, can hold any non-negative integer, and begin with a value of 0. The instructions are as follows:

hlf r sets register r to half its current value, then continues with the next instruction.
tpl r sets register r to triple its current value, then continues with the next instruction.
inc r increments register r, adding 1 to it, then continues with the next instruction.
jmp offset is a jump; it continues with the instruction offset away relative to itself.
jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
All three jump instructions work with an offset relative to that instruction. The offset is always written with a prefix + or - to indicate the direction of the jump (forward or backward, respectively). For example, jmp +1 would simply continue with the next instruction, while jmp +0 would continuously jump back to itself forever.

The program exits when it tries to run an instruction beyond the ones defined.

For example, this program sets a to 2, because the jio instruction causes it to skip the tpl instruction:

inc a
jio a, +2
tpl a
inc a
What is the value in register b when the program in your puzzle input is finished executing?
"""

from utils import load_input, print_answer

instructions = load_input().split('\n')


registers = {'a': 0, 'b': 0}


class Instruction:
    command: str = ''
    register: str = ''
    operand: int = 0

    def __init__(self, instruction):
        match instruction[:3]:
            case 'hlf' | 'tpl' | 'inc':
                self.command, self.register = instruction.split(' ')
            case 'jio' | 'jie':
                self.command = instruction[:3]
                register, operand = instruction[3:].split(',')
                self.register = register.strip()
                self.operand = int(operand)
            case 'jmp':
                self.command, operand = instruction.split(' ')
                self.operand = int(operand)

    def execute(self, ind):
        match self.command:
            case 'hlf':
                registers[self.register] = int(registers[self.register]/2)
                ind += 1
            case 'inc':
                registers[self.register] += 1
                ind += 1
            case 'tpl':
                registers[self.register] = int(registers[self.register]*3)
                ind += 1
            case 'jmp':
                ind += self.operand
            case 'jio':
                if registers[self.register] == 1:
                    ind += self.operand
                else:
                    ind += 1
            case 'jie':
                if registers[self.register]%2 == 0:
                    ind += self.operand
                else:
                    ind += 1
        return ind

    def __repr__(self):
        return f'{self.command}, {self.register}, {self.operand}'


instructions = [Instruction(i)for i in load_input().split('\n')]
ind = 0
while ind < len(instructions):
    ind = instructions[ind].execute(ind)
first_answer = registers['b']
registers = {'a': 1, 'b': 0}
ind = 0
while ind < len(instructions):
    ind = instructions[ind].execute(ind)
second_answer = registers['b']
print_answer(first_answer, second_answer)
