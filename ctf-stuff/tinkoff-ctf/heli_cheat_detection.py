from requests import get, post
import json


def detect_cheats(time, trace):
    lap = [t for t in trace if t.get("lap") == 1]
    trace = lap
    if len(trace) <= 2:
        return 1
    if not isinstance(trace[0].get("z"), (int, float)) or not isinstance(
        trace[-1].get("z"), (int, float)
    ):
        return 2
    dz_limit = 300
    speed_limit = 28000
    track_length = 783600
    if trace[0].get("z") < 0 or trace[0].get("z") > dz_limit:
        return 3
    if trace[-1].get("z") < 0 or trace[-1].get("z") <= track_length - dz_limit:
        return 4
    max_dt = 0
    max_dz = 0
    max_speed = 0
    dt_sum = 0
    for i in range(1, len(trace)):
        dt = trace[i].get("t") - trace[i - 1].get("t")
        dz = trace[i].get("z") - trace[i - 1].get("z")
        if not isinstance(dt, (int, float)) or dt < 0.005555555555:
            return f"5: {i} ~ {dt}"
        if dz > dz_limit:
            return f"6: {i} ~ {dz}"
        if trace[i].get("speed") > speed_limit:
            return f'7: {i} ~ {trace[i].get("speed")}'
        dt_sum += dt
        max_speed = max(max_speed, trace[i].get("speed"))
        max_dz = max(max_dz, dz)
        max_dt = max(max_dt, dt)
    if abs(time - dt_sum) > 0.1:
        return f"8: {abs(time - dt_sum)}, t:{time}, dts:{dt_sum}"
    return False


# ------------------------------------------------------ #
trace = [
    {"lap": 1, "speed": 1, "t": float("nan"), "z": i * 300}
    for i in range(1, 783600 // 300 + 1)
]


res = {"username": "noname", "time": 0.1, "trace": trace}

url = r"https://its-heliracer-78n52jqp.spbctf.ru/api/scoreboard"
headers = {"Content-type": "application/json", "Accept": "text/plain"}
ans = post(url, data=json.dumps(res, allow_nan=True), headers=headers)

print(ans.text)
