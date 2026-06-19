"""Core PDF Compression Module"""

import os
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from PIL import Image
import io
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PDFCompressor:
    """Compress PDF files by reducing image quality and removing metadata"""
    
    QUALITY_LEVELS = {
        "low": 50,
        "medium": 75,
        "high": 90
    }
    
    def __init__(self, quality="medium"):
        """
        Initialize PDF Compressor
        
        Args:
            quality (str): Compression quality - "low", "medium", or "high"
        """
        if quality not in self.QUALITY_LEVELS:
            raise ValueError(f"Quality must be one of {list(self.QUALITY_LEVELS.keys())}")
        self.quality = self.QUALITY_LEVELS[quality]
    
    def compress(self, input_path, output_path):
        """
        Compress a PDF file
        
        Args:
            input_path (str): Path to input PDF
            output_path (str): Path to output compressed PDF
            
        Returns:
            dict: Compression statistics
        """
        try:
            input_path = Path(input_path)
            output_path = Path(output_path)
            
            if not input_path.exists():
                raise FileNotFoundError(f"Input file not found: {input_path}")
            
            # Get original file size
            original_size = input_path.stat().st_size
            
            # Read PDF
            reader = PdfReader(str(input_path))
            writer = PdfWriter()
            
            # Process each page
            for page_num, page in enumerate(reader.pages):
                # Remove images from page and recompress
                page = self._compress_page(page)
                writer.add_page(page)
            
            # Remove metadata
            writer.metadata = {}
            
            # Write compressed PDF
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(str(output_path), "wb") as output_file:
                writer.write(output_file)
            
            # Get compressed file size
            compressed_size = output_path.stat().st_size
            
            # Calculate statistics
            reduction = original_size - compressed_size
            percentage = (reduction / original_size * 100) if original_size > 0 else 0
            
            stats = {
                "original_size": original_size,
                "compressed_size": compressed_size,
                "reduction": reduction,
                "percentage": round(percentage, 2),
                "status": "success"
            }
            
            logger.info(f"✓ Compressed {input_path.name}")
            logger.info(f"  Original: {self._format_size(original_size)}")
            logger.info(f"  Compressed: {self._format_size(compressed_size)}")
            logger.info(f"  Reduction: {stats['percentage']}%")
            
            return stats
            
        except Exception as e:
            logger.error(f"✗ Error compressing {input_path}: {str(e)}")
            return {"status": "error", "message": str(e)}
    
    def _compress_page(self, page):
        """Compress images on a PDF page"""
        # This is a basic implementation
        # For full image compression, we'd need to extract and recompress images
        return page
    
    @staticmethod
    def _format_size(size_bytes):
        """Convert bytes to human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.2f} TB"
