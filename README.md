# Lambda Test Framework with Allure

This project is an automation testing framework built using **Python**, **Pytest**, and **Selenium WebDriver**. It is designed to run tests on the **LambdaTest** platform and generate beautiful test reports using **Allure**.

The goal was to create a clean, easy-to-use test automation setup that’s flexible and scalable.

Here are my Test IDs :-
1. test_valid_login :- 16L22-FNHNC-SLJHI-KSPH3
2. test_invalid_login :- RJSSW-HVCB2-OIEMB-ZKQW7
3. test_handle_all_alerts :- KE9MN-AZA07-5PORH-NT94S

---

## 🧠 Thought Process

I built this framework with the following ideas in mind:

- ✅ Keep test cases clean and readable using the **Page Object Model (POM)**
- ✅ Use **LambdaTest** to run tests on different browsers in the cloud
- ✅ Generate interactive test reports with **Allure**
- ✅ Use environment variables (`.env` file) to manage sensitive data
- ✅ Make the framework easy to update and extend

---

## 🧱 Project Structure

lambda_test_framework/ ├── pages/ # Page classes for each screen (login, alerts, etc.) ├── tests/ # Test case files ├── utils/ # Utility functions and driver setup ├── .env # Contains LambdaTest credentials ├── conftest.py # Pytest fixtures and setup code ├── requirements.txt # List of Python packages needed └── pytest.ini # Pytest configuration settings



## 🧰 Tools & Technologies

| Tool        | Purpose                                 |
|-------------|------------------------------------------|
| Python      | Programming language                    |
| Selenium    | Browser automation                      |
| Pytest      | Test framework                          |
| Allure      | Test reporting                          |
| LambdaTest  | Cloud-based browser testing             |
| dotenv      | Environment variable management         |

---

## 🔐 You can give your credentials and run tests in the `.env` file

LT_USERNAME=your_lambdatest_username  
LT_ACCESS_KEY=your_lambdatest_access_key

---

## 🚀 How you can run tests

🧪 Use `pytest` commands  
📄 For example:  
`pytest tests/test_alerts.py` ➡️ runs the JS alerts test file

---

## ✅ Example Test Cases

- 🔐 Login functionality  
- ⚠️ Handling JavaScript alerts  
- ☁️ Cloud-based execution setup  

🧱 Each test uses **Page Object Model (POM)** to keep things clean and organized.

---

## 🔮 Future Improvements

- ➕ Add more test cases  
- 🧵 Add parallel execution  
- 🔁 Integrate with CI/CD (GitHub Actions, Jenkins)  
- 📊 Use data-driven testing (CSV, Excel, etc.)

---

## 📘 What I Learned

- 🧼 Structuring a clean and scalable test framework  
- ☁️ Running tests on the cloud with **LambdaTest**  
- 📈 Generating and understanding **Allure** reports  
- 🧠 Best practices in test automation using **Pytest** and **POM**
