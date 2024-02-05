import PyPDF2

def crop_pdf(input_pdf, output_pdf, crop_box):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for idx, page in enumerate(pdf_reader.pages):
            page.cropbox.lower_left = crop_box[0]
            page.cropbox.upper_right = crop_box[1]
            pdf_writer.add_page(page)
            # if idx == 30:
            #     break

        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

# Example usage:
input_pdf_path = 'input.pdf'
output_pdf_path = 'output.pdf'

# Crop box format: (lower_left_x, lower_left_y, upper_right_x, upper_right_y)
crop_box = ((0, 100), (500, 690))

crop_pdf(input_pdf_path, output_pdf_path, crop_box)
