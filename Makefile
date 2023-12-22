# 通过 make 进行任务管理
# $(HOME)/
open:
	subl statsbombpy-local.sublime-project

test:
	poetry run ruff .
	poetry run mypy .
	poetry run pytest
