def map_scores(preds, top=3):
    """
    Maps the scores/probabilities to the corresponding class/label

    # Arguments
        preds: Numpy tensor encoding a batch of predictions.
        top: Integer, how many top-guesses to return.

    # Returns
        A list of lists of top class prediction tuples
        `(class_name, class_description, score)`.
        One list of tuples per sample in batch input.
    """
    
    CLASS_INDEX = {
        '0': ['akiec',"Actinic keratoses and intraepithelial carcinoma / Bowen's disease"], 
        '1': ['bcc',"basal cell carcinoma"], 
        '2': ['bkl',"benign keratosis-like lesions, solar lentigines / seborrheic keratoses and lichen-planus like keratoses"], 
        '3': ['df',"dermatofibroma"], 
        '4': ['mel',"melanoma"], 
        '5': ['nv',"melanocytic nevi"], 
        '6': ['vasc',"vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage)"]
    }

    if top > 7:
        top = 7

    results = []
    for pred in preds:
        top_indices = pred.argsort()[-top:][::-1]
        result = [tuple(CLASS_INDEX[str(i)]) + (pred[i],) for i in top_indices]
        result.sort(key=lambda x: x[2], reverse=True)
        results.append(result)
    return results