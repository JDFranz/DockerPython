FROM python:3.11.1-alpine3.17

WORKDIR /project
COPY ./ /project

# If you have working ssl files uncomment those below:
# COPY ./certificates/SSL/CERT.cer /project/certificates/SSL/CERT.cer
# COPY ./certificates/SSL/KEY.key  /project/certificates/SSL/KEY.key
# RUN chmod 777 /project/certificates/SSL/KEY.key
# RUN chmod 777 /project/certificates/SSL/CERT.cer


# required for installing pandas numpy and some other libs
RUN apk add g++ cargo gcc python3-dev libffi-dev musl-dev zlib-dev jpeg-dev
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r ./pip3Requirements.txt

CMD ["python", "main.py"]