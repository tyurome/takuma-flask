Pythonを用いたWeb開発講義資料　　  
現状はDocker環境を想定、requirements.txtをpip installして生でmain.pyを叩けばローカル  
検証済みpython verは3.11　　

    .
    ├── Dockerfile
    ├── README.md
    ├── app
    │   ├── controller.py
    │   ├── data
    │   │   ├── test.csv
    │   │   └── train.csv
    │   ├── instance
    │   │   └── database.db
    │   ├── main.py
    │   ├── models.py
    │   ├── static
    │   └── templates
    │       ├── base.html
    │       ├── home.html
    │       ├── login.html
    │       └── register.html
    ├── docker-compose.yml
    └── requirements.txt


使用パッケージ（requirements.txt）  
Flask==2.3.3  
flask_login  
flask_sqlalchemy  
werkzeug  
#以下データ分析用  
numpy  
pandas  
matplotlib  
scikit-learn  
joblib  
