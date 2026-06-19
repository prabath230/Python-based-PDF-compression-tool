# PDF Compressor

A Python-based PDF compression tool created specifically for publishing PDFs to the **NMRA (National Medicines regulatory Authority) website**.

## Purpose & Background

### The Problem

The NMRA website CMS has a **10MB file size limit** for PDF uploads. Many organizational documents exceed this limit, making it impossible to publish them through the standard webflow CMS.

### Why a Custom Solution?

Rather than relying on third-party tools or services, this custom compressor was created because:

1. **Data Privacy & Security** - Keep sensitive documents in-house without uploading to external services
2. **Consistency** - Control the compression algorithm and quality levels to ensure consistent results
3. **Integration** - Easily integrate with internal workflows and batch processes
4. **Cost Efficiency** - No subscription fees or usage limits
5. **Customization** - Adjust compression parameters specifically for organizational needs

### Use Cases

- **Primary**: Compress organizational PDFs before uploading to NMRA website
- **Secondary**: Batch compress multiple documents for archival, reduce storage space, prepare publications for digital distribution

---

## Features

- 🗜️ **Compress PDFs** - Reduce file size significantly
- 🎚️ **Quality Levels** - Choose between low, medium, and high quality
- 📁 **Batch Processing** - Compress multiple PDFs at once
- 📊 **Statistics** - See detailed compression metrics
- 🚀 **CLI Interface** - Easy-to-use command-line tool
- 🔒 **No External Services** - Works completely offline

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

| Level  | Quality | File Size Reduction | Best For |
|--------|---------|-------------------|----------|
| **low** | 50% | Maximum | Text-heavy documents, technical specs |
| **medium** | 75% | Balanced | Most documents (recommended) |
| **high** | 90% | Minimal | Documents with important graphics |

## How It Works

The compressor:
1. Reads the input PDF
2. Removes unnecessary metadata
3. Recompresses images to the selected quality level
4. Writes the compressed PDF to the output path
5. Reports compression statistics

## Publishing Workflows

### Standard Workflow

```
Original PDF (>10MB)
        ↓
    [Compress]
        ↓
Compressed PDF (<10MB)
        ↓
[Upload to NMRA CMS]
        ↓
[Publish to Website]
```

### Batch Processing Workflow

```
PDF Directory
        ↓
[Batch Compress All Files]
        ↓
Output Directory (All <10MB)
        ↓
[Verification & Review]
        ↓
[Upload to NMRA CMS]
```

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
- **Pillow** (11.0.0) - Image processing
- **click** (8.1.7) - CLI framework
- **pytest** (7.4.3) - Testing framework

## Technical Benefits

- **No External API Calls** - Works completely offline
- **Python-Based** - Easy to maintain and modify
- **Simple CLI** - Easy to automate in scripts
- **Detailed Logging** - Compression statistics and reporting
- **Robust Error Handling** - Gracefully handles problematic files

## Limitations

- Currently supports basic compression through metadata removal
- Image recompression requires additional implementation
- Works with standard PDFs; complex layouts may have reduced effectiveness

## Future Enhancements

- [ ] Advanced image recompression with quality profiles
- [ ] Support for password-protected PDFs

## License

MIT License - Feel free to use and modify as needed

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

---

**Version:** 1.0.0  
**Created:** 2026  
**Purpose:** NMRA Website PDF Publishing  
**Status:** Active & Maintained
