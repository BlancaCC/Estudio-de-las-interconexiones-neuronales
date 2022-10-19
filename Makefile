all: render

## Órdenes de compilación
preview:
	quarto preview
render:
	quarto render --to pdf
	open Renders/Memoria.pdf

## Experimentos
experimento_umbrales:
	python src/experiment_gets_threshold.py