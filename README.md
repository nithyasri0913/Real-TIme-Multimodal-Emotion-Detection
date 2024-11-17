# Real-TIme-Multimodal-Emotion-Detection



## Summary

Multimodal emotion recognition was performed by integrating voice and facial expression analysis techniques. Leveraging Short-Time Fourier Transform (STFT) and Mel-Frequency Cepstral Coefficients (MFCC) from Librosa for audio processing, alongside OpenCV for facial expression analysis from video inputs, we developed a robust system. Additionally, we incorporated decision-level fusion techniques to combine the outputs from both modalities effectively, ensuring comprehensive emotion recognition.

This fusion of techniques from computer vision and deep learning enables our system to effectively understand human emotions. The STFT and MFCC techniques capture temporal variations and spectral characteristics in audio signals, while OpenCV facilitates facial landmark detection and expression analysis from video inputs.

Our system boasts robust performance, with high accuracy and reliability in recognizing diverse emotional states. Through meticulous integration and fusion of multimodal information, we achieve enhanced emotion recognition capabilities. With potential applications in conversational agents, recommendation systems, smart homes, and beyond, our work contributes to the advancement of emotion recognition in artificial intelligence.

## Methodology 

Two separate models (audio and video) predict the emotion in parallel. The final class prediction is a weighted and combined "multimodal" prediction of the two seperate predictions.

## Training 

 - CNN - chosen model for audio and video analyzing
	
 - Audio:
	 - datasets:
		- <a href="https://zenodo.org/record/1188976">Ryerson Audio-Visual Database of Emotional Speech and Song (Ravdess)<a>
		- <a href="https://github.com/CheyneyComputerScience/CREMA-D">Crowd Sourced Emotional Multimodal Actors Dataset (CREMA-D)<a>
		- <a href="https://tspace.library.utoronto.ca/handle/1807/24487">Toronto emotional speech set (TESS)<a>
		- <a href="http://kahlan.eps.surrey.ac.uk/savee/Database.html">Surrey Audio-Visual Expressed Emotion (SAVEE) Database<a>
		- <a href="http://emodb.bilderbar.info/docu/">Berlin Database of Emotional Speech (emo-db)<a>
	
	
	
		| Emotion  | Number of Audiofiles |
		| ------------- | ------------- |
		| Angry  | 652  |
		| Fear  | 652  |
		| Happy  | 652  |
		| Sad  | 652  |
		
 	- feature sets: Zero Crossing Rate, Chroma, MFCC, Root Mean Square Value, MelSpectrogram
 	- improved by augmentation techniques: added noise, streched, shifted and pitched audio files (see jupyter training files for more details)
	
- Video: 📽️
	- dataset: <a href="https://www.kaggle.com/datasets/gauravsharma99/ck48-5-emotions">CK+48 5 emotions<a> (used 4 of them)
	
		| Emotion  | Number of Images |
		| ------------- | ------------- |
		| Angry  | 135  |
		| Fear  | 75  |
		| Happy  | 207  |
		| Sad  | 84  |
		
		ImageDataGenerator: To generate different images using e.g. rotation or zoom range 
	- feature sets: 
	- improved by: Flatten, Dropout
	
## Tech Stack

 - models trained using tensorflow in jupyter notebook
 - real-live graphs shown using highcharts.js and Ajax 
 - Webapp built with Flask
	
- Front-end:
	- Flask
	- Ajax
	- Bootstrap
- Back-end: 
	- Python
	- Keras
	- Numpy
	- OpenCV
	- Pyaudio
	- Librosa

## Requirements and installation instructions / Tutorial

 - a <a href="https://www.python.org/downloads/">python installation<a> is necessary (at least V3.7)
 - a working webcam and microphone is necessary. The input ports should be detected automatically.
 - git clone the repo
 - install the dependencies from requirements.txt (pip install -r requirements.txt)
 - run the app.py file and wait until the server is started and ready. This can take up to 2 minutes
 - open localhost <a href="https://127.0.0.1:5000/">127.0.0.1:5000/<a> on your favorite web browser
 - the usage of the application is self-explanatory
 
 ## Features
 
 - both models can be used standalone or together
	
 - Audio:
	- analyzing audio
	- displaying probability of each emotion as a real-time updating bar chart
 - Video: 
	- analyzing video and face
	- displaying probability of each emotion as a real-time updating bar chart
 - Multimodal: 
	- analyzing audio and video
	- displaying video and audio probability of each emotion as a real-time updating bubble chart 
	- combined value (70-30)
	- predicted emotion displayed using emojis 
	
## Results

 - Accuracy on test data Video: 99%
 - Accuracy on test data Audio: 91%

 ## Future Objectives
 - Explore other fusion techniques like Early Fusion.
 - Hyperparameter tuning of our deep neural network model
 - Integrate real-time noise removal feature
