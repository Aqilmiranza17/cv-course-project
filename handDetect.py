import cv2
import numpy as np

# Capture video dari kamera (0 adalah default kamera)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Membaca frame dari video capture
    ret, frame = cap.read()

    if not ret:
        break

    # Konversi frame menjadi grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Menggunakan Gaussian Blur untuk mengurangi noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Menggunakan thresholding untuk memisahkan tangan dari latar belakang
    _, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)

    # Mencari kontur di dalam gambar threshold
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Menggambar kontur tangan
        cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

        # Mencari convex hull untuk kontur
        hull = cv2.convexHull(contour)
        cv2.drawContours(frame, [hull], -1, (0, 0, 255), 2)

    # Menampilkan frame hasil
    cv2.imshow("Hand Detection", frame)

    # Tombol 'q' untuk keluar dari loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Melepaskan video capture dan menutup semua jendela
cap.release()
cv2.destroyAllWindows()