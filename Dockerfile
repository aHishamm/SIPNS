FROM python:3.10-slim 
ADD . .
RUN pip install -r requirements.txt
EXPOSE 8500 
CMD ["python","checkssh.py"]