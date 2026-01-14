from pages.twitch_page import TwitchPage


class TestTwitchSearch:
    """Test class for Twitch mobile search"""
    
    def test_search_starcraft_and_select_streamer(self, driver):
        """
        Test Case: Search by keyword <<StarCraft II>> and select streamer
        
        Steps:
        1. Navigate to Twitch
        2. Click the search icon and search "StarCraft II"
        3. Scroll down 2 times
        4. Select a streamer
        Additional steps:
        5. Handle any potential modals or pop-ups
        6. Wait for the page to load and take a screenshot
        """

        twitch_page = TwitchPage(driver)
        
        twitch_page.navigate_to_url()
        
        twitch_page.click_on_search()
        twitch_page.search_by_keyword("StarCraft II")
        
        twitch_page.scroll_down_by_attempts(attempts=2)
        
        twitch_page.select_streamer(index=0)
        
        twitch_page.wait_for_stream_page()
        twitch_page.handle_modals()
        
        screenshot_path = twitch_page.take_screenshot("starcraft_streamer.png")
        
        assert screenshot_path is not None
        print(f"Screenshot saved to: {screenshot_path}")
