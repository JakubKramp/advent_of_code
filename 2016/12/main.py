"""
--- Day 12: Leonardo's Monorail ---
You finally reach the top floor of this building: a garden with a slanted glass ceiling. Looks like there are no more stars to be had.

While sitting on a nearby bench amidst some tiger lilies, you manage to decrypt some of the files you extracted from the servers downstairs.

According to these documents, Easter Bunny HQ isn't just this building - it's a collection of buildings in the nearby area. They're all connected by a local monorail, and there's another building not far from here! Unfortunately, being night, the monorail is currently not operating.

You remotely connect to the monorail control systems and discover that the boot sequence expects a password. The password-checking logic (your puzzle input) is easy to extract, but the code it uses is strange: it's assembunny code designed for the new computer you just assembled. You'll have to execute the code and get the password.

The assembunny code you've extracted operates on four registers (a, b, c, and d) that start at 0 and can hold any integer. However, it seems to make use of only a few instructions:

cpy x y copies x (either an integer or the value of a register) into register y.
inc x increases the value of register x by one.
dec x decreases the value of register x by one.
jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.
The jnz instruction moves relative to itself: an offset of -1 would continue at the previous instruction, while an offset of 2 would skip over the next instruction.

For example:

cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
The above code would set register a to 41, increase its value by 2, decrease its value by 1, and then skip the last dec a (because a is not zero, so the jnz a 2 skips it), leaving register a at 42. When you move past the last instruction, the program halts.

After executing the assembunny code in your puzzle input, what value is left in register a?
"""
from utils import load_input, print_answer

class Registry(object):

    def __init__(self, instructions):
        self.current_instruction = ''
        self.index = 0
        self.instructions = instructions
        self.registry = {}


    def increase(self, register: str) -> None:
        """
        Increases value of a given register by 1.
        :param register: Register that the value should be increased
        :return: None
        """
        if register not in self.registry:
            self.index += 1
            return
        self.registry[register] += 1
        self.index += 1


    def decrease(self, register: str) -> None:
        """
        Decreases value of a given register by 1.
        :param register: Register that the value should be decreased
        :return: None
        """
        if register not in self.registry:
            self.index += 1
            return
        self.registry[register] -= 1
        self.index += 1

    def copy(self, register: str, value: str) -> None:
        """
        Copies a given value to given registry
        :param register: Target
        :param value: value or registry name
        :return:
        """
        if value.isdigit():
            self.registry[register] = int(value)
        elif self.registry.get(value, 0) !=0:
            self.registry[register] = self.registry[value]
        self.index += 1

    def jump(self, register: str, value: int) -> None:
        """
        If the value of a given register is  positive jump by a given number of instructions
        :param register: Register to be checked
        :return: None
        """
        if (register.isdigit() and int(register)) or (self.registry.get(register, 0) != 0):
            self.index += int(value)
            if self.index < 0:
                self.index = 0
            return
        self.index += 1

    def evaluate(self, instruction: str) -> None:
        """
        Evaluates instruction, calling functions accordingly
        :param instruction:
        :return: None
        """
        functions = {"inc": self.increase,
                "dec": self.decrease,
                "cpy": self.copy,
                "jnz": self.jump}
        instruction = instruction.split(' ')
        match len(instruction):
            case 2:
                functions[instruction[0]](instruction[1])
            case 3:
                if instruction[0] == 'jnz':
                    functions[instruction[0]](instruction[1], instruction[2])
                elif instruction[0] == 'cpy':
                    functions[instruction[0]](instruction[2], instruction[1])


    def process(self):
        """
        Processes given instructions
        :return:
        """
        while self.index < len(self.instructions):
            self.current_instruction = self.instructions[self.index]
            self.evaluate(self.current_instruction)

r1 = Registry(load_input().split('\n'))
r1.process()
part_one = r1.registry['a']
r2 = Registry(load_input().split('\n'))
r2.registry = {'c': 1}
r2.process()
part_two = r2.registry['a']
print_answer(part_one, part_two)