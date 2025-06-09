FROM python:3.11-slim AS python
	SHELL ["/bin/bash", "-c"]

	RUN apt-get update && apt-get install -y --no-install-recommends \
		build-essential \ 
		make \ 
		git 

FROM python AS base 
	RUN pip install poetry==1.8.3
	RUN poetry config virtualenvs.create false

	ENV APP_PATH=/var/app
	WORKDIR $APP_PATH

	ENV PYTHONPATH=$APP_PATH

	COPY ./pyproject.toml ./poetry.lock* ./


FROM base AS development 
	RUN poetry lock && poetry install --no-interaction --no-ansi --no-root

