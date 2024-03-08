import functions as func


class Test_LbsToKgs:
    def test_int(self):
        assert func.LbsToKgs(120) == 54

    def test_float(self):
        assert func.LbsToKgs(120.7) == 54.315

class Test_HeightToMeters:
    def test_function(self):
        assert func.HeightToMeters(5, 2) == 1.55

class Test_BMI:
    def test_int(self):
        assert func.BMI(54, 2) == 13.5
    
    def test_float(self):
        assert func.BMI(54.315, 1.55) == 22.608

    def test_mix(self):
        assert func.BMI(54, 1.55) == 22.477

class Test_Categorize:
    def test_under(self):
        assert func.Categorize(15) == "underweight"

    def test_norm(self):
        assert func.Categorize(22) == "normal weight"

    def test_over(self):
        assert func.Categorize(27) == "overweight"

    def test_obese(self):
        assert func.Categorize(32) == "obese"

    def test_bound1off(self):
        assert func.Categorize(18.45) == "underweight"

    def test_bound1on(self):
        assert func.Categorize(18.5) == "normal weight"

    def test_bound2off(self):
        assert func.Categorize(24.95) == "normal weight"

    def test_bound2on(self):
        assert func.Categorize(25) == "overweight"

    def test_bound3off(self):
        assert func.Categorize(29.95) == "overweight"

    def test_bound3on(self):
        assert func.Categorize(30) == "obese"

class Test_getHeight:
    def test_int(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda: "5, 2")
        f, i = func.getHeight()
        assert f == 5
        assert i == 2

    def test_float(self, monkeypatch, capfd):
        inputs = iter(["5.8, 1.2", "5, 2"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs))
        func.getHeight()
        out, err = capfd.readouterr()
        assert out == "Please enter a valid integer combination\n"
    
    def test_mix(self, monkeypatch, capfd):
        inputs = iter(["5, 1.2", "5, 2"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs))
        func.getHeight()
        out, err = capfd.readouterr()
        assert out == "Please enter a valid integer combination\n"
    
    def test_single(self, monkeypatch, capfd):
        inputs = iter(["5", "5, 2"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs))
        func.getHeight()
        out, err = capfd.readouterr()
        assert out == "Please enter a valid integer combination\n"
    
    def test_text(self, monkeypatch, capfd):
        inputs = iter(["test", "5, 2"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs))
        func.getHeight()
        out, err = capfd.readouterr()
        assert out == "Please enter a valid integer combination\n"

class Test_getWeight:
    def test_int(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda: "120")
        p = func.getWeight()
        assert p == 120
    
    def test_int(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda: "120.7")
        p = func.getWeight()
        assert p == 120.7

    def test_text(self, monkeypatch, capfd):
        inputs = iter(["test", "120"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs))
        func.getWeight()
        out, err = capfd.readouterr()
        assert out == "Please enter a valid number\n"