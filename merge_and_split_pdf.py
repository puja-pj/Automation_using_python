import PyPDF2

"""This script includes two functionalities
    1.Merge  PDF's
    2.Split PDF's
This script can also be used as module
    """


#Merge PDF Functionality
def merge_pdf(merge_file1,merge_file2):
    #Create PdfFileMerger object to merge
    merge = PyPDF2.PdfFileMerger()
    #Append the files to PdfFileMerger object and write to new PDF
    file_object1= open(merge_file1, 'rb')
    merge.append(file_object1)
    file_object2 = open(merge_file2, 'rb')
    merge.append(file_object2)
    merge.write('merged_file.pdf')


#Split PDF Functionality
def split_pdf(file_to_split,page_to_split):
    split_file1 = open('split_file1.pdf', 'wb')
    split_file2 = open('split_file2.pdf', 'wb')
    # Create FileWriter objects for new files
    writer1 = PyPDF2.PdfFileWriter()
    writer2 = PyPDF2.PdfFileWriter()
    #Create FileReader object
    file_object1 = open(file_to_split, 'rb')
    reader1 = PyPDF2.PdfFileReader(file_object1)
    #Loop over pages,read and write them using reader and writer objects and write to PDF
    for page in range(0,page_to_split):
        each_page=reader1.getPage(page)
        writer1.addPage(each_page)
    writer1.write(split_file1)
    for page in range(page_to_split,reader1.numPages):
        each_page=reader1.getPage(page)
        writer2.addPage(each_page)
    writer2.write(split_file2)



def main():
    use = int(input("""What is your requirement?
                Enter
                   1 for PDF Merge
                   2 for PDF Split
                   """))
    if use == 1:
        merge_file1 = input("Enter first file path to be merged\n")
        merge_file2 = input("Enter second file path to be merged\n ")
        merge_pdf(merge_file1, merge_file2)
    elif use == 2:
        file_to_split = input("Enter path of file to be split\n")
        page_to_split = int(input("Enter the page number for split\n"))
        split_pdf(file_to_split, page_to_split)


if __name__== "__main__":
    main()
