# 通过 make 进行任务管理
# $(HOME)/
open:
	subl statsbombpy-local.sublime-project

test:
	poetry run ruff --format=github --target-version=py310 .
	poetry run mypy .
	poetry run pytest
