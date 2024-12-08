import os
import logging

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
# logging.debug("A DEBUG Message")
# logging.info("An INFO")
# logging.warning("A WARNING")
# logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")


def setup_loggers():
    global event_logger, error_logger

    script_dir = os.path.dirname(os.path.abspath(__file__))

    event_logger = logging.getLogger('event_logger')
    event_logger.setLevel(logging.DEBUG)
    event_handler = logging.FileHandler(os.path.join(script_dir, 'events.log'), encoding='utf-8')
    event_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d.%m.%Y %H:%M:%S')
    event_handler.setFormatter(event_formatter)
    event_logger.addHandler(event_handler)

    error_logger = logging.getLogger('error_logger')
    error_logger.setLevel(logging.ERROR)
    error_handler = logging.FileHandler(os.path.join(script_dir, 'errors.log'), encoding='utf-8')
    error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s', datefmt='%d.%m.%Y %H:%M:%S')
    error_handler.setFormatter(error_formatter)
    error_logger.addHandler(error_handler)


def main():
    while True:
        try:
            event_logger.info('Программа запущена')
            while True:
                command = input("Введите команду: ")
                if command.lower() == 'exit':
                    event_logger.info('Программа завершена')
                    quit()
                elif command == 'error':
                    raise ValueError('Неверное значение')
                elif command == 'dl':
                    event_logger.debug('Баги!..')
                    event_logger.warning('Предупреждение!')
                    event_logger.critical('КРИТИЧЕСКАЯ ОШИБКА Б*ТЬ!!!')
                    error_logger.critical('КРИТИЧЕСКАЯ ОШИБКА Б*ТЬ!!!')
                else:
                    event_logger.info(f'Выполнена команда: {command}')
                    print(f'Вы ввели: {command}')
        except Exception:
            error_logger.error('Произошла ошибка', exc_info=True)

if __name__ == "__main__":
    setup_loggers()
    main()
