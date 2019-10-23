import fpdf

"""This script converts an Image to PDF.
Also works as module """


#Image to PDF Conversion Functionality
def image_to_pdf(image_path):
    #Create FPDF object and add Portrait type page to it
    fpdf_object=fpdf.FPDF()
    fpdf_object.add_page('P')
    #Put Image into the page
    fpdf_object.image(image_path,w=180,h=250)
    #Save it to PDF file
    fpdf_object.output('image_to_pdf.pdf','F')

def main():
        image_path = input("Enter image path to be converted to PDF\n")
        image_to_pdf(image_path)


if __name__== "__main__":
    main()