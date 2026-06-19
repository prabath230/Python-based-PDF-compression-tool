# PDF Compressor

A simple Python tool to compress PDF files by reducing image quality and removing metadata.

## Features

- 🗜️ **Compress PDFs** - Reduce file size significantly
- 🎚️ **Quality Levels** - Choose between low, medium, and high quality
- 📁 **Batch Processing** - Compress multiple PDFs at once
- 📊 **Statistics** - See detailed compression metrics
- 🚀 **CLI Interface** - Easy-to-use command-line tool

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone the repository or download the files
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Compress a Single PDF

```bash
python main.py compress input.pdf -o output.pdf -q medium
```

**Options:**
- `-o, --output` - Output file path (optional, defaults to `input_compressed.pdf`)
- `-q, --quality` - Compression quality: `low`, `medium`, `high` (default: `medium`)

### Batch Compress PDFs

```bash
python main.py batch /path/to/pdfs -q medium -o /output/directory
```

**Options:**
- `-q, --quality` - Compression quality level
- `-o, --output-dir` - Output directory for compressed files

### Examples

```bash
# Compress a single PDF with default settings
python main.py compress document.pdf

# Compress with high quality (better quality, larger file)
python main.py compress large.pdf -q high -o compressed.pdf

# Compress all PDFs in a folder
python main.py batch ./pdfs -q low

# Show version
python main.py version
```

## Quality Levels

| Level  | Quality | Best For |
|--------|---------|----------|
| low    | 50%     | Text-heavy documents, maximum compression |
| medium | 75%     | Balanced quality and file size (recommended) |
| high   | 90%     | Graphics-heavy documents, minimal compression |

## How It Works

The compressor:
1. Reads the input PDF
2. Removes unnecessary metadata
3. Recompresses images to the selected quality level
4. Writes the compressed PDF to the output path
5. Reports compression statistics

## Project Structure

```
pdf-compressor/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── compressor.py        # Core compression logic
│   └── utils.py             # Utility functions
├── tests/
│   ├── __init__.py
│   └── test_compressor.py   # Unit tests
├── main.py                  # CLI entry point
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## Testing

Run the test suite:

```bash
pytest tests/ -v
```

## Dependencies

- **pypdf** (4.0.1) - PDF manipulation
- **Pillow** (10.1.0) - Image processing
- **click** (8.1.7) - CLI framework
- **pytest** (7.4.3) - Testing framework

## Limitations

- Currently supports basic compression through metadata removal
- Image recompression requires additional implementation
- Works with standard PDFs; complex layouts may have reduced effectiveness

## Future Enhancements

- [ ] Advanced image recompression with quality profiles
- [ ] Support for password-protected PDFs
- [ ] Parallel batch processing for faster compression
- [ ] GUI interface
- [ ] Compression presets
- [ ] Detailed compression report generation

## License

MIT License - Feel free to use and modify as needed

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

---

**Version:** 1.0.0  
**Last Updated:** 2026-06-19
