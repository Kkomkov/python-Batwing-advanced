FROM  python:latest

WORKDIR  /app

COPY  ./requirementes.txt ./requirementes.txt

RUN  python -m pip install --upgrade pip && ls && pip install -r ./requirementes.txt

CMD python -v
CMD python --version
CMD  ["python","app.py"]