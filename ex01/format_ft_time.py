import time
import datetime

now = time.time()

normal = f"{now:,.4f}"  # f"{値: フォーマット}" "," 三桁ごとにカンマ
scientific = f"{now:.2e}"  # .2: 小数点2桁より下を指数表記

dt = datetime.datetime.fromtimestamp(now)
date_str = dt.strftime("%b %d %Y")

print(
    f"Seconde since January 1, 1970: {normal} "
    f"or {scientific} in scientific notation"
)
print(date_str)
