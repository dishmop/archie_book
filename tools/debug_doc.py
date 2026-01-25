#!/usr/bin/env python3
"""Debug: show paragraphs containing 'Fig' from a Word doc."""
import zipfile
import xml.etree.ElementTree as ET

def extract_text_from_docx(docx_path):
    """Extract all text from a docx file."""
    with zipfile.ZipFile(docx_path, 'r') as z:
        xml_content = z.read('word/document.xml')
    tree = ET.fromstring(xml_content)

    paragraphs = []
    for para in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
        text = ''.join(node.text for node in para.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text)
        if text.strip():
            paragraphs.append(text.strip())
    return paragraphs

# Check Chapter 1
filepath = "/Users/diarmidcampbell/Desktop/Archies book project/Final_Versions_F2 2/CHAPTER I_v14_F1 DC.docx"
paragraphs = extract_text_from_docx(filepath)

print("Paragraphs containing 'Fig' in Chapter 1:")
print("=" * 60)
for i, para in enumerate(paragraphs):
    if 'Fig' in para or 'fig' in para:
        print(f"{i}: {para[:200]}...")
        print()
