FROM python:3.9

WORKDIR /app

COPY ./backend /app

RUN pip install -r requirements.txt

# CMD ["bash" , "run_server.sh"]
CMD ["python3" ,"-m" ,"fastapi" ,"run", "src/main_route.py"]