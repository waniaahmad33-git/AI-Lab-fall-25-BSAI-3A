
def check_application(score, documents_complete, attendance, recommendations):
    if score < 70:
        return "Rejected"

    if documents_complete == False:
        return "Rejected"

    if attendance < 75:
        return "Rejected"

    if recommendations < 1:
        return "Rejected"

    return "Approved"


test_cases = [
    {
        "name": "Test Case 1: Pass",
        "input": (85, True, 90, 2),
        "expected": "Approved",
        "reason": "All four conditions are satisfied."
    },
    {
        "name": "Test Case 2: Attendance Failure",
        "input": (85, True, 70, 2),
        "expected": "Rejected",
        "reason": "Attendance is below 75%."
    },
    {
        "name": "Test Case 3: Recommendation Failure",
        "input": (85, True, 90, 0),
        "expected": "Rejected",
        "reason": "At least one recommendation is required."
    },
    {
        "name": "Test Case 4: Threshold Boundary",
        "input": (70, True, 75, 1),
        "expected": "Approved",
        "reason": "Score is exactly 70 and attendance is exactly 75%."
    }
]


for case in test_cases:
    score, documents, attendance, recommendations = case["input"]

    actual = check_application(
        score, documents, attendance, recommendations
    )

    print("\n", case["name"])
    print("Input:", case["input"])
    print("Expected Result:", case["expected"])
    print("Actual Result:", actual)
    print("Reason:", case["reason"])
    print("-" * 40)


print("\nThresholds are synthetic lab assumptions.")
