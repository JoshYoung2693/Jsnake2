import pygame, sys, time, random
from pygame.locals import *

# Initialize pygame
pygame.init()

# Make sprite objects
class Constants:
    def __init__(self):
        # Make the colors
        self.WHITE = (255,255,255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.BLACK = (0,0,0)
        
        # Make a window
        self.WINDOW_WIDTH = 620
        self.WINDOW_HEIGHT = 620
        self.window_surface = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT),0, 32)
        pygame.display.set_caption('Snake')

        # Set up direction variables
        self.DOWN = 'down'
        self.UP = 'up'
        self.LEFT = 'left'
        self.RIGHT = 'right'

        self.MOVE_SPEED = 20

        # Clock and FPS
        self.clock = pygame.time.Clock()
        self.FPS = 5

        # Snake length starts at 100 pixels, but move speed streches it out
        self.length = 100
        self.length = self.length//self.MOVE_SPEED
    
class Apple:
    def __init__(self, constants):
        constants.__init__()
        self.apple = pygame.Rect(0, 0, 20, 20)
        self.get_new_coordinates()
        colornames = ['WHITE', 'RED', 'GREEN', 'BLUE', 'BLACK']
        
    
    def get_new_coordinates(self):
        ran1 = random.randint(1, 30)
        ran1 = ran1 * 20 # Make it a multiple of 20, to be on the grid.
        ran2 = random.randint(1, 30)
        ran2 = ran2 * 20 # Same as previous

        # Redefine apple's x and y
        self.apple.x = ran1
        self.apple.y = ran2
        
        
    def draw_apple(self):
        pygame.draw.rect(constants.window_surface, constants.RED, self.apple)
        
    def make_apple(self):
        self.get_new_coordinates()
        self.draw_apple()
        
class PlayerHead:
    def __init__(self, constants):
        constants.__init__()
        self.head = pygame.Rect(20, 20, 20, 20)
        self.color = constants.GREEN
        self.dir = constants.RIGHT
    def move(self, x_list, y_list):
        if self.dir == constants.UP:
            self.head.y -= constants.MOVE_SPEED
        elif self.dir == constants.DOWN:
            self.head.y += constants.MOVE_SPEED
        elif self.dir == constants.RIGHT:
            self.head.x += constants.MOVE_SPEED
        elif self.dir == constants.LEFT:
            self.head.x -= constants.MOVE_SPEED
        x_list.append(self.head.x)
        y_list.append(self.head.y)
        return x_list, y_list
    def check_if_off_screen(self, constants):
        if (self.head.x < 0) or (self.head.y < 0) or (self.head.x > constants.WINDOW_WIDTH) or (self.head.y > constants.WINDOW_HEIGHT):
            self.die()
    def draw(self):
        pygame.draw.rect(constants.window_surface, self.color, self.head)
    def die(self):
        pygame.quit()
        sys.exit()

class PlayerTail:
    def __init__(self, constants):
        constants.__init__()
        self.tail = pygame.Rect(0, 0, 20, 20)
        self.color = constants.BLACK
    def move(self, x_list, y_list):
        if count >= constants.length:
            self.tail.x = x_list[(count-constants.length)]
            self.tail.y = y_list[(count-constants.length)]
    def draw(self):
        pygame.draw.rect(constants.window_surface, self.color, self.tail)


###### D E F I N I T I O N S ######
# Count (for list purposes)
count = 0

# Constants is a class, for easy importation
constants = Constants()

# Make the apple
apple = Apple(constants)

# Make the head and tail
head = PlayerHead(constants)
tail = PlayerTail(constants)

# Make x and y lists
x_list = []
y_list = []

# Make the initial apple
apple.make_apple()


####### M A I N  L O O P ######

dead = False
while not dead:
    # Pygame events loop
    for event in pygame.event.get():
        
        # If someone clicks on the 'x' in the top corner
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard input
        if event.type == KEYDOWN:
            # Change the direction of the head
            if event.key == K_LEFT or event.key == K_a:
                head.dir = constants.LEFT
            if event.key == K_RIGHT or event.key == K_d:
                head.dir = constants.RIGHT
            if event.key == K_UP or event.key == K_w:
                head.dir = constants.UP
            if event.key == K_DOWN or event.key == K_s:
                head.dir = constants.DOWN
            if event.key == K_p:
                constants.length += 1

    # I won't refresh the screen like everyone else
    # You will see why later.

    # Move the sprites
    head.move(x_list, y_list)
    tail.move(x_list, y_list)

    # Draw the sprites
    head.draw()
    tail.draw()
    
    # Update the display
    pygame.display.update()
    constants.clock.tick(constants.FPS)

    # Check if the snake ate the apple
    if head.head.x == apple.apple.x and head.head.y == apple.apple.y:
        constants.length += 1
        apple.make_apple()
    
    # Check if the Snake is off of the screen.
    head.check_if_off_screen(constants)
    
    # Count
    count += 1
    
