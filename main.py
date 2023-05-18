# Importando Librerias
import cv2
import numpy as np

# Variables
path = "/Users/vkurama7u7v/Downloads/v_Kurama7u7_v_anime_style_18a2b008-5108-41a8-ba41-75c08da17a11.png"

# ===== FUNCIONES =====
# Leer una imagen usando cv2
def leer_imagen(route):
    img = cv2.imread(route,1)
    return img

# Mostrar una imagen en pantalla
def mostrar_img(title, image):
    cv2.imshow(title, image)
    cv2.waitKey()

# Convertir una imagen a escala de grises
def escala_grises(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return img

# Aplicar filtro para eliminación de ruido
def eliminar_ruido(image):
    img = cv2.GaussianBlur(image, (5, 5), 0)
    return img

# Detección de bordes
def detectar_bordes(image):
    img = cv2.Canny(image, 0, 50)
    return img

# Conteo de contornos
def buscar_contornos(image):
    (contornos,_) = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contornos, -1, (255, 0, 255), 2)
    return "Se detectaron {} objeto(s)". format(len(contornos))

# ===== MAIN =====
img = leer_imagen(path)
mostrar_img("Imagen", img)

imagen_grises = escala_grises(img)
mostrar_img("Escala de Grises", imagen_grises)

imagen_ruido = eliminar_ruido(imagen_grises)
mostrar_img("Eliminar Ruido", imagen_ruido)

imagen_bordes = detectar_bordes(imagen_ruido)
mostrar_img("Detectar Bordes", imagen_bordes)

print(buscar_contornos(imagen_bordes))