from logging import Logger
import pyperclip
from re import sub
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from typing import List

class Game():
    def __init__(self, driver: WebDriver, logger: Logger, room_name: str) -> None:
        assert isinstance(driver, WebDriver), "driver should be of type WebDriver"
        self.driver = driver
        assert isinstance(logger, Logger), "logger should be a Logger"
        self.logger = logger
        assert isinstance(room_name, str), "room_name should be a string"
        self.room_name = room_name
        self.create_room()
        self.num_players = 0
        self.num_living_players = 0
    
    def create_room(self):
        driver = self.driver
        driver.get("https://clocktower.live/")
        wait = WebDriverWait(driver, 10)
        cog_svg = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".svg-inline--fa.fa-cog.fa-w-16")))
        cog_svg.click()
        sleep(1)
        live_session = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".svg-inline--fa.fa-broadcast-tower.fa-w-20")))
        live_session.click()
        sleep(1)
        host_game = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Host (Storyteller)')]"))
        )
        host_game.click()
        alert = wait.until(EC.alert_is_present())
        alert.send_keys(self.room_name) 
        alert.accept()
        copy_player_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Copy player link')]"))
        )
        copy_player_link.click()
        sleep(1)
        clipboard_content = pyperclip.paste()
        self.room_link = clipboard_content
        self.logger.info(f"Created room at {self.room_link}")
    
    def add_players(self, player_names: List[str]) -> None:
        assert isinstance(player_names, list), "player_names should be a list"
        assert all(isinstance(element, str) for element in player_names), "player names should be a list of strings"
        assert len(player_names) > 0, "There should be a positive number of players"
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        live_session = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".svg-inline--fa.fa-users.fa-w-20")))
        live_session.click()
        sleep(1)
        for player_name in player_names:
            pattern = r'[^a-zA-Z0-9 ]'
            player_name = sub(pattern, '', player_name)
            add_player = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Add')]"))
            )
            add_player.click()
            alert = wait.until(EC.alert_is_present())
            alert.send_keys(player_name)
            alert.accept()
            sleep(1)
            self.num_players += 1
            self.num_living_players += 1
        self.logger.info(f"{self.num_players} players added to the grim")
        
    def nomination(self, nominator_idx: int, nominee_idx: int) -> None:
        assert isinstance(nominator_idx, int)
        assert nominator_idx >= 0
        assert nominator_idx < self.num_players
        assert isinstance(nominee_idx, int)
        assert nominee_idx >= 0
        assert nominee_idx < self.num_players
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        townsquare_div = wait.until(
            EC.presence_of_element_located((By.ID, "townsquare"))
        )
        players = townsquare_div.find_elements(By.CLASS_NAME, "player")
        print(f"Num classes {len(players)}")
        nominator = players[nominator_idx].find_element(By.CLASS_NAME, "name")
        driver.execute_script("arguments[0].scrollIntoView(true);", nominator)
        nominator.click()
        sleep(5)
        
        