"""
SPACE INVADERS ANSWER VERSION (ASSETS + SPRITES)

Steps:
  1. Import modules and define screen size
  2. Image loader + Assets class
  3. Player / Bullet / Alien sprite classes
  4. Game over screen
  5. Main game loop:
       - window, assets, sprites
       - input, spawning, updates, collisions
       - drawing and game over
"""

import pygame  # import pygame for graphics, input, and game loop
import sys     # import sys to allow a clean program exit
import random  # import random for random alien speeds and positions


# ---------- CONFIG ----------
# define WIDTH and HEIGHT as the size of the game window
WIDTH, HEIGHT = 800, 600


# ---------- ASSET LOADING ----------
def load_image(path, scale=None):
    """
    Load an image from the given path.
    Optionally scale it to (width, height) if scale is provided.
    """
    # load the image and convert it for per-pixel alpha transparency
    img = pygame.image.load(path).convert_alpha()
    # if a scale (width, height) is provided, resize the image
    if scale:
        img = pygame.transform.scale(img, scale)
    # return the prepared image surface
    return img


class Assets:
    """
    Assets class stores all loaded images so we only load them once.
    """
    def __init__(self):
        # load the player image at size 64x64 pixels
        self.player = load_image("assets/player.png", (64, 64))
        # load the laser (bullet) image at size 16x32 pixels
        self.laser = load_image("assets/laser.png", (16, 32))
        # load the alien image at size 48x48 pixels
        self.alien = load_image("assets/alien.png", (48, 48))

        # try to load the background image and scale to full screen
        try:
            self.background = load_image("assets/background.png", (WIDTH, HEIGHT))
        # if loading fails (file not found, etc.), set background to None
        except:
            self.background = None


# ---------- SPRITES ----------
class Player(pygame.sprite.Sprite):
    """
    Player sprite: controlled by the user, moves left/right, shoots bullets.
    """
    def __init__(self, assets):
        # call the parent sprite constructor
        super().__init__()
        # use the player image from the assets
        self.image = assets.player
        # get the rectangle used for positioning
        self.rect = self.image.get_rect()
        # horizontally center the player on the screen
        self.rect.centerx = WIDTH // 2
        # place the player near the bottom of the screen
        self.rect.bottom = HEIGHT - 20
        # define how many pixels to move each frame
        self.speed = 6

    def update(self, keys):
        """
        Update player position based on key presses.
        """
        # if LEFT arrow key is pressed, move left
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        # if RIGHT arrow key is pressed, move right
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # prevent the player from going past the left edge
        if self.rect.left < 0:
            self.rect.left = 0
        # prevent the player from going past the right edge
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


class Bullet(pygame.sprite.Sprite):
    """
    Bullet sprite: fired by the player, travels upward.
    """
    def __init__(self, assets, x, y):
        # call the parent sprite constructor
        super().__init__()
        # use the laser image from the assets
        self.image = assets.laser
        # get the rectangle for positioning
        self.rect = self.image.get_rect()
        # set the bullet's horizontal center to the given x
        self.rect.centerx = x
        # set the bullet's bottom position to the given y (top of player)
        self.rect.bottom = y
        # define bullet speed (negative to move upwards)
        self.speed = -10

    def update(self, *args):
        """
        Move the bullet upward and destroy it if it leaves the screen.
        """
        # move the bullet upward by speed
        self.rect.y += self.speed
        # if the bullet has moved off the top of the screen
        if self.rect.bottom < 0:
            # remove it from all sprite groups
            self.kill()


class Alien(pygame.sprite.Sprite):
    """
    Alien sprite: falls from the top of the screen toward the bottom.
    """
    def __init__(self, assets, x, y):
        # call the parent sprite constructor
        super().__init__()
        # use the alien image from the assets
        self.image = assets.alien
        # get the rectangle for positioning
        self.rect = self.image.get_rect()
        # set its starting x position
        self.rect.x = x
        # set its starting y position
        self.rect.y = y
        # choose a random downward speed between 2 and 5
        self.speed_y = random.randint(2, 5)

    def update(self, *args):
        """
        Move the alien downward and remove it if it goes off screen.
        """
        # move the alien downward by speed_y
        self.rect.y += self.speed_y
        # if the alien has moved off the bottom of the screen
        if self.rect.top > HEIGHT:
            # remove it from all sprite groups
            self.kill()


# ---------- GAME OVER ----------
def game_over_screen(screen, font, score):
    """
    Display a simple game over screen showing the final score
    and wait for any key press or window close.
    """
    # fill the entire screen with black
    screen.fill((0, 0, 0))

    # render the "GAME OVER" text in red
    over_text = font.render("GAME OVER", True, (255, 0, 0))
    # render the final score text in white
    score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
    # render an info line that tells the player how to quit
    info_text = font.render("Press any key to quit", True, (255, 255, 255))

    # place "GAME OVER" roughly slightly above the vertical center
    rect = over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
    # place "Final Score" at the center
    srect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
    # place the info text a bit below the center
    irect = info_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))

    # draw the texts onto the screen
    screen.blit(over_text, rect)
    screen.blit(score_text, srect)
    screen.blit(info_text, irect)

    # update the display to show the texts
    pygame.display.flip()

    # wait for the user to either press a key or close the window
    waiting = True
    while waiting:
        # get all events
        for event in pygame.event.get():
            # if the window close button is pressed, stop waiting
            if event.type == pygame.QUIT:
                waiting = False
            # if any key is pressed, stop waiting
            elif event.type == pygame.KEYDOWN:
                waiting = False


# ---------- MAIN ----------
def main():
    """
    Main game function: handles window creation, loop, events, updates, drawing.
    """
    # initialize pygame
    pygame.init()

    # create the game window using WIDTH and HEIGHT
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # set the title of the window to "Space Invaders"
    pygame.display.set_caption("Space Invaders")
    # create a clock object to control the frame rate
    clock = pygame.time.Clock()

    # create an Assets instance to load all images
    assets = Assets()
    # create a font with default system font and size 32
    font = pygame.font.SysFont(None, 32)

    # create the player sprite using the loaded assets
    player = Player(assets)
    # create sprite groups for organizing sprites
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()

    # add the player to the all_sprites group
    all_sprites.add(player)

    # initialize score and lives
    score = 0
    lives = 3

    # set up variables used to spawn aliens periodically
    spawn_timer = 0               # current frame count since last alien spawn
    spawn_interval = 40           # number of frames between spawns

    # flag indicating whether the game loop should keep running
    running = True
    while running:
        # ----- events -----
        # process all pending pygame events
        for event in pygame.event.get():
            # if the user clicks the window close button
            if event.type == pygame.QUIT:
                # end the game loop
                running = False
            # if a key was pressed down
            elif event.type == pygame.KEYDOWN:
                # if that key was the SPACE bar
                if event.key == pygame.K_SPACE:
                    # create a new bullet at the top-center of the player
                    bullet = Bullet(assets, player.rect.centerx, player.rect.top)
                    # add the bullet to all_sprites so it is updated and drawn
                    all_sprites.add(bullet)
                    # also add it to bullets group for collision handling
                    bullets.add(bullet)

        # get the current state of all keys (pressed / not pressed)
        keys = pygame.key.get_pressed()

        # ----- spawn aliens -----
        # increment spawn_timer each frame
        spawn_timer += 1
        # if enough frames have passed, spawn a new alien
        if spawn_timer >= spawn_interval:
            # reset spawn_timer back to 0
            spawn_timer = 0
            # choose a random x position within the screen (with margins)
            x = random.randint(50, WIDTH - 50)
            # create an alien just above the top of the screen
            alien = Alien(assets, x, -60)
            # add the alien to the all_sprites group
            all_sprites.add(alien)
            # also add to the aliens group for collision checks
            aliens.add(alien)

        # ----- update -----
        # update all sprites; player will respond to keys, others ignore them
        all_sprites.update(keys)

        # bullet vs alien collisions:
        # groupcollide returns a dict of aliens hit and bullets involved
        hits = pygame.sprite.groupcollide(aliens, bullets, True, True)
        # if hits is not empty, at least one alien was destroyed
        if hits:
            # increase score by 10 points per alien hit
            score += len(hits) * 10

        # alien vs player collisions:
        # spritecollide returns a list of aliens that collided with the player
        player_hits = pygame.sprite.spritecollide(player, aliens, True)
        # if the list is not empty, the player has been hit
        if player_hits:
            # reduce the number of lives by 1
            lives -= 1
            # if the player has no more lives, end the game
            if lives <= 0:
                running = False

        # ----- draw -----
        # if a background image is available, draw it
        if assets.background:
            screen.blit(assets.background, (0, 0))
        # otherwise, just fill the screen with black
        else:
            screen.fill((0, 0, 0))

        # draw all sprites (player, bullets, aliens) onto the screen
        all_sprites.draw(screen)

        # create a text surface showing the current score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        # create a text surface showing remaining lives
        lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
        # draw the score at the top-left corner
        screen.blit(score_text, (10, 10))
        # draw the lives text near the top-right corner
        screen.blit(lives_text, (WIDTH - 120, 10))

        # update the full display surface to the screen
        pygame.display.flip()
        # limit the frame rate to 60 frames per second
        clock.tick(60)

    # when the main loop exits, show the game over screen
    game_over_screen(screen, font, score)
    # quit pygame
    pygame.quit()
    # exit the program
    sys.exit()


# run main() only if this script is executed directly
if __name__ == "__main__":
    main()
