FROM python:3.10.5-slim-bullseye
WORKDIR /app
RUN python3 -m pip install --upgrade pip && \
    pip3 install telethon discord
COPY forwarder.py .
ENTRYPOINT [ "bash" ]
