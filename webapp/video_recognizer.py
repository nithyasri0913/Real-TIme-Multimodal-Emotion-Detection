import cv2
import numpy as np
import json as json
import keras

model = keras.models.load_model('models/model_8_50epoch80_CK48dataset.h5')

try:
    face_haar_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')
except Exception:
    st.write("Error loading cascade classifiers")
camera = cv2.VideoCapture(0)


def gen_frames():  # generate frame by frame from camera
    while True:
        try:
            # Capture frame by frame
            success, frame = camera.read()
            if not success:
                break
            else:
                frame = np.array(frame)
                gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.1, 4)

                for (x, y, w, h) in faces_detected:
                    # print('WORKING')
                    frame = np.array(frame)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)
                    roi_gray = gray_img[y:y + w, x:x + h]  # cropping region of interest i.e. face area from  image
                    roi_color = frame[y:y + h, x:x + w]
                    roi_color = cv2.resize(roi_color, (80, 80))
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    facess = face_haar_cascade.detectMultiScale(roi_gray)
                    if len(facess) == 0:
                        print("Face not detected")
                    else:
                        for (ex, ey, ew, eh) in facess:
                            face_roi = roi_color[ey: ey + eh, ex:ex + ew]  ## cropping the face
                            # img_pixels = image.img_to_array(roi_gray)
                            # img_pixels = np.expand_dims(img_pixels, axis=0)
                            # img_pixels /= 255
                            final_image = cv2.resize(face_roi, (80, 80))
                            final_image = np.expand_dims(final_image, axis=0)  ## need fourth dimension
                            final_image = final_image / 255.0

                        predictions = model.predict(final_image)
                        pred_list = predictions.tolist()
                        pred_json = json.dumps(pred_list[0])
                        with open('./video_prediction.json', 'w') as file:
                            file.write(pred_json)

                        max_index = np.argmax(predictions[0])
                        highest_prediction_value = predictions.max(1) * 100.0
                        # print(highest_prediction_value)

                        emotions = ['angry', 'fear', 'happy', 'sad']
                        predicted_emotion = emotions[max_index]
                        display_percentage_of_emotion = str(predicted_emotion) + ": " + str(highest_prediction_value)
                        # print(display_percentage_of_emotion)
                        cv2.putText(frame, display_percentage_of_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    (0, 0, 255), 2)

                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()

                yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'  # concat frame one by one and show result

        except Exception as e:
            print(str(e))
