from onecode import slider, file_output, Logger


def run():
    n = slider(key="Table de multiplication jusqu'à", value=5, min=1, max=100)
    output_file = file_output(key="Fichier résultat", value="multiplication.txt")

    with open(output_file, "w", encoding="utf-8") as f:
        for i in range(1, n + 1):
            f.write(f"Table de {i}:\n")
            Logger.info(f"Table de {i}:")
            for j in range(1, 11):  # Table de 1 à 10
                line = f"{i} x {j} = {i * j}"
                f.write(line + "\n")
                Logger.info(line)
            f.write("\n")
