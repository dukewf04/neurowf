import pyautogui
import cv2
import numpy as np
import time

#test

fps = 0
tic = time.time()
while True:
    # Получаем координаты и размеры окна
    window = pyautogui.getWindowsWithTitle('Перезвоны')[0]
    x, y = window.topleft
    width, height = window.size

    # Захватываем скриншот окна
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    # Сохраняем скриншот в файл
    screenshot.save('screenshot.png')
    #-----------------------------------

    # Загружаем изображение
    frame = cv2.imread('screenshot.png')

    # Вычисляем FPS
    toc = time.time()
    fps_curr = 1 / (toc - tic) # сделать проверку деления на 0
    tic = toc
    fps = (fps + fps_curr) / 2

    # Отображаем FPS на кадре
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "FPS: {:.2f}".format(fps), (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Отображаем кадр
    cv2.imshow('frame', frame)

    # Если нажата клавиша 'q', выходим из цикла
    if cv2.waitKey(1) == ord('q'):
        break

# Освобождаем ресурсы
cv2.destroyAllWindows()