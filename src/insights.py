def generate_insights(df):
    insights = {}

    high_risk = df[df["risk_flag"] == "HIGH"]["student_id"].tolist()
    insights["high_risk_students"] = high_risk

    chapter_difficulty = (
        df.groupby("chapter_order")
        .agg(
            avg_score=("score", "mean"),
            avg_time=("time_spent", "mean"),
            dropout_rate=("completion_prediction", lambda x: 1 - x.mean())
        )
        .reset_index()
    )

    insights["difficult_chapters"] = chapter_difficulty[
        chapter_difficulty["dropout_rate"] > 0.5
    ]["chapter_order"].tolist()

    insights["key_factors"] = [
        "Low scores increase dropout risk",
        "Low time spent is strongly correlated with non-completion"
    ]

    return insights
