class process_data:
    def __init__(self, scraped_data, credit):
        self.result = []
        self.debugger = False
        self.get_list_of_each_course(scraped_data, credit)

    def get_list_of_each_course(self, scraped_data, credit):
        result = []
        split_data = scraped_data.split("\n")
        for i in range(len(split_data)):
            self.debugger and self.validate_course_and_get_credit(split_data[i])[0] and print(split_data[i])
            if self.validate_course_and_get_credit(split_data[i])[1] == credit:
                self.result.append(split_data[i])

    def validate_course_and_get_credit(self, courseString):
        split = courseString.split()
        for s in split:
            if s[-2:] == ".0":
                return [True, s]
        return [False, "null"]

    def get_result(self):
        return self.result