```python
class AboutMe:
    def __init__(self, name, role, age, experience, education):
        self.name = name
        self.role = role
        self.age = age
        self.experience = experience
        self.education = education

    def introduce_yourself(self):
        intro = f"Hi, my name is {self.name}. I am a {self.role}."
        details = f"I am {self.age} years old with {self.experience} of experience."
        edu = f"I studied {self.education['jurusan']} at {self.education['school']}."
        return f"{intro}\n{details}\n{edu}"

name = "Ahmad Rafi'i"
role = "Full Stack Developer"
age = "16 years old"
experience = "2 years"
education = {
    "school": "SMKN 6 Malang",
    "jurusan": "SIJA (SISTEM INFORMASI JARINGAN APLIKASI)"
}

developer = AboutMe(name, role, age, experience, education)
```
