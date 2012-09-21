import pygame
import game.globals as globals
import game.core
import game.entities
import game.effects
import game.data



if __name__ == "__main__":
	engine = game.core.Engine('Pip-Boy 3000', globals.WIDTH, globals.HEIGHT)

	#Mapper
	mapper = game.entities.Map(1200, pygame.Rect(0, 0, globals.WIDTH-8, globals.HEIGHT-80))
	#mapper.fetch_map((-5.9234923, 54.5899493), 0.02)
	mapper.fetch_map((-77.02016830444336, 38.90319040137062), 0.01)
	mapper.move_map(400, 560)
	engine.add(mapper)

	#Scanlines
	scanlines = game.effects.Scanlines(800, 480, 3, 1, [(0, 13, 3, 50),(6, 42, 22, 100), (0, 13, 3, 50)])
	engine.add(scanlines)
	scanlines2 = game.effects.Scanlines(800, 480, 8, 4, [(0, 10, 1, 0),(21, 62, 42, 90),(61, 122, 82, 100),(21, 62, 42, 90)] + [(0, 10, 1, 0) for x in range(50)])
	engine.add(scanlines2)
	
	#Header & Footer
	header = game.entities.Header("DATA", "The Gasworks")
	engine.add(header)
	footer = game.entities.Footer(game.data.menus)
	engine.add(footer)
	
	#Overlay
	overlay = game.entities.Overlay()
	engine.add(overlay)
	
	running = True
	while running:
		for event in pygame.event.get():
			if (event.type == pygame.KEYUP) or (event.type == pygame.KEYDOWN):
				if (event.key == pygame.K_UP):
					mapper.move_map(0, -5)
				if (event.key == pygame.K_DOWN):
					mapper.move_map(0, 5)
				if (event.key == pygame.K_LEFT):
					mapper.move_map(-5, 0)
				if (event.key == pygame.K_RIGHT):
					mapper.move_map(5, 0)
				if (event.key == pygame.K_ESCAPE):
					running = False
			elif event.type == pygame.QUIT:
				running = False
					
		engine.update()
		engine.render()
		pygame.time.wait(30)
