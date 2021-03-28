import traffic_light


class TestTrafficLights:
    def test_reaction_on_red(self):
        assert traffic_light.traffic_lights('red') == 'Traffic is prohibited'

    def test_reaction_on_yellow(self):
        assert traffic_light.traffic_lights('yellow') == 'Attention'

    def test_reaction_on_green(self):
        assert traffic_light.traffic_lights('green') == 'Traffic allowed'

    def test_reaction_on_unsuitable_word(self):
        assert traffic_light.traffic_lights('orange') == 'Wrong color'
