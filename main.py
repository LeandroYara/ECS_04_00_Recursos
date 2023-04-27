#!/usr/bin/python3
"""Función Main"""

from src.engine.game_engine import GameEngine
import asyncio

if __name__ == "__main__":
    engine = GameEngine()
    asyncio.run(engine.run())
