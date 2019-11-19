import pygame, sys, os

class SlidePuzzle:
    def __init__(self, gridsize,tilesize, marginsize):
        self.gridsize,self.tilesize, self.marginesize = gridsize, tilesize, marginsize
      
        self.tiles_len = gridsize[0]*gridsize[1]-1
    
   
        self.tiles = [(x,y) for y in range(gridsize[1]) for x in range(gridsize[0])]
    
    
        self.tilepos = {(x,y):(x*(tilesize+marginsize)+marginsize,y*(tilesize+marginsize)+marginsize)for y in range(gridsize[1]) for x in range(gridsize[0])}
    
    def update(self, dt):
        pass
    
    def draw(self, screen):
        for i in range(self.tiles_len):
         x,y = self.tilepos[self.tiles[i]]    
         pygame.draw.rect(screen, (0,255,0),(x,y,self.tilesize, self.tilesize))


def main():
    pygame.init()
    os.environ['SDL_VIDEOCENTERED'] = '1'
    pygame.display.set_caption('Slide Puzzle')
    screen = pygame.display.set_mode((800,600))
    fpsclock = pygame.time.Clock()
    program = SlidePuzzle((3,3),100,5)
    


    while True:
        
        dt = fpsclock.tick()/100
        
        screen.fill((0,0,0))
        program.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:pygame.quit();sys.exit()

        program.update(dt)


if __name__ == '__main__':
    main()
