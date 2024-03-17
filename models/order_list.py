import datetime
from models.order import Order

orders = [
    Order("Oleksii", datetime.datetime(2024, 3, 17), 2, 'ACER Swift X 14" Laptop - Intel® Core™ i7, 1 TB SSD, Grey', 'ACER', 12),
    Order("Alice", datetime.datetime(2024, 3, 16), 1, 'iPhone 15 Pro Max - 512GB, Pacific Blue', 'Apple', 24),
    Order("Bob", datetime.datetime(2024, 3, 15), 3, 'Xbox Series X Console', 'Microsoft', 12),
    Order("Charlie", datetime.datetime(2024, 3, 14), 1, 'The Last of Us Part III - PlayStation 6', 'Naughty Dog', 0),
    Order("David", datetime.datetime(2024, 3, 13), 2, 'Nikon Z9 Mirrorless Camera with 24-70mm Lens', 'Nikon', 36),
    Order("Emily", datetime.datetime(2024, 3, 12), 1, 'Nintendo Switch OLED Model', 'Nintendo', 12),
    Order("Frank", datetime.datetime(2024, 3, 11), 1, 'Dyson V15 Detect Total Clean Cordless Vacuum', 'Dyson', 24),
    Order("Grace", datetime.datetime(2024, 3, 10), 2, 'Samsung 75" QLED 8K UHD Smart TV', 'Samsung', 12),
    Order("Hannah", datetime.datetime(2024, 3, 9), 1, 'Kindle Oasis E-reader - 32GB, Wi-Fi + Free Cellular Connectivity', 'Amazon', 12),
    Order("Isaac", datetime.datetime(2024, 3, 8), 3, 'PlayStation VR2 Bundle - PS5', 'Sony', 12)
]