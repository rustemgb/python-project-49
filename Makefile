install:
	uv sync

make lint: uv run ruff check brain_games

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool uninstall hexlet-code
	uv tool install dist/*.whl
