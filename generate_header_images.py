#!/usr/bin/env python3
"""
Generate professional blog header images for FundedList blog posts.
Creates clean, minimalist, geometric designs with B2B SaaS aesthetic.
"""

import os
from PIL import Image, ImageDraw
import random
import math

def create_header_image(title, filename, width=1200, height=630):
    """Create a professional header image with abstract geometric design"""
    
    # Create image with white background
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Define color schemes for different tools
    color_schemes = {
        'zoominfo': ['#1e3a8a', '#3b82f6', '#93c5fd'],  # Blue tones
        'apollo': ['#7c3aed', '#a855f7', '#c4b5fd'],    # Purple tones  
        'rocketreach': ['#059669', '#10b981', '#86efac'], # Green tones
        'lemlist': ['#dc2626', '#ef4444', '#fca5a5'],   # Red tones
        'clearbit': ['#ea580c', '#f97316', '#fed7aa'],  # Orange tones
        'linkedin': ['#0f172a', '#475569', '#94a3b8'],  # Dark blue/gray
        'hunter': ['#16a34a', '#22c55e', '#bbf7d0'],    # Green tones
        'lusha': ['#be185d', '#ec4899', '#fbcfe8'],     # Pink tones
        'clay': ['#7c2d12', '#ea580c', '#fed7aa']       # Brown/orange tones
    }
    
    # Determine color scheme based on filename
    scheme_key = 'default'
    for key in color_schemes.keys():
        if key in filename.lower():
            scheme_key = key
            break
    
    if scheme_key == 'default':
        colors = ['#1e40af', '#3b82f6', '#93c5fd']  # Default blue
    else:
        colors = color_schemes[scheme_key]
    
    # Create gradient background
    for y in range(height):
        # Create subtle gradient from top to bottom
        ratio = y / height
        r1, g1, b1 = tuple(int(colors[0][1:][i:i+2], 16) for i in (0, 2, 4))
        r2, g2, b2 = tuple(int(colors[1][1:][i:i+2], 16) for i in (0, 2, 4))
        
        r = int(r1 + (r2 - r1) * ratio * 0.1)  # Very subtle gradient
        g = int(g1 + (g2 - g1) * ratio * 0.1)
        b = int(b1 + (b2 - b1) * ratio * 0.1)
        
        draw.rectangle([(0, y), (width, y+1)], fill=(r, g, b))
    
    # Add geometric shapes
    shape_count = random.randint(3, 6)
    
    for i in range(shape_count):
        # Random position and size
        x = random.randint(-100, width + 100)
        y = random.randint(-100, height + 100)
        size = random.randint(50, 200)
        
        # Pick color from scheme
        color = colors[random.randint(0, len(colors)-1)]
        
        # Convert hex to RGB and add transparency
        r, g, b = tuple(int(color[1:][i:i+2], 16) for i in (0, 2, 4))
        alpha = random.randint(20, 60)  # Low opacity for subtlety
        
        # Create a temporary image for alpha blending
        overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        
        # Random shape
        shape_type = random.choice(['circle', 'rectangle', 'triangle'])
        
        if shape_type == 'circle':
            overlay_draw.ellipse([x, y, x+size, y+size], fill=(r, g, b, alpha))
        elif shape_type == 'rectangle':
            rotation = random.randint(0, 45)
            # Simple rectangle for now (rotation would be more complex)
            overlay_draw.rectangle([x, y, x+size, y+size//2], fill=(r, g, b, alpha))
        else:  # triangle
            points = [(x, y+size), (x+size//2, y), (x+size, y+size)]
            overlay_draw.polygon(points, fill=(r, g, b, alpha))
        
        # Blend with main image
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    
    # Add some subtle lines/connections
    for i in range(2, 4):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height) 
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        
        line_color = colors[1]
        r, g, b = tuple(int(line_color[1:][i:i+2], 16) for i in (0, 2, 4))
        
        # Very subtle lines
        overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.line([x1, y1, x2, y2], fill=(r, g, b, 15), width=2)
        
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    
    return img

def main():
    """Generate all header images"""
    
    # Blog posts data
    posts = [
        {'slug': 'zoominfo-alternatives', 'title': 'ZoomInfo Alternatives'},
        {'slug': 'apollo-io-alternatives', 'title': 'Apollo.io Alternatives'}, 
        {'slug': 'rocketreach-alternatives', 'title': 'RocketReach Alternatives'},
        {'slug': 'lemlist-alternatives', 'title': 'Lemlist Alternatives'},
        {'slug': 'clearbit-alternatives', 'title': 'Clearbit Alternatives'},
        {'slug': 'linkedin-sales-navigator-alternatives', 'title': 'LinkedIn Sales Navigator Alternatives'},
        {'slug': 'hunter-io-alternatives', 'title': 'Hunter.io Alternatives'},
        {'slug': 'lusha-alternatives', 'title': 'Lusha Alternatives'},
        {'slug': 'clay-alternatives', 'title': 'Clay Alternatives'}
    ]
    
    # Create images directory if it doesn't exist
    img_dir = 'img/blog'
    os.makedirs(img_dir, exist_ok=True)
    
    for post in posts:
        filename = f"{img_dir}/{post['slug']}.png"
        print(f"Generating {filename}...")
        
        # Generate image
        img = create_header_image(post['title'], post['slug'])
        
        # Save image
        img.save(filename, 'PNG', quality=95)
        print(f"Saved {filename}")

if __name__ == '__main__':
    main()