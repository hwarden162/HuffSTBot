from bot.setup._argument_parser import get_cli_args
from bot.setup._get_webdriver import get_webdriver
from bot.setup._setup_logger import setup_logger

def main() -> None:
    args = get_cli_args()
    logger = setup_logger(args.logging_level)
    driver = get_webdriver(logger, args.browser)
    try:
        pass
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
