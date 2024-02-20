import random

# Define the items based on their aspect groups
items = {
    'menjunjung_tinggi_moral': list(range(1, 18)),  # Items 1-17
    'perasaan_emosi_negatif': list(range(18, 31)),  # Items 18-30
    'motivasi_untuk_memperbaiki': list(range(31, 46))  # Items 31-45
}

# Shuffle the items within each aspect
shuffled_items = {aspect: random.sample(items[aspect], len(items[aspect])) for aspect in items}

# Combine and shuffle all items together to randomize across aspects
combined_shuffled_items = shuffled_items['menjunjung_tinggi_moral'] + \
                          shuffled_items['perasaan_emosi_negatif'] + \
                          shuffled_items['motivasi_untuk_memperbaiki']
random.shuffle(combined_shuffled_items)

print(combined_shuffled_items)