import sys
import pygame
import esper
from src.ecs.components.c_velocity import CVelocity


def system_pause(world:esper.World, clock:pygame.time.Clock, _player_c_v:CVelocity,
                 framerate:int, vel:int, title:int, desc:int):
    pause = True
    while pause:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pause = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
                    world.delete_entity(title)
                    world.delete_entity(desc)
                    clock.tick(framerate)
                if event.key == pygame.K_LEFT:
                    _player_c_v.vel.x -= vel
                if event.key == pygame.K_RIGHT:
                    _player_c_v.vel.x += vel
                if event.key == pygame.K_UP:
                    _player_c_v.vel.y -= vel
                if event.key == pygame.K_DOWN:
                    _player_c_v.vel.y += vel
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    _player_c_v.vel.x += vel
                if event.key == pygame.K_RIGHT:
                    _player_c_v.vel.x -= vel
                if event.key == pygame.K_UP:
                    _player_c_v.vel.y += vel
                if event.key == pygame.K_DOWN:
                    _player_c_v.vel.y -= vel