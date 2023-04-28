import pygame
import esper
from src.create.prefab_creator import create_text


def system_beam_wait(world:esper.World, screen:pygame.Surface, delta_time:float, counter:float,
                     time_text:int, font_route:str):
    if counter > 0:
        counter -= delta_time
    if counter <= 0:
        actual_text = "¡Cargado!"
        world.delete_entity(time_text)
        pos = (0, screen.get_height() / 1.07)
        counter_time = create_text(world, font_route, actual_text, pos, 13, (255,255,0))
    if counter > 0:
        actual_text = str(int(counter + 1)) + " s"
        world.delete_entity(time_text)
        pos = (0, screen.get_height() / 1.07)
        counter_time = create_text(world, font_route, actual_text, pos, 13, (255,255,0))
        
    return counter, counter_time