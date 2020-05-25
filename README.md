# Resume website with Flask
Flask implementation of a static resume website.

## Project tree
```
.
├── README.md
├── build
│   ├── index.html
│   └── static
│       └── main.css
├── freeze.py
├── info.yml
├── main.py
├── requirements.txt
├── static
│   └── main.css
└── templates
    ├── layout.html
    └── main.html
```

## How to run locally
* Using Python 3.8.1:
````pip install -r requirements.txt````
* ````export FLASK_APP=main.py````
* ````flask run````

## Configure content
* Add information in info.yml

## Note
* Flask Frozen is used to turn Flask application files into static ones. Files frozen prior to deployment.


## References
* https://flask.palletsprojects.com/en/1.1.x/quickstart/
* https://pythonhosted.org/Frozen-Flask/
* https://medium.com/@francescaguiducci/how-to-build-a-simple-personal-website-with-python-flask-and-netlify-d800c97c283d
* https://themes.3rdwavemedia.com/demo/orbit/