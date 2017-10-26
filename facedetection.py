import os
import glob
import argparse
from google.cloud import vision
from google.cloud.vision import types


def detect_face(face_file, max_results=4):
    """Uses the Vision API to detect faces in the given file.
    Args:
        face_file: A file-like object containing an image with faces.
    Returns:
        An array of Face objects with information about the picture.
    """
    # [START get_vision_service]
    client = vision.ImageAnnotatorClient()
    # [END get_vision_service]

    content = face_file.read()
    image = types.Image(content=content)

    return client.face_detection(image=image).face_annotations


#main function
def main(input_filepath, max_results):
    for file in glob.glob('/home/Jeevan-Anand-Anne/cloudvision/images/*.jpg'):
        with open(file, 'rb') as image:
            faces = detect_face(image, max_results)
            print('Found {} face{} in {}'.format(
                len(faces), '' if len(faces) == 1 else 's',os.path.basename(file)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Detects faces in the given image.')
    parser.add_argument(
        'input_path', help='the path of images you\'d like to detect faces in.')
    parser.add_argument(
        '--max-results', dest='max_results', default=4,
        help='the max results of face detection.')
    args = parser.parse_args()

    main(args.input_path, args.max_results)

