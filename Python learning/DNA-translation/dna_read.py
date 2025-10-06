from proteins import proteins_dict

def protein_start_translate(dna_string):
    print("\n__________________")
    print("Translating protein sequence\n")
    print(f"mRNA: {dna_string}")
    input("Press enter to continue...")
    dna_string_list = list(dna_string)
    try:

        for cell_index in range(len(dna_string_list)):
            print(dna_string_list[cell_index])
            print(dna_string_list[cell_index+1])
            print(dna_string_list[cell_index+2])
            if dna_string_list[cell_index] + dna_string_list[cell_index+1] + dna_string_list[cell_index+2]=="AUG":
                dna_string_list=dna_string_list[cell_index+2:]
                print("Start of sequence")
                protein_translate_center(dna_string_list)
                break

    except IndexError:
        print("Dna Sequence don't have any start")
        input("Press enter to left...")
        read_dna_sequence()


def protein_translate_center(dna_string_list):
    protein_sequence = ["Metheonin"]
    print(dna_string_list)
    try:
        for cell_index in range(len(dna_string_list)):
            input(dna_string_list[cell_index])
            input(dna_string_list[cell_index+1])
            input(dna_string_list[cell_index+2])

            if dna_string_list[cell_index] + dna_string_list[cell_index + 1] + dna_string_list[cell_index + 2] == "UAA":
                print("End of sequence")
                break
            if dna_string_list[cell_index] + dna_string_list[cell_index + 1] + dna_string_list[cell_index + 2] == "UAG":
                print("End of sequence")
                break
            if dna_string_list[cell_index] + dna_string_list[cell_index + 1] + dna_string_list[cell_index + 2] == "UGA":
                print("End of sequence")
                break
            protein_sequence.append(proteins_dict[dna_string_list[cell_index]][dna_string_list[cell_index+1]][dna_string_list[cell_index+2]])
            dna_string_list=dna_string_list[cell_index+2:]

    except IndexError:
        print("Dna Sequence don't have any end")
        input("Press enter to left...")
        read_dna_sequence()

    print(f"Protein sequence: {protein_sequence}")


def dna_replication(dna_string):
    print("\n__________________\n")
    print(f"DNA: {dna_string}")
    input("Press enter to continue...")
    dna_string_list = list(dna_string)
    for cell_index in range(len(dna_string_list)):
        match dna_string_list[cell_index]:
            case "A":
                dna_string_list[cell_index] = "T"
            case "T":
                dna_string_list[cell_index] = "A"
            case "C":
                dna_string_list[cell_index] = "G"
            case "G":
                dna_string_list[cell_index] = "C"

    dna_string = "".join(dna_string_list)
    print(f"Replication DNA: {dna_string}")

    transcription_dna(dna_string)


def transcription_dna(dna_string):
    print("\n__________________\n")
    print(f"DNA: {dna_string}")
    input("Press enter to continue...")

    dna_string_list = list(dna_string)
    for cell_index in range(len(dna_string_list)):
        match dna_string_list[cell_index]:
            case "A":
                dna_string_list[cell_index] = "U"
            case "T":
                dna_string_list[cell_index] = "A"
            case "C":
                dna_string_list[cell_index] = "G"
            case "G":
                dna_string_list[cell_index] = "C"

    dna_string = "".join(dna_string_list)
    print(f"Transcription mRNA: {dna_string}")
    protein_start_translate(dna_string)


def read_dna_sequence():
    print("\n__________________\n")
    dna_string = input("Enter a DNA string: ").upper()
    dna_string = dna_string.replace(' ', '')
    if not dna_string.isalpha():
        print("DNA string is invalid")
        read_dna_sequence()
    for cell in list(dna_string):
        if cell not in "ATGC":
            print("DNA string is invalid")
            read_dna_sequence()
    dna_replication(dna_string)

read_dna_sequence()
