# Complete the following tasks to work with Amazon Rekognition for label detection

# Import the required boto3 library

import boto3

# Create an Amazon Rekognition client
rekognition = boto3.client('rekognition')



# Create a simple function that takes two parameters:
#    - image_path (str): Path to the local image file
#    - max_labels (int): Maximum number of labels to return (default: 10)
def detect_labels(image_path, max_labels=10):
    """
    Detects labels in images using Amazon Rekognition.
    
    Parameters:
        image_path: Path to the local image file
        max_labels: Maximum number of labels to return (default: 10)
    """
    #TODO: Complete the function and replace the word 'pass' with your code

    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()

    response = rekognition.detect_labels(
        Image={'Bytes': image_bytes},
        MaxLabels=max_labels
    )

    labels = []
    for label in response['Labels']:
        labels.append(label['Name'])
    
    return labels



# Test your function with this example call:
result = detect_labels("assets/sample_image.jpeg", max_labels=5)
print("Labels detected:", result)

print("end of file")

# Helpful resources:
# - API Reference: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_labels
