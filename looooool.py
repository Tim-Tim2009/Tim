import pygame, math, random, time
import pandas as pd
from openpyxl import load_workbook
import os
pygame.init()

def save_game_data(file_name, data):
    # Crée un DataFrame à partir des données de jeu
    df = pd.DataFrame([data])

    # Si le fichier existe, ouvre-le et ajoute les données, sinon crée un nouveau fichier
    if os.path.exists(file_name):
        book = load_workbook(file_name)
        writer = pd.ExcelWriter(file_name, engine='openpyxl')
        writer.book = book
        writer.sheets = {ws.title: ws for ws in book.worksheets}
        for sheetname in writer.sheets:
            df.to_excel(writer, sheet_name=sheetname, startrow=writer.sheets[sheetname].max_row, index=False, header=False)
        writer.save()
    else:
        df.to_excel(file_name, index=False)

WIDTH, HEIGHT = 800, 600

FEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

TARGET_INCREMENT = 800
TARGET_EVENT = pygame.USEREVENT

TARGET_WAVE1_EVENT = pygame.USEREVENT

TARGET_WAVE2_EVENT = pygame.USEREVENT

TARGET_PADDING = 30

BG_COLOR = (0, 15, 25)
LIVES = 3
TOP_BAR_HEIGTH = 50

LABEL_FONT = pygame.font.SysFont("comicsans", 24)
LABEL_COLOR = "white"

class Target:
    ISBONUS = False
    MAX_SIZE = 30
    BONUS_MAX_SIZE = 50
    GROWTH_RATE = 0.2
    
    COLOR = "red"
    BONUS_COLOR = "green"
    SECOND_COLOR = "white"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True
        BONUS = random.randint(0,10)
        if BONUS == 10:
            self.ISBONUS = True

    def update(self):
        if not self.ISBONUS:
            if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
                self.grow = False

            if self.grow:
                self.size += self.GROWTH_RATE
            else:
                self.size -= self.GROWTH_RATE
        else:
            if self.size + self.GROWTH_RATE >= self.BONUS_MAX_SIZE:
                self.grow = False

            if self.grow:
                self.size += self.GROWTH_RATE
            else:
                self.size -= self.GROWTH_RATE
    
    def draw(self, FEN):
        if not self.ISBONUS:
            pygame.draw.circle(FEN, self.COLOR, (self.x, self.y), self.size)
            pygame.draw.circle(FEN, self.SECOND_COLOR, (self.x, self.y), self.size * 0.8)
            pygame.draw.circle(FEN, self.COLOR, (self.x, self.y), self.size * 0.6)
            pygame.draw.circle(FEN, self.SECOND_COLOR, (self.x, self.y), self.size * 0.4)
        else:
            pygame.draw.circle(FEN, self.BONUS_COLOR, (self.x, self.y), self.size)
            pygame.draw.circle(FEN, self.SECOND_COLOR, (self.x, self.y), self.size * 0.8)
            pygame.draw.circle(FEN, self.BONUS_COLOR, (self.x, self.y), self.size * 0.6)
            pygame.draw.circle(FEN, self.SECOND_COLOR, (self.x, self.y), self.size * 0.4)

    def collide(self, x, y):
        dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
        return dis <= self.size
    
    def isbonus(self):
        if self.ISBONUS:
            return True
        else:
            return False

def draw(FEN, targets):
    FEN.fill(BG_COLOR)

    for target in targets:
        target.draw(FEN)

def format_time(secs):
    milli = math.floor(int(secs * 1000 % 1000) / 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)

    return f"{minutes:02d}:{seconds:02d}.{milli}"

def draw_top_bar(FEN, elapsed_time, targets_pressed, misses, wave, score):
    pygame.draw.rect(FEN, "grey", (0, 0, WIDTH, TOP_BAR_HEIGTH))
    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", 1, "black")

    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", 1, "black")

    score_label = LABEL_FONT.render(f"Score: {score}", 1, "black")

    lives_label = LABEL_FONT.render(f"Lives: {LIVES - misses}", 1, "black")

    wave_label = LABEL_FONT.render(f"Wave: {wave}", 1, "black")


    FEN.blit(time_label, (5, 5))
    FEN.blit(speed_label, (210, 5))
    FEN.blit(score_label, (430, 5))
    FEN.blit(lives_label, (575, 5))
    FEN.blit(wave_label, (700, 5))

def end_screen(FEN, elapsed_time, targets_pressed, clicks, score):
    FEN.fill(BG_COLOR)
    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", 1, LABEL_COLOR)

    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", 1, LABEL_COLOR)

    score_label = LABEL_FONT.render(f"Score: {score}", 1, LABEL_COLOR)

    accuracy = round(targets_pressed / clicks * 100, 1)
    accuracy_label = LABEL_FONT.render(f"Accuracy: {accuracy}%", 1, LABEL_COLOR)

    FEN.blit(time_label, (get_middle(time_label), 100))
    FEN.blit(speed_label, (get_middle(speed_label), 200))
    FEN.blit(score_label, (get_middle(score_label), 300))
    FEN.blit(accuracy_label, (get_middle(accuracy_label), 400))

    pygame.display.update()
    
    game_data = pd.DataFrame({
        'Time': [format_time(elapsed_time)],
        'Targets Pressed': [targets_pressed],
        'Clicks': [clicks],
        'Score': [score],
        'Accuracy': [accuracy]
    })
    
    save_game_data('game_data.csv', game_data)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()
        
def get_middle(surface):
    return WIDTH / 2 - surface.get_width()/2

def main():
    run = True
    targets = []
    clock = pygame.time.Clock()

    score = 0
    targets_pressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()

    wave = 0
    wave1 = False
    wave2 = False

    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)
    
    while run:
        run = True
  
        clock.tick(60)
        click = False
        mouse_pos = pygame.mouse.get_pos()
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == TARGET_EVENT or event.type == TARGET_WAVE1_EVENT or event.type == TARGET_WAVE2_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING + TOP_BAR_HEIGTH, HEIGHT - TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1

        for target in targets:
            target.update()

            if target.size <= 0:
                targets.remove(target)
                misses += 1
            
            if click and target.collide(*mouse_pos):
                targets.remove(target)
                if target.isbonus():
                    score += 5
                else:
                    score += 1
                targets_pressed += 1
        
        if misses >= LIVES:
            end_screen(FEN, elapsed_time, targets_pressed, clicks, score)
            
        if elapsed_time >= 15 and not wave1:
            pygame.time.set_timer(TARGET_EVENT, 0)
            pygame.time.set_timer(TARGET_WAVE1_EVENT, TARGET_INCREMENT-200)
            wave1 = True
            wave += 1
        
        if elapsed_time >= 30 and not wave2:
            pygame.time.set_timer(TARGET_WAVE1_EVENT, 0)
            pygame.time.set_timer(TARGET_WAVE2_EVENT, TARGET_INCREMENT-400)
            wave2 = True
            wave += 1
        
        draw(FEN, targets)
        draw_top_bar(FEN, elapsed_time, targets_pressed, misses, wave, score)
        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    main()
        