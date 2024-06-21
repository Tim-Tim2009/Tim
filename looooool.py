import pygame, math, random, time
import pandas as pd
from openpyxl import load_workbook
import os
import sqlite3
pygame.init()

WIDTH, HEIGHT = 800, 600

FEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

TARGET_INCREMENT = 800
TARGET_EVENT = pygame.USEREVENT

BIRD_EVENT = pygame.USEREVENT + 4
BIRD_INCREMENT = 10000

TARGET_WAVE1_EVENT = pygame.USEREVENT + 1

TARGET_WAVE2_EVENT = pygame.USEREVENT + 2

TARGET_WAVE3_EVENT = pygame.USEREVENT + 3

TARGET_PADDING = 30

BG_COLOR = (0, 15, 25)
LIVES = 3
TOP_BAR_HEIGTH = 50

LABEL_FONT = pygame.font.SysFont("comicsans", 24)
GAMEOVER_FONT = pygame.font.SysFont("consolas", 70, bold=True)
LABEL_COLOR = "white"

background = pygame.image.load('background.png')
FEN.blit(background, (0,50))

bird_images = [
    pygame.image.load('bird1.png'),
    pygame.image.load('bird2.png'),
    pygame.image.load('bird3.png'),
    pygame.image.load('bird4.png'),
    pygame.image.load('bird5.png'),
    pygame.image.load('bird6.png')
]


class Target:
    ISBONUS = False
    MAX_SIZE = 30
    BONUS_MAX_SIZE = 50
    GOLD_MAX_SIZE = 20
    GROWTH_RATE = 0.2
    
    COLOR = "red"
    BONUS_COLOR = "green"
    GOLD_COLOR = (255, 215, 0)
    SECOND_COLOR = "white"

    def __init__(self, x, y, bonus, gold):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True
        self.bonuschances = bonus
        self.goldchances = gold

        self.ISBONUS = random.randint(0, self.bonuschances) == 1
        if not self.ISBONUS:
            self.ISGOLD = random.randint(0, self.goldchances) == 2
        else:
            self.ISGOLD = False

    def update(self):
        if self.ISBONUS:
            if self.size + self.GROWTH_RATE >= self.BONUS_MAX_SIZE:
                self.grow = False

            if self.grow:
                self.size += self.GROWTH_RATE
            else:
                self.size -= self.GROWTH_RATE
        elif self.ISGOLD:
            if self.size + self.GROWTH_RATE >= self.GOLD_MAX_SIZE:
                self.grow = False

            if self.grow:
                self.size += self.GROWTH_RATE
            else:
                self.size -= self.GROWTH_RATE
        else:
            if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
                self.grow = False

            if self.grow:
                self.size += self.GROWTH_RATE
            else:
                self.size -= self.GROWTH_RATE
    
    def draw(self, FEN):
        if self.ISBONUS:
            pygame.draw.circle(FEN, self.BONUS_COLOR, (self.x, self.y), self.size)
            pygame.draw.circle(FEN, self.SECOND_COLOR, (self.x, self.y), self.size * 0.8)
            pygame.draw.circle(FEN, self.BONUS_COLOR, (self.x, self.y), self.size * 0.6)
            pygame.draw.circle(FEN, self.SECOND_COLOR, (self.x, self.y), self.size * 0.4)
        elif self.ISGOLD:
            pygame.draw.circle(FEN, self.GOLD_COLOR, (self.x, self.y), self.size)
            pygame.draw.circle(FEN, self.SECOND_COLOR, (self.x, self.y), self.size * 0.8)
            pygame.draw.circle(FEN, self.GOLD_COLOR, (self.x, self.y), self.size * 0.6)
            pygame.draw.circle(FEN, self.SECOND_COLOR, (self.x, self.y), self.size * 0.4)
        else:
            pygame.draw.circle(FEN, self.COLOR, (self.x, self.y), self.size)
            pygame.draw.circle(FEN, self.SECOND_COLOR, (self.x, self.y), self.size * 0.8)
            pygame.draw.circle(FEN, self.COLOR, (self.x, self.y), self.size * 0.6)
            pygame.draw.circle(FEN, self.SECOND_COLOR, (self.x, self.y), self.size * 0.4)
        

    def collide(self, x, y):
        dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
        return dis <= self.size
    
    def isbonus(self):
        return self.ISBONUS
    
    def isgold(self):    
        return self.ISGOLD
    
        
class Bird():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.size = 100  # Taille de l'oiseau pour la collision
        self.images = [
            pygame.image.load('bird1.png'),
            pygame.image.load('bird2.png'),
            pygame.image.load('bird3.png'),
            pygame.image.load('bird4.png'),
            pygame.image.load('bird5.png'),
            pygame.image.load('bird6.png')
        ]
        self.pos = 0
        
        self.animation_interval = 0.1  # Intervalle d'animation en secondes
        self.last_update_time = time.time()  # Temps de la dernière mise à jour

    def draw(self, FEN):
        current_time = time.time()
        if current_time - self.last_update_time >= self.animation_interval:
            self.last_update_time = current_time
            self.pos += 1
            self.x += 50
            if self.pos == 6:
                self.pos = 0
        FEN.blit(self.images[self.pos], (self.x, self.y))

    def collide(self, x, y):
        dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        return dis <= self.size

def draw(FEN, targets):
    FEN.blit(background, (0, 50))
    
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

def save_game_data(file_name, data):
    conn = sqlite3.connect('example.db')




    df = pd.DataFrame([data])
    if os.path.exists(file_name):
        df.to_csv(file_name, mode='a', header=False, index=False)
        
        df_existing = pd.read_csv(file_name)
        best_score = df_existing['Score'].max() if 'Score' in df_existing.columns else 0
        
        # Création d'un DataFrame pour le meilleur score
        best = pd.DataFrame({'Best Score': [f'Best Score: {best_score}']})
        best.to_csv(file_name, mode='a', header=False, index=False)

        bestacc = df_existing['Accuracy'].max() if 'Accuracy' in df_existing.columns else 0

        best_accuracy = pd.DataFrame({'Best Accuracy': [f'Best Accuracy: {bestacc}']})
        best_accuracy.to_csv(file_name, mode='a', header=False, index=False)


    else:
        df.to_csv(file_name, index=False)


def end_screen(FEN, elapsed_time, targets_pressed, clicks, score):
    print("Entering end_screen function")
    FEN.fill(BG_COLOR)
    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", 1, LABEL_COLOR)

    speed = round(targets_pressed / elapsed_time, 1) if elapsed_time > 0 else 0
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", 1, LABEL_COLOR)

    score_label = LABEL_FONT.render(f"Score: {score}", 1, LABEL_COLOR)

    accuracy = round(targets_pressed / clicks * 100, 1) if clicks >= 15 else 0
    accuracy_label = LABEL_FONT.render(f"Accuracy: {accuracy}%", 1, LABEL_COLOR)

    gameover_label = GAMEOVER_FONT.render(f"GAMEOVER !", 1, LABEL_COLOR)

    FEN.blit(gameover_label, (get_middle(gameover_label), 75))
    FEN.blit(time_label, (get_middle(time_label), 200))
    FEN.blit(speed_label, (get_middle(speed_label), 300))
    FEN.blit(score_label, (get_middle(score_label), 400))
    FEN.blit(accuracy_label, (get_middle(accuracy_label), 500))

    pygame.display.update()
    
    game_data = {
        'Time': format_time(elapsed_time),
        'Targets Pressed': targets_pressed,
        'Clicks': clicks,
        'Score': score,
        'Accuracy': accuracy
    }
    save_game_data('game_data.csv', game_data)

    print("End screen displayed, entering loop to wait for user action")
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                run = False
                break
        pygame.time.delay(100)  # Small delay to reduce CPU usage

    pygame.quit()
    print("Exiting end_screen function")
    quit()

    
def get_middle(surface):
    return WIDTH / 2 - surface.get_width()/2

def main():
    run = True
    targets = []
    clock = pygame.time.Clock()

    actual_lives = LIVES
    score = 0
    targets_pressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()

    bonuschances = 10
    goldchances = 20

    wave = 0
    wave1 = False
    wave2 = False
    wave3 = False

    isbirdevent = False

    birdy = random.randint(50, HEIGHT)
    birdx = -100
    bird_pos = (birdx, birdy)


    bird = Bird(birdx, birdy, bird_images[0])

    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)
    pygame.time.set_timer(BIRD_EVENT, BIRD_INCREMENT)
    
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

            if event.type == TARGET_EVENT or event.type == TARGET_WAVE1_EVENT or event.type == TARGET_WAVE2_EVENT or event.type == TARGET_WAVE3_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING + TOP_BAR_HEIGTH, HEIGHT - TARGET_PADDING)
                target = Target(x, y, bonuschances, goldchances)
                targets.append(target)

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1

            if event.type == BIRD_EVENT:
                isbirdevent = True

        for target in targets:
            target.update()

            if target.size <= 0:
                targets.remove(target)
                if target.isgold():
                    misses += 3
                else:
                    misses += 1
            
            if click and target.collide(*mouse_pos):
                targets.remove(target)
                if target.isbonus():
                    score += 5
                    misses -= 1
                elif target.isgold():
                    score += 10
                    misses -= 3
                else:
                    score += 1
                targets_pressed += 1
            

        if misses >= actual_lives:
            end_screen(FEN, elapsed_time, targets_pressed, clicks, score)
            break
            
        if elapsed_time >= 15 and not wave1:
            pygame.time.set_timer(TARGET_EVENT, 0)
            pygame.time.set_timer(TARGET_WAVE1_EVENT, TARGET_INCREMENT-200)
            wave1 = True
            wave += 1
        
        if elapsed_time >= 30 and not wave2:
            pygame.time.set_timer(TARGET_WAVE1_EVENT, 0)
            pygame.time.set_timer(TARGET_WAVE2_EVENT, TARGET_INCREMENT-300)
            wave2 = True
            wave += 1
        
        if elapsed_time >= 45 and not wave3:
            pygame.time.set_timer(TARGET_WAVE1_EVENT, 0)
            pygame.time.set_timer(TARGET_WAVE2_EVENT, 0)
            pygame.time.set_timer(TARGET_WAVE3_EVENT, TARGET_INCREMENT-400)
            wave3 = True
            wave += 1
        
        draw(FEN, targets)

        if isbirdevent:
            bird.draw(FEN)
        
            if click and bird.collide(*mouse_pos):
                bonuschances = round(bonuschances * 0.8)
                goldchances = round(goldchances * 0.8)
                isbirdevent = False
                bird.x = -200
                bird.y = random.randint(100, HEIGHT - 100)
            
            if bird.x >= WIDTH + 150:
                isbirdevent = False
                bird.x = -200
                bird.y = random.randint(100, HEIGHT - 100)
        
        draw_top_bar(FEN, elapsed_time, targets_pressed, misses, wave, score)
        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    main()
        
