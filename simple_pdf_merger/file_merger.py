from os import walk
import fitz


def initialize(origin, destination):
    pdfs = get_files(origin)

    if len(pdfs) == 0:
        print(
            "There are no PDF files to process in the current directory. Operation finished")

        return

    print(f"There are {len(pdfs)} files to be processed")

    pdf_name = ""
    current_file_group = []

    pdf_name = set_name(pdfs)
    current_file_group.append(pdfs[0])

    for current_pdf in pdfs:
        current_index = pdfs.index(current_pdf)
        next_index = current_index + 1

        if next_index >= len(pdfs):
            message = f"Merging the following files: {current_file_group}"
            print(message)

            try:
                merge_pdfs(
                    current_file_group,
                    pdf_name,
                    origin,
                    destination
                )
            except Exception as e:
                print(
                    f"Failed to merge the following files {current_file_group}")


            print("The PDF files have been processed successfuly")

            break

        next_pdf = pdfs[next_index]

        if next_pdf.startswith(pdf_name):
            current_file_group.append(next_pdf)
        else:
            message = f"Merging the following files: {current_file_group}"
            print(message)

            try:
                merge_pdfs(
                    current_file_group,
                    pdf_name,
                    origin,
                    destination
                )

            except Exception as e:
                print(
                    f"Failed to merge the following files {current_file_group}, {e.__notes__}")

            current_file_group = []
            current_file_group.append(next_pdf)

            pdf_name = set_name(current_file_group)


def get_files(origin):
    files = []
    pdfs = []

    for (dirpath, dirnames, filenames) in walk(origin):
        files.extend(filenames)

        break

    for current_file in files:
        if current_file.endswith(".pdf"):
            pdfs.append(current_file)

    pdfs.sort(key=lambda x: x.replace(".pdf", ""))
    return pdfs


def set_name(files):
    return files[0].replace(".pdf", "")


def merge_pdfs(files, pdf_name, origin, destination):
    result = fitz.open()

    for pdf in files:
        pdf_path = f"{origin}/{pdf}"
        with fitz.open(pdf_path) as mfile:
            result.insert_pdf(mfile)

    try:
        result.save(f"{destination}/{pdf_name}.pdf")
    except Exception as e:
        raise e
