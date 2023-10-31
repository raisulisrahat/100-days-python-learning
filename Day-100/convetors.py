import pandas as pd
from PIL import Image
import PyPDF2
import os

class DataConverter:
    @staticmethod
    def json_to_csv(json_file, csv_file):
        try:
            df = pd.read_json(json_file)
            df.to_csv(csv_file, index=False)
            print(f"JSON file '{json_file}' converted to CSV file '{csv_file}'")
        except Exception as e:
            print(f"Error converting JSON to CSV: {e}")

    @staticmethod
    def csv_to_json(csv_file, json_file):
        try:
            df = pd.read_csv(csv_file)
            df.to_json(json_file, orient='records')
            print(f"CSV file '{csv_file}' converted to JSON file '{json_file}'")
        except Exception as e:
            print(f"Error converting CSV to JSON: {e}")

    @staticmethod
    def image_to_pdf(image_file, pdf_file):
        try:
            img = Image.open(image_file)
            img.save(pdf_file, "PDF")
            print(f"Image file '{image_file}' converted to PDF file '{pdf_file}'")
        except Exception as e:
            print(f"Error converting Image to PDF: {e}")

    @staticmethod
    def pdf_to_text(pdf_file, text_file):
        try:
            with open(pdf_file, 'rb') as file:
                pdf_reader = PyPDF2.PdfFileReader(file)
                text = ''
                for page in range(pdf_reader.numPages):
                    page_text = pdf_reader.getPage(page).extractText()
                    text += page_text

            with open(text_file, 'w') as file:
                file.write(text)

            print(f"PDF file '{pdf_file}' converted to text file '{text_file}'")
        except Exception as e:
            print(f"Error converting PDF to Text: {e}")

    @staticmethod
    def text_to_pdf(text_file, pdf_file):
        try:
            pdf = PyPDF2.PdfFileWriter()
            with open(text_file, 'r') as file:
                pdf.addPage(PyPDF2.pdf.PageObject.createTextPage(file.read()))

            with open(pdf_file, 'wb') as file:
                pdf.write(file)

            print(f"Text file '{text_file}' converted to PDF file '{pdf_file}'")
        except Exception as e:
            print(f"Error converting Text to PDF: {e}")

def main():
    data_converter = DataConverter()

    choice = int(input("Choose an option:\n1. JSON to CSV\n2. CSV to JSON\n3. Image to PDF\n4. PDF to Text\n5. Text to PDF\nEnter choice: "))

    if choice == 1:
        json_file = "data.json"
        csv_file = "data-csv.csv"
        data_converter.json_to_csv(json_file, csv_file)
    elif choice == 2:
        csv_file = "data-csv.csv"
        json_file = "data-json.json"
        data_converter.csv_to_json(csv_file, json_file)
    elif choice == 3:
        image_file = "image.jpg"
        pdf_file = "image-pdf.pdf"
        data_converter.image_to_pdf(image_file, pdf_file)
    elif choice == 4:
        pdf_file = "image-pdf.pdf"
        text_file = "doc-txt.txt"
        data_converter.pdf_to_text(pdf_file, text_file)
    elif choice == 5:
        text_file = "doc-txt.txt"
        pdf_file = "doc-pdf.pdf"
        data_converter.text_to_pdf(text_file, pdf_file)
    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
