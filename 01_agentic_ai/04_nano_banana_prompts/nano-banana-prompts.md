Nano Banana Prompts Collection and Guide
========================================

A curated library of high-quality, production-ready prompts designed specifically for **Gemini Nano Banana**, enabling creators, developers, and enthusiasts to generate consistent, realistic, and finely-controlled outputs across images, text, and mixed-media tasks.

This repository serves two purposes:

1.  A **collection** of reusable prompts.
    
2.  A **guide** that teaches how to craft, structure, and scale prompts for reliable results.
    

Why This Exists
---------------

Most users struggle with prompt instability, inconsistency, and creative drift.Nano Banana is powerful, but it rewards **structured prompting**, not guesswork.

This repository gives you:

*   Professional-grade prompt templates
    
*   Ready-to-use presets for images, characters, aesthetics, and environments
    
*   Guidance on how to control style, lighting, textures, realism, and mood
    
*   Practical tips for improving quality, reducing hallucination, and preserving subject identity
    

What You Will Find Inside
-------------------------

### 1\. Image Prompts

High-quality JSON-style structured prompts for:

*   Portraits
    
*   Mirror selfies
    
*   Character recreation
    
*   Product shots
    
*   Retro aesthetics
    
*   Clean studio realism
    
*   Fashion, style, and cultural imagery
    

### 2\. Nano Banana Prompt Syntax Breakdown

Understand:

*   Required fields
    
*   Optional styling controls
    
*   Subject preservation logic
    
*   Background control
    
*   Lighting modes
    
*   Texture parameters
    
*   Pose and camera-angle definitions
    

### 3\. Before/After Experiments

Mini case studies showing:

*   Weak prompt
    
*   Improved structured prompt
    
*   Final optimized versionIncluding visual reasoning behind each improvement.
    

### 4\. Best Practices for Prompt Engineering

Covers:

*   Content grouping
    
*   Multi-attribute chaining
    
*   Consistency controls
    
*   Face-preservation techniques
    
*   How to avoid over-stylization
    
*   How to maintain realism

How to Use These Prompts
------------------------

### Basic Flow

1.  Upload your input image (if required).
    
2.  Pick a prompt template from the **prompts** folder.
    
3.  Insert your custom details (clothing, mood, camera type, etc.).
    
4.  Run it through Gemini Nano Banana.
    
5.  Adjust parameters if you want a different feel.
    

### General Tip

Keep your prompt structured, stable, and grouped.Nano Banana responds better to clear JSON-style definitions than casual natural language.

Example Prompt
--------------
```
{    "subject": {      "description": "Use the attached image as the subject. A young man in black shalwar kameez and black coat, confident expression.",      "preserve_original": true    },    "photography": {      "camera_style": "early-2000s digital camera aesthetic",      "lighting": "harsh flash, high grain",      "angle": "mirror selfie"    },    "background": {      "setting": "retro 2000s room",      "elements": ["CD player", "wooden dresser", "posters"]    }  }
```

When to Use This Repository
---------------------------

Use this repo if you want to generate:

*   Consistent photo-realistic images
    
*   Professional portraits
    
*   Cultural/traditional outfits
    
*   Aesthetic-specific visuals (Pakistani retro, 2000s, studio clean shots, etc.)
    
*   Multi-scene versions of the same subject
    
*   High-control character or product images
    

Who This Is For
---------------

*   Developers
    
*   Designers
    
*   Content creators
    
*   Photographers experimenting with AI
    
*   Anyone who wants better control over Nano Banana outputs
    

Future Roadmap
--------------

*   Prebuilt prompt packs (Fashion, Travel, Home Studio)
    
*   Advanced realism tuning guide
    
*   Face consistency toolkit
    
*   Batch prompt generation scripts
    
*   Pretrained “persona” prompt templates
    

Contribute
----------

Pull requests are welcome.If you want to submit your own prompt template, include:

*   The structured prompt
    
*   Expected output style
    
*   Input photo (optional)
    
*   Notes or recommendations
    

License
-------

Open-source for learning and non-commercial use.For commercial usage, please check the Gemini model licensing guidelines.
