.PHONY: start test db_upgrade db_downgrade


db_upgrade: 
	docker exec -it pismo_app bash -c "poetry run alembic upgrade head"

db_downgrade:
	docker exec -it pismo_app bash -c "poetry run alembic downgrade base"

test: 
	docker exec -it pismo_app bash -c "poetry run pytest --cov=src --cov-report=term-missing -vvv"

start:
	docker exec -it pismo_app bash -c "poetry run python -m gunicorn src.main:app --bind 0.0.0:8000 --reload"

docker-build: 
	docker compose up -d 

db_console: 
	docker exec -it pismo_db bash -c "psql -U postgres -d pismo_tech_case"
