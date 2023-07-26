import matplotlib.pyplot as pylt


def generate_pie_chart():
    labels = [ 'A', 'B', 'C' ]
    values = [ 200, 34, 120 ]

    fig, ax = pylt.subplots()
    ax.pie(values, labels=labels)
    pylt.savefig('./pie.png')
    pylt.close()