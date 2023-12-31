<h1 align="center"> X-ray Bone Fracture Classifier</h1> <p align="center"> <a href="https://github.com/abhinavmishra/X-ray-Bone-Fracture-Classifier/issues"> <img alt="Issues" src="https://img.shields.io/github/issues/abhinavmishra/X-ray-Bone-Fracture-Classifier?style=flat-square" /> </a> <a href="https://github.com/abhinavmishra/X-ray-Bone-Fracture-Classifier/pulls"> <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/abhinavmishra/X-ray-Bone-Fracture-Classifier?style=flat-square" /> </a> <a href="https://github.com/abhinavmishra/X-ray-Bone-Fracture-Classifier/blob/master/LICENSE"> <img alt="License" src="https://img.shields.io/github/license/abhinavmishra/X-ray-Bone-Fracture-Classifier?style=flat-square" /> </a> </p>
Introduction
This project aims to develop a web application to classify X-ray images of bones into two categories - Fractured and Not Fractured.

Installation
Clone the repository and install the dependencies using pip.

bash
Copy code
git clone https://github.com/abhinavmishra/X-ray-Bone-Fracture-Classifier.git
cd X-ray-Bone-Fracture-Classifier
pip install -r requirements.txt
Usage
Run the application using the following command.

bash
Copy code
uvicorn main:app --reload
API Reference
The application exposes a single endpoint /predict which accepts a file in jpeg or png format. The endpoint returns a JSON object containing the prediction class and its probability.

Example usage:

bash
Copy code
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@test.jpg" http://localhost:8000/predict
Example response:

json
Copy code
{
    "prediction": "Fractured",
    "probability": 0.975
}
Contributing
Feel free to contribute to this project by raising issues or submitting pull requests. Please ensure you follow the existing coding style and use clear and concise commit messages.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

