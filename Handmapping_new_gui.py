from tkinter import N, NE, NS, NW, Button, Tk, Canvas, PhotoImage
import cv2 
import mediapipe as mp

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

def photo_image(img):
    h, w = img.shape[:2]
    data = f'P6 {w} {h} 255 '.encode() + img[..., ::-1].tobytes()
    return PhotoImage(width=w, height=h, data=data, format='PPM')

def update():
    ret, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handslms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handslms, mpHands.HAND_CONNECTIONS)
    if ret:
        photo = photo_image(img)
        canvas.create_image(0, 0, image=photo, anchor=NW)
        canvas.image = photo
    root.after(15, update)

root = Tk()
root.title("Handmapping")
cap = cv2.VideoCapture(0)

canvas = Canvas(root, width=1200, height=700)
canvas.grid(row=0,column=0)
sub_btn=Button(root,text = 'Submit', command ="")
sub_btn.grid(row=0,column=1,sticky=NE)
update()
root.mainloop()
cap.release()
