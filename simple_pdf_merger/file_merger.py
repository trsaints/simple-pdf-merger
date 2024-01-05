from os import walk
import fitz
import re
from datetime import datetime


def initialize(origin, destination):
    pdfs = get_files(origin)
    process_log = []

    if len(pdfs) == 0:
        print(
            "There are no PDF files to process in the current directory. Operation finished")

        return process_log

    print(f"There are {len(pdfs)} files to be processed \n")

    pdf_name = ""
    current_file_group = []

    pdf_name = set_name(pdfs)
    pdf_attachment_pattern = re.compile(rf"{re.escape(pdf_name)}\-\d+")
    current_file_group.append(pdfs[0])

    for current_pdf in pdfs:
        current_index = pdfs.index(current_pdf)
        next_index = current_index + 1

        if next_index >= len(pdfs):
            merge_output = merge(current_file_group,
                                 pdf_name, origin, destination)
            process_log.append(merge_output)

            break

        next_pdf = pdfs[next_index]

        if re.search(pdf_attachment_pattern, next_pdf):
            current_file_group.append(next_pdf)
        else:
            merge_output = merge(current_file_group,
                                 pdf_name, origin, destination)
            process_log.append(merge_output)

            current_file_group.clear()
            current_file_group.append(next_pdf)

            pdf_name = set_name(current_file_group)
            pdf_attachment_pattern = re.compile(rf"{re.escape(pdf_name)}\-\d+")

    print("The operation has been finished.\n")

    return process_log


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

    current_date = datetime.now()
    formatted_date = current_date.strftime("[%d/%m/%Y - %H:%M:%S]")

    try:
        result_path = merge_pdfs(
            files,
            pdf_name,
            origin_path,
            destination_path
        )

        print(
            f"The files have been merged successfully\nOutput: {result_path}\n")

        return f"{formatted_date} - {files} - {result_path} - Success"
    except Exception:
        print(
            f"Failed to merge the following files {files}\n")

        return f"{formatted_date} - {files} - N/A - Failed"
