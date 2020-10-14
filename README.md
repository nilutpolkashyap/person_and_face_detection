**person_and_face_detection**
Project for Person and Face Detection for public Security using the Pre-trained models from Intel Distribution of OpenVINO toolkit.
Final youtube Video Link - https://youtu.be/QiGPc9fVRfk

**Steps**
1. Download and install Anaconda Distribution of Python
2. Install all the dependencies
3. Download the Intel Distribution of OpenVINO toolkit.(My OpenVINO version - 2020.0.1.033)


**Python Virtual Environment**
1. Install virtual environment

    > pip install virtualenv

    > virtualenv --system-site-packages -p python openvinoenv

2. Activate virtual environment

    > openvinoenv\Scripts\activate

3. Running "setupvars.bat" file to set up the OpenVINO environment variables

    > cd "C:\Program Files (x86)\IntelSWTools\openvino_2020.1.033\bin\"setupvars.bat

4. Installing all the requirements from the "requirements.txt" file

    > cd "C:\Program Files (x86)\IntelSWTools\openvino_2020.1.033\deployment_tools\model_optimizer>"

    > pip install -r requirements.txt

5. Once done with OpenVINO, deactivate the environment

    > deactivate
    
**NOTE** - *I have created  a batch file named "openvinoenv.bat" to run the following steps in one singe line*

    > call "openvinoenv\Scripts\activate"call "C:\Program Files (x86)\IntelSWTools\openvino_2020.1.033\bin\setupvars.bat"

With a single line, the python virtual environment for OpenVINO toolkit can be created and the OpenVINO environment variables can be initialized.

    > openvinoenv.bat

**Pre-trained Models**

It uses the pre-trained models from the Intel OpenVino pre-trained models.

The following pre-trained models were downloaded using the model downloader

    > python "C:\Program Files (x86)\IntelSWTools\openvino\deployment_tools\open_model_zoo\tools\downloader\downloader.py"

    1. face-detection-adas-0001 - https://docs.openvinotoolkit.org/latest/omz_models_intel_face_detection_adas_0001_description_face_detection_adas_0001.html
    2. person-detection-retail-0013 - https://docs.openvinotoolkit.org/latest/omz_models_intel_person_detection_retail_0013_description_person_detection_retail_0013.html

Demonstration Videos used from the sample videos of intel-iot-devkit Github Repository. - https://github.com/intel-iot-devkit/sample-videos

**System specifications used**

- Processor - Intel Core i7 9750H

- Ram - 16 GB

- OS - Windows 10 64 bit 
