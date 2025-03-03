from setuptools import setup, find_packages

setup(
    name="llm_evaluation_app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.109.2",
        "uvicorn==0.27.1",
        "python-multipart==0.0.9",
        "pillow==10.2.0",
        "boto3==1.34.34",
        "python-dotenv==1.0.1",
        "pydantic==2.6.1",
        "requests==2.31.0"
    ]
)