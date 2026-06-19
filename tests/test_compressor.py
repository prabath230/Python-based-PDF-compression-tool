"""Tests for PDF Compressor"""

import pytest
from pathlib import Path
from src.compressor import PDFCompressor
from src.utils import validate_pdf_path, get_output_path


class TestPDFCompressor:
    """Test PDFCompressor class"""
    
    def test_init_valid_quality(self):
        """Test initialization with valid quality"""
        compressor = PDFCompressor(quality="low")
        assert compressor.quality == 50
        
        compressor = PDFCompressor(quality="medium")
        assert compressor.quality == 75
        
        compressor = PDFCompressor(quality="high")
        assert compressor.quality == 90
    
    def test_init_invalid_quality(self):
        """Test initialization with invalid quality"""
        with pytest.raises(ValueError):
            PDFCompressor(quality="ultra")
    
    def test_format_size(self):
        """Test size formatting"""
        assert PDFCompressor._format_size(512) == "512.00 B"
        assert PDFCompressor._format_size(1024) == "1.00 KB"
        assert PDFCompressor._format_size(1024 * 1024) == "1.00 MB"


class TestUtils:
    """Test utility functions"""
    
    def test_validate_pdf_path_nonexistent(self):
        """Test validation of non-existent file"""
        is_valid, error = validate_pdf_path("/nonexistent/file.pdf")
        assert not is_valid
        assert "not found" in error.lower()
    
    def test_validate_pdf_path_non_pdf(self):
        """Test validation of non-PDF file"""
        # Create temp non-PDF file
        temp_file = Path("test.txt")
        temp_file.touch()
        
        try:
            is_valid, error = validate_pdf_path(str(temp_file))
            assert not is_valid
            assert "not a pdf" in error.lower()
        finally:
            temp_file.unlink()
    
    def test_get_output_path_with_custom_output(self):
        """Test output path generation with custom path"""
        output = get_output_path("input.pdf", "/output/custom.pdf")
        assert str(output) == "/output/custom.pdf"
    
    def test_get_output_path_default(self):
        """Test output path generation with default naming"""
        output = get_output_path("document.pdf")
        assert "document_compressed.pdf" in str(output)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
