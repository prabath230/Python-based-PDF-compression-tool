"""Utility Functions"""

import os
from pathlib import Path


def validate_pdf_path(file_path):
    """Validate if file is a valid PDF"""
    file_path = Path(file_path)
    
    if not file_path.exists():
        return False, f"File not found: {file_path}"
    
    if file_path.suffix.lower() != ".pdf":
        return False, f"File is not a PDF: {file_path.suffix}"
    
    return True, None


def get_output_path(input_path, output_path=None, suffix="_compressed"):
    """Generate output path if not provided"""
    input_path = Path(input_path)
    
    if output_path:
        return Path(output_path)
    
    return input_path.parent / f"{input_path.stem}{suffix}.pdf"


def get_pdf_files(directory):
    """Get all PDF files in a directory"""
    directory = Path(directory)
    
    if not directory.is_dir():
        return []
    
    return list(directory.glob("*.pdf"))


def format_bytes(size_bytes):
    """Convert bytes to human-readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"
