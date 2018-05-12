import pytest
from django.shortcuts import reverse


@pytest.mark.django_db
def test_office_dashboard_view(logged_in_client, member):
    response = logged_in_client.get(reverse('office:dashboard'))
    assert response.status_code == 200
