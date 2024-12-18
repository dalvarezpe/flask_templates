from flask import Flask, render_template
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)

@app.route('/')
def show_graph():
    # Datos para el gráfico
    subjects = ['Physics', 'Maths', 'Chemistry', 'Hindi', 'English']
    marks = [80, 85, 90, 70, 75]  # Datos ficticios

    # Crear el gráfico con Plotly
    fig = go.Figure(data=[go.Bar(x=subjects, y=marks, marker_color='blue')])
    fig.update_layout(
        title="Marks Distribution",
        xaxis_title="Subjects",
        yaxis_title="Marks",
        plot_bgcolor="white",
        margin=dict(l=40, r=40, t=40, b=40)
    )

    # Renderizar el gráfico como HTML
    graph = pio.to_html(fig, full_html=False)

    return render_template('home.html', graph=graph)

if __name__ == '__main__':
    app.run(debug=True)
