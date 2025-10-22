from fpdf import FPDF
import os

def generate_pdf(result):
    os.makedirs("static/reports", exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "NeuroGuard Clinical Report", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Predicted Outcome: {result}", ln=True)
    path = "static/reports/result.pdf"
    pdf.output(path)
    return path
