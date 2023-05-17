import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sol",
             (100,80),
             cv2.FONT_HERSHEY_COMPLEX,
             2,
             (0,0,255)
             )

cv2.putText(img,
            "Mercurio",
             (110,180),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
            "Venus",
             (190,270),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
            "Tierra",
             (300,270),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )
cv2.putText(img,
            "Marte",
             (400,270),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )           
            
#Agrega el código para los otros 4 planetas. Nota: Son 8 en total.

cv2.imshow("Output",img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)