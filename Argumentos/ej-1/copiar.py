import argparse


def main():
    parser = argparse.ArgumentParser(description="Copiar archivos")
    parser.add_argument('-i', '--input', type=str, help='Archivo que desa copiar')
    parser.add_argument('-o', '--output', type=str, help='Archivo de destino')
    args = parser.parse_args()

    print('Input: ', args.input)
    print('Output: ', args.output)

    with open(args.input, 'r') as inputfile:
        with open(args.output, 'w') as outputfile:
            outputfile.write(inputfile.read())

if __name__ == '__main__':
    main()