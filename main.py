#!/usr/bin/env python3
"""PDF Compressor CLI"""

import click
from pathlib import Path
from src.compressor import PDFCompressor
from src.utils import validate_pdf_path, get_output_path, get_pdf_files


@click.group()
def cli():
    """PDF Compressor - Reduce PDF file sizes efficiently"""
    pass


@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('-o', '--output', type=click.Path(), help='Output file path')
@click.option('-q', '--quality', type=click.Choice(['low', 'medium', 'high']), 
              default='medium', help='Compression quality level')
def compress(input_file, output, quality):
    """Compress a single PDF file"""
    
    # Validate input
    is_valid, error = validate_pdf_path(input_file)
    if not is_valid:
        click.echo(f"❌ Error: {error}", err=True)
        return
    
    # Generate output path
    output_path = get_output_path(input_file, output)
    
    # Compress
    compressor = PDFCompressor(quality=quality)
    result = compressor.compress(input_file, output_path)
    
    if result['status'] == 'success':
        click.echo(f"✅ Compression complete!")
        click.echo(f"   Output: {output_path}")
    else:
        click.echo(f"❌ Compression failed: {result.get('message')}", err=True)


@cli.command()
@click.argument('directory', type=click.Path(exists=True))
@click.option('-q', '--quality', type=click.Choice(['low', 'medium', 'high']), 
              default='medium', help='Compression quality level')
@click.option('-o', '--output-dir', type=click.Path(), help='Output directory')
def batch(directory, quality, output_dir):
    """Compress all PDFs in a directory"""
    
    pdf_files = get_pdf_files(directory)
    
    if not pdf_files:
        click.echo(f"❌ No PDF files found in {directory}")
        return
    
    click.echo(f"Found {len(pdf_files)} PDF(s) to compress...")
    
    compressor = PDFCompressor(quality=quality)
    
    total_original = 0
    total_compressed = 0
    
    for pdf_file in pdf_files:
        output_path = get_output_path(
            pdf_file, 
            output_dir + '/' + pdf_file.name if output_dir else None
        )
        
        result = compressor.compress(str(pdf_file), str(output_path))
        
        if result['status'] == 'success':
            total_original += result['original_size']
            total_compressed += result['compressed_size']
    
    if total_original > 0:
        total_reduction = ((total_original - total_compressed) / total_original * 100)
        click.echo(f"\n✅ Batch compression complete!")
        click.echo(f"   Total reduction: {total_reduction:.2f}%")


@cli.command()
def version():
    """Show version"""
    click.echo("PDF Compressor v1.0.0")


if __name__ == '__main__':
    cli()
