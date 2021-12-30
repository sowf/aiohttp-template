FROM python:3.7-alpine

WORKDIR /opt

COPY requirements.txt .

RUN apk add --no-cache python3 postgresql-libs curl && \
    apk add --no-cache --virtual .build-deps git gcc python3-dev musl-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

COPY . .
COPY settings/local.py.default settings/local.py

EXPOSE 80

HEALTHCHECK --interval=5s --timeout=5s --retries=5 --start-period=5s CMD curl -f 0.0.0.0/healthcheck || exit 1
ENTRYPOINT ["python", "manage.py"]
CMD ["run"]
