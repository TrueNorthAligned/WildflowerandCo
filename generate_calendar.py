#!/usr/bin/env python3
"""
Wildflower & Co. 2027 Calendar PDF Generator
Generates beautiful print-at-home wildflower calendar pages
"""

import calendar
import os
from datetime import date
from fpdf import FPDF
from PIL import Image

# Configuration
YEAR = 2027
OUTPUT_DIR = "/home/team/shared/calendar"
IMAGE_DIR = OUTPUT_DIR

# Month data: month_number, name, image_filename
MONTHS = [
    (1, "January", "01-january-snowdrops.png", "Snowdrops"),
    (2, "February", "02-february-crocus.png", "Crocus"),
    (3, "March", "03-march-daffodils.png", "Daffodils"),
    (4, "April", "04-april-bluebells.png", "Bluebells"),
    (5, "May", "05-may-wild-roses.png", "Wild Roses"),
    (6, "June", "06-june-foxgloves.png", "Foxgloves"),
    (7, "July", "07-july-lavender.png", "Lavender"),
    (8, "August", "08-august-sunflowers.png", "Sunflowers"),
    (9, "September", "09-september-coneflowers.png", "Coneflowers"),
    (10, "October", "10-october-chrysanthemums.png", "Chrysanthemums"),
    (11, "November", "11-november-heather.png", "Heather"),
    (12, "December", "12-december-winterberry.png", "Winterberry & Holly"),
]

# Colors
DARK_GREEN = (47, 79, 56)
MEDIUM_GREEN = (80, 120, 80)
LIGHT_GREEN = (200, 220, 190)
CREAM = (250, 245, 235)
DARK_BROWN = (80, 60, 40)
BLACK = (30, 30, 30)
LIGHT_GRAY = (240, 240, 240)
WHITE = (255, 255, 255)
SOFT_PINK = (230, 200, 195)
WARM_GOLD = (200, 170, 100)

class CalendarPDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_auto_page_break(auto=False)
        # Add a Unicode-compatible font
        # fpdf2 includes DejaVu by default
        self.add_font("DejaVu", "", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
        self.add_font("DejaVu", "B", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
        # fpdf2 will synthesize italic from the regular font

    def header(self):
        pass

    def footer(self):
        pass

    def draw_calendar_page(self, month_num, month_name, image_path, flower_name):
        """Draw a full calendar page with illustration, month name, calendar grid, and notes area."""
        self.add_page()
        
        page_w = self.w
        page_h = self.h
        
        # -- Background --
        self.set_fill_color(*CREAM)
        self.rect(0, 0, page_w, page_h, 'F')
        
        # -- Subtle border --
        self.set_draw_color(*DARK_GREEN)
        self.set_line_width(1.5)
        self.rect(5, 5, page_w - 10, page_h - 10, 'D')
        
        # -- Inner border --
        self.set_draw_color(*MEDIUM_GREEN)
        self.set_line_width(0.5)
        self.rect(8, 8, page_w - 16, page_h - 16, 'D')
        
        # -- Illustration --
        # Place illustration at the top, full width
        img_h = 70  # mm height for the illustration
        if os.path.exists(image_path):
            # Get image dimensions to maintain aspect ratio
            with Image.open(image_path) as img:
                orig_w, orig_h = img.size
                aspect = orig_w / orig_h
            
            # Calculate image width to fit within page margins
            max_img_w = page_w - 20  # 10mm margin each side
            img_display_w = max_img_w
            img_display_h = img_display_w / aspect
            
            # If too tall, constrain by height
            if img_display_h > img_h:
                img_display_h = img_h
                img_display_w = img_display_h * aspect
            
            x_center = (page_w - img_display_w) / 2
            self.image(image_path, x=x_center, y=12, w=img_display_w, h=img_display_h)
            
            # -- Flower name label under illustration --
            self.set_font("DejaVu", "", 9)
            self.set_text_color(*MEDIUM_GREEN)
            label_y = 12 + img_display_h + 2
            self.set_xy(10, label_y)
            self.cell(page_w - 20, 5, f"— {flower_name} —", align='C')
            content_y = label_y + 8
        else:
            # Fallback if image not found
            content_y = 15
            self.set_xy(10, content_y)
            self.set_font("DejaVu", "", 14)
            self.set_text_color(*MEDIUM_GREEN)
            self.cell(page_w - 20, 10, f"[{flower_name}]", align='C')
            content_y = content_y + 15
        
        # -- Month Title --
        self.set_font("DejaVu", "B", 22)
        self.set_text_color(*DARK_GREEN)
        title_y = content_y
        self.set_xy(0, title_y)
        self.cell(page_w, 10, month_name.upper(), align='C')
        
        # -- Decorative line under month --
        line_y = title_y + 12
        self.set_draw_color(*WARM_GOLD)
        self.set_line_width(0.8)
        line_w = 60
        self.line((page_w - line_w) / 2, line_y, (page_w + line_w) / 2, line_y)
        
        # -- Calendar grid --
        grid_y = line_y + 5
        
        # Calendar grid dimensions
        grid_top = grid_y
        grid_left = 15
        grid_right = page_w - 15
        grid_w = grid_right - grid_left
        grid_h = 110  # height of the full grid
        
        # Day cell dimensions
        col_w = grid_w / 7
        # Header row for day names + 6 weeks of dates
        header_h = 7
        row_h = (grid_h - header_h) / 6
        
        # -- Day of week headers --
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        
        # Light header background
        self.set_fill_color(*DARK_GREEN)
        for i, day in enumerate(days):
            x = grid_left + i * col_w
            self.set_fill_color(*DARK_GREEN)
            self.rect(x, grid_top, col_w, header_h, 'F')
            self.set_font("DejaVu", "B", 7)
            self.set_text_color(*WHITE)
            self.set_xy(x, grid_top)
            self.cell(col_w, header_h, day, align='C')
        
        # -- Get calendar data --
        cal = calendar.monthcalendar(YEAR, month_num)
        
        # -- Draw day cells --
        self.set_draw_color(*DARK_GREEN)
        self.set_line_width(0.3)
        
        # Draw horizontal grid lines
        for week_idx in range(7):  # 0 = header line, 1-6 = week lines
            y = grid_top + header_h + week_idx * row_h
            self.set_draw_color(*DARK_GREEN)
            self.set_line_width(0.3)
            self.line(grid_left, y, grid_right, y)
        
        # Draw vertical grid lines
        for day_idx in range(8):
            x = grid_left + day_idx * col_w
            self.line(x, grid_top, x, grid_top + header_h + 6 * row_h)
        
        # -- Fill in dates --
        for week_idx, week in enumerate(cal):
            for day_idx, day in enumerate(week):
                if day == 0:
                    continue
                
                cell_x = grid_left + day_idx * col_w
                cell_y = grid_top + header_h + week_idx * row_h
                
                # Highlight weekends (Sat = 5, Sun = 6)
                if day_idx >= 5:
                    self.set_fill_color(*SOFT_PINK)
                    alpha = 0.3
                    self.set_fill_color(250, 240, 240)
                    self.rect(cell_x + 0.5, cell_y + 0.5, col_w - 1, row_h - 1, 'F')
                
                # Today highlight (just for reference - not applicable for future calendar)
                
                # Day number
                self.set_font("DejaVu", "B", 9)
                self.set_text_color(*DARK_GREEN)
                self.set_xy(cell_x + 1, cell_y + 1)
                self.cell(col_w - 2, 5, str(day))
        
        # -- Notes section at bottom --
        notes_y = grid_top + grid_h + 5
        notes_h = page_h - notes_y - 15
        
        # Notes label
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*MEDIUM_GREEN)
        self.set_xy(grid_left, notes_y)
        self.cell(grid_w, 6, "Notes & Reminders")
        
        # Notes lines
        self.set_draw_color(*LIGHT_GREEN)
        self.set_line_width(0.3)
        line_spacing = max(6, (notes_h - 6) / 4)
        for i in range(4):
            ly = notes_y + 6 + (i + 1) * line_spacing
            self.line(grid_left, ly, grid_right, ly)
        
        # -- Page footer --
        self.set_font("DejaVu", "", 7)
        self.set_text_color(*MEDIUM_GREEN)
        self.set_xy(0, page_h - 12)
        self.cell(page_w, 5, f"Wildflower & Co. \u2022 {YEAR} Calendar \u2022 {month_name} \u2022 Print-at-home", align='C')
        
        # -- Decorative corner elements --
        self.set_draw_color(*MEDIUM_GREEN)
        self.set_line_width(0.5)
        # Top-left corner
        self.line(10, 10, 20, 10)
        self.line(10, 10, 10, 20)
        # Top-right corner
        self.line(page_w - 10, 10, page_w - 20, 10)
        self.line(page_w - 10, 10, page_w - 10, 20)
        # Bottom-left corner
        self.line(10, page_h - 10, 20, page_h - 10)
        self.line(10, page_h - 10, 10, page_h - 20)
        # Bottom-right corner
        self.line(page_w - 10, page_h - 10, page_w - 20, page_h - 10)
        self.line(page_w - 10, page_h - 10, page_w - 10, page_h - 20)

    def draw_cover_page(self):
        """Draw the cover page for the calendar."""
        self.add_page()
        
        page_w = self.w
        page_h = self.h
        
        # -- Background --
        self.set_fill_color(*CREAM)
        self.rect(0, 0, page_w, page_h, 'F')
        
        # -- Decorative border --
        self.set_draw_color(*DARK_GREEN)
        self.set_line_width(2)
        self.rect(5, 5, page_w - 10, page_h - 10, 'D')
        
        self.set_draw_color(*WARM_GOLD)
        self.set_line_width(0.8)
        self.rect(10, 10, page_w - 20, page_h - 20, 'D')
        
        # -- Cover image --
        cover_img_path = os.path.join(IMAGE_DIR, "00-cover-wildflower-collage.png")
        if os.path.exists(cover_img_path):
            # Place the cover image in the upper portion
            with Image.open(cover_img_path) as img:
                orig_w, orig_h = img.size
                aspect = orig_w / orig_h
            
            max_w = page_w - 40
            max_h = 100
            img_w = max_w
            img_h = img_w / aspect
            if img_h > max_h:
                img_h = max_h
                img_w = img_h * aspect
            
            x_center = (page_w - img_w) / 2
            self.image(cover_img_path, x=x_center, y=20, w=img_w, h=img_h)
            content_y = 20 + img_h + 10
        else:
            content_y = 40
        
        # -- Title --
        self.set_font("DejaVu", "B", 36)
        self.set_text_color(*DARK_GREEN)
        self.set_xy(0, content_y)
        self.cell(page_w, 15, "Wildflower & Co.", align='C')
        
        # -- Subtitle --
        self.set_font("DejaVu", "", 12)
        self.set_text_color(*MEDIUM_GREEN)
        self.set_xy(0, content_y + 18)
        self.cell(page_w, 8, "Botanical Calendar", align='C')
        
        # -- Year --
        self.set_font("DejaVu", "B", 48)
        self.set_text_color(*DARK_BROWN)
        self.set_xy(0, content_y + 35)
        self.cell(page_w, 20, str(YEAR), align='C')
        
        # -- Decorative line --
        line_y = content_y + 62
        self.set_draw_color(*WARM_GOLD)
        self.set_line_width(1.2)
        line_w = 80
        self.line((page_w - line_w) / 2, line_y, (page_w + line_w) / 2, line_y)
        
        # -- Description --
        self.set_font("DejaVu", "", 10)
        self.set_text_color(*MEDIUM_GREEN)
        desc_text = "A year of seasonal wildflowers — print, display, and enjoy nature's beauty all year long."
        self.set_xy(30, line_y + 8)
        self.cell(page_w - 60, 10, desc_text, align='C')
        
        # -- Month preview list --
        self.set_font("DejaVu", "", 9)
        self.set_text_color(*DARK_GREEN)
        preview_y = line_y + 25
        months_short = ["Jan: Snowdrops", "Feb: Crocus", "Mar: Daffodils", "Apr: Bluebells",
                        "May: Wild Roses", "Jun: Foxgloves", "Jul: Lavender", "Aug: Sunflowers",
                        "Sep: Coneflowers", "Oct: Chrysanthemums", "Nov: Heather", "Dec: Winterberry"]
        
        col_width = page_w / 4
        for i, m in enumerate(months_short):
            col = i % 4
            row = i // 4
            x = 10 + col * col_width
            y = preview_y + row * 12
            self.set_xy(x, y)
            self.cell(col_width - 5, 8, m, align='C')
        
        # -- Footer --
        self.set_font("DejaVu", "", 8)
        self.set_text_color(*MEDIUM_GREEN)
        self.set_xy(0, page_h - 20)
        self.cell(page_w, 8, "Print at home \u2022 A4 / Letter size \u2022 Designed with love \u2665", align='C')
        
        # -- Decorative corner elements --
        self.set_draw_color(*DARK_GREEN)
        self.set_line_width(0.8)
        self.line(15, 15, 30, 15)
        self.line(15, 15, 15, 30)
        self.line(page_w - 15, 15, page_w - 30, 15)
        self.line(page_w - 15, 15, page_w - 15, 30)
        self.line(15, page_h - 15, 30, page_h - 15)
        self.line(15, page_h - 15, 15, page_h - 30)
        self.line(page_w - 15, page_h - 15, page_w - 30, page_h - 15)
        self.line(page_w - 15, page_h - 15, page_w - 15, page_h - 30)


def main():
    pdf = CalendarPDF()
    
    # -- Generate cover --
    print("Generating cover page...")
    pdf.draw_cover_page()
    
    # -- Generate each month --
    individual_pdfs = []
    
    for month_num, month_name, img_file, flower_name in MONTHS:
        print(f"Generating {month_name}...")
        img_path = os.path.join(IMAGE_DIR, img_file)
        pdf.draw_calendar_page(month_num, month_name, img_path, flower_name)
        
        # Also create individual monthly PDF
        month_pdf = CalendarPDF()
        month_pdf.draw_calendar_page(month_num, month_name, img_path, flower_name)
        month_output = os.path.join(OUTPUT_DIR, f"{month_num:02d}-{month_name.lower()}-2027.pdf")
        month_pdf.output(month_output)
        individual_pdfs.append(month_output)
        print(f"  -> Saved {month_output}")
    
    # -- Save full-year combined PDF --
    full_output = os.path.join(OUTPUT_DIR, "wildflower-and-co-2027-calendar-full.pdf")
    pdf.output(full_output)
    print(f"\nFull calendar saved: {full_output}")
    
    print(f"\nIndividual month PDFs saved:")
    for p in individual_pdfs:
        print(f"  {p}")
    
    print("\nDone!")


if __name__ == "__main__":
    main()