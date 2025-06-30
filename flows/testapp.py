from onecode import slider, file_output, Logger


def run():
    n = slider("Table de multiplication jusqu’à", value=5, min=1, max=100)
    output_file = file_output("Fichier résultat", "multiplication.txt")

    with open(output_file, "w", encoding="utf-8") as f:
        for i in range(1, n + 1):
            line = f"{i} x {i} = {i * i}"
            f.write(line + "\n")
            Logger.info(line)
