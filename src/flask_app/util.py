import numpy as np

def map_scores(preds, top=3):
    """
    Maps the scores/probabilities to the corresponding class/label

    # Arguments
        preds: Numpy tensor encoding a batch of predictions.
        top: Integer, how many top-guesses to return.

    # Returns
        A list of lists of model name and top class prediction tuples
        `model_name, (class_name, class_description, score), ...`.
        One list of tuples per sample in batch input.
    """
    
    CLASS_INDEX = {
        '0': ["akiec","Actinic Keratoses and Intraepithelial Carcinoma / Bowen's Disease"], 
        '1': ["bcc","Basal Cell Carcinoma"], 
        '2': ["bkl","Solar Lentigines / Seborrheic Keratoses"], 
        '3': ["df","Dermatofibroma"], 
        '4': ["mel","Melanoma"], 
        '5': ["nv","Melanocytic Nevi"], 
        '6': ["vasc","Vascular Lesions (Angiomas, Angiokeratomas, Pyogenic Granulomas and Hemorrhage)"]
    }

    if top > 7:
        top = 7

    results = []
    for pred in preds:
        result = [pred[0]]
        top_indices = pred[1].argsort()[-top:][::-1]
        scores = [tuple(CLASS_INDEX[str(i)]) + (np.double(pred[1][i]),) for i in top_indices]
        #scores = [list(CLASS_INDEX[str(i)]) + (pred[1][i],) for i in top_indices]
        scores.sort(key=lambda x: x[2], reverse=True)
        result.extend(scores)
        results.append(result)
    return results



'''
Original Descriptions
'0': ["akiec","Actinic Keratoses and Intraepithelial Carcinoma / Bowen's Disease"], 
'1': ["bcc","Basal Cell Carcinoma"], 
'2': ["bkl","Benign Keratosis-like Lesions, Solar Lentigines / Seborrheic Keratoses and Lichen-planus like Keratoses"], 
'3': ["df","Dermatofibroma"], 
'4': ["mel","Melanoma"], 
'5': ["nv","Melanocytic Nevi"], 
'6': ["vasc","Vascular Lesions (Angiomas, Angiokeratomas, Pyogenic Granulomas and Hemorrhage)"]
'''