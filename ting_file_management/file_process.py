from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in instance._data:
        if path_file in i["nome_do_arquivo"]:
            return None

    text = txt_importer(path_file)
    result = {
      "nome_do_arquivo": path_file,
      "qtd_linhas": len(text),
      "linhas_do_arquivo": text
    }

    instance.enqueue(result)
    print(result)


def remove(instance):
    try:
        result = instance.dequeue()
        filename = result["nome_do_arquivo"]
        print(f"Arquivo {filename} removido com sucesso")
    except IndexError:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        result = instance.search(position)
        print(result)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
