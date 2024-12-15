install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool uninstall hexlet-code
	uv tool install dist/*.whl

