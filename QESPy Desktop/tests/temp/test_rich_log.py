from rich.logging import RichHandler
import logging

# Настройка логирования с Rich
logging.basicConfig(
    level="DEBUG",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()]
)

logger = logging.getLogger("rich_logger")

# Пример использования логгера с Rich
logger.debug("Это отладочное сообщение")
logger.info("Это информационное сообщение")
logger.warning("Это предупреждение")
logger.error("Это сообщение об ошибке")
logger.critical("Это критическое сообщение")
