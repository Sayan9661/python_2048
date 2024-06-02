import pygame
import random
import math

pygame.init()

FPS=60
WIDTH,HEIGHT=800,800
ROWS,COLS=4,4
RECT_HEIGHT=HEIGHT//ROWS
RECT_WIDTH=WIDTH//COLS

OUTLINE_COLOR=(187,173,160)
OUTLINE_THICKNESS=10
BACKGROUND_COLOR=(205,192,180)
FONT_COLOR=(119,110,101)
WINDOW=pygame.display.set_mode((WIDTH,HEIGHT))  
pygame.display.set_caption("2048")
FONT=pygame.font.SysFont("comicsans", 60,bold=True)
MOVE_VEL=20



#classs for rendering Tiles
class Tile:
    COLORS=[
        (238,228,218),
        (237,224,200),
        (242,177,121),
        (245,149,99),
        (246,124,95),
        (246,94,59),
        (237,207,114),
        (237,204,97),
        (237,200,80),
        (237,197,63),
    ]
    
    def __init__(self,value,row,col):
        self.value=value
        self.row=row
        self.col=col
        self.x=col*RECT_WIDTH
        self.y=row*RECT_HEIGHT
        
    def get_color(self):
        color_index=int(math.log2(self.value))-1
        color=self.COLORS[color_index]
        return color
    
    #rendering one tile
    def draw(self,window):
        color=self.get_color()
        pygame.draw.rect(window,color,(self.x,self.y,RECT_WIDTH,RECT_HEIGHT))
        
        text=FONT.render(str(self.value), 1, FONT_COLOR)
        window.blit(
            text,
            (
                self.x+(RECT_WIDTH/2-text.get_width()/2),
                self.y+(RECT_WIDTH/2-text.get_height()/2)
            )
            )
    
    def set_pos(self):
        pass
    
    def move(self,delta):
        pass




#outline grid of game
def draw_grid(window):
    #draw horizontal grid lines
    for row in range(1,ROWS):
        y=row*RECT_HEIGHT
        pygame.draw.line(window,OUTLINE_COLOR,(0,y),(WIDTH,y),OUTLINE_THICKNESS)
        
    #draw vertical grid lines
    for col in range(1,COLS):
        x=col*RECT_WIDTH
        pygame.draw.line(window,OUTLINE_COLOR,(x,0),(x,HEIGHT),OUTLINE_THICKNESS)
    pygame.draw.rect(window,OUTLINE_COLOR,(0,0,WIDTH,HEIGHT), OUTLINE_THICKNESS)


#main fraw function
def draw(window,tiles):
    window.fill(BACKGROUND_COLOR)
    
    for tile in tiles.values():
        tile.draw(window)
    
    draw_grid(window)
    pygame.display.update()

def get_random_pos(tiles):
    row=None
    col=None
    while True:
        row=random.randrange(0, ROWS)
        col=random.randrange(0,COLS)
        
        if f"{row}{col}" not in tiles:
            break
    
    return row,col
            
    
def generate_tiles():
    tiles={}
    for _ in range(2):
        row,col=get_random_pos(tiles)
        tiles[f"{row}{col}"]=Tile(2,row,col)
        
    return tiles

def main(window):
    clock=pygame.time.Clock()
    run=True
    
    tiles=generate_tiles()
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
        
        draw(window,tiles)
        
    
    pygame.quit()

if __name__=="__main__":
    main(WINDOW)
    
