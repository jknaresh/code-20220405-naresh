import pandas as pd


class CalculatorBMI(object):
    """
    Calculator BMI
    """

    def __init__(self, data):
        self.data = data
        self.df = None

    @staticmethod
    def bmi(d1: dict) -> float:
        """
        :param d1:
        :return: float
        """
        return d1["WeightKg"] / (d1["HeightCm"] / 100) ** 2

    @staticmethod
    def bmi_category_risk(score: float) -> dict:
        """
        based on BMI score, return category and risk of the score.
        :param score:
        :return: dict
        """
        if score < 0:
            return {"cat": "n/a", "risk": "n/a"}

        if score >= 40:
            return {"cat": "Very severely obese", "risk": "Very high risk"}
        elif score >= 35:
            return {"cat": "Severely obese", "risk": "High risk"}
        elif score >= 30:
            return {"cat": "Moderately obese", "risk": "Medium risk"}
        elif score >= 25:
            return {"cat": "Overweight", "risk": "Enhanced risk"}
        elif score >= 18.5:
            return {"cat": "Normal weight", "risk": "Low risk"}
        else:
            return {"cat": "Underweight", "risk": "Malnutrition risk"}

    def update_cat_risk(self, d2: dict) -> tuple:
        """
        find based on input date bmi score, category and risk
        :param d2:
        :return: tuple
        """
        b = self.bmi(d2)
        o = self.bmi_category_risk(b)
        return b, o.get("cat"), o.get("risk")

    def overweight_count(self):
        ow_shape = self.df[self.df["category"] == "Overweight"].shape
        print("total overweight's are ", ow_shape[0])

    def count_by_category(self, category="category"):
        print(self.df.groupby(category).count())

    def run(self) -> None:

        self.df = pd.DataFrame(data=self.data)
        # extend dataframe with bmi, category and risk
        self.df["bmi"], self.df["category"], self.df["risk"] = zip(*self.df.apply(self.update_cat_risk, axis=1))

        # print overweight count
        self.overweight_count()

        # category by count
        self.count_by_category()
        # risk by count
        self.count_by_category(category="risk")


data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
        {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
        {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
        {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
        {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
        {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
bmi = CalculatorBMI(data)
bmi.run()
