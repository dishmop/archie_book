# Image Attribution & Copyright Plan for OUP Book Submission

## Overview

This document outlines the tasks required to prepare images for Oxford University Press book submission, following their [artwork guidelines](https://academic.oup.com/pages/for-authors/books/the-book-publishing-process/writing-and-content-preparation/artwork-and-figures).

## Current State

- **207 image files** in `archie book figures/` folder
- **13 chapters** in manuscript (Chapters I-XIII)
- Existing tracking spreadsheet: `Archie book figure links.csv`
- Many filenames exceed 200+ characters (max found: 250 chars)

### Image Sources (from CSV analysis)
| Source | Notes |
|--------|-------|
| draw.io diagrams | Created by authors - OK |
| Google Docs diagrams | Created by authors - OK |
| GIMP files | Created by authors - OK |
| Hugh's photos/diagrams | Need confirmation of permission |
| Original manuscript | Unknown origin - needs investigation |
| Wikipedia/Wikimedia | Check license (CC, Public Domain) |
| External websites | Marked "Possible copyright issue" - needs resolution |

---

## OUP Requirements Summary

### File Formats
- **Preferred**: EPS, AI, PDF (vector), TIFF (raster)
- **Acceptable**: PNG, JPG
- **NOT acceptable**: Web-downloaded low-res images (72 dpi)

### Resolution
- **Line art/B&W**: 600 dpi minimum
- **Colour/halftone**: 300 dpi minimum
- Width: max 1081 pixels at target DPI

### Colour
- Use **CMYK** (not RGB) for colour images
- Consider if images need colour or can be B&W (cost implications)

### File Naming
- Save each piece of artwork as a separate file
- Name with artwork/figure number
- **Your target**: max 30 characters

### Other Requirements
- Do NOT embed images in text documents
- Use placement cues in manuscript instead
- Provide **alt text** for accessibility
- Line weights: 0.35pt to 1.5pt (minimum 2pt)
- Use standard fonts: Times, Courier, Arial, Helvetica, Symbol
- Embed fonts in figures

---

## Task List

### Phase 1: Audit & Categorise Images

- [ ] **1.1** Create master spreadsheet with columns:
  - `old_filename` - current filename
  - `new_filename` - shortened name (max 30 chars)
  - `chapter` - chapter number (1-13)
  - `figure_num` - figure number within chapter
  - `format` - current file format
  - `source` - who created/where from
  - `copyright_status` - OK / Needs Permission / Needs Replacement
  - `action_required` - None / Get Permission / Replace / Redraw
  - `alt_text` - accessibility description

- [ ] **1.2** Populate spreadsheet from existing CSV and image folder

- [ ] **1.3** Categorise each image by copyright status:
  - **Green**: Self-created (draw.io, GIMP, Google Docs) or Public Domain
  - **Amber**: Wikipedia CC images (can use with attribution)
  - **Red**: Unknown source or marked "copyright issue"

### Phase 2: Rename Files

- [ ] **2.1** Create filename mapping following pattern:
  ```
  fig_[chapter]_[figure][part].ext
  Examples:
  fig_01_01.png      (Chapter 1, Figure 1)
  fig_01_10a.svg     (Chapter 1, Figure 10, part a)
  fig_10_05b.jpg     (Chapter 10, Figure 5, part b)
  ```

- [ ] **2.2** Create script or manually rename files
- [ ] **2.3** Update spreadsheet with old/new filename mapping

### Phase 3: Resolve Copyright Issues

Images flagged with copyright concerns (from CSV):

| Figure | Issue | Suggested Action |
|--------|-------|------------------|
| Fig 1.11 | Planetary gear from tec-science.com | Take new photo of 3D printed model |
| Fig 2.5 | 1922 Scientific American | Check if public domain (100+ years) |
| Fig 4.1 | Slinky from BBC One Show | Request permission or replace |
| Fig 4.9 | Physics tutor website | Redraw or find CC alternative |
| Fig 5.1 | Airbus 380 source unknown | Use Wikimedia Commons image |
| Fig 7.3 | Chegg vapour pressure plot | Redraw from data |
| Fig 8.1 | Garmin GPS image | Hugh to take own photo |
| Fig 9.5b | Pitot tube photo | Find CC image or take own |
| Fig 9.13a | Perfume atomiser | Take own photo |
| Fig 10.3 | Met office weather map | Find CC alternative |
| Fig 10.4 | Matt Parker YouTube | Contact Matt Parker |
| Fig 10.5a | Foucault pendulum | Purchase licence or find alternative |
| Fig 11.1 | Moon formation | Purchase licence from sciencephoto.com |
| Fig 11.4 | Coupled pendulums | Request Exploratorium permission |
| Fig 11.5 | Tippe top | Hugh to take own photo |
| Fig 12.3 | Sunrise/sunset diagram | Find CC or redraw |
| Fig 13.1b | De Havilland Comet | Find alternative image |
| Fig 13.10 | Archer's paradox | Redraw diagram |

- [ ] **3.1** For each "Red" image, decide: replace, redraw, or seek permission
- [ ] **3.2** Contact copyright holders where needed
- [ ] **3.3** Find replacement images from OUP-approved sources (Getty, Shutterstock)
- [ ] **3.4** Note: OUP has standing agreements with Getty/Shutterstock

### Phase 4: Technical Preparation

- [ ] **4.1** Check resolution of all raster images (PNG, JPG)
  - Flag any below 300 dpi
  - SVG files are vector - OK at any size

- [ ] **4.2** Convert problematic formats:
  - WEBP (5 files) → PNG or TIFF
  - AVIF (2 files) → PNG or TIFF
  - GIF (1 file) → PNG

- [ ] **4.3** Check colour mode (RGB vs CMYK) if colour printing planned

- [ ] **4.4** Review SVG files for:
  - Font embedding
  - Line weights (min 2pt)

### Phase 5: Alt Text & Captions

- [ ] **5.1** Write alt text for each figure (accessibility requirement)
- [ ] **5.2** Verify captions match between manuscript and spreadsheet

### Phase 6: Final Spreadsheet & Handover

- [ ] **6.1** Create final CSV with these columns only:
  - `filename` (new short name)
  - `chapter`
  - `figure`
  - `source`
  - `copyright_status`
  - `alt_text`

- [ ] **6.2** Ensure all images renamed and in correct folder
- [ ] **6.3** Update manuscript figure references if needed
- [ ] **6.4** Final review against OUP checklist

---

## Proposed New Filename Convention

**Pattern**: `fig_CC_NN[x].ext`

Where:
- `CC` = chapter number (01-13), zero-padded
- `NN` = figure number within chapter, zero-padded
- `[x]` = optional part letter (a, b, c) for multi-part figures
- `.ext` = original file extension

**Examples**:
| Current (truncated) | New |
|---------------------|-----|
| `1_1_Hydraulic capstan, Liverpool 1901.png` | `fig_01_01.png` |
| `10_10a_A stone bouncing...` | `fig_10_10a.png` |
| `13_1b_Well-known engineering...` | `fig_13_01b.webp` |

This keeps all filenames under 20 characters.

---

## Quick Wins (Do First)

1. Rename all files using new convention (removes 200+ char filenames)
2. Convert WEBP/AVIF/GIF to standard formats
3. Get Hugh to photograph: GPS38, Tippe top, other items he has
4. Verify all Wikimedia images have correct CC attribution recorded

---

## Sources

- [OUP Artwork Guidelines](https://academic.oup.com/pages/for-authors/books/the-book-publishing-process/writing-and-content-preparation/artwork-and-figures)
- [OUP Manuscript Preparation](https://academic.oup.com/pages/authoring/books/preparing-your-manuscript)
