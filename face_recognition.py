import face_recognition

# Loading the images of known person
person1_image = face_recognition.load_image_file("Swastik.jpg")
person2_image = face_recognition.load_image_file("Swapnil.jpg")
person3_image = face_recognition.load_image_file("Avinash.jpg")

# Getting the face encoding of each person.
person1_faceencoding = face_recognition.face_encodings(person1_image)[0]
person2_faceencoding = face_recognition.face_encodings(person2_image)[0]
person3_faceencoding = face_recognition.face_encodings(person3_image)[0]

# Creating a list of all known face encodings
knownfaceencodings = [
    person1_faceencoding,
    person2_faceencoding,
    person3_faceencoding
]

# Load the image we want to check
img_unknown = face_recognition.load_image_file("unknown.jpg")

# Get face encodings for any people in the picture
unknown_faceencodings = face_recognition.face_encodings(img_unknown)

# There might be more than one person in the photo, so we need to loop over each face we found
for unknown_faceencoding in unknown_faceencodings:

    # Test if this unknown face encoding matches any of the three people we know
    res = face_recognition.compare_faces(knownfaceencodings, unknown_faceencoding, tolerance=0.6)

    name = "Unknown"

    if res[0]:
        name = "Swastik"
    elif res[1]:
        name = "Swapnil"
    elif res[2]:
        name = "Avinash"

    print(f"Found {name} in the photo!")
