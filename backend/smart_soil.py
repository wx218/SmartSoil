def analyze_soil(nitrogen, water_level, weather):

    recommendations = []

    if nitrogen == "low":
        recommendations.append("Add nitrogen fertilizer")

    if weather == "heavy rain":
        recommendations.append("Reduce irrigation")

    if water_level == "high":
        recommendations.append("Improve drainage")

    return recommendations


# test simulation
result = analyze_soil("low", "high", "heavy rain")
print(result)
