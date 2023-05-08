import pyglet

abcd_0 = 0b0111011100110110
abcd_1 = 0b0101010101000101
abcd_2 = 0b0101010101000101
abcd_3 = 0b0101011001000101
abcd_4 = 0b0101011101000101
abcd_5 = 0b0111010101000101
abcd_6 = 0b0101010101000101
abcd_7 = 0b0101011100110110

efgh_0 = 0b0111011101110101
efgh_1 = 0b0100010001010101
efgh_2 = 0b0100010001000101
efgh_3 = 0b0100010001000101
efgh_4 = 0b0110011001010101
efgh_5 = 0b0100010001010111
efgh_6 = 0b0100010001010101
efgh_7 = 0b0111010001110101

ijkl_0 = 0b0111011101010100
ijkl_1 = 0b0010000101010100
ijkl_2 = 0b0010000101010100
ijkl_3 = 0b0010000101100100
ijkl_4 = 0b0010000101010100
ijkl_5 = 0b0010000101010100
ijkl_6 = 0b0010010101010100
ijkl_7 = 0b0111011101010111

mnop_0 = 0b0101011101110111
mnop_1 = 0b0111010101010101
mnop_2 = 0b0111010101010101
mnop_3 = 0b0101010101010111
mnop_4 = 0b0101010101010100
mnop_5 = 0b0101010101010100
mnop_6 = 0b0101010101010100
mnop_7 = 0b0101010101110100

qrst_0 = 0b0111011101110111
qrst_1 = 0b0101010101010010
qrst_2 = 0b0101010101000010
qrst_3 = 0b0101011101100010
qrst_4 = 0b0101011000110010
qrst_5 = 0b0101010100010010
qrst_6 = 0b0110010101010010
qrst_7 = 0b0001010101110010

uvwx_0 = 0b0101010101010101
uvwx_1 = 0b0101010101010101
uvwx_2 = 0b0101010101010101
uvwx_3 = 0b0101010101010010
uvwx_4 = 0b0101010101010010
uvwx_5 = 0b0101010101110101
uvwx_6 = 0b0101010101110101
uvwx_7 = 0b0111001001010101

yz___0 = 0b0101011100000000
yz___1 = 0b0101000100000000
yz___2 = 0b0101000100000000
yz___3 = 0b0101001100000000
yz___4 = 0b0010011000000000
yz___5 = 0b0010010000000000
yz___6 = 0b0010010000000000
yz___7 = 0b0010011100000000

class Computer:
    def __init__(self, scale):
        self.cpu = CPU()
        self.scale = scale
        self.window = pyglet.window.Window(
            width=(32 * self.scale), height=(32 * self.scale), caption="Display")
        self.window.push_handlers(self)
        self.background_white = pyglet.image.SolidColorImagePattern(
            (255, 255, 255, 255)).create_image(self.scale, self.scale)
        self.background_black = pyglet.image.SolidColorImagePattern(
            (0, 0, 0, 255)).create_image(self.scale, self.scale)

    def load_program(self, program):
        self.cpu.load_ROM(program)

    def reset(self):
        self.__init__(self.scale)

    def run(self):
        pyglet.clock.schedule_interval(self.clock_cycle, 0.00001)
        pyglet.app.run()

    def clock_cycle(self, dt):
        self.cpu.run_cycle()
        if not (self.cpu.can_run):
            pyglet.app.exit()

    def on_draw(self):
        self.window.clear()
        self.refresh_display()
        self.cpu.run_cycle()

    def refresh_display(self):
        for r in range(32):
            row = (self.cpu.memory.ram[4032 + (2*r)] << 16
                   | self.cpu.memory.ram[4032 + 2*r + 1])
            for column in range(31, -1, -1):
                pixel = (row >> column) & 1
                if (pixel != 0):
                    self.background_white.blit(
                        self.scale * (31 - column), self.scale * (31 - r))
                else:
                    self.background_black.blit(
                        self.scale * (31 - column), self.scale * (31 - r))


class CPU:
    def __init__(self):
        self.memory = Memory()
        self.rom = ROM()
        self.counter = Counter()
        self.a = 0
        self.d = 0
        self.a_star = 0
        self.can_run = True
        
        self.memory.ram[0] = abcd_0
        self.memory.ram[1] = abcd_1
        self.memory.ram[2] = abcd_2
        self.memory.ram[3] = abcd_3
        self.memory.ram[4] = abcd_4
        self.memory.ram[5] = abcd_5
        self.memory.ram[6] = abcd_6
        self.memory.ram[7] = abcd_7

        self.memory.ram[8] = efgh_0
        self.memory.ram[9] = efgh_1
        self.memory.ram[10] = efgh_2
        self.memory.ram[11] = efgh_3
        self.memory.ram[12] = efgh_4
        self.memory.ram[13] = efgh_5
        self.memory.ram[14] = efgh_6
        self.memory.ram[15] = efgh_7

        self.memory.ram[16] = ijkl_0
        self.memory.ram[17] = ijkl_1
        self.memory.ram[18] = ijkl_2
        self.memory.ram[19] = ijkl_3
        self.memory.ram[20] = ijkl_4
        self.memory.ram[21] = ijkl_5
        self.memory.ram[22] = ijkl_6
        self.memory.ram[23] = ijkl_7

        self.memory.ram[24] = mnop_0
        self.memory.ram[25] = mnop_1
        self.memory.ram[26] = mnop_2
        self.memory.ram[27] = mnop_3
        self.memory.ram[28] = mnop_4
        self.memory.ram[29] = mnop_5
        self.memory.ram[30] = mnop_6
        self.memory.ram[31] = mnop_7

        self.memory.ram[32] = qrst_0
        self.memory.ram[33] = qrst_1
        self.memory.ram[34] = qrst_2
        self.memory.ram[35] = qrst_3
        self.memory.ram[36] = qrst_4
        self.memory.ram[37] = qrst_5
        self.memory.ram[38] = qrst_6
        self.memory.ram[39] = qrst_7

        self.memory.ram[40] = uvwx_0
        self.memory.ram[41] = uvwx_1
        self.memory.ram[42] = uvwx_2
        self.memory.ram[43] = uvwx_3
        self.memory.ram[44] = uvwx_4
        self.memory.ram[45] = uvwx_5
        self.memory.ram[46] = uvwx_6
        self.memory.ram[47] = uvwx_7

        self.memory.ram[48] = yz___0
        self.memory.ram[49] = yz___1
        self.memory.ram[50] = yz___2
        self.memory.ram[51] = yz___3
        self.memory.ram[52] = yz___4
        self.memory.ram[53] = yz___5
        self.memory.ram[54] = yz___6
        self.memory.ram[55] = yz___7
        
        self.memory.ram[56] = 0
        self.memory.ram[57] = 1
        self.memory.ram[58] = 2
        self.memory.ram[59] = 4
        self.memory.ram[60] = 8
        self.memory.ram[61] = 12
        self.memory.ram[62] = 16
        self.memory.ram[63] = 0xFFFF
        
        self.memory.ram[64] = 0     #row
        self.memory.ram[65] = 0     #col
        self.memory.ram[66] = 0     #letterset
        self.memory.ram[67] = 0     #letteroffset
        self.memory.ram[68] = 0     #reserved
        self.memory.ram[69] = 0     #reserved
        self.memory.ram[70] = 0     #line number of the function
        self.memory.ram[71] = 0     #line to return to
        
        self.memory.ram[72] = 4032  #reserved
        self.memory.ram[73] = 0     #reserved
        self.memory.ram[74] = 0     #reserved
        self.memory.ram[75] = 0     #reserved
        self.memory.ram[76] = 0     #reserved
        self.memory.ram[77] = 0     #reserved
        self.memory.ram[78] = 0     #reserved
        self.memory.ram[79] = 0     #reserved
        
        self.memory.ram[80] = 0     #reserved
        self.memory.ram[81] = 0     #reserved
        self.memory.ram[82] = 0     #reserved
        self.memory.ram[83] = 0     #reserved
        self.memory.ram[84] = 0     #reserved
        self.memory.ram[85] = 0     #reserved
        self.memory.ram[86] = 0     #reserved
        self.memory.ram[87] = 0     #reserved

    def load_ROM(self, instructions: list[int]) -> None:
        self.rom.load(instructions)

    def reset(self):
        self.__init__()

    def run_fresh(self) -> None:
        a = 0
        d = 0
        a_star = 0

        while self.counter.get() < self.rom.length:
            addr = self.counter.get()
            inst = self.rom.get(addr)
            A, D, A_STAR = self.memory.update(a, d, a_star, 0)
            R, a, d, a_star, j = Control_Unit(inst, A, D, A_STAR)
            A, D, A_STAR = self.memory.update(a, d, a_star, R)
            self.counter.update(j, A)

        if (self.counter.get() >= self.rom.length):
            self.can_run = False

    def run_cycle(self):
        addr = self.counter.get()
        inst = self.rom.get(addr)
        A, D, A_STAR = self.memory.get()
        R, self.a, self.d, self.a_star, j = Control_Unit(inst, A, D, A_STAR)
        A, D, A_STAR = self.memory.update(self.a, self.d, self.a_star, R)
        self.counter.update(j, A)

        if (self.counter.get() >= self.rom.length):
            self.can_run = False


class Memory:
    def __init__(self):
        self.register_A = 0
        self.register_D = 0
        self.ram = [0 for _ in range(4096)]

    def update(self, a: bool, d: bool, a_star: bool, X: int) -> tuple[int, int, int]:
        if a:
            self.register_A = X
        elif d:
            self.register_D = X
        elif a_star:
            self.ram[self.register_A] = X

        return (self.register_A, self.register_D, self.ram[self.register_A & 4095])

    def get(self):
        return (self.register_A, self.register_D, self.ram[self.register_A & 4095])


class ROM:
    def __init__(self):
        self.instructions = [0 for _ in range(4096)]
        self.length = 0

    def get(self, address: int) -> int:
        return self.instructions[address]

    def load(self, instructions: list[int]) -> None:
        if (self.length + len(instructions) < 4096):
            for i in range(len(instructions)):
                self.instructions[self.length + i] = instructions[i]
            self.length += i

    def clear(self) -> None:
        for i in range(4096):
            self.instructions[i] = 0
        self.length = 0


class Counter:
    def __init__(self):
        self.counter = 0

    def update(self, st: bool, X: int) -> None:
        if st:
            self.counter = X
        else:
            self.counter += 1

    def get(self) -> int:
        return self.counter


def Control_Unit(I: int, A: int, D: int, A_STAR: int) -> tuple[int, bool, bool, bool, bool]:
    d_sel = (((I >> 15) & 1) == 1)

    if d_sel:
        return ALU_Instruction(A, A_STAR, D, I)
    else:
        return (I, True, False, False, False)


def ALU_Instruction(A: int, A_STAR: int, D: int, I: int) -> tuple[int, bool, bool, bool, bool]:
    X = D
    Y = None
    gt = (((I >> 0) & 1) == 1)
    eq = (((I >> 1) & 1) == 1)
    lt = (((I >> 2) & 1) == 1)
    dest_a_star = (((I >> 3) & 1) == 1)
    dest_d = (((I >> 4) & 1) == 1)
    dest_a = (((I >> 5) & 1) == 1)
    sw = (((I >> 6) & 1) == 1)
    zx = (((I >> 7) & 1) == 1)
    zy = (((I >> 8) & 1) == 1)
    op3 = (((I >> 9) & 1) == 1)
    op2 = (((I >> 10) & 1) == 1)
    op1 = (((I >> 11) & 1) == 1)

    sel = (((I >> 12) & 1) == 1)
    if sel:
        Y = A_STAR
    else:
        Y = A
    
    shr = (((I >> 13) & 1) == 1)
    sh = (((I >> 14) & 1) == 1)

    output = ALU(X, Y, sh, shr, zx, zy, sw, op1, op2, op3)
    j = condition(output, lt, eq, gt)

    return (output, dest_a, dest_d, dest_a_star, j)


def ALU(X: int, Y: int, sh: bool, shr: bool, zx: bool, zy: bool, sw: bool, op1: bool, op2: bool, op3: bool) -> int:
    x_ = X
    y_ = Y
    output = None

    if sw:
        temp = x_
        x_ = y_
        y_ = temp

    if sh:
        if shr:
            x_ >>= y_
        else:
            x_ <<= y_
            
    if zx:
        x_ = 0

    if zy:
        y_ = 0

    if op1:
        if op2 and op3:
            output = x_ - 1
        elif op2 and (not op3):
            output = x_ - y_
        elif (not op2) and op3:
            output = x_ + 1
        elif (not op2) and (not op3):
            output = x_ + y_
    else:
        if op2 and op3:
            output = ~x_
        elif op2 and (not op3):
            output = x_ ^ y_
        elif (not op2) and op3:
            output = x_ | y_
        elif (not op2) and (not op3):
            output = x_ & y_

    return output


def condition(X: int, lt: bool, eq: bool, gt: bool) -> bool:
    output = False

    if lt:
        output = output or (X < 0)

    if eq:
        output = output or (X == 0)

    if gt:
        output = output or (X > 0)

    return output


row_0_1 = 0b0111010101110101
row_0_2 = 0b0111011101000000
row_1_1 = 0b0101010101010101
row_1_2 = 0b0100010001000000
row_2_1 = 0b0101010101000101
row_2_2 = 0b0100010001000000
row_3_1 = 0b0111010101100101
row_3_2 = 0b0100010001000000
row_4_1 = 0b0110010100110111
row_4_2 = 0b0110011001000000
row_5_1 = 0b0101010100010101
row_5_2 = 0b0100010001000000
row_6_1 = 0b0101010101010101
row_6_2 = 0b0100010001000000
row_7_1 = 0b0101011101110101
row_7_2 = 0b0111011101110000


row_10_1 = 0b0110011101110111
row_10_2 = 0b0111011100000000
row_11_1 = 0b0101010101010101
row_11_2 = 0b0101001000000000
row_12_1 = 0b0101010101000101
row_12_2 = 0b0101001000000000
row_13_1 = 0b0101010101100101
row_13_2 = 0b0111001000000000
row_14_1 = 0b0101010100110101
row_14_2 = 0b0110001000000000
row_15_1 = 0b0101011100010111
row_15_2 = 0b0101001000000000
row_16_1 = 0b0101010101010101
row_16_2 = 0b0101001000000000
row_17_1 = 0b0110010101110101
row_17_2 = 0b0101011100000000

computer = Computer(18)

computer.load_program(
    # Wait for 75 cycles
    [0 for _ in range(10)]

    # Load the first half of row 0 into A
    + [row_0_1]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 4 into A
    + [(63 << 6) + 4]

    # Set the value of RAM[4032 + 4] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the second half of row 0 into A
    + [row_0_2]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 5 into A
    + [(63 << 6) + 5]

    # Set the value of RAM[4032 + 5] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the first half of row 1 into A
    + [row_1_1]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 6 into A
    + [(63 << 6) + 6]

    # Set the value of RAM[4032 + 6] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the second half of row 1 into A
    + [row_1_2]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 7 into A
    + [(63 << 6) + 7]

    # Set the value of RAM[4032 + 7] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the first half of row 2 into A
    + [row_2_1]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 8 into A
    + [(63 << 6) + 8]

    # Set the value of RAM[4032 + 8] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the second half of row 2 into A
    + [row_2_2]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 9 into A
    + [(63 << 6) + 9]

    # Set the value of RAM[4032 + 9] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the first half of row 3 into A
    + [row_3_1]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 10 into A
    + [(63 << 6) + 10]

    # Set the value of RAM[4032 + 10] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the second half of row 3 into A
    + [row_3_2]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 11 into A
    + [(63 << 6) + 11]

    # Set the value of RAM[4032 + 11] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the first half of row 4 into A
    + [row_4_1]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 12 into A
    + [(63 << 6) + 12]

    # Set the value of RAM[4032 + 12] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the second half of row 4 into A
    + [row_4_2]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 13 into A
    + [(63 << 6) + 13]

    # Set the value of RAM[4032 + 13] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the first half of row 5 into A
    + [row_5_1]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 14 into A
    + [(63 << 6) + 14]

    # Set the value of RAM[4032 + 14] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the second half of row 5 into A
    + [row_5_2]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 15 into A
    + [(63 << 6) + 15]

    # Set the value of RAM[4032 + 15] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the first half of row 6 into A
    + [row_6_1]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 16 into A
    + [(63 << 6) + 16]

    # Set the value of RAM[4032 + 16] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the second half of row 6 into A
    + [row_6_2]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 17 into A
    + [(63 << 6) + 17]

    # Set the value of RAM[4032 + 17] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the first half of row 7 into A
    + [row_7_1]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 18 into A
    + [(63 << 6) + 18]

    # Set the value of RAM[4032 + 18] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the second half of row 7 into A
    + [row_7_2]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 19 into A
    + [(63 << 6) + 19]

    # Set the value of RAM[4032 + 19] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the first half of row 10 into A
    + [row_10_1]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 24 into A
    + [(63 << 6) + 24]

    # Set the value of RAM[4032 + 24] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the second half of row 10 into A
    + [row_10_2]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 25 into A
    + [(63 << 6) + 25]

    # Set the value of RAM[4032 + 25] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the first half of row 11 into A
    + [row_11_1]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 26 into A
    + [(63 << 6) + 26]

    # Set the value of RAM[4032 + 26] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the second half of row 11 into A
    + [row_11_2]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 27 into A
    + [(63 << 6) + 27]

    # Set the value of RAM[4032 + 27] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the first half of row 12 into A
    + [row_12_1]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 28 into A
    + [(63 << 6) + 28]

    # Set the value of RAM[4032 + 28] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the second half of row 12 into A
    + [row_12_2]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 29 into A
    + [(63 << 6) + 29]

    # Set the value of RAM[4032 + 29] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the first half of row 13 into A
    + [row_13_1]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 30 into A
    + [(63 << 6) + 30]

    # Set the value of RAM[4032 + 30] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the second half of row 13 into A
    + [row_13_2]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 31 into A
    + [(63 << 6) + 31]

    # Set the value of RAM[4032 + 31] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the first half of row 14 into A
    + [row_14_1]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 32 into A
    + [(63 << 6) + 32]

    # Set the value of RAM[4032 + 32] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the second half of row 14 into A
    + [row_14_2]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 33 into A
    + [(63 << 6) + 33]

    # Set the value of RAM[4032 + 33] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the first half of row 15 into A
    + [row_15_1]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 34 into A
    + [(63 << 6) + 34]

    # Set the value of RAM[4032 + 34] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the second half of row 15 into A
    + [row_15_2]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 35 into A
    + [(63 << 6) + 35]

    # Set the value of RAM[4032 + 35] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the first half of row 16 into A
    + [row_16_1]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 36 into A
    + [(63 << 6) + 36]

    # Set the value of RAM[4032 + 36] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the second half of row 16 into A
    + [row_16_2]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 37 into A
    + [(63 << 6) + 37]

    # Set the value of RAM[4032 + 37] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the first half of row 17 into A
    + [row_17_1]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 38 into A
    + [(63 << 6) + 38]

    # Set the value of RAM[4032 + 38] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Load the second half of row 17 into A
    + [row_17_2]

    # D = 0 + A
    + [(1 << 15) | (1 << 11) | (1 << 4) | (1 << 7)]

    # Load 4032 + 39 into A
    + [(63 << 6) + 39]

    # Set the value of RAM[4032 + 39] to D
    + [(1 << 15) | (1 << 3) | (1 << 11) | (1 << 8)]

    # Wait for 150 cycles
    + [0 for _ in range(40)]

    # Load 4032 + 4 into A
    + [(63 << 6) + 4]

    # Set the value of RAM[4032 + 4] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 5 into A
    + [(63 << 6) + 5]

    # Set the value of RAM[4032 + 5] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 6 into A
    + [(63 << 6) + 6]

    # Set the value of RAM[4032 + 6] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 7 into A
    + [(63 << 6) + 7]

    # Set the value of RAM[4032 + 7] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 8 into A
    + [(63 << 6) + 8]

    # Set the value of RAM[4032 + 8] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 9 into A
    + [(63 << 6) + 9]

    # Set the value of RAM[4032 + 9] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 10 into A
    + [(63 << 6) + 10]

    # Set the value of RAM[4032 + 10] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 11 into A
    + [(63 << 6) + 11]

    # Set the value of RAM[4032 + 11] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 12 into A
    + [(63 << 6) + 12]

    # Set the value of RAM[4032 + 12] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 13 into A
    + [(63 << 6) + 13]

    # Set the value of RAM[4032 + 13] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 14 into A
    + [(63 << 6) + 14]

    # Set the value of RAM[4032 + 14] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 15 into A
    + [(63 << 6) + 15]

    # Set the value of RAM[4032 + 15] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 16 into A
    + [(63 << 6) + 16]

    # Set the value of RAM[4032 + 16] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 17 into A
    + [(63 << 6) + 17]

    # Set the value of RAM[4032 + 17] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 18 into A
    + [(63 << 6) + 18]

    # Set the value of RAM[4032 + 18] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 19 into A
    + [(63 << 6) + 19]

    # Set the value of RAM[4032 + 19] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 24 into A
    + [(63 << 6) + 24]

    # Set the value of RAM[4032 + 24] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 25 into A
    + [(63 << 6) + 25]

    # Set the value of RAM[4032 + 25] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 26 into A
    + [(63 << 6) + 26]

    # Set the value of RAM[4032 + 26] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 27 into A
    + [(63 << 6) + 27]

    # Set the value of RAM[4032 + 27] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 28 into A
    + [(63 << 6) + 28]

    # Set the value of RAM[4032 + 28] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 29 into A
    + [(63 << 6) + 29]

    # Set the value of RAM[4032 + 29] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 30 into A
    + [(63 << 6) + 30]

    # Set the value of RAM[4032 + 30] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 31 into A
    + [(63 << 6) + 31]

    # Set the value of RAM[4032 + 31] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 32 into A
    + [(63 << 6) + 32]

    # Set the value of RAM[4032 + 32] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 33 into A
    + [(63 << 6) + 33]

    # Set the value of RAM[4032 + 33] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 34 into A
    + [(63 << 6) + 34]

    # Set the value of RAM[4032 + 34] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 35 into A
    + [(63 << 6) + 35]

    # Set the value of RAM[4032 + 35] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 36 into A
    + [(63 << 6) + 36]

    # Set the value of RAM[4032 + 36] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 37 into A
    + [(63 << 6) + 37]

    # Set the value of RAM[4032 + 37] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 38 into A
    + [(63 << 6) + 38]

    # Set the value of RAM[4032 + 38] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Load 4032 + 39 into A
    + [(63 << 6) + 39]

    # Set the value of RAM[4032 + 39] to 0
    + [(1 << 15) | (1 << 3) | (1 << 7) | (1 << 8)]

    # Wait for 75 cycles
    + [0 for _ in range(20)]
)
computer.run()
