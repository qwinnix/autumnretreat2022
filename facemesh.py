################################################################################

import cv2
import mediapipe as mp
import numpy

from utilities import *

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

################################################################################

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    width , height = ( cap.get( 3 ) , cap.get( 4 ) )
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image)


    # Draw the face mesh annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_face_landmarks:

        for face_landmarks in results.multi_face_landmarks:
            #mp_drawing.draw_landmarks(
            #    image=image,
            #    landmark_list=face_landmarks,
            #    connections=mp_face_mesh.FACEMESH_TESSELATION,
            #    landmark_drawing_spec=None,
            #    connection_drawing_spec=mp_drawing_styles
            #    .get_default_face_mesh_tesselation_style()
            #)
            mp_drawing.draw_landmarks(
                image=image,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles
                .get_default_face_mesh_contours_style()
            )
            mp_drawing.draw_landmarks(
                image=image,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_IRISES,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles
                .get_default_face_mesh_iris_connections_style()
            )

            # additions
            cv2.fillPoly(
                img=image,
                pts= \
                    [numpy.array(convertlandmarks(
                        numpy.array(face_landmarks.landmark)[
                            getorderedpoints( FACEMESH_LEFT_EYEBROW )
                        ], width, height
                    ), dtype=numpy.int32)],
                color=(255, 255, 255)
            )

            cv2.fillPoly(
                img=image,
                pts= \
                    [numpy.array(convertlandmarks(
                        numpy.array(face_landmarks.landmark)[
                            getorderedpoints( FACEMESH_LOWER_LIP )
                        ], width, height
                    ), dtype=numpy.int32)],
                color=(256, 128, 0)
            )

            cv2.fillPoly(
                img=image,
                pts= \
                    [numpy.array(convertlandmarks(
                        numpy.array(face_landmarks.landmark)[
                            getorderedpoints(
                                frozenset.union(
                                    FACEMESH_LOWER_LIP_INNER ,
                                    FACEMESH_UPPER_LIP_INNER
                                )
                            )
                        ], width, height
                    ), dtype=numpy.int32)],
                color=(0, 0, 0)
            )

            cv2.fillPoly(
                img=image,
                pts= \
                    [numpy.array(convertlandmarks(
                        numpy.array(face_landmarks.landmark)[
                            getorderedpoints(FACEMESH_UPPER_LIP)
                        ], width, height
                    ), dtype=numpy.int32)],
                color=(128, 255, 0)
            )

            cv2.fillPoly(
                img=image,
                pts= \
                    [numpy.array(convertlandmarks(
                        numpy.array(face_landmarks.landmark)[
                            getorderedpoints(mp_face_mesh.FACEMESH_RIGHT_EYE)
                        ], width, height
                    ), dtype=numpy.int32)],
                color=(0, 255, 128)
            )



            mp_drawing.draw_landmarks(
                image = image ,
                landmark_list = face_landmarks ,
                connections = frozenset( [

                ] ),
                landmark_drawing_spec = None ,
                connection_drawing_spec = \
                    mp_drawing_styles.DrawingSpec(
                        color = ( 128 , 128 , 128 ) ,
                        thickness = 2 ,
                        circle_radius = 10
                    )
            )

        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Face Mesh', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
