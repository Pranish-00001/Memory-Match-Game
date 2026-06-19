import pygame


class Menu:

    def __init__(self):

        self.open = False

        # Menu icon (☰)
        self.menu_rect = pygame.Rect(10, 10, 40, 40)

        # Dropdown buttons
        self.restart_rect = pygame.Rect(10, 55, 140, 40)

        self.quit_rect = pygame.Rect(10, 100, 140, 40)

        self.font = pygame.font.SysFont(None, 30)

    def draw(self, screen):

        # Menu icon background
        pygame.draw.rect(screen, (80, 80, 80), self.menu_rect)

        # Hamburger lines
        pygame.draw.line(screen, (255, 255, 255), (18, 20), (42, 20), 3)
        pygame.draw.line(screen, (255, 255, 255), (18, 30), (42, 30), 3)
        pygame.draw.line(screen, (255, 255, 255), (18, 40), (42, 40), 3)

        # Dropdown
        if self.open:

            pygame.draw.rect(
                screen,
                (209, 209, 0),
                self.restart_rect
            )

            pygame.draw.rect(               #Border for restart button
                screen,
                (0, 0, 0),
                self.restart_rect,
                2
            )

            pygame.draw.rect(
                screen,
                (163, 0, 0),
                self.quit_rect
            )
            pygame.draw.rect(               #Border for quit button
                screen,
                (0, 0, 0),
                self.quit_rect,
                2
            )

            restart_text = self.font.render(
                "Restart",
                True,
                (255, 255, 255)
            )

            quit_text = self.font.render(
                "Quit",
                True,
                (255, 255, 255)
            )

            screen.blit(                                            #Restart text to center
                restart_text,
                restart_text.get_rect(center=self.restart_rect.center)
            )


            screen.blit(                                            #Quit text to center
                quit_text,
                quit_text.get_rect(center=self.quit_rect.center)
            )

    def handle_click(self, mouse_pos):

        # Click menu icon
        if self.menu_rect.collidepoint(mouse_pos):

            self.open = not self.open

            return None

        if self.open:

            if self.restart_rect.collidepoint(mouse_pos):

                self.open = False

                return "restart"

            if self.quit_rect.collidepoint(mouse_pos):

                self.open = False

                return "quit"

        return None