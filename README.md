# Real-TIme-Multimodal-Emotion-Detection



## Objective

The objective of this project is to train and deploy a microservice that detects the current emotion of a user based on his voice and facial expression from a webcam and microphone inputs.

## Methodology 

Two separate models (audio and video) predict the emotion in parallel. The final class prediction is a weighted and combined "multimodal" prediction of the two seperate predictions.

## Overview 👓

<a href="https://github.com/wintechis/emotion-detection-and-reaction/tree/main/SER">Train model Audio<a>
	
<a href="https://github.com/wintechis/emotion-detection-and-reaction/tree/main/FacialEmotion">Train model Video<a>
	
<a href="https://github.com/wintechis/emotion-detection-and-reaction/tree/main/webapp/models">h5 files<a> 
	
<a href="https://github.com/wintechis/emotion-detection-and-reaction/tree/main/webapp">Webapp<a> 

## Training 📉

 - CNN as chosen models for audio and video analyzing
	
 - Audio:🎧
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
	
## Deployment Tech Stack💻

 - models trained using tensorflow and jupyter notebooks
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
	- CV2
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
	
 - Audio:🎧
	- analyzing audio
	- displaying probability of each emotion as a real-time updating bar chart
 - Video: 📽️
	- analyzing video and face
	- displaying probability of each emotion as a real-time updating bar chart
 - Multimodal: 🎧📽️
	- analyzing audio and video
	- displaying video and audio probability of each emotion as a real-time updating bubble chart (no multimodality yet!)
	- combined value (70-30)
	- reaction to human by displaying emoji of predicted emotion (multimodality used!)
	
## Results

 - Accuracy on test data Video: 99%
 - Accuracy on test data Audio: 91%

 ## Future Objectives
 - Explore other fusion techniques like Early Fusion.
 - Hyperparameter tuning of our deep neural network model
 - Integrate real-time noise removal feature
