'''
Saca las gráficas de los resultados obtenidos 
'''
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.express as px

def read_data(source: str, columns_name: list[str]) -> pd.DataFrame:
    '''
    - `source`: ruta y nombre del fichero a leer.
    - `columns_name`: Nombre de las columnas
    '''
    signal = pd.read_csv(
        source,
        names=columns_name,
        delimiter="|",
        skiprows=range(2),
        index_col=False,
        decimal="."
    )
    return signal

def plot_one_line(x,y, label):
    plt.plot(x,y, label=label)

# Nombre de las columnas: 
trozo_column = 'trozo'
bits_column = 'bits'
words_column = 'words'
alphabet_size_column = 'alphabet_size'
IM_column = 'IM(LP,VD)'

if __name__ == '__main__':
    alphabet = [1,2,5,10,20,50]
    top = 10
    words = {
    'C': [11,87,187], #[1,2,11,87,187],
    'R':[17,42,125],
    'G' : [66, 93,248]#[1, 2, 66, 93,248]
}
    ## __ para el trozo C __
    trozo = 'C'
    path = f'./img/SAX/trozo{trozo}/'
    print('='*20,
    f'Analizando trozo C')
    df = read_data('./experiment_results/SAX/mutual_information_C.csv',
                  ['none',trozo_column, bits_column , words_column , alphabet_size_column, IM_column])
    bits = list(range(1,9))

    # Información mutua variando bits fijando w y a 
    folder = 'bits/'
    for w in words[trozo]:
        for a in alphabet:
            new_df = df.query(f'words == {w} & alphabet_size == {a}' )
            y = new_df[IM_column].to_list()
            plot_one_line(bits, y, f'a= {a}')
        plt.title(f'Información mutua variando bits para w = {w}, a={a} para trozo {trozo}')
        plt.legend()
        plt.xlabel('Número de bits')
        plt.ylabel('IM')
        plt.savefig(path+folder+f'IM_variando_bits_w={w}', bbox_inches='tight')
        #plt.show()
        plt.close()
    
    # Conseguir el máximo y el mínimo  
    maximo = df.iloc[df[IM_column].idxmax()] 
    print(f'La IM máxima del trozo C es {maximo}.') 
    sorted_df = df.sort_values(by=IM_column,  ascending=False)
    print(f'El top de IM es de {top}')
    print(sorted_df.head(10)) 

    # Fijado un bit y tamaño de alfabeto ver cómo varía en función de w
    folder = 'palabra/'
    for a in alphabet:
        for b in bits:
            new_df = df.query(f'{alphabet_size_column} == {a} & {bits_column} == {b}' )
            y = new_df[IM_column].to_list()
            # Tamaños de w para el trozo C
            plot_one_line(words[trozo], y, f'bits= {b}')
        plt.title(f'Información mutua variando tamaño de palabra para  a={a} para trozo {trozo}')
        plt.legend()
        plt.xlabel('Tamaño de palabra')
        plt.ylabel('IM')
        plt.savefig(path+folder+f'IM_variando_palabra_a={a}', bbox_inches='tight')
        #plt.show()
        plt.close()

    # Fijado bit y palabra ver cómo influye el tamaño de alfabeto
    folder = 'alfabeto/'
    for w in words[trozo]:
        for b in bits:
            new_df = df.query(f'{words_column} == {w} & {bits_column} == {b}' )
            y = new_df[IM_column].to_list()
            # Tamaños de w para el trozo c 
            plot_one_line(alphabet, y, f'bits= {b}')
        plt.title(f'Información mutua variando tamaño alfabeto para  a={a} para trozo {trozo}')
        plt.legend()
        plt.xlabel('Tamaño de alfabeto')
        plt.ylabel('IM')
        plt.savefig(path+folder+f'IM_variando_alfabeto_w={w}', bbox_inches='tight')
        #plt.show()
        plt.close()

    # Mapas de color 
    folder = 'heatmap/'
    for b in bits: 
        new_df = df.query(f'{bits_column} == {b}' )
        fig = px.density_heatmap(new_df[[words_column, alphabet_size_column, IM_column]],
        x=words_column, 
        y=alphabet_size_column,
         z=IM_column, 
         histfunc="avg",
         title=f'IM en función del tamaño de palabra y del alfabeto para {b} bits'
        )

        fig.write_image(path+folder+f'mapaCalor_bits={b}.png')

    print(f'Imágenes guardadas en {path} con éxito')