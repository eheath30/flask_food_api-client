import json

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == 'Hello from Flask!'

    def test_get_food(self, api):
        res = api.get('/api/food')
        assert res.status == '200 OK'
        assert len(res.json) == 2

    def test_get_food(self, api):
        res = api.get('/api/food/2')
        assert res.status == '200 OK'
        assert res.json['name'] == 'Test Food 2'

    def test_get_food_error(self, api):
        res = api.get('/api/food/4')
        assert res.status == '400 BAD REQUEST'
        assert "food with id 4" in res.json['message']

    def test_post_food(self, api):
        mock_data = json.dumps({'name': 'Cheese and Spinach'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/api/food', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 3

    def test_patch_food(self, api):
        mock_data = json.dumps({'name': 'Peri Peri Chicken'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.patch('/api/food/2', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 2
        assert res.json['name'] == 'Peri Peri Chicken'

    def test_delete_food(self, api):
        res = api.delete('/api/food/1')
        assert res.status == '204 NO CONTENT'

    def test_not_found(self, api):
        res = api.get('/food/3')
        assert res.status == '404 NOT FOUND'
        assert 'Oops!' in res.json['message']
