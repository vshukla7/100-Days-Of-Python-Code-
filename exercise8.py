import pypdf2
from pathlib import Path

def merge_pdfs(paths, output):
    
    pdf_writer = pypdf2.PdfWriter()

    for path in paths:
        pdf_reader = pypdf2.PdfReader(path)
        num_pages = pdf_reader.getNumPages()
        for page in range(num_pages):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output, 'wb') as fh:
        pdf_writer.write(fh(fh)

if __name__ == '__main__':
    paths = [os.path.join('pdfs', f'{i}.pdf') for i in range(1, 4)]
    merge_pdfs(paths, 'output.pdf')
