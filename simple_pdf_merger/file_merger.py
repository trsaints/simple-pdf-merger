from os import walk
import fitz


def initialize(origin, destination):
    pdfs = get_files(origin)

    if len(pdfs) == 0:
        print(
            "There are no PDF files to process in the current directory. Operation finished")

        return

    print(f"There are {len(pdfs)} files to be processed \n")

    pdf_name = ""
    current_file_group = []

    pdf_name = set_name(pdfs)
    current_file_group.append(pdfs[0])

    for current_pdf in pdfs:
        current_index = pdfs.index(current_pdf)
        next_index = current_index + 1

        if next_index >= len(pdfs):
            merge(current_file_group, pdf_name, origin, destination)

            break

        next_pdf = pdfs[next_index]

        if next_pdf.startswith(pdf_name):
            current_file_group.append(next_pdf)
        else:
            merge(current_file_group, pdf_name, origin, destination)

            current_file_group.clear()
            current_file_group.append(next_pdf)

            pdf_name = set_name(current_file_group)

    print("The operation has been finished.\n")


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


def merge_pdfs(files, pdf_name, origin_path, destination_path):
    final_result = fitz.open()

    for pdf in files:
        pdf_path = f"{origin_path}/{pdf}"

        try:
            with fitz.open(pdf_path) as mfile:
                final_result.insert_pdf(mfile)
        except Exception as e:
            raise e

    try:
        final_result_path = f"{destination_path}/{pdf_name}.pdf"
        final_result.save(final_result_path)

        return final_result_path
    except Exception as e:
        raise e


def merge(files, pdf_name, origin_path, destination_path):
    print(f"Merging the following files: {files}")

    try:
        result_path = merge_pdfs(
            files,
            pdf_name,
            origin_path,
            destination_path
        )

        print(f"The files have been merged successfully\nOutput: {result_path}\n")

        return result_path
    except Exception:
        print(
            f"Failed to merge the following files {files}\n")

        return files
