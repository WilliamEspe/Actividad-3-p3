from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Leer el archivo CSV
    df = pd.read_csv('7817_1.csv')

    # Crear la columna 'resumen_limpio' para limpiar saltos de línea y espacios redundantes
    df['resumen_limpio'] = df['reviews.text'].str.replace(r'\\n|\n|\r', ' ', regex=True).str.strip()

    # Utilizar 'resumen_limpio' para la columna 'Reseña'
    df['Reseña'] = df['resumen_limpio'].apply(lambda x: x[:100] + '...' if len(x) > 100 else x)

    # Formatear la fecha para mostrar solo año, mes y día
    df['reviews.date'] = pd.to_datetime(df['reviews.date'], errors='coerce').dt.strftime('%Y-%m-%d')

    # Cambiar nombres de columnas
    df.rename(columns={
        'name': 'Nombre del Producto',
        'reviews.date': 'Fecha de la Reseña',
        'Reseña': 'Reseña',
        'sentimiento': 'Valoración'
    }, inplace=True)

    # Seleccionar las columnas a mostrar
    columnas_mostradas = ['Nombre del Producto', 'Fecha de la Reseña', 'Reseña', 'Valoración']

    # Generar tabla HTML con los datos formateados
    return render_template('index.html', df=df, columnas_mostradas=columnas_mostradas)

if __name__ == '__main__':
    app.run(debug=True)
