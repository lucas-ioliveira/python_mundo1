'''
Faça um programa que abra e reproduza o áudio
de um arquivo mp3.
'''
import pygame
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.play()
pygame.event.wait()