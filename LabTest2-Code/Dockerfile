FROM python:slim

WORKDIR /app

RUN pip install flask scikit-learn prometheus_client

COPY ./svm/requirements.txt ./svm/requirements.txt
RUN pip install -r ./svm/requirements.txt

COPY ./svm ./svm

EXPOSE 5002

CMD ["python", "./svm/svm_classifier.py"]