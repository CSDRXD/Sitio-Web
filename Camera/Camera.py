import cv2

# Iniciar la cámara (0 es la cámara predeterminada)
camara = cv2.VideoCapture(0)

while True:
    # Leer frame a frame
    ret, frame = camara.read()

    if not ret:
        print("No se pudo capturar imagen 😥")
        break

    # Mostrar el frame en una ventana
    cv2.imshow('Cámara en vivo 🎥', frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar ventanas
camara.release()
cv2.destroyAllWindows()
