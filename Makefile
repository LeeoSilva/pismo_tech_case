.PHONY: start test db_upgrade db_downgrade

start:
	docker exec -it pismo_app bash -c "poetry run python -m uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload"

test: 
	docker exec -it pismo_app bash -c "poetry run pytest --cov=src --cov-report=term-missing -vvv"

docker-build: 
	docker compose up -d 

db_upgrade: 
	docker exec -it pismo_app bash -c "poetry run alembic upgrade head"

db_downgrade:
	docker exec -it pismo_app bash -c "poetry run alembic downgrade base"

db_console: 
	docker exec -it pismo_db bash -c "psql -U postgres -d pismo_tech_case"
