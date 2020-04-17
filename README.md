# Produce Item Recognition Application For Retail Stores Based on Machine Learning	

For user guide please refere - https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN/blob/master/PIR-User%20Guide.pdf
For setup plaese refere- https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN/blob/master/PIR-Setup%20Guide.pdf


<b>1) Introduction</b>
<p>
Produce is the generalized term for farm raised crops which includes fruits and vegetables. This same term is well adopted by most retail stores in Canada to describe the section where fruits and vegetables are kept in stores. Produce section in retail stores have items which are not UPC tagged thus making the self-checkout process difficult for both the customer and employees. We approached this problem with the help of image recognition with the help of data analytic life cycle. In this file, we will be explaining in detail how to set up environment and execute files for the produce item prediction. </P><br><br>
<b>Solution Overview</b>

 <img src="https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN/blob/master/PIR-Images/Solution%20Overwiew.PNG" alt="Smiley face" >
 
 <br>
<b>2) Model Execution Steps</b>
  <p>
  This project can be executed on your local system or on google colab. First We will be talking about on how to execute on your local system.</p>
  
 <b> 2.1) To execute on local system</b>-
        Local Environment has to be setup  first. For this we have to verify our hardware and software configuration first.<br>
        
 <b> Required Hardware Configuration </b> - NVIDIA® GPU card with CUDA® Compute Capability 3.5 or higher<br>
  
 <b> Required Software Configuration </b>- NVIDIA® GPU drivers —CUDA 10.1 requires 418.x or higher. CUDA® Toolkit —TensorFlow       supports CUDA 10.1 (TensorFlow >= 2.1.0) CUPTI ships with the CUDA Toolkit. cuDNN SDK (>= 7.6)<br><br>
 
 After making sure of hardware and software environment following steps must be performed-<br>
 
 step a: Install Anaconda from  https://www.anaconda.com/ <br>
 
 step b: Open Anacond Navigator and click on console option <br>
 
 step c: Install tensorflow in anaconda with the following commands <br>
 &emsp;&emsp;&emsp;conda create -n tf tensorflow<br>
 &emsp;&emsp;&emsp;conda activate tf<br>
 
 step d: Clone github repository from the command line <br> git clone https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN.git <br>
 
 step e:  execute <i>cd ProduceItemRecognitionUsingCNN</i> to navigate to repository and install required libraries with the below command<br>
 &emsp;&emsp;&emsp; pip install -r requiremnets.txt
 
 step f: Open jupyter notebook with the tf environment and execute all the steps in all three model files. Model files listed below. <br>
&emsp;&emsp;&emsp;  (Change dataset path, and  model save and load path in ipynb file according to your local system)<br>
 &emsp;&emsp;&emsp;  PIR-CNN-rmsprop-bs16-ep10.ipynb 	<br>
  &emsp;&emsp;&emsp;
 PIR-Resnet50-rmsprop-bs5-epoch5.ipynb	<br>
  &emsp;&emsp;&emsp;
 PIR-VGG16_sgd-bs32-epoch11.ipynb
 <br><br>
 step g: can see final result- classification report, confusion matrix and prediction for all the three models in your notebook.<br><br>
 
<b> 2.2)To execute on google colab</b> - <br>
 
 step a: we just need  plotly library, remaining libraries comes with the google colab. We can install Plotly with the below command <br>
&emsp;&emsp;&emsp; !pip install plotly<br>

step b: project can be extracted to your own drive with the below link. <br>
&emsp;&emsp;&emsp;
https://drive.google.com/open?id=1a9G7L8ztvcolDm6HJ9IDBAzveIQjIgU0 <br>

 step c: Open colab notebook and execute all the steps in all three model files. Model files listed below. <br>
&emsp;&emsp;&emsp;  (Change dataset path, and  model save and load path in ipynb file according to your drive location)<br>
 &emsp;&emsp;&emsp;  PIR-CNN-rmsprop-bs16-ep10.ipynb 	<br>
  &emsp;&emsp;&emsp;
 PIR-Resnet50-rmsprop-bs5-epoch5.ipynb	<br>
  &emsp;&emsp;&emsp;
 PIR-VGG16_sgd-bs32-epoch11.ipynb
 <br><br>
 step d:  can see final result- classification report, confusion matrix and prediction for all the three models in your notebook.<br><br>
 <br>
 <b>Train loss vs Validation loss </b><br>
 <img src="https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN/blob/master/PIR-Images/loss.PNG" alt="Smiley face" >

 <br><br>
 <b>Train accuracy vs Validation accuracy</b><br>
 <img src="https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN/blob/master/PIR-Images/accuracy.PNG" alt="Smiley face" >

 <br><br>
 <b>Classification Report</b><br>
 <img src="https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN/blob/master/PIR-Images/classification%20report.PNG" alt="Smiley face" >

 <br><br>
 <b>Confusion Matrix</b><br>
<img src="https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN/blob/master/PIR-Images/confusion%20matrix.PNG" alt="Smiley face" >

<br><br>
<b> Results </b><br>
<img src="https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN/blob/master/PIR-Images/FinalResults.PNG" alt="Smiley face" >

 
 <b>3) Kivy Application</b><br>
  If you are executing only application and don't bother to run model, you might have to follow only below few steps and can ignore all above steps. If you have alredy installed  all libraries mentioned in above steps, no need to follow below steps. <br><br>
  
  step a: Follow step a to c from the section 2.1<br><br>
  step b: Download kivy application code from the below command<br>
  git clone https://github.com/AdarshKoppManjunath/PIR--Kivy-Application.git<br><br>
  step c: Execute  any of below command to install kivy <br><br><i>
  conda install -c conda-forge kivy<br>
  conda install -c conda-forge/label/cf201901 kivy<br>
  conda install -c conda-forge/label/cf202003 kivy</i><br><br>
  
Navigate to <b><i>cd PIR--Kivy-Application</i></b><br>
Execute <b></i>python main.py</i></b><br>
  
 
<b>4) Screenshots</b><br><br>

<b> Open Camera </b>
  
<img src="https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN/blob/master/PIR-Screenshots/Open%20Camera.PNG" alt="Smiley face" > <br><br>
  
  
 <b> Capture Image </b>
  
<img src="https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN/blob/master/PIR-Screenshots/Capture.PNG" alt="Smiley face" ><br><br>

<b> Results of different produce items</b><br><br>
 
 <img src="https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN/blob/master/PIR-Screenshots/Apple.PNG" alt="Smiley face" >
 <img src="https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN/blob/master/PIR-Screenshots/Bannana.PNG" alt="Smiley face" >
 <img src="https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN/blob/master/PIR-Screenshots/Brocolli.PNG" alt="Smiley face" >
 <img src="https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN/blob/master/PIR-Screenshots/Pineapple.PNG" alt="Smiley face" >
 <img src="https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN/blob/master/PIR-Screenshots/redchilli.PNG" alt="Smiley face" >
 <img src="https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN/blob/master/PIR-Screenshots/CarrotPrediction.PNG" alt="Smiley face" >

<br><br><br>

<b>5) Contributors </b><br><br>
  
1) DataSet - <br>
&emsp;&emsp;&emsp;  Iveatu Jane Obioha: Captured Fruits and Vegetable Videos<br>
&emsp;&emsp;&emsp;  Adarsh Koppa Manjunath: Videos and DataSet preparation<br><br>

2) Model Development-<br>
&emsp;&emsp;&emsp; Adarsh Koppa Manjunath: Data Preprocessing, Data Visualization, Model Training and Testing, and Testing Metrics<br><br>

3) Kivy Application-<br>
&emsp;&emsp;&emsp;  Stephen Oluwatobi Bello: Kivy Application UI development<br>
&emsp;&emsp;&emsp;  Adarsh Koppa Manjunath: Model Integration


<br><br>
<b>Contact Information:</b><br>
Name: Adarsh Koppa Manjunath<br>
Email: adarshkoppamanjunath@gmail.com
