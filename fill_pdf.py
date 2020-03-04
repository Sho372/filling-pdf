import pdfrw
from reportlab.pdfgen import canvas
import json


def create_overlay():
    """
    Create the data that will be overlayed on top
    of the form that we want to fill
    """
    json_str = u'{"success": 1,"data": [{"id":"54","first_name":"Hitesh","last_name":"Patel","gender":"Male","student_dob":"1992-06-07","address":"","tc_number":null,"image":"Image URL","admission_number":"33","student_email":"tohitehmca@gmail.com","student_contact":"9725656525","blood_group":"","profile_summary":"","allergies":null,"medications":null,"medical_notes":null,"text_36":null,"checkbox_37":"opt1,opt4","student_name":"Hitesh Patel","class_id":"2", "class_name":"Class - 2","class_code":"cls2","section_id":"3", "section_name":"Section - A (CLS2)","section_code":"2secA","father_name":"","mother_name":"","parents_contact":"9725656525","parents_email":"","country":"Country Name","subjects":[{"id":"29","subject_name":"Socail Science","type":"Core","class_name":"Class - 2","section_name":"Section - A (CLS2)"},{"id":"30","subject_name":"PT","type":"Elective","class_name":"Standared 8","section_name":"Section B"}]}]}'
    data_dict = json.loads(json_str)
    last_name = data_dict['data'][0]['last_name']
    first_name = data_dict['data'][0]['first_name']
    dob = data_dict['data'][0]['student_dob']
    id = data_dict['data'][0]['id']

    c = canvas.Canvas('/home/shouhei/PycharmProjects/filling_pdf/pdf_dir/demo_overlay.pdf')

    c.drawString(100, 655, last_name)
    c.drawString(350, 655, first_name)
    c.drawString(100, 635, dob)
    c.drawString(350, 635, id)

    c.save()


def merge_pdfs(form_pdf, overlay_pdf, output):
    """
    Merge the specified fillable form PDF with the
    overlay PDF and save the output
    """
    form = pdfrw.PdfReader(form_pdf)
    olay = pdfrw.PdfReader(overlay_pdf)

    for form_page, overlay_page in zip(form.pages, olay.pages):
        merge_obj = pdfrw.PageMerge()
        overlay = merge_obj.add( overlay_page )[0]
        pdfrw.PageMerge(form_page).add(overlay).render()

    writer = pdfrw.PdfWriter()
    writer.write(output, form)


if __name__ == '__main__':
    create_overlay()
    merge_pdfs('/home/shouhei/PycharmProjects/filling_pdf/pdf_dir/demo.pdf'
               ,'/home/shouhei/PycharmProjects/filling_pdf/pdf_dir/demo_overlay.pdf'
               ,'/home/shouhei/PycharmProjects/filling_pdf/pdf_dir/merged_form.pdf')
