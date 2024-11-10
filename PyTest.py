import pytest
import requests

class TestTenderAPI:
    base_url = "https://zakupki.mos.ru/auction/{}"

    @pytest.mark.parametrize("tender_id", range(9867400, 9867483))  # Includes 9867482
    def test_post_tender_urls(self, tender_id):
        url = self.base_url.format(tender_id)
        response = requests.post("http://127.0.0.1:8000/api/tender/", json={'url': url})  # Adjust URL as needed

        # Check that the request was successful (status 201 or 200)
        assert response.status_code in [201, 200]
        # Additional checks can be added here, such as validating response content
