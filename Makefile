all: render

## Órdenes de compilación
preview:
	quarto preview
render:
	quarto render --to pdf
	open Renders/Memoria.pdf

## Experimentos
experimento_umbrales:
	python src/experiment_gets_threshold.py > ./experiment_results/get_threshold_nuevo.txt &
	python src/experiment_gets_threshold.py

plot_experimental_thresholds:
	python src/experiment_view_threshold.py

calcular_informacion_mutua:
	python src/experiment_gets_muaual_information.py > ./experiment_results/mutual_information.txt &
	python src/experiment_gets_muaual_information.py > ./experiment_results/mutual_information.txt 

calcular_informacion_mutua_paralelo:
		python src/experiment_gets_muaual_information.py C > ./experiment_results/mutual_information_C.txt &
		python src/experiment_gets_muaual_information.py R > ./experiment_results/mutual_information_R.txt &
		python src/experiment_gets_muaual_information.py G > ./experiment_results/mutual_information_G.txt &

# Calcula cuál es la mejor distnacia de ventana 
calcular_distancia_spike:
		python src/spike_distance.py

calcular_informacion_ventana_grande_mutua_paralelo:
		python src/experiment_get_transformed_mutual_information.py C > ./experiment_results/transformed_mutual_information_C.txt &
		python src/experiment_get_transformed_mutual_information.py R > ./experiment_results/transformed_mutual_information_R.txt &
		python src/experiment_get_transformed_mutual_information.py G > ./experiment_results/transformed_mutual_information_G.txt &

calcular_entropia_normalizada:
		python src/experiment_get_transformed_normalized_mutual_information.py C > ./experiment_results/entropia_mutua_normalizada/entropia_mutua_normalizada_C.txt &
		python src/experiment_get_transformed_normalized_mutual_information.py R > ./experiment_results/entropia_mutua_normalizada/entropia_mutua_normalizada_R.txt &
		python src/experiment_get_transformed_normalized_mutual_information.py G > ./experiment_results/entropia_mutua_normalizada/entropia_mutua_normalizada_G.txt &

calcular_sax:
	python src/experiment_sax_mi.py C > ./experiment_results/SAX/mutual_information_C.csv &
	python src/experiment_sax_mi.py R > ./experiment_results/SAX/mutual_information_R.csv &
	python src/experiment_sax_mi.py G > ./experiment_results/SAX/mutual_information_G.csv &