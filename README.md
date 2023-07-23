# 🚀 FastPaste

- A new solution to make your own pastes api using python & flask

# ⭐ Features

- 🧬 Simple installation (flask is the only one depedencie !)
- ⚡ Fast & Easy to use (GET requests only !)
- ✔ Create, Delete, See pastes
- ⚜ Short code

# 📖 Documentation

## 📜 Create a new paste

*You can create a paste with a simple get request*

```python
import requests

r = requests.get("https://api.strium.tech/new?content=" + input("Enter your text >>> "))
print(r.text)
```

*You will get a response like that*

```json
{"data": {"id": "y6s1qb", "secret": "// Nothing to see here :)", "url": "http://api.strium.tech/paste?id=y6s1qb"}, "success": true}
```

** 🗑️ Delete a paste

*You can delete a paste with a simple get request*

```python
import requests

r = requests.get("https://api.strium.tech/delete?id=y6s1qb&secret=yourSecret")
print(r.text)
```

*You will get a response like that*

```json
{"success": True}
```

** 👀 See a paste

*You can see a paste with a simple get request* **or** *by opening the link in your browser*

```python
import requests

r = requests.get("https://api.strium.tech/paste?id=y6s1qb")
print(r.text)
```

*The response never will be the same because every paste is different 🤷‍♂️*

```github.com/vodkarm```
