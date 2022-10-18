all: render
preview:
	quarto preview
render:
	quarto render --to pdf
	open Renders/Memoria.pdf