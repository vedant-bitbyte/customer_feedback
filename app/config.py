class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/feedback_system'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'  
