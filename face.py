# Import
import face_recognition
import os
import cv2

# constants to name the directories
KNOWN_FACES_DIR = "/Known_faces"
UNKNOWN_FACES_DIR = "/Unknown_faces"

# Default tolerance for face recognition is 0.6
# Higher false positive
# Lower false negative
TOLERANCE = 0.6

# Depends on the size of the image
# Pixel of the rectangle
FRAME_THICKNESS = 3
FONT_THICKNESS = 2

# In deep learning,
# a convolutional neural network is
# a class of artificial neural network,
# most commonly applied to analyze visual imagery.
MODEL = "cnn"  # hog can also be used

# Returns (R, G, B) from name
# takes the first 3 letters in the string,
# and convert these to RGB values:


def name_to_color(name):
    color = [(ord(c.lower())-97)*8 for c in name[:3]]
    return color
# Loading images(known faces)


print("loading known faces")
# Two lists, one for faces and one for their respective names
known_faces = []
known_names = []

# Iterate over Known faces directory
for name in os.listdir(KNOWN_FACES_DIR):
    # load every file of faces of known persons
    for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        # Loading image
        image = face_recognition.load_image_file(
            f"{KNOWN_FACES_DIR}/{name}/{filename}")
        # Encode each of the faces and store the encodings associated with identity
        # 128 dimesion face encoding
        encoding = face_recognition.face_encodings(image)[0]

        # append encoding and name
        known_faces.append(encoding)
        known_names.append(name)

# Iterate over Unknown faces and names
# and compare to Known faces
print("Processing unknown faces")
for filename in os.listdit(UNKNOWN_FACES_DIR):
    print(filename)
    image = face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")
    # Loacte the image
    locations = face_recognition.face_locations(image, model=MODEL)
    # encode
    encodings = face_recognition.face_encodings(image, locations)
    # Now we can iterate over the faces found in the unknown images,
    # to see if we can find a match with any of our known faces.
    # If we find one, we want to draw a rectangle around them.
    # we'll first convert the image from RGB to BGR since OpenCV uses BGR.
    image = cv2.cvtColor(image, cv2.RGB2BGR)

    for face_encoding, face_location, in zip(encodings, locations):
        results = face_recognition.compare_faces(
            known_faces, face_encoding, TOLERANCE)
        match = None
        if True in results:
            match = known_names[results.index(True)]
            print(f"Match found: {match}")

            # Coordinates for match for  a rectangle
            # To draw a rectangle in OpenCV,
            # we need the top left and bottom right coordinates,
            # and we use cv2.rectangle to draw it.
            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])

            color = name_to_color(match)

            # Paint frame
            cv2.rectangle(image, top_left, bottom_right,
                          color, FRAME_THICKNESS)

            #
            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1], face_location[2] + 22)

            # Paint frame
            cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)

            # Write a name
            cv2.putText(
                image, match, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HER)

            # Show image
            cv2.startWindowThread()
            cv2.imshow(filename, image)
            cv2.waitKey(0)
            cv2.destroyWindow(filename)
