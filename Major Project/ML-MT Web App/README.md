# ML-MT Web App
## Overview
This is a Machine Learning (ML) and Medical Technology (MT) web application that allows users to predict and detect various diseases using a range of ML models. The project is built using the Streamlit library and currently includes prediction models for five diseases:

1. Breast Cancer Classification
2. Diabetes Prediction
3. Heart Disease Prediction
4. Lung Cancer Prediction
5. Parkinson's Disease Detection
   
In addition to these existing features, there are plans to expand the application to include two more disease prediction modules:

1. Malaria Detection: Utilizing cell images for detecting malaria.
2. Pneumonia Detection: Using chest X-ray images for pneumonia diagnosis.

These two additions will be developed as future enhancements to the project.

## Getting Started
To use the ML-MT web app locally, follow these steps:
1. Clone the repository to your local machine:
   git clone https://github.com/yourusername/ML-MT-Web-App.git
2. Navigate to the project directory:
   cd ML-MT-Web-App
3. Install the required Python packages:
   pip install -r requirements.txt
4. Run the Streamlit app:
   streamlit run app.py
5. The app should now be accessible in your web browser at http://localhost:8501.

## How to Use
Upon launching the web app, you will see a menu on the left-hand side listing the available disease prediction modules.
Select a disease prediction module of your choice by clicking on it.
Depending on the selected module, you may be prompted to input specific data or parameters (e.g., age, gender, test results).
After providing the necessary input, click the "Predict" button.
The model will process your input and provide a prediction or diagnosis on the right-hand side of the app interface.
For the future enhancements (Malaria and Pneumonia detection), these modules will be added to the menu once they are developed.
Future Scope
The project's future scope includes:

## Malaria Detection
A deep learning model will be implemented to analyze cell images for the detection of malaria. Users will be able to upload cell images, and the model will provide a diagnosis based on the presence or absence of malaria parasites.

## Pneumonia Detection
A deep learning model will be developed to analyze chest X-ray images for the detection of pneumonia. Users will be able to upload X-ray images, and the model will diagnose whether pneumonia is present.

These future enhancements will expand the capabilities of the ML-MT web app, providing users with additional tools for disease diagnosis and detection.

### Contributors
Shyam Singh - Project Lead and Developer

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Special thanks to the developers and contributors of the Streamlit library for making the creation of this web app possible.
Acknowledgment to the dataset providers and the open-source ML community for their valuable resources and tools.
