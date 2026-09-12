from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
  message = ""
  status = ""  # Змінна для кольору/стилю повідомлення

  if request.method == "POST":
    try:
      age = int(request.form.get("age"))

      if age >= 18:
        message = "Доступ дозволено! Ви повнолітній."
        status = "success"
      elif 13 <= age < 18:
        message = (
            "Увага: Вам від 13 до 17 років. Потрібна згода батьків для"
            " користування."
        )
        status = "warning"
      else:
        # Якщо менше 13 — «викидаємо» / блокуємо доступ
        message = (
            "❌ Доступ заборонено! Вам менше 13 років. Ви не можете користуватись"
            " цією програмою."
        )
        status = "danger"

    except ValueError:
      message = "Будь ласка, введіть коректне ціле число!"
      status = "error"

  return render_template("index.html", result=message, status=status)


if __name__ == "__main__":
  app.run(debug=True)