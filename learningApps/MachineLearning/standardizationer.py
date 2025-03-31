class Standardization:

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
    def standardizeData(self, data, attributeName):
        addDataForAttribute = []
        for i in range(len(data)):
            addDataForAttribute.append(data[i][attributeName])
        print(f"standardizeData:addDataForAttribute {addDataForAttribute}")
        # find the average
        sum = 0
        for i in range(len(addDataForAttribute)):
            sum += addDataForAttribute[i]
        mean = sum / len(addDataForAttribute)
        # find the standard deviation
        sum = 0
        for i in range(len(addDataForAttribute)):
            sum += (addDataForAttribute[i] - mean) ** 2
        standardDeviation = (sum / len(addDataForAttribute)) ** 0.5
        for i in range(len(data)):
            data[i][attributeName] = {
                "original": data[i][attributeName],
                "standardized": (data[i][attributeName] - mean) / standardDeviation,
            }

        return data
