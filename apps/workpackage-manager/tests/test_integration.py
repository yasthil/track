import pytest

try:
    from wpm.app import app, openproject
    openproject.testing = True
except Exception:
    app = None


@pytest.fixture()
def test_client():
    if app is None:
        pytest.skip("Cannot load app. Probably missing config.yml")
    with app.test_client() as client:
        yield client


def test_custom_field_fetching(test_client):
    regions = test_client.get('/region').json['regions']
    assert len(regions) > 5
    for region in regions:
        assert region['label'] is not None
        assert region['id'] is not None
    labels = set([r['label'] for r in regions])
    assert 'Victoria' in labels


def test_order_submission(test_client):
    test_client.post(dict(

    ))