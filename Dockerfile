FROM python:3.11.5-alpine AS builder-base

ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_NO_INTERACTION=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
RUN apk --update add --no-cache gcc musl-dev libffi-dev
RUN pip install poetry

WORKDIR /project
COPY pyproject.toml .

RUN poetry install --no-ansi --no-root --no-cache

FROM python:3.11.5-alpine AS final

ENV APP_PATH=/project
ENV PYTHONPATH=$APP_PATH/src
ENV COVERAGE_FILE=/tmp/coverage
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTEST_ADDOPTS="-p no:cacheprovider"
ENV PATH="$APP_PATH/.venv/bin:$PATH"

RUN adduser --system --uid 101 python-user && \
    apk update && apk add --no-cache make && \
    rm -rf /var/cache/apk/*


WORKDIR $APP_PATH
COPY --from=builder-base  $APP_PATH/.venv/ $APP_PATH/.venv/

# копирование файлов с установкой прав доступа
COPY --chown=root:root --chmod=u=rwX,g=rX,o=rX src src
COPY Makefile .
COPY pyproject.toml .

EXPOSE 8080

USER python-user

ENTRYPOINT ["python", "main.py"]
