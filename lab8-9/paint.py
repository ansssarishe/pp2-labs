import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []  # points for the current line
    all_shapes = []  # store all shapes drawn
    drawing = False  # flag to check if LMB is pressed
    shape_mode = 'line'  # current drawing mode: 'line', 'rectangle', 'circle', 'eraser'
    start_pos = None  # starting position for rectangle or circle
    
    # create a transparent surface for drawing
    drawing_surface = pygame.Surface((1000, 1000), pygame.SRCALPHA)
    drawing_surface.set_alpha(128)  # set constant opacity (128 = 50% transparent)
    
    # button setup
    font = pygame.font.SysFont("helvetica", 20)  # changed font to Helvetica
    buttons = {
        "line": pygame.Rect(10, 10, 100, 40),
        "rectangle": pygame.Rect(120, 10, 100, 40),
        "circle": pygame.Rect(230, 10, 100, 40),
        "eraser": pygame.Rect(340, 10, 100, 40),
        "red": pygame.Rect(10, 60, 50, 50),
        "green": pygame.Rect(70, 60, 50, 50),
        "blue": pygame.Rect(130, 60, 50, 50),
        "black": pygame.Rect(190, 60, 50, 50),
        "white": pygame.Rect(250, 60, 50, 50),
    }
    colors = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255), "black": (0, 0, 0), "white": (255, 255, 255)}
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                # Increase or decrease brush size
                if event.key == pygame.K_a:  # Increase radius
                    radius = min(100, radius + 5)
                elif event.key == pygame.K_s:  # Decrease radius
                    radius = max(1, radius - 5)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                
                # check if a button is clicked
                for button_name, rect in buttons.items():
                    if rect.collidepoint(mouse_pos):
                        if button_name in colors:  # color buttons
                            mode = button_name
                        else:  # shape buttons
                            shape_mode = button_name
                
                # start drawing
                if event.button == 1:  # left click
                    drawing = True
                    start_pos = event.pos
                    if shape_mode == 'line' or shape_mode == 'eraser':
                        points = []  # reset points for the new line
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # stop drawing when LMB is released
                    drawing = False
                    if shape_mode == 'line' and points:
                        all_shapes.append(('line', points, radius, mode))
                    elif shape_mode == 'eraser' and points:
                        all_shapes.append(('line', points, radius, 'white'))  # eraser uses white color
                    elif shape_mode == 'rectangle' and start_pos:
                        end_pos = event.pos
                        all_shapes.append(('rectangle', start_pos, end_pos, radius, mode))
                    elif shape_mode == 'circle' and start_pos:
                        end_pos = event.pos
                        all_shapes.append(('circle', start_pos, end_pos, radius, mode))
            
            if event.type == pygame.MOUSEMOTION:
                if drawing and (shape_mode == 'line' or shape_mode == 'eraser'):
                    position = event.pos
                    points.append(position)
                    points = points[-256:]
        
        screen.fill((255, 255, 255))  # clear the screen with white
        
        # draw buttons
        for button_name, rect in buttons.items():
            if button_name in colors:  # color buttons
                pygame.draw.rect(screen, colors[button_name], rect)
            else:  # shape buttons
                pygame.draw.rect(screen, (200, 200, 200), rect)
                text = font.render(button_name.capitalize(), True, (0, 0, 0))  # use Helvetica font
                screen.blit(text, (rect.x + 10, rect.y + 10))
            if mode == button_name or shape_mode == button_name:
                pygame.draw.rect(screen, (0, 0, 0), rect, 3)  # highlight selected button
        
        # draw all saved shapes
        for shape in all_shapes:
            if shape[0] == 'line':
                for i in range(len(shape[1]) - 1):
                    drawLineBetween(drawing_surface, i, shape[1][i], shape[1][i + 1], shape[2], shape[3])
            elif shape[0] == 'rectangle':
                x0, y0 = shape[1]
                x1, y1 = shape[2]
                rect = pygame.Rect(min(x0, x1), min(y0, y1), abs(x1 - x0), abs(y1 - y0))
                pygame.draw.rect(drawing_surface, colors[shape[4]], rect, shape[3])
            elif shape[0] == 'circle':
                center = shape[1]
                radius = int(((shape[2][0] - shape[1][0]) ** 2 + (shape[2][1] - shape[1][1]) ** 2) ** 0.5)
                pygame.draw.circle(drawing_surface, colors[shape[4]], center, radius, shape[3])
        
        # draw the current shape
        if drawing and shape_mode == 'line':
            for i in range(len(points) - 1):
                drawLineBetween(drawing_surface, i, points[i], points[i + 1], radius, mode)
        elif drawing and shape_mode == 'eraser':
            for i in range(len(points) - 1):
                drawLineBetween(drawing_surface, i, points[i], points[i + 1], radius, 'white')  # eraser uses white color
        elif drawing and shape_mode == 'rectangle' and start_pos:
            end_pos = pygame.mouse.get_pos()
            x0, y0 = start_pos
            x1, y1 = end_pos
            rect = pygame.Rect(min(x0, x1), min(y0, y1), abs(x1 - x0), abs(y1 - y0))
            pygame.draw.rect(drawing_surface, colors[mode], rect, radius)
        elif drawing and shape_mode == 'circle' and start_pos:
            end_pos = pygame.mouse.get_pos()
            center = start_pos
            radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
            pygame.draw.circle(drawing_surface, colors[mode], center, radius, 2)
        
        # blit the transparent surface onto the main screen
        screen.blit(drawing_surface, (0, 0))
        
        # draw the slider for brush radius
        pygame.draw.line(screen, (0, 0, 0), (700, 50), (900, 50), 3)  # slider line
        slider_x = 700 + int((radius / 100) * 200)  # calculate slider position
        pygame.draw.circle(screen, (0, 0, 0), (slider_x, 50), 8)  # slider marker
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    color = (0, 0, 0, 255) if color_mode == 'black' else (255, 255, 255, 255) if color_mode == 'white' else (0, 0, 255, 255) if color_mode == 'blue' else (255, 0, 0, 255) if color_mode == 'red' else (0, 255, 0, 255)
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()