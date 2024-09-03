FROM python:3.12.5-alpine

ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
      json-schema-for-humans==1.0.2

COPY config.json /app/config.json
COPY entrypoint.sh /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]
