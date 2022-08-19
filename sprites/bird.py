from math import floor
import pygame as pg

class Bird(pg.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.frames = [pg.image.load('assets/yellowbird-upflap.png').convert_alpha(), pg.image.load('assets/yellowbird-midflap.png').convert_alpha(), pg.image.load('assets/yellowbird-downflap.png').convert_alpha()]
    self.current_frame = 0
    self.image = self.frames[self.current_frame]
    self.rect = self.image.get_rect(center = (100, 300))
    self.gravity = 0
    self.rotation = 0

  def reset(self):
    self.gravity = 0
    self.rotation = 0
    self.rect.center = (100, 300)

  def flap(self):
    self.gravity = -4

  def detect_border_collision(self):
    if self.rect.bottom <= 0 or self.rect.bottom >= 400:
      return True

  def switch_frame(self):
    self.current_frame = self.current_frame + 0.2 if self.current_frame < len(self.frames) - 1 else 0
    self.image = self.frames[floor(self.current_frame)]

  def rotate(self):
    if self.gravity < 0:
      if self.rotation < 25:
        self.rotation += 5
      else: self.rotation = 25
      self.image = pg.transform.rotate(self.image, self.rotation)
    else:
      if self.rotation > -25:
        self.rotation -= 3
      else: self.rotation = -25
      self.image = pg.transform.rotate(self.image, self.rotation)

  def update(self):
    self.detect_border_collision()
    self.switch_frame()
    self.rotate()
    self.gravity += 0.2
    self.rect.y += self.gravity