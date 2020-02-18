import requests
import sys
from itertools import islice
from bs4 import BeautifulSoup


def main():
    try:
        sym = sys.argv[1]
    except IndexError:
        sym = None

    if not sym:
        print("Insira uma palavra que deseja buscar o sinônimo.")
        sys.exit(-1)

    url = f'https://www.sinonimos.com.br/{sym}/'
    response = requests.get(url)

    if response.status_code != 200:
        print("Houve um problema na requisição")
        sys.exit(-1)

    content = response.text
    parser = BeautifulSoup(content, 'html.parser')

    all_sym = parser.findAll('a', {'class': 'sinonimo'})

    if not len(all_sym):
        print("Não foi encontrado nenhum sinônimo para esta palavra.")
        sys.exit(0)

    all_sym = [sym.string for sym in all_sym]
    all_rest_sym = None

    elements_by_list = 20
    total_slices = len(all_sym) // elements_by_list

    if total_slices == 0:
        total_slices = 1
        elements_by_list = len(all_sym)

    rest = len(all_sym) % elements_by_list

    if rest != 0:
        all_sym = all_sym[:-(rest)]
        all_rest_sym = all_sym[-(rest):]

    result = len(all_sym) // total_slices

    slice_iter = [10 for i in range(total_slices)]

    all_sym = iter(all_sym)

    tabbed_syms = [list(islice(all_sym, slc)) for slc in slice_iter]

    if all_rest_sym:
        tabbed_syms.append(all_rest_sym)

    print("\n")
    for tab_sym in tabbed_syms:
        print(*tab_sym, sep="   ")
        print("\n")


if __name__ == '__main__':
    main()
