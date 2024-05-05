import pypdf

def crop_pdf(input_pdf, output_pdf, crop_box_odd, crop_box_even):
    with open(input_pdf, 'rb') as file:
        pdf_reader = pypdf.PdfReader(file)
        pdf_writer = pypdf.PdfWriter()

        for idx, page in enumerate(pdf_reader.pages):
            if idx % 2 == 0:
                page.cropbox.lower_left = crop_box_odd[0]
                page.cropbox.upper_right = crop_box_odd[1]
            else:
                page.cropbox.lower_left = crop_box_even[0]
                page.cropbox.upper_right = crop_box_even[1]
            pdf_writer.add_page(page)
            # if idx == 30:
            #     break

        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

# Example usage:
input_pdf_path = r'/home/alex/Dropbox/PHD/SOTA/Liu Wang Tegmark - KAN.pdf'
output_pdf_path = r'/home/alex/Dropbox/PHD/SOTA/Liu Wang Tegmark - KAN_crop.pdf'

# Crop box format: (lower_left_x, lower_left_y, upper_right_x, upper_right_y)
crop_box_odd = ((45, 60), (560, 730))
crop_box_even = ((45, 60), (560, 730))

crop_pdf(input_pdf_path, output_pdf_path, crop_box_odd, crop_box_even)
