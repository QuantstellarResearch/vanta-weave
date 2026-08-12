import simbench as sb

# Chọn mã lưới cần nghiên cứu
sb_code = "1-MV-urban--0-sw"

# 1. Tải profile của năm hiện tại (Scenario 0)
profiles_current = sb.get_absolute_values(sb.get_simbench_net(sb_code), scenario=0)
load_now = profiles_current["load"]["p_mw"]

# 2. Tải profile của kịch bản tương lai xa (Scenario 2 - Tải đã tăng trưởng)
profiles_future = sb.get_absolute_values(sb.get_simbench_net(sb_code), scenario=2)
load_future = profiles_future["load"]["p_mw"]

# So sánh sự tăng trưởng tải giữa quá khứ và tương lai
print("Tải hiện tại (Nút số 0):\n", load_now.iloc[:, 0].head())
print("Tải tương lai sau khi tăng trưởng (Nút số 0):\n", load_future.iloc[:, 0].head())
