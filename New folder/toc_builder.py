import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

IMAGE_WIDTH = Inches(5.5)

def style_cell(cell, fill_hex=None, top_pad=100, bottom_pad=100, left_pad=150, right_pad=150, border_color="CCCCCC"):
    tcPr = cell._tc.get_or_add_tcPr()
    if fill_hex:
        tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top_pad}" w:type="dxa"/><w:bottom w:w="{bottom_pad}" w:type="dxa"/><w:left w:w="{left_pad}" w:type="dxa"/><w:right w:w="{right_pad}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)
    if border_color:
        borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/><w:left w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/><w:right w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/></w:tcBorders>')
        tcPr.append(borders)

def make_clean_table(doc, title, img_path, note_points, caption=""):
    tbl = doc.add_table(rows=3, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    c_hdr = tbl.cell(0, 0)
    c_hdr.width = Inches(6.2)
    style_cell(c_hdr, fill_hex="F0F4F8", top_pad=90, bottom_pad=90, left_pad=140, right_pad=140, border_color="B0B0B0")
    
    p_hdr = c_hdr.paragraphs[0]
    p_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_hdr.paragraph_format.space_before = Pt(2)
    p_hdr.paragraph_format.space_after = Pt(2)
    run_hdr = p_hdr.add_run(title)
    run_hdr.bold = True
    run_hdr.font.name = "Calibri"
    run_hdr.font.size = Pt(10.5)
    run_hdr.font.color.rgb = RGBColor(31, 78, 121)

    c_img = tbl.cell(1, 0)
    c_img.width = Inches(6.2)
    style_cell(c_img, fill_hex="FFFFFF", top_pad=120, bottom_pad=80, left_pad=80, right_pad=80, border_color="CCCCCC")
    p_img = c_img.paragraphs[0]
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(4)
    p_img.paragraph_format.space_after = Pt(4)
    
    if os.path.exists(img_path):
        p_img.add_run().add_picture(img_path, width=IMAGE_WIDTH)
    else:
        p_img.add_run(f"[Gambar {img_path} tidak ditemukan]")

    if caption:
        p_cap = c_img.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(4)
        run_cap = p_cap.add_run(caption)
        run_cap.italic = True
        run_cap.font.name = "Calibri"
        run_cap.font.size = Pt(9.5)
        run_cap.font.color.rgb = RGBColor(90, 90, 90)

    c_note = tbl.cell(2, 0)
    c_note.width = Inches(6.2)
    style_cell(c_note, fill_hex="FAFAFA", top_pad=100, bottom_pad=100, left_pad=160, right_pad=160, border_color="CCCCCC")
    
    p_note_title = c_note.paragraphs[0]
    p_note_title.paragraph_format.space_before = Pt(2)
    p_note_title.paragraph_format.space_after = Pt(4)
    r_nlbl = p_note_title.add_run("Note & Analisis Hasil:")
    r_nlbl.bold = True
    r_nlbl.font.name = "Calibri"
    r_nlbl.font.size = Pt(10)
    r_nlbl.font.color.rgb = RGBColor(31, 78, 121)

    for pt in note_points:
        p_pt = c_note.add_paragraph()
        p_pt.paragraph_format.line_spacing = 1.2
        p_pt.paragraph_format.space_before = Pt(2)
        p_pt.paragraph_format.space_after = Pt(2)
        p_pt.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        
        if ":" in pt:
            lead, body = pt.split(":", 1)
            r_lead = p_pt.add_run(f"• {lead.strip()}: ")
            r_lead.bold = True
            r_lead.font.name = "Calibri"
            r_lead.font.size = Pt(9.5)
            
            r_body = p_pt.add_run(body.strip())
            r_body.font.name = "Calibri"
            r_body.font.size = Pt(9.5)
        else:
            r_all = p_pt.add_run(f"• {pt.strip()}")
            r_all.font.name = "Calibri"
            r_all.font.size = Pt(9.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    return tbl

def make_clean_code_table(doc, title, img_path, caption=""):
    tbl = doc.add_table(rows=2, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    c_hdr = tbl.cell(0, 0)
    c_hdr.width = Inches(6.2)
    style_cell(c_hdr, fill_hex="252526", top_pad=90, bottom_pad=90, left_pad=140, right_pad=140, border_color="333333")
    
    p_hdr = c_hdr.paragraphs[0]
    p_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_hdr.paragraph_format.space_before = Pt(2)
    p_hdr.paragraph_format.space_after = Pt(2)
    run_hdr = p_hdr.add_run(title)
    run_hdr.bold = True
    run_hdr.font.name = "Calibri"
    run_hdr.font.size = Pt(10.5)
    run_hdr.font.color.rgb = RGBColor(255, 255, 255)

    c_img = tbl.cell(1, 0)
    c_img.width = Inches(6.2)
    style_cell(c_img, fill_hex="1E1E1E", top_pad=100, bottom_pad=80, left_pad=80, right_pad=80, border_color="333333")
    p_img = c_img.paragraphs[0]
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(4)
    p_img.paragraph_format.space_after = Pt(4)
    
    if os.path.exists(img_path):
        p_img.add_run().add_picture(img_path, width=IMAGE_WIDTH)
    else:
        p_img.add_run(f"[Gambar {img_path} tidak ditemukan]")

    if caption:
        p_cap = c_img.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(4)
        run_cap = p_cap.add_run(caption)
        run_cap.italic = True
        run_cap.font.name = "Calibri"
        run_cap.font.size = Pt(9.5)
        run_cap.font.color.rgb = RGBColor(160, 160, 160)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    return tbl

def add_table_of_contents(doc, toc_p_index):
    # Items for table of contents
    toc_items = [
        ("DAFTAR ISI", "ii", 0, True),
        ("A. PENGENALAN HTML TINGKAT DASAR", "1", 0, True),
        ("1. Install dan Jalankan Visual Studio Code", "1", 1, False),
        ("2. Struktur Dasar HTML", "2", 1, False),
        ("3. Elemen Head", "3", 1, False),
        ("4. Elemen Level (Block Level vs Inline Level)", "4", 1, False),
        ("5. Elemen Text Formatting", "5", 1, False),
        ("6. Elemen List (Ordered, Unordered, & Description)", "6", 1, False),
        ("7. Elemen Image", "7", 1, False),
        ("8. Elemen Audio", "8", 1, False),
        ("9. Elemen Video", "9", 1, False),
        ("10. Elemen Table & Nested Table", "10", 1, False),
        ("B. TUGAS HTML DASAR (tugas.html)", "11", 0, True),
        ("1. Kode Program Visual Studio Code (tugas.html)", "11", 1, False),
        ("2. Hasil Output Browser Port 5500 & Analisis", "12", 1, False),
        ("C. PENGENALAN HTML TINGKAT LANJUT", "13", 0, True),
        ("1. Elemen Form & Ragam Kontrol Input", "13", 1, False),
        ("2. Elemen Embed", "14", 1, False),
        ("3. Elemen Object", "15", 1, False),
        ("4. Elemen Iframe", "16", 1, False),
        ("5. Tag Semantic HTML5", "17", 1, False),
        ("6. Visual Studio Code Plugin : Live Server", "18", 1, False),
        ("D. TUGAS HTML LANJUT", "19", 0, True),
        ("1. Implementasi Tag Semantic HTML5 (semantic.html)", "19", 1, False),
        ("2. Implementasi Form Registrasi Mahasiswa (form.html)", "21", 1, False),
        ("3. Publikasi Halaman Web Secara Online (Vercel)", "23", 1, False)
    ]

    # Create clean 2-column table for Daftar Isi
    tbl_toc = doc.add_table(rows=len(toc_items), cols=2)
    tbl_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_toc.autofit = False

    w_title = Inches(5.6)
    w_page = Inches(0.6)

    for idx, (title, page, level, is_bold) in enumerate(toc_items):
        row = tbl_toc.rows[idx]
        
        # Left cell (Title + dots)
        c0 = row.cells[0]
        c0.width = w_title
        style_cell(c0, fill_hex=None, top_pad=40, bottom_pad=40, left_pad=60, right_pad=60, border_color=None)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.line_spacing = 1.15
        p0.paragraph_format.space_before = Pt(1)
        p0.paragraph_format.space_after = Pt(1)
        
        indent = "    " if level == 1 else ""
        run0 = p0.add_run(indent + title)
        run0.bold = is_bold
        run0.font.name = "Calibri"
        run0.font.size = Pt(10)
        if level == 0:
            run0.font.color.rgb = RGBColor(31, 78, 121)

        # Right cell (Page number)
        c1 = row.cells[1]
        c1.width = w_page
        style_cell(c1, fill_hex=None, top_pad=40, bottom_pad=40, left_pad=20, right_pad=20, border_color=None)
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p1.paragraph_format.line_spacing = 1.15
        p1.paragraph_format.space_before = Pt(1)
        p1.paragraph_format.space_after = Pt(1)
        run1 = p1.add_run(page)
        run1.bold = is_bold
        run1.font.name = "Calibri"
        run1.font.size = Pt(10)

    # Insert table after DAFTAR ISI paragraph
    target_p = doc.paragraphs[toc_p_index]
    target_p._p.addnext(tbl_toc._tbl)

print("TOC builder ready.")
