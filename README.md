# PDF File Merger

This Python script provides a convenient way to merge PDF files using the `PyPDF2` library. The script includes two functions, `by_appending()` and `by_inserting()`, each demonstrating different PDF merging methods.

## Installation

Before using the script, make sure you have the `PyPDF2` library installed. If you haven't already, you can install it using pip:

```bash
pip install PyPDF2
```

## Usage

The script contains two functions, each serving a distinct PDF merging purpose:

### Merging PDFs by Appending

The `by_appending()` function appends two PDF files, creating a new merged PDF file. It provides two input methods:

1. **File Stream**: Open the first PDF file as a binary read stream using the `open()` function and then use the `append()` method to merge it.
2. **Direct File Path**: Provide the file path of the second PDF file directly to the `append()` method.

After appending both PDF files, the merged content is saved as a new PDF file named `mergedPdf.pdf`.

### Merging PDFs by Inserting

The `by_inserting()` function merges one PDF file into another at a specified page number, resulting in a new merged PDF file.

The process involves:

1. Creating a `PdfFileMerger` object.
2. Appending the first PDF file to the merger object using the `append()` method.
3. Using the `merge()` method to insert the second PDF file at the specified page number (0-indexed) within the first PDF.
4. Writing the merged content to a new PDF file named `mergedPdf1.pdf`.

## Running the Script

To merge PDF files, execute the script, and it will automatically call both merging functions, creating the merged PDF files in the same directory where the script is located.

```bash
python merge_pdfs.py
```

Before running the script, ensure that you have the PDF files "samplePdf1.pdf" and "samplePdf2.pdf" present in the same directory as the script.

## Note

This script is based on the `PyPDF2` library as of the knowledge cutoff date in September 2021. If there have been updates or changes to the library after this date, it is recommended to check the latest documentation for the library for any potential modifications. Always stay updated with the latest advancements to make the most of this script.