import logging


# Створення логера
logger = logging.getLogger(__name__)

# Налаштування рівня логування
logger.setLevel(logging.DEBUG)

# Створення обробника для виводу в stdout (консоль)
console_handler = logging.StreamHandler()

# Створення обробника для запису в файл
file_handler = logging.FileHandler('example.log', encoding="utf8")

# Налаштування рівня логування для обробників
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

# Створення форматера для обробника
formatter = logging.Formatter('%(asctime)s | %(filename)s | %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Додавання обробника до логера
logger.addHandler(console_handler)
logger.addHandler(file_handler)

if __name__ == "__main__":
    logger.debug('Це повідомлення рівня DEBUG')
    logger.info('Це повідомлення рівня INFO')
    logger.warning('Це повідомлення рівня WARNING')
    logger.error('Це повідомлення рівня ERROR')
    logger.critical('Це повідомлення рівня CRITICAL')
# """
# - **%(asctime)s**: Додає час логування у форматі "рік-місяць-день година:хвилина:секунда,мілісекунда".
# - **%(levelname)s**: Додає рівень логування (наприклад, DEBUG, INFO, WARNING, ERROR, CRITICAL).
# - **%(message)s**: Додає текстове повідомлення логу.
# - **%(filename)s**: Додає ім'я файлу, з якого було викликано логування.
# - **%(funcName)s**: Додає ім'я функції, з якої було викликано логування.
# - **%(lineno)d**: Додає номер рядка у файлі, з якого було викликано логування.
# - **%(name)s**: Додає ім'я логера.
# """
