# AWS Rekognition Hands-On

This project contains Python scripts demonstrating AWS Rekognition and Bedrock services for image analysis and AI-powered recipe generation for pets.

## Project Overview

The project includes two main applications:

1. **amazon_rekognition.py** - Basic image label detection using AWS Rekognition
2. **pet_food_recipes.py** - Advanced application combining Rekognition for ingredient detection with Bedrock for recipe generation and image synthesis

## Prerequisites

Before running these scripts, you need to set up the following:

### AWS Credentials
- AWS account with appropriate IAM permissions
- AWS credentials configured locally (via AWS CLI or environment variables)
- Required IAM permissions for:
  - `rekognition:DetectLabels` (for Rekognition service)
  - `bedrock:InvokeModel` (for Bedrock service - only needed for pet_food_recipes.py)

### Python Environment
- Python 3.7 or higher
- Required Python packages:
  ```bash
  pip install boto3
  ```

### Sample Assets
- Image files in the `assets/` directory:
  - `sample_image.jpeg` - Used for ingredient detection and testing
  - `ingredients.jpeg` - Alternative test image

## File Descriptions

### amazon_rekognition.py

Simple script demonstrating AWS Rekognition's label detection capability.

**Functions:**
- `detect_labels(image_path, max_labels=10)` - Detects labels (objects, activities, concepts) in an image
  - **Parameters:**
    - `image_path` (str): Path to the local image file
    - `max_labels` (int): Maximum number of labels to return (default: 10)
  - **Returns:** List of detected label names

**Usage:**
```bash
python amazon_rekognition.py
```

**Example Output:**
```
Labels detected: ['Dog', 'Pet', 'Animal', 'Food', 'Bowl']
```

### pet_food_recipes.py

Advanced application that combines multiple AWS services to create pet food recipes.

**Functions:**

1. **detect_ingredients_from_image(image_path)**
   - Reads an image and detects food ingredients using Rekognition
   - Filters results with confidence > 50%
   - **Returns:** List of detected food ingredients

2. **generate_recipe(ingredients, pet_info)**
   - Creates a healthy pet food recipe using Amazon Bedrock (Nova Micro model)
   - Accepts detected ingredients and pet information
   - Includes nutritional analysis in the generated recipe
   - **Parameters:**
     - `ingredients` (list): List of food items
     - `pet_info` (dict): Dictionary with 'breed' and 'age' keys
   - **Returns:** Recipe object with formatted recipe text

3. **generate_recipe_image(recipe_name)**
   - Generates a visual representation of the recipe using Bedrock Nova Canvas
   - Creates appetizing food photography
   - **Parameters:**
     - `recipe_name` (str): Name of the recipe to visualize
   - **Returns:** Path to saved image file (generated_recipe.png)

4. **save_recipe(recipe, output_file)**
   - Saves the generated recipe text to a file
   - **Parameters:**
     - `recipe` (str): Recipe text content
     - `output_file` (str): Output filename
   - **Returns:** Boolean indicating success/failure

**Usage:**
```bash
python pet_food_recipes.py
```

**Workflow:**
1. Reads image from `assets/sample_image.jpeg`
2. Detects ingredients using Amazon Rekognition
3. Generates recipe for a Golden Retriever (2 years old)
4. Saves recipe to `recipe.txt`
5. Generates a visual representation of the recipe
6. Saves generated image as `generated_recipe.png`

**Expected Output Files:**
- `recipe.txt` - Generated recipe with ingredients, instructions, and nutritional analysis
- `generated_recipe.png` - AI-generated image of the recipe

## Running the Scripts

### Basic Image Label Detection
```bash
# Run the simple Rekognition example
python amazon_rekognition.py
```

### Advanced Pet Food Recipe Generation
```bash
# Run the complete pet food recipe application
python pet_food_recipes.py
```

## Configuration

### Customizing Pet Information
To generate recipes for different pets, edit the `pet_info` dictionary in `pet_food_recipes.py`:

```python
pet_info = {
    "breed": "Golden Retriever",  # Change breed name
    "age": 2                        # Change pet age
}
```

### Adjusting Rekognition Parameters
- Modify `MaxLabels` parameter to get more or fewer detected items
- Adjust the confidence threshold in `detect_ingredients_from_image()` (currently 50%)

### Bedrock Model Configuration
- Text generation uses: `amazon.nova-micro-v1:0`
- Image generation uses: `amazon.nova-canvas-v1:0`
- Adjust `numberOfImages`, `cfgScale`, `height`, and `width` in image generation config as needed

## Output

The `pet_food_recipes.py` script generates:
- **Console Output:** Progress messages and detected ingredients
- **recipe.txt:** Complete recipe with instructions and nutritional information
- **generated_recipe.png:** AI-generated image of the recipe

## Error Handling

Both scripts include error handling with try-except blocks:
- File reading errors are caught and reported
- API call failures print descriptive error messages
- Missing images or credentials will produce appropriate error messages

## AWS Costs

Be aware that:
- Rekognition charges per image analyzed
- Bedrock charges per token used in API calls
- Monitor AWS billing to understand usage costs

## Resources

- [AWS Rekognition Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html)
- [AWS Bedrock Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html)
- [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/)

## Troubleshooting

**Issue:** `NoCredentialsError` or credential-related errors
- **Solution:** Ensure AWS credentials are configured. Run `aws configure` or set environment variables.

**Issue:** `FileNotFoundError` for image files
- **Solution:** Ensure sample images exist in the `assets/` directory.

**Issue:** Permission denied errors
- **Solution:** Verify IAM user has permissions for rekognition:DetectLabels and bedrock:InvokeModel.

**Issue:** Bedrock model not found
- **Solution:** Ensure you have access to Nova models in your AWS region. Check AWS Bedrock console for available models.

