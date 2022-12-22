import matplotlib.pyplot as plt


# By OpenAI
def generate_pie_chart():
    values = [200, 34, 120]
    labels = ['A', 'B', 'C']

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels)
    plt.title('Pie Chart')
    plt.savefig('pie.png')
    plt.close()


# By Platzi
    # plt.pie(values, labels=labels)#Except for this line, that was made by OpenAI
    # fig, ax = plt.subplots()
    # ax.pie(values, labels=labels)
    # plt.savefig('pie.png')
    # plt.close()
