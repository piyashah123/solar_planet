import cv2

# Read the image
img = cv2.imread("solar-system.jpg")

# Define the text, font, and color for each planet
planet_texts = {
    "Mercury": {"text": "Mercury", "position": (50, 150), "font": cv2.FONT_HERSHEY_SIMPLEX, "color": (255, 255, 255)},
    "Venus": {"text": "Venus", "position": (200, 350), "font": cv2.FONT_HERSHEY_SIMPLEX, "color": (255, 255, 255)},
    "Earth": {"text": "Earth", "position": (350, 150), "font": cv2.FONT_HERSHEY_SIMPLEX, "color": (255, 255, 255)},
    # Add more planets and their details here
}

# Add text for each planet
for planet, details in planet_texts.items():
    cv2.putText(img, details["text"], details["position"], details["font"], 1, details["color"], 2, cv2.LINE_AA)

# Display the image
cv2.imshow("output", img)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the modified image
cv2.imwrite("solar-system.jpg", img)
