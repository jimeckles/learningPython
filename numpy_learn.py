import numpy as np

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]


# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)


# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2

for i in range(len(np_weight_kg)):
    print("kg: %s - lbs: %s" % (round(np_weight_kg[i], 2), round(np_weight_lbs[i], 2)))

# Print out np_weight_lbs
