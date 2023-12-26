import pyglet

abcd_0 = 0b0111011100110110
abcd_1 = 0b0101010101000101
abcd_2 = 0b0101010101000101
abcd_3 = 0b0101011001000101
abcd_4 = 0b0111010101000101
abcd_5 = 0b0101010101000101
abcd_6 = 0b0101011100110110
abcd_7 = 0b0000000000000000

efgh_0 = 0b0111011101110101
efgh_1 = 0b0100010001010101
efgh_2 = 0b0100010001000101
efgh_3 = 0b0110011001010111
efgh_4 = 0b0100010001010101
efgh_5 = 0b0100010001010101
efgh_6 = 0b0111010001110101
efgh_7 = 0b0000000000000000

ijkl_0 = 0b0111011101010100
ijkl_1 = 0b0010000101010100
ijkl_2 = 0b0010000101010100
ijkl_3 = 0b0010000101100100
ijkl_4 = 0b0010000101010100
ijkl_5 = 0b0010010101010100
ijkl_6 = 0b0111011101010111
ijkl_7 = 0b0000000000000000

mnop_0 = 0b0101011101110111
mnop_1 = 0b0111010101010101
mnop_2 = 0b0111010101010101
mnop_3 = 0b0101010101010111
mnop_4 = 0b0101010101010100
mnop_5 = 0b0101010101010100
mnop_6 = 0b0101010101110100
mnop_7 = 0b0000000000000000

qrst_0 = 0b0111011101110111
qrst_1 = 0b0101010101010010
qrst_2 = 0b0101010101000010
qrst_3 = 0b0101011001110010
qrst_4 = 0b0101010100010010
qrst_5 = 0b0110010101010010
qrst_6 = 0b0001010101110010
qrst_7 = 0b0000000000000000

uvwx_0 = 0b0101010101010101
uvwx_1 = 0b0101010101010101
uvwx_2 = 0b0101010101010101
uvwx_3 = 0b0101010101010010
uvwx_4 = 0b0101010101110101
uvwx_5 = 0b0101010101110101
uvwx_6 = 0b0111001001010101
uvwx_7 = 0b0000000000000000

yz___0 = 0b0101011100000000
yz___1 = 0b0101000100000000
yz___2 = 0b0101000100000000
yz___3 = 0b0111001000000000
yz___4 = 0b0010010000000000
yz___5 = 0b0010010000000000
yz___6 = 0b0010011100000000
yz___7 = 0b0000000000000000

class Computer:
    def __init__(self, scale, screen_size):
        self.cpu = CPU()
        self.scale = scale
        self.screen_size = screen_size
        self.window = pyglet.window.Window(
            width=(self.screen_size * self.scale), height=(self.screen_size * self.scale), caption="Display", config = pyglet.gl.Config(double_buffer=False))
        self.window.push_handlers(self)
        self.background_white = pyglet.image.SolidColorImagePattern(
            (255, 255, 255, 255)).create_image(self.scale, self.scale)
        self.background_black = pyglet.image.SolidColorImagePattern(
            (0, 0, 0, 255)).create_image(self.scale, self.scale)

    def load_program(self, program):
        self.cpu.load_ROM(program)

    def reset(self):
        self.__init__(self.scale, self.screen_size)

    def run(self):
        pyglet.clock.schedule(self.clock_cycle)
        pyglet.app.run()

    def clock_cycle(self, dt):
        self.cpu.check_screen_refresh()
        if (self.cpu.can_run):
            self.cpu.run_cycle()

    def on_draw(self):
        if(self.cpu.refresh_screen):
            self.window.clear()
            self.refresh_display()
            self.cpu.refresh_screen = False
    
    def on_mouse_press(self, x, y, button, modifiers):
        if(button == pyglet.window.mouse.LEFT):
            self.cpu.memory.ram[59] = 1
        elif(button == pyglet.window.mouse.MIDDLE):
            self.cpu.memory.ram[60] = 1
        elif(button == pyglet.window.mouse.RIGHT):
            self.cpu.memory.ram[61] = 1
    
    def on_mouse_release(self, x, y, button, modifiers):
        if(button == pyglet.window.mouse.LEFT):
            self.cpu.memory.ram[59] = 0
        elif(button == pyglet.window.mouse.MIDDLE):
            self.cpu.memory.ram[60] = 0
        elif(button == pyglet.window.mouse.RIGHT):
            self.cpu.memory.ram[61] = 0
    
    def on_mouse_motion(self, x, y, dx, dy):
        screen_x = x // self.scale
        screen_y = (self.scale * self.screen_size - y) // self.scale
        self.cpu.memory.ram[63] = screen_y
        self.cpu.memory.ram[62] = screen_x

    def on_key_press(self, symbol, modifiers):
        if(symbol == pyglet.window.key.ESCAPE):
            pyglet.app.exit()
        elif(symbol == pyglet.window.key.LSHIFT or symbol == pyglet.window.key.RSHIFT):
            self.cpu.memory.ram[68] = 1 << 0
        elif(symbol == pyglet.window.key.ENTER):
            self.cpu.memory.ram[68] = 1 << 1
        elif(symbol == pyglet.window.key.A):
            self.cpu.memory.ram[68] = 1 << 2
        elif(symbol == pyglet.window.key.B):
            self.cpu.memory.ram[68] = 2 << 2
        elif(symbol == pyglet.window.key.C):
            self.cpu.memory.ram[68] = 3 << 2
        elif(symbol == pyglet.window.key.D):
            self.cpu.memory.ram[68] = 4 << 2
        elif(symbol == pyglet.window.key.E):
            self.cpu.memory.ram[68] = 5 << 2
        elif(symbol == pyglet.window.key.F):
            self.cpu.memory.ram[68] = 6 << 2
        elif(symbol == pyglet.window.key.G):
            self.cpu.memory.ram[68] = 7 << 2
        elif(symbol == pyglet.window.key.H):
            self.cpu.memory.ram[68] = 8 << 2
        elif(symbol == pyglet.window.key.I):
            self.cpu.memory.ram[68] = 9 << 2
        elif(symbol == pyglet.window.key.J):
            self.cpu.memory.ram[68] = 10 << 2
        elif(symbol == pyglet.window.key.K):
            self.cpu.memory.ram[68] = 11 << 2
        elif(symbol == pyglet.window.key.L):
            self.cpu.memory.ram[68] = 12 << 2
        elif(symbol == pyglet.window.key.M):
            self.cpu.memory.ram[68] = 13 << 2
        elif(symbol == pyglet.window.key.N):
            self.cpu.memory.ram[68] = 14 << 2
        elif(symbol == pyglet.window.key.O):
            self.cpu.memory.ram[68] = 15 << 2
        elif(symbol == pyglet.window.key.P):
            self.cpu.memory.ram[68] = 16 << 2
        elif(symbol == pyglet.window.key.Q):
            self.cpu.memory.ram[68] = 17 << 2
        elif(symbol == pyglet.window.key.R):
            self.cpu.memory.ram[68] = 18 << 2
        elif(symbol == pyglet.window.key.S):
            self.cpu.memory.ram[68] = 19 << 2
        elif(symbol == pyglet.window.key.T):
            self.cpu.memory.ram[68] = 20 << 2
        elif(symbol == pyglet.window.key.U):
            self.cpu.memory.ram[68] = 21 << 2
        elif(symbol == pyglet.window.key.V):
            self.cpu.memory.ram[68] = 22 << 2
        elif(symbol == pyglet.window.key.W):
            self.cpu.memory.ram[68] = 23 << 2
        elif(symbol == pyglet.window.key.X):
            self.cpu.memory.ram[68] = 24 << 2
        elif(symbol == pyglet.window.key.Y):
            self.cpu.memory.ram[68] = 25 << 2
        elif(symbol == pyglet.window.key.Z):
            self.cpu.memory.ram[68] = 26 << 2
        elif(symbol == pyglet.window.key.SPACE):
            self.cpu.memory.ram[68] = 27 << 2
    
    # def on_key_release(self, symbol, modifiers):
    #     self.cpu.memory.ram[68] = 0

    def refresh_display(self):
        for r in range(self.screen_size):
            row = (self.cpu.memory.ram[self.cpu.memory.ram[72] + (4*r)] << (16 * 3)
                   | self.cpu.memory.ram[self.cpu.memory.ram[72] + 4*r + 1] << (16 * 2)
                   | self.cpu.memory.ram[self.cpu.memory.ram[72] + 4*r + 2] << (16 * 1)
                   | self.cpu.memory.ram[self.cpu.memory.ram[72] + 4*r + 3] << (16 * 0))
            for column in range((self.screen_size - 1), -1, -1):
                pixel = (row >> column) & 1
                if (pixel != 0):
                    self.background_white.blit(
                        self.scale * ((self.screen_size - 1) - column), self.scale * ((self.screen_size - 1) - r))
                else:
                    self.background_black.blit(
                        self.scale * ((self.screen_size - 1) - column), self.scale * ((self.screen_size - 1) - r))


class CPU:
    def __init__(self):
        self.memory = Memory()
        self.rom = ROM()
        self.counter = Counter()
        self.a = 0
        self.d = 0
        self.a_star = 0
        self.can_run = True
        self.refresh_screen = False
        
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
        self.memory.ram[57] = 0xFFFF
        self.memory.ram[58] = 0
        self.memory.ram[59] = 0     #mouse left down
        self.memory.ram[60] = 0     #mouse middle down
        self.memory.ram[61] = 0     #mouse right down
        self.memory.ram[62] = 0     #mouse row
        self.memory.ram[63] = 0     #mouse col
        
        self.memory.ram[64] = 0     #row
        self.memory.ram[65] = 0     #col
        self.memory.ram[66] = 0     #letterset
        self.memory.ram[67] = 0     #letteroffset
        self.memory.ram[68] = 0     #keyboard symbol
        self.memory.ram[69] = 113   #line number of the disp function
        self.memory.ram[70] = 0     #line number of the print function
        self.memory.ram[71] = 0     #line to return to
        
        self.memory.ram[72] = 3840  #screen start location
        self.memory.ram[73] = 1     #draw screen flag
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

        self.memory.ram[88] = 0     #reserved
        self.memory.ram[89] = 0     #reserved
        self.memory.ram[90] = 0     #reserved
        self.memory.ram[91] = 0     #reserved
        self.memory.ram[92] = 0     #reserved
        self.memory.ram[93] = 0     #reserved
        self.memory.ram[94] = 0     #reserved
        self.memory.ram[95] = 0     #reserved

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

    def check_screen_refresh(self):
        if(self.memory.ram[73] != 0):
            self.memory.ram[73] = 0
            self.refresh_screen = True
    
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
        if d:
            self.register_D = X
        if a_star:
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
            self.length += len(instructions)

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
    x_ = X if not(sw) else Y
    y_ = Y if not(sw) else X
    output = None

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


computer = Computer(12, 64)
computer.load_program([59]
+ [39056]
+ [77]
+ [35080]
+ [61]
+ [37392]
+ [0]
+ [32770]
+ [62]
+ [39056]
+ [2]
+ [49168]
+ [75]
+ [35080]
+ [63]
+ [39056]
+ [76]
+ [35080]
+ [4]
+ [57424]
+ [75]
+ [38928]
+ [72]
+ [38928]
+ [75]
+ [35080]
+ [76]
+ [39056]
+ [15]
+ [32784]
+ [1]
+ [49232]
+ [76]
+ [35080]
+ [77]
+ [39056]
+ [44]
+ [32770]
+ [76]
+ [39056]
+ [75]
+ [37384]
+ [0]
+ [32775]
+ [76]
+ [38480]
+ [75]
+ [36872]
+ [0]
+ [32775])
"""
computer.load_program(
   [64]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [5]
 + [(1 << 15) | (1 << 14) | (1 << 11) | (1 << 8) | (1 << 4)]
 + [75]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [65]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [2]
 + [(1 << 15) | (1 << 14) | (1 << 13) | (1 << 11) | (1 << 8) | (1 << 4)]
 + [75]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 4)]
 + [72]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 4)]
 + [75]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [65]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [3]
 + [(1 << 15) | (1 << 4)]
 + [2]
 + [(1 << 15) | (1 << 14) | (1 << 11) | (1 << 8) | (1 << 4)]
 + [12]
 + [(1 << 15) | (1 << 11) | (1 << 10) | (1 << 6) | (1 << 4)]
 + [76]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [66]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [3]
 + [(1 << 15) | (1 << 14) | (1 << 11) | (1 << 8) | (1 << 4)]
 + [77]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [8]
 + [(1 << 15) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [78]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 3)]
 + [70]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [42]
 + [(1 << 15) | (1 << 11) | (1 << 4)]
 + [79]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [78]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [8]
 + [(1 << 15) | (1 << 11) | (1 << 10) | (1 << 6) | (1 << 4)]
 + [80]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [77]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5)]
 + [(1 << 15) | (1 << 11) | (1 << 5)]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [81]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [67]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [3]
 + [(1 << 15) | (1 << 11) | (1 << 10) | (1 << 6) | (1 << 4)]
 + [2]
 + [(1 << 15) | (1 << 14) | (1 << 11) | (1 << 8) | (1 << 4)]
 + [82]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [81]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [82]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5)]
 + [(1 << 15) | (1 << 14) | (1 << 13) | (1 << 11) | (1 << 8) | (1 << 4)]
 + [15]
 + [(1 << 15) | (1 << 4)]
 + [76]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5)]
 + [(1 << 15) | (1 << 14) | (1 << 11) | (1 << 8) | (1 << 4)]
 + [83]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [75]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [80]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5)]
 + [(1 << 15) | (1 << 11) | (1 << 5)]
 + [84]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [15]
 + [(1 << 15) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [76]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5)]
 + [(1 << 15) | (1 << 14) | (1 << 11) | (1 << 8) | (1 << 4)]
 + [(1 << 15) | (1 << 10) | (1 << 9) | (1 << 8) | (1 << 4)]
 + [84]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5)]
 + [(1 << 15) | (1 << 12) | (1 << 3)]
 + [83]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [84]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5)]
 + [(1 << 15) | (1 << 12) | (1 << 9) | (1 << 3)]
 + [4]
 + [(1 << 15) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [75]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5)]
 + [(1 << 15) | (1 << 11) | (1 << 4)]
 + [75]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [78]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 10) | (1 << 9) | (1 << 6) | (1 << 3)]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [79]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5)]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 0)]
 + [73]
 + [(1 << 15) | (1 << 11) | (1 << 9) | (1 << 7) | (1 << 3)]
 + [71]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5)]
 + [(1 << 15) | (1 << 2) | (1 << 1) | (1 << 0)]
 
 )
computer.load_program(
   [68]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [95]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [68]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 7) | (1 << 3)]
 + [95]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [69]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5)]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 2) | (1 << 1)]
 + [95]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]                  
 + [1]
 + [(1 << 15) | (1 << 4)]
 + [88]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [69]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [67]                                                          
 + [(1 << 15) | (1 << 11) | (1 << 4)]
 + [91]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [88]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [91]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5)]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 0)]
 + [95]                                                           
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [2]
 + [(1 << 15) | (1 << 4)]
 + [89]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [69]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [78]                                                          
 + [(1 << 15) | (1 << 11) | (1 << 4)]
 + [92]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [89]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [92]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5)]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 0)]
 + [95]                                                           
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [2]
 + [(1 << 15) | (1 << 14) | (1 << 13) | (1 << 11) | (1 << 10) | (1 << 9) | (1 << 4)]
 + [90]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [2]
 + [(1 << 15) | (1 << 14) | (1 << 13) | (1 << 11) | (1 << 8) | (1 << 4)]
 + [66]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [90]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [3]
 + [(1 << 15) | (1 << 4)]
 + [67]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [69]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [71]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 + [70]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5) | (1 << 2) | (1 << 1) | (1 << 0)]
 + [65]                                                           
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [15]
 + [(1 << 15) | (1 << 11) | (1 << 10) | (1 << 6) | (1 << 4)]
 + [69]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5)]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 2) | (1 << 1)]
 + [65]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 9) | (1 << 8) | (1 << 6) | (1 << 3)] 
 + [69]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5) | (1 << 2) | (1 << 1) | (1 << 0)]
 + [64]                                                         
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 4)]
 + [7]
 + [(1 << 15) | (1 << 11) | (1 << 10) | (1 << 6) | (1 << 4)]
 + [69]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5)]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 2) | (1 << 1)]
 + [64]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 9) | (1 << 8) | (1 << 6) | (1 << 3)] 
 + [65]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 7) | (1 << 3)]
 + [69]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5) | (1 << 2) | (1 << 1) | (1 << 0)]
)
"""

computer.cpu.rom.length = 300
computer.cpu.counter.counter = 300

'''
computer.load_program(
   [3]                                              # row
 + [(1 << 15) | (1 << 11) | (1 << 7) | (1 << 4)]    # D = A
 + [64]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 
 + [5]                                              # col   
 + [(1 << 15) | (1 << 11) | (1 << 7) | (1 << 4)]    # D = A
 + [65]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 
 + [4]                                              # letterset
 + [(1 << 15) | (1 << 11) | (1 << 7) | (1 << 4)]    # D = A
 + [66]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 
 + [1]                                              # letteroffset
 + [(1 << 15) | (1 << 11) | (1 << 7) | (1 << 4)]    # D = A
 + [67]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 
 + [324]                                            # return address
 + [(1 << 15) | (1 << 11) | (1 << 7) | (1 << 4)]    # D = A
 + [71]
 + [(1 << 15) | (1 << 11) | (1 << 8) | (1 << 3)]
 
 + [70]
 + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5)]
 + [(1 << 15) | (1 << 2) | (1 << 1) | (1 << 0)]
 
 + [0 for _ in range(100)]
)
computer.run()
'''


computer.load_program(
    [69]
  + [(1 << 15) | (1 << 12) | (1 << 11) | (1 << 7) | (1 << 5) | (0b111)]
)
computer.run()
