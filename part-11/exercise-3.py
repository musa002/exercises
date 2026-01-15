def best_results(results: list):
    return [max(r.grade1, r.grade2, r.grade3) for r in results]

class ExamResult:
    def __init__(self, name, grade1, grade2, grade3):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

result1 = ExamResult("Peter", 5, 3, 4)
result2 = ExamResult("Pippa", 3, 4, 1)
result3 = ExamResult("Paul", 2, 1, 3)

results = [result1, result2, result3]
print(best_results(results))

