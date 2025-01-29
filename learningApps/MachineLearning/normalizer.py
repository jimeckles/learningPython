class Normalizer:

    def __init__(self, classVar):
        self.classVar = classVar

    def printMyStuff(self):
        return self.classVar

    # nomalize data
    # [70000, 60000, 52000]
    # [[70000, 1.0], [60000, 0.4444444444444444], [52000, 0.0]]
    # response is list of arrays,
    # each array has two elements
    # first element is the original value
    # second element is the normalized value
    def normalizeData(self, data, attributeName):
        addDataForAttribute = []
        for i in range(len(data)):
            addDataForAttribute.append(data[i][attributeName])

        minVal = min(addDataForAttribute)
        maxVal = max(addDataForAttribute)
        for i in range(len(data)):
            data[i][attributeName] = {
                "original": data[i][attributeName],
                "normalized": round(
                    (data[i][attributeName] - minVal) / (maxVal - minVal), 3
                ),
            }

        return data
