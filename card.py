import pygame


class Card:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

        self.value = None
        self.flipped = False
        self.matched = False

    def draw(self, screen):

        if self.matched:
            return

        if self.flipped:
            color = (220, 220, 220)             #After-Flip card color

            pygame.draw.rect(screen, color, self.rect)
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)         #Border of flipped cards

            font = pygame.font.SysFont(None, 36)

            text = font.render(str(self.value), True, (14, 33, 63))  # Text color (card number)

            text_rect = text.get_rect(center=self.rect.center)

            screen.blit(text, text_rect)

        else:
            color = (14, 33, 63)                        #Card color

            pygame.draw.rect(screen, color, self.rect)
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)         #Border of cards