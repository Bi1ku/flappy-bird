from random import randint
import pygame as pg
from sprites.bird import Bird
from sprites.pipe import Pipe

def main():
  pg.init()

  game_active = False

  screen = pg.display.set_mode((285, 500))
  clock = pg.time.Clock()

  # Load assets
  # Starting Image
  start_image = pg.transform.scale(pg.image.load('assets/message.png').convert_alpha(), (220, 330))
  start_image_rect = start_image.get_rect(center = (142.5, 200))

  # Background & Base
  bg = pg.image.load('assets/background-day.png').convert()
  base = pg.image.load('assets/base.png').convert_alpha()
  base_rect = base.get_rect(topleft = (0, 400))

  # Create another base for animation
  base_2 = pg.image.load('assets/base.png').convert_alpha()
  base_2_rect = base_2.get_rect(topleft = (base_rect.right, 400))

  # Bird Sprite
  bird = pg.sprite.GroupSingle(Bird())

  # Pipe Sprite & Time Loop
  pipes = pg.sprite.Group()
  pipe_timer = pg.USEREVENT + 1
  pg.time.set_timer(pipe_timer, 1000)

  # Game Loop
  while 1:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        quit()

      if game_active:
        if event.type == pipe_timer:
          y_pos = randint(300, 475)
          pipes.add(Pipe("top", y_pos))
          pipes.add(Pipe("bottom", y_pos))

        if event.type == pg.MOUSEBUTTONDOWN:
          bird.sprite.flap()
      
      else:
        if event.type == pg.MOUSEBUTTONDOWN and not game_active:
          game_active = True

    screen.blit(bg, (0, 0))

    if game_active:
      pipes.draw(screen)
      bird.draw(screen)

      if pg.sprite.spritecollide(bird.sprite, pipes, False) or bird.sprite.detect_border_collision():
        pipes.empty()
        bird.sprite.reset()
        base_rect.topleft = (0, 400)
        base_2_rect.topleft = (base_rect.right, 400)
        game_active = False

      bird.update()
      pipes.update()
    else:
      screen.blit(start_image, start_image_rect)

    screen.blit(base, base_rect)
    screen.blit(base_2, base_2_rect)

    base_rect.x -= 3
    base_2_rect.x -= 3

    print(base_rect.right, base_2_rect.right)

    if base_rect.right < 0:
      base_rect.left = base_2_rect.right

    if base_2_rect.right < 0:
      base_2_rect.left = base_rect.right

    pg.display.update()
    clock.tick(60)

if __name__ == "__main__":
  main()