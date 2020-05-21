from operator import itemgetter
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

headers = ['Piloto', 'Corridas', 'PRI', 'SEG', 'TER', 'Pódios', 'Poles', 'Voltas', 'Mais rápidas', 'Pontos']
col_podios_ndex = headers.index('Pódios')
col_pilotos_index = headers.index('Piloto')
data = [
    ["Ayrton Senna", 16, 6, 2, 3, 11, 10, 895, 2, 78],
    ["Alain Prost", 16, 5, 2, 2, 9, 0, 859, 2, 73],
    ["Nelson Piquet", 16, 2, 1, 1, 4, 0, 958, 0, 44],
    ["Nigel Mansell", 16, 1, 3, 1, 5, 3, 886, 3, 37],
    ["Thierry Boutsen", 16, 1, 1, 1, 3, 1, 793, 1, 34],
    ["Riccardo Patrese", 16, 1, 0, 0, 1, 0, 915, 4, 23],
    ["Gerhard Berger", 16, 0, 2, 5, 7, 2, 946, 3, 43],
    ["Aguri Suzuki", 16, 0, 0, 1, 1, 0, 620, 0, 6],
    ["Éric Bernard", 16, 0, 0, 0, 0, 0, 692, 0, 5],
    ["Derek Warwick", 16, 0, 0, 0, 0, 0, 746, 0, 3],
    ["Stefano Modena", 16, 0, 0, 0, 0, 0, 619, 0, 2],
    ["Nicola Larini", 16, 0, 0, 0, 0, 0, 842, 0, 0],
    ["Jean Alesi", 15, 0, 2, 0, 2, 0, 724, 0, 13],
    ["Satoru Nakajima", 15, 0, 0, 0, 0, 0, 546, 0, 3],
    ["Pierluigi Martini", 15, 0, 0, 0, 0, 0, 593, 0, 0],
    ["Andrea de Cesaris", 15, 0, 0, 0, 0, 0, 483, 0, 0],
    ["Philippe Alliot", 15, 0, 0, 0, 0, 0, 743, 0, 0],
    ["Alessandro Nannini", 14, 0, 1, 2, 3, 0, 738, 1, 21],
    ["Ivan Capelli", 14, 0, 1, 0, 1, 0, 579, 0, 6],
    ["Emanuele Pirro", 14, 0, 0, 0, 0, 0, 337, 0, 0],
    ["Michele Alboreto", 13, 0, 0, 0, 0, 0, 624, 0, 0],
    ["Martin Donnelly", 13, 0, 0, 0, 0, 0, 509, 0, 0],
    ["Alex Caffi", 11, 0, 0, 0, 0, 0, 602, 0, 2],
    ["Maurício Gugelmin", 11, 0, 0, 0, 0, 0, 467, 0, 1],
    ["Olivier Grouillard", 9, 0, 0, 0, 0, 0, 417, 0, 0],
    ["Paolo Barilla", 8, 0, 0, 0, 0, 0, 406, 0, 0],
    ["David Brabham", 8, 0, 0, 0, 0, 0, 227, 0, 0],
    ["Gregor Foitek", 7, 0, 0, 0, 0, 0, 299, 0, 0],
    ["Roberto Moreno", 5, 0, 1, 0, 1, 0, 200, 0, 6],
    ["Yannick Dalmas", 5, 0, 0, 0, 0, 0, 223, 0, 0],
    ["Jyrki Järvilehto", 5, 0, 0, 0, 0, 0, 222, 0, 0],
    ["Gabriele Tarquini", 4, 0, 0, 0, 0, 0, 178, 0, 0],
    ["Gianni Morbidelli", 3, 0, 0, 0, 0, 0, 102, 0, 0],
    ["Johnny Herbert", 2, 0, 0, 0, 0, 0, 88, 0, 0],
    ["Bernd Schneider", 1, 0, 0, 0, 0, 0, 70, 0, 0],
]


# Filtrar arrays filhos por valor minimo em um coluna
def filter_data_list(data_list, col_index, min_value):
    filtered = []
    for item in data_list:
        if(item[col_index] >= min_value):
            filtered.append(item)

    # return filtered
    return sorted(filtered, key=itemgetter(col_index), reverse=True)


def extract_list(index, data_list):
    extracted = []
    for item in data_list:
        extracted.append(item[index])

    return extracted


def plot(podios, pilotos):
    indexes = np.arange(len(podios))

    f = plt.figure()
    plt.barh(indexes, podios)
    plt.yticks(indexes, pilotos)

    # criar ticks em X de 0 ao maior número de podios
    x_tick_list = list(range(0, max(podios) + 1))
    plt.xticks(x_tick_list)

    plt.title('Ranking do Pódios por piloto')
    plt.xlabel('Pódios')

    plt.show()

    f.savefig("podios.pdf")


filtered = filter_data_list(data, col_podios_ndex, 1)
pilotos_ext = extract_list(col_pilotos_index, filtered)
podios_ext = extract_list(col_podios_ndex, filtered)

plot(podios_ext, pilotos_ext)
