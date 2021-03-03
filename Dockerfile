FROM python:3.7.2-alpine3.8
ADD sumator.py /
CMD [ "python", "/sumator.py" ]
