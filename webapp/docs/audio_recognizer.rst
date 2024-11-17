audio\_recognizer module
========================

.. automodule:: audio_recognizer
   :members:
   :undoc-members:
   :show-inheritance:

.. py:function:: analyze_audio()

   This function is called from the main app.py via the live-data route. It records a 3 seconds audio snippet, saves the snippet and passes it to helper functions to analyze it.
   All important parameters can be set at the top: Sample rate, chunk size, seconds to be recorded, the microphone device index and the output filename. The audio recordings are done with the pyaudio library.
   The function uses the pretrained audio recognition model and returns a predictions array of 4 class probabilities.
   
.. py:function:: get_audio_features(path)

   This function was created for a better code structure. It loads the wave file using the librosa library. Then features are extracted using the ``extract_audio_features()`` function.
   Returns a stacked array of features: without augmentation, with noise and streched / pitched. The model was trained with the same augmentation techniques.

.. py:function:: extract_audio_features(data, sample_rate)

   A helper function that extracts audio features from a given audio file using the librosa library. The features are the zero-crossing rate of the audio time series, a chromagram from the waveform, Mel-frequency cepstral coefficients (MFCCs), the root mean square value and finally a mel-scaled spectrogram.
   The features are stacked horizontally in a numpy array.
   This function also creates and saves diagrams that are shown in the frontend.