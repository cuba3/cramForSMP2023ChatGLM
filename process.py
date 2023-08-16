import PyPDF2
import json
import tabula
from PIL import Image
def pdf_to_json(filename):
    # Open and read PDF file
    with open(filename, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        # Initialize variables to store data
        tables = []
        images = []
        text = ""
        # Loop through each page of PDF
        for page in range(pdf_reader.getNumPages()):
            pdf_page = pdf_reader.getPage(page)
            # Extract text from PDF page
            text += pdf_page.extractText()
            # Extract tables from PDF page
            try:
                table = tabula.read_pdf(filename, pages=page+1, output_format='json')
                tables.extend(table)
            except:
                pass
            # Extract images from PDF page
            xObject = pdf_page['/Resources']['/XObject'].getObject()
            for obj in xObject:
                if xObject[obj]['/Subtype'] == '/Image':
                    img_data = xObject[obj]._data
                    img_type = xObject[obj]['/Filter']
                    img_ext = img_type.split('/')[-1]
                    img_file = f"image-{page+1}-{obj}.{img_ext}"
                    with open(img_file, 'wb') as img:
                        img.write(img_data)
                    images.append(img_file)
        # Convert text, tables, and images to JSON format
        json_data = {
            "text": text,
            "tables": tables,
            "images": images
        }
        return json.dumps(json_data)
# Test the function with example PDF file
pdf_file = "example.pdf"
json_data = pdf_to_json(pdf_file)
print(json_data)