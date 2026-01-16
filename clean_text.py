def clean_text(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if line:
            cleaned_lines.append(line)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(cleaned_lines))


if __name__ == "__main__":
    clean_text("input.txt", "output.txt")
    print("Text cleaned successfully. Output saved to output.txt")
