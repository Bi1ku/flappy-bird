import pygame as pg

class Pipe(pg.sprite.Sprite):
  def __init__(self, type, y_pos):
    super().__init__()
    self.image = pg.image.load('assets/pipe-green.png').convert_alpha()
    self.passed = False
    if type == "top":
      self.image = pg.transform.rotate(self.image, 180)
      self.rect = self.image.get_rect(center = (400, y_pos - 425))
    else: self.rect = self.image.get_rect(center = (400, y_pos))

  def check_passed(self, pos):
    if self.rect.right < pos and not self.passed:
      self.passed = True
      return True

  def destroy(self):
    if self.rect.right < 0:
      self.kill()

  def update(self):
    self.destroy()
    self.rect.x -= 3