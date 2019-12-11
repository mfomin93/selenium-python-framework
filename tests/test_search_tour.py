import pytest
import allure

from pages.search_tours_form import SearchToursForm
from utils.read_xlsx import XlsxReader


@pytest.mark.usefixtures("setup")
class TestTourSearch:

    @allure.title("Search flight test")
    @allure.description("This is test of searching flight")
    def test_search_tour_general(self):
        search_tour = SearchToursForm(self.driver)
        search_tour.open_page()
        search_tour.open_tours_tab()
        search_tour.set_tour_destination("Sheraton Trip")
        search_tour.set_tour_type("Private")
        search_tour.set_date("2020", "Jan", "3")
        search_tour.set_adults_number(3)
        search_tour.search_perform()
