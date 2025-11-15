"""
SPACE INVADERS QUESTION VERSION (ASSETS + SPRITES)

Student task:
Use these remarks to write the full game.

Steps:
  1. Import modules and define screen size
  2. Write image loader and Assets class
  3. Write Player, Bullet, and Alien sprite classes
  4. Write game_over_screen function
  5. Write main() game loop:
       - create window
       - create assets and sprites
       - handle input
       - spawn aliens
       - update sprites
       - check collisions
       - draw everything
       - show game over
"""

# import the pygame module
# import the sys module
# import the random module

# ---------- CONFIG ----------
# define constants WIDTH and HEIGHT for the screen size (e.g. 800, 600)


# ---------- ASSET LOADING ----------
# define a function load_image(path, scale=None):
#     load an image from the given path with pygame
#     convert the image to include alpha transparency
#     if a scale (width, height) is provided:
#         scale the image to that size
#     return the final image

# define a class Assets:
#     in __init__(self):
#         load the player image from "assets/player.png" with size (64, 64)
#         load the laser image from "assets/laser.png" with size (16, 32)
#         load the alien image from "assets/alien.png" with size (48, 48)
#         try to load the background image from "assets/background.png"
#             with size (WIDTH, HEIGHT)
#         if loading background fails:
#             set background to None


# ---------- SPRITES ----------
# define a class Player that inherits from pygame.sprite.Sprite:
#     in __init__(self, assets):
#         call the parent class constructor
#         set self.image to the player image from assets
#         get the rect of the image and assign to self.rect
#         set rect.centerx to half of WIDTH
#         set rect.bottom to slightly above the bottom of the screen
#         define a speed value for horizontal movement

#     define update(self, keys):
#         if LEFT key is pressed:
#             move rect.x left by speed
#         if RIGHT key is pressed:
#             move rect.x right by speed
#         if the player goes past the left edge:
#             clamp rect.left to 0
#         if the player goes past the right edge:
#             clamp rect.right to WIDTH


# define a class Bullet that inherits from pygame.sprite.Sprite:
#     in __init__(self, assets, x, y):
#         call the parent class constructor
#         set self.image to the laser image from assets
#         get the rect and assign to self.rect
#         set rect.centerx to x
#         set rect.bottom to y
#         set a negative speed value so bullet moves upward

#     define update(self, *args):
#         move rect.y by the speed
#         if rect.bottom is less than 0 (off the top of screen):
#             remove the bullet (self.kill())


# define a class Alien that inherits from pygame.sprite.Sprite:
#     in __init__(self, assets, x, y):
#         call the parent class constructor
#         set self.image to the alien image from assets
#         get the rect and assign to self.rect
#         set rect.x to the given x
#         set rect.y to the given y
#         choose a random downward speed between 2 and 5 and store in speed_y

#     define update(self, *args):
#         move rect.y downward by speed_y
#         if rect.top is greater than HEIGHT (off bottom of screen):
#             remove the alien (self.kill())


# ---------- GAME OVER ----------
# define a function game_over_screen(screen, font, score):
#     fill the screen with black
#     create a "GAME OVER" text surface in red using the given font
#     create a "Final Score: <score>" text surface in white
#     create an instruction text "Press any key to quit" in white
#
#     get centered rect positions for each text surface
#         (GAME OVER slightly above center,
#          score at center,
#          instructions below center)
#
#     draw (blit) all three text surfaces on the screen
#     update the display
#
#     set waiting = True
#     while waiting:
#         get events from pygame
#         if event is QUIT:
#             set waiting to False
#         if event is KEYDOWN:
#             set waiting to False


# ---------- MAIN ----------
# define a main() function:
#     initialize pygame
#     create a window with WIDTH and HEIGHT
#     set the window caption to "Space Invaders"
#     create a clock for FPS control
#
#     create an Assets instance
#     create a font using pygame.font.SysFont with size 32
#
#     create a Player instance using assets
#
#     create sprite groups:
#         all_sprites = Group()
#         bullets = Group()
#         aliens = Group()
#
#     add the player to all_sprites
#
#     initialize score to 0
#     initialize lives to 3
#
#     set spawn_timer = 0
#     set spawn_interval to some number of frames (e.g. 40)
#
#     set running = True
#     while running:
#         # handle events
#         for each event in pygame.event.get():
#             if event type is QUIT:
#                 set running to False
#             if event type is KEYDOWN:
#                 if key is SPACE:
#                     create a Bullet using assets and player's position
#                     add the bullet to all_sprites
#                     add the bullet to bullets group
#
#         get the current pressed keys using pygame.key.get_pressed()
#
#         # spawn aliens
#         increase spawn_timer by 1
#         if spawn_timer is greater or equal to spawn_interval:
#             reset spawn_timer to 0
#             choose a random x between some margin and WIDTH - margin
#             create an Alien using assets and this x, with a starting y above screen
#             add the alien to all_sprites
#             add the alien to aliens group
#
#         # update all sprites
#         call all_sprites.update(keys)
#
#         # collision: bullets vs aliens
#         call pygame.sprite.groupcollide(aliens, bullets, True, True)
#         if there are hits:
#             increase score by 10 times number of hits
#
#         # collision: aliens vs player
#         call pygame.sprite.spritecollide(player, aliens, True)
#         if player was hit:
#             decrease lives by 1
#             if lives is less or equal to 0:
#                 set running to False
#
#         # draw everything
#         if assets.background is not None:
#             draw (blit) the background at (0, 0)
#         else:
#             fill the screen with black
#
#         draw all_sprites to the screen
#
#         create score_text from font: "Score: <score>"
#         create lives_text from font: "Lives: <lives>"
#         draw score_text at top-left
#         draw lives_text near the top-right
#
#         update the display (pygame.display.flip())
#         limit FPS with clock.tick(60)
#
#     # after the loop finishes:
#     call game_over_screen(screen, font, score)
#     quit pygame
#     exit the program using sys.exit()
#
# if this module is run as the main program:
#     call main()
