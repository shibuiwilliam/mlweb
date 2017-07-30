# mlweb
This is a simple demo of using prediction model of random forest classifier, trained with scikit-learn, on a website.
Using classification model of a famous Iris dataset, this website provides classification according to your input of iris parameters: sepal length, sepal width, petal length and petal width.
The model is trained with random forest classifier in scikit-learn, with GridSearchCV and saved as "rfcParam.pkl".
You can retrain the model using "iris_train.ipynb".

## Usage
This website is developed and tested on CentOS 7.3 with Python 3.6. You need Python, flask, wtform, scikit-learn and their dependencies to run the website.
You also need Jupyter Notebook to retrain the model.

1. Copy the repository

```
git clone https://github.com/shibuiwilliam/mlweb.git
```

2. Set OS security to allow port 5000 and external access.

3. Run website

```
python web.py
```

4. You can access the website on port 5000.
ie: http://<your ip address>:5000/

5. To retrain the model, edit "iris_train.ipynb" and save the model as "rfcParam.pkl".

