import pygame
import random

# Initialize the game
pygame.init()

# Set up display
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pac-Man")

# Set up clock
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Load images
pacman_img = pygame.image.load('pacman.png')
ghost_img = pygame.image.load('ghost.png')

# Resize images
pacman_img = pygame.transform.scale(pacman_img, (30, 30))
ghost_img = pygame.transform.scale(ghost_img, (30, 30))
