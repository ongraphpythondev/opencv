import cv2 as cv
#img = cv.imread('Photos/sunny.jpg')
#cv.imshow('sunny', img)

#cv.waitKey(0)
# Reading Videos
capture = cv.VideoCapture('Videos/mehndi.mp4')

while True:
    isTrue, frame = capture.read()
    
 
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()