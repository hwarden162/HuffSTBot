from bot.game._game import Game
from bot.setup._argument_parser import get_cli_args
from bot.setup._get_webdriver import get_webdriver
from bot.setup._setup_logger import setup_logger

def main() -> None:
    args = get_cli_args()
    logger = setup_logger(args.logging_level)
    driver = get_webdriver(logger, args.browser)
    try:
        game = Game(driver, logger, args.room_name)
        game.add_players(["Huff", "Sun", "FakeHarry", "Ponko", "Procyon", "Bas", "Acaila", "Dela", "Utku", "Kal", "Skaggs", "Isaac"])
        game.nomination(0, 1)
    finally:
        driver.quit()
        logger.info("Disconnected web driver")

if __name__ == "__main__":
    main()
