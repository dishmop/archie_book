#!/usr/bin/env python3
"""Extract figure captions from Word documents and compare with CSV."""
import zipfile
import xml.etree.ElementTree as ET
import re
import csv
import os

def extract_text_from_docx(docx_path):
    """Extract all text from a docx file."""
    try:
        with zipfile.ZipFile(docx_path, 'r') as z:
            xml_content = z.read('word/document.xml')
        tree = ET.fromstring(xml_content)

        paragraphs = []
        for para in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            text = ''.join(node.text for node in para.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text)
            if text.strip():
                paragraphs.append(text.strip())
        return paragraphs
    except Exception as e:
        print(f"Error reading {docx_path}: {e}")
        return []

def find_figure_captions(paragraphs, chapter_num):
    """Find figure captions in paragraph list."""
    captions = {}

    # Pattern 1: "Fig. 1.1" or "Figure 1.1" (chapter.figure format)
    pattern1 = re.compile(r'^(Fig\.?|Figure)\s*(\d+)\.(\d+[a-z]?)\.?\s*(.*)', re.IGNORECASE)

    # Pattern 2: "Fig 2." or "Fig. 2" (just figure number, we'll add chapter)
    pattern2 = re.compile(r'^(Fig\.?|Figure)\s*(\d+[a-z]?)\.?\s+(.*)', re.IGNORECASE)

    for para in paragraphs:
        # Skip paragraphs that are just references to figures in text (not captions)
        # Captions typically start with Fig/Figure and have substantial text

        # Try pattern 1 first (chapter.figure)
        match = pattern1.match(para)
        if match:
            ch = match.group(2)
            fig_num = match.group(3)
            key = f"{ch}_{fig_num}"
            captions[key] = para
            continue

        # Try pattern 2 (just figure number)
        match = pattern2.match(para)
        if match:
            fig_num = match.group(2)
            # Use provided chapter number
            key = f"{chapter_num}_{fig_num}"
            captions[key] = para

    return captions

# Chapter files mapping
base_path = "/Users/diarmidcampbell/Desktop/Archies book project/Final_Versions_F2 2"
chapter_files = {
    1: "CHAPTER I_v14_F1 DC.docx",
    2: "CHAPTER II_V11_F1 DC.docx",
    3: "CHAPTER III_V08_F1 DC.docx",
    4: "CHAPTER IV_v06_F1 DC.docx",
    5: "CHAPTER V_v11_F1 DC2.docx",
    6: "CHAPTER VI_v06_F1 DC.docx",
    7: "CHAPTER VII_v06_F1 DC.docx",
    8: "CHAPTER VIII_07_F1 DC.docx",
    9: "CHAPTER IX_v09_F1 DC.docx",
    10: "CHAPTER X_v07_F1 DC.docx",
    11: "CHAPTER XI_v04_F1 DC.docx",
    12: "CHAPTER XII_V05_F1 DC.docx",
    13: "CHAPTER XIII_v05_F1 DC.docx",
}

# Extract captions from all docs
all_doc_captions = {}
for chapter_num, filename in chapter_files.items():
    filepath = os.path.join(base_path, filename)
    if os.path.exists(filepath):
        print(f"Processing Chapter {chapter_num}: {filename}")
        paragraphs = extract_text_from_docx(filepath)
        captions = find_figure_captions(paragraphs, chapter_num)
        all_doc_captions.update(captions)
        print(f"  Found {len(captions)} figure captions")
        for key in sorted(captions.keys()):
            print(f"    {key}: {captions[key][:60]}...")
    else:
        print(f"File not found: {filepath}")

print(f"\nTotal captions from docs: {len(all_doc_captions)}")

# Load CSV captions
csv_captions = {}
csv_path = "/Users/diarmidcampbell/Desktop/Archies book project/image_submission_final.csv"
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        chapter = row['chapter']
        figure = row['figure']
        key = f"{chapter}_{figure}"
        csv_captions[row['filename']] = {
            'key': key,
            'caption': row['figure_text']
        }

# Create comparison output
output_path = "/Users/diarmidcampbell/Desktop/Archies book project/caption_comparison.csv"
with open(output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['filename', 'caption_from_docs', 'caption_in_spreadsheet'])

    for filename, data in sorted(csv_captions.items()):
        key = data['key']
        csv_caption = data['caption']
        doc_caption = all_doc_captions.get(key, "NOT FOUND IN DOC")
        writer.writerow([filename, doc_caption, csv_caption])

print(f"\nComparison saved to: {output_path}")
