import pygame
import time
import os
WHITE = (255, 255, 255)

class Gui_menu():
    # 생성자
    def __init__(self):
        global gamepad, background, clock
        global start_btn, set_11_btn, set_15_btn, load_img

        pygame.init()  # 초기화
        self.width = 945    # window 사이즈
        self.height = 720   # window 사이즈

        self.button_width = 124 # 버튼 사이즈
        self.button_height = 48 # 버튼 사이즈
        self.corner1 = (130, 470) # 꼭지점 코너 위치
        self.corner2 = (130,370)  # 꼭지점 코너 위치
        self.corner3 = (130,470)  # 꼭지점 코너 위치
        self.step = 0

        self.rule = 11

        gamepad = pygame.display.set_mode((self.width, self.height))  # 화면 크기
        pygame.display.set_caption("알파제로 오목")  # 제목
        self.menu = True  # 종료를 위한 플래그
        background = pygame.image.load(os.getcwd() + "/image/main.jpg") # 메인 이미지 배경화면
        start_btn = pygame.image.load(os.getcwd() + "/image/start.jpg")
        set_11_btn = pygame.image.load(os.getcwd() + "/image/11.jpg")
        set_15_btn = pygame.image.load(os.getcwd() + "/image/15.jpg")
        load_img = pygame.image.load(os.getcwd() + "/image/loading.jpg")

        clock = pygame.time.Clock()
        pygame.display.flip()

        # 배경음악
        pygame.mixer.init()
        pygame.mixer.music.load(os.getcwd() + '/sound/game.ogg')
        pygame.mixer.music.play(-1)  # 무한 루프

        self.run()


    def run(self):
        global gamepad, background
        global start_btn, set_11_btn, set_15_btn, load_img

        while self.menu:
            # ket evnet
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu = False # 종료
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y position of the mouse click
                    mouse_x, mouse_y = event.pos # 마우스로 클릭한 지점
                    # 시작 버튼을 누른 경우
                    if self.step == 0 and (mouse_x >= self.corner1[0]) and (mouse_x <= self.corner1[0] + self.button_width) and (mouse_y >= self.corner1[1]) and (mouse_y <= self.corner1[1] + self.button_height):
                        print(event.pos)
                        print("click on image start")
                        self.step = 1
                    # 11 버튼과 15 버튼
                    # 11 버튼
                    elif self.step == 1 and (mouse_x >= self.corner2[0]) and (mouse_x <= self.corner2[0] + self.button_width) and (mouse_y >= self.corner2[1]) and (mouse_y <= self.corner2[1] + self.button_height):
                        print(event.pos)
                        print("click on image 11")
                        self.rule = 11
                        self.step = 2
                    # 15 버튼
                    elif self.step == 1 and (mouse_x >= self.corner3[0]) and (mouse_x <= self.corner3[0] + self.button_width) and (mouse_y >= self.corner3[1]) and (mouse_y <= self.corner3[1] + self.button_height):
                        print(event.pos)
                        print("click on image 15")
                        self.rule = 15
                        self.step = 2
            # 배경 set
            gamepad.fill(WHITE)
            gamepad.blit(background, (0, 0))

            # 시작 단계
            if self.step == 0:
                gamepad.blit(start_btn, (130, 470))
            elif self.step == 1:
                gamepad.blit(set_11_btn, (130, 370))
                gamepad.blit(set_15_btn, (130, 470))
            elif self.step == 2:
                gamepad.blit(load_img,(300, 300)) # 945, 720
                pygame.display.update()  # 디스플레이 업데이트
                time.sleep(3)
                self.menu = False  # 종료
            pygame.display.update()  # 디스플레이 업데이트
            clock.tick(60)

        pygame.quit()   # 게임 종료

