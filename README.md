# Produce Item Recognition

<b>1) Introduction</b>
<p>
Produce is the generalized term for farm raised crops which includes fruits and vegetables. This same term is well adopted by most retail stores in Canada to describe the section where fruits and vegetables are kept in stores. Produce section in retail stores have items which are not UPC tagged thus making the self-checkout process difficult for both the customer and employees. We approched this problem with the help of image recognition with the help of data analytic life cycel. In this file, we will be explaining in detail how to set up environment and execute files for the produce item prediction. </P>

<b>2) Project Execution Steps</b>
  <p>
  This projecte can be executed on your local system or on google colab. First We will be talking about on how to execute on your local system.</p>
  
 <b> 2.1) To execute on loacl system</b>-
        Local Environment has to be setup  first. For this we have to verify our hardware and software configuration first.<br>
        
 <b> Required Hardware Configuration </b> - NVIDIA® GPU card with CUDA® Compute Capability 3.5 or higher<br>
  
 <b> Required Software Configuration </b>- NVIDIA® GPU drivers —CUDA 10.1 requires 418.x or higher. CUDA® Toolkit —TensorFlow       supports CUDA 10.1 (TensorFlow >= 2.1.0) CUPTI ships with the CUDA Toolkit. cuDNN SDK (>= 7.6)<br><br>
 
 After making sure of hardware and software environment following steps has to be performed-<br>
 
 step a: Install Anaconda from  https://www.anaconda.com/ <br>
 
 step b: Open Anacond Navigator and click on console option <br>
 
 step c: Install tensorflow in anaconda with the following commands <br>
 &emsp;&emsp;&emsp;conda create -n tf tensorflow<br>
 &emsp;&emsp;&emsp;conda activate tf<br>
 
 step d: Clone github repository from the command line <br> git clone https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN.git <br>
 
 step e:  execute <i>cd ProduceItemRecognitionUsingCNN</i> to navigate to repository and install depending libraries with the below command<br>
 &emsp;&emsp;&emsp; pip install -r requiremnets.txt
 
 step f: Open jupyter notebook with the tf environment and execute all the steps in all three model files. Model files listed below. <br>
&emsp;&emsp;&emsp;  (Change dataset path, and  model save and load path in ipynb file according to your local system)<br>
 &emsp;&emsp;&emsp;  PIR-CNN-rmsprop-bs16-ep10.ipynb 	<br>
  &emsp;&emsp;&emsp;
 PIR-Resnet50-rmsprop-bs5-epoch5.ipynb	<br>
  &emsp;&emsp;&emsp;
 PIR-VGG16_sgd-bs32-epoch11.ipynb
 <br><br>
 step g: you can see final result- classification report, confusion matrix and prediction for all the three models in your notebook.<br><br>
 
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
 step d: you can see final result- classification report, confusion matrix and prediction for all the three models in your notebook.<br><br>
 <br>
 
 <b>3) Kivy Application</b><br>
  If you are executing only application and don't bother to run model, you might have to follow only below few steps and can ignore all above steps. If you have alredy installed  all libraries mentioned in above steps, no need to follow below steps. <br><br>
  
  step a) Follow step a to c from the section 2.1<br>
  step b) Download kivy application code from the below command<br>
  git clone https://github.com/AdarshKoppManjunath/PIR--Kivy-Application.git<br>
  step c) Execute  any of below command to install kivy <br><br><i>
  conda install -c conda-forge kivy<br>
  conda install -c conda-forge/label/cf201901 kivy<br>
  conda install -c conda-forge/label/cf202003 kivy</i><br><br>
  
Navigate <b>cd PIR--Kivy-Application<b><br>
Execute <b>python main.py<b><br>
  
  
  
  
  
  
     
        
        
        
        
<img src="https://github.com/AdarshKoppManjunath/ProduceItemRecognitionUsingCNN/blob/master/PIR-Screenshots/Apple.PNG" alt="Smiley face" >


Step 1: DataSet can be downloaded either using github or using google drive         (https://drive.google.com/openid=1zGn8_CsleUBuRMfVG7JYnwqjaQtBp5Gl)





Finally to test model through UI, we have a kivy application, but it's not packaged to exe. Howerver, On Installing Kivy on your windows machine along with the Tensorflow will help in running the code. 
