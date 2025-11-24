from PIL import Image, ImageDraw, ImageFont
import os

def optimize_image(input_path, max_size=(800, 800), quality=80):
    try:
        with Image.open(input_path) as img:
            # Convert to RGB if necessary (e.g. if RGBA)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # Resize if larger than max_size
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # Save with optimization
            img.save(input_path, "JPEG", quality=quality, optimize=True)
            print(f"Optimized {input_path}")
    except Exception as e:
        print(f"Error optimizing {input_path}: {e}")

def create_favicon(output_path, size=(64, 64), color="#111111", text_color="#ffffff"):
    try:
        img = Image.new('RGB', size, color)
        d = ImageDraw.Draw(img)
        
        # Draw a simple "M"
        # Since we might not have a specific font, we'll draw lines or use default
        # Drawing a simple geometric M
        margin = size[0] // 4
        w, h = size
        points = [
            (margin, h - margin),
            (margin, margin),
            (w // 2, h // 2),
            (w - margin, margin),
            (w - margin, h - margin)
        ]
        d.line(points, fill=text_color, width=4)
        
        img.save(output_path, "PNG")
        print(f"Created {output_path}")
    except Exception as e:
        print(f"Error creating favicon: {e}")

if __name__ == "__main__":
    optimize_image("me.jpg")
    create_favicon("favicon.png")
