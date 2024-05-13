def eat(food, is_healthy):
    ending = "because YOLO!"
    if is_healthy:
        ending = "because my body is a temple"
    return f"I'm eating {food}, {ending}"


def nap(num_hours):
    if num_hours < 2:
        return f"I'm feeling refreshed after my {num_hours} hour nap"
    else:
        return f"damn, I overslept for {num_hours} hours"
