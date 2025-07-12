FROM redhat/ubi8

RUN yum install python3 -y 

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "app.py"]