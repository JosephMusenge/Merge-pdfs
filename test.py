# How to test the code to merge two PDF files

# Import the PdfFileMerger class from the PyPDF2 library
from PyPDF2 import PdfFileMerger

# Define a function to merge two PDF files
def merge_pdfs(file1, file2, output_file):
    # Create an instance of the PdfFileMerger class
    merger = PdfFileMerger()
    
    # Append the first PDF file to the merger object
    merger.append(file1)
    
    # Append the second PDF file to the merger object
    merger.append(file2)
    
    # Write the merged PDF to the output file
    merger.write(output_file)

# Check if the code is being run as the main program
if __name__ == "__main__":
    # Call the merge_pdfs function with the input file names and output file name
    merge_pdfs("file1.pdf", "file2.pdf", "merged.pdf")
