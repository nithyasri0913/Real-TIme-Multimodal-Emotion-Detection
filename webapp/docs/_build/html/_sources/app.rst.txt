app module
==========

In general, the app.py module is Flasks working core. From here, all routes that shall be reachable from the frontend are defined.
There are three different types: routes that return an html template, routes that return data such as JSON or a video stream, and a route that returns picture files.
The working principles of the most important routes are explained in the following section.

.. automodule:: app
   :members:
   :undoc-members:
   :show-inheritance:

.. py:function:: live_data()

   Fetches audio predictions, updates global variables for further internal use and dumps them as JSON files on the live_data app route to be used in the frontend Highchart diagrams. This route is called from every other place where audio predictions are needed.
   
.. py:function:: live-data_video()

   Works similar to the live_data() function. The video live data cannot be retrieved directly from the recognizer module but is stored as a file, because the video_recognizer can only return one thing, and thats the video stream. live-data_video() therefore fetches the video predictions from the saved JSON file video_prediction.json.

.. py:function:: live-data_multi()

   Combines both functions above. This function returns a combined JSON file with multimodal emotion predictions from both the audio and video stream. The video predictions are more reliable, so the internal global variable multi_emotion is updated with weighted predictions (at the moment 70-30 video-audio).
   
.. py:function:: emotion()

   Reads in the global audio_emotion variable that is updated from live_data() and returns the matching emotion picture via Flasks send_file command. The picture is used in the html files to display a reaction.