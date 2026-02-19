#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""时区转换功能验证脚本。在项目根目录运行: python test_timezone.py"""

import sys
import os

# 确保从项目根目录导入
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_timezone_utils():
    """验证 timezone_utils 各函数在默认配置（Asia/Shanghai）下的行为。"""
    from utils import timezone_utils
    from datetime import datetime, timezone

    errors = []
    # 1. get_display_zone
    try:
        z = timezone_utils.get_display_zone()
        assert z is not None
        print("[OK] get_display_zone() 返回有效时区")
    except Exception as e:
        errors.append(f"get_display_zone: {e}")

    # 2. utc_to_display: UTC 10:00 -> 北京时间 18:00 (UTC+8)
    try:
        out = timezone_utils.utc_to_display("2025-02-17T10:00:00Z")
        assert out == "2025-02-17 18:00:00", f"utc_to_display 结果不符: got {out}"
        print("[OK] utc_to_display('2025-02-17T10:00:00Z') => 北京时间 18:00:00")
    except Exception as e:
        errors.append(f"utc_to_display: {e}")

    # 2b. utc_to_display 空字符串
    try:
        out = timezone_utils.utc_to_display("")
        assert out == ""
        print("[OK] utc_to_display('') => ''")
    except Exception as e:
        errors.append(f"utc_to_display empty: {e}")

    # 3. jst_to_display: JST 19:00 -> 北京时间 18:00 (时差 -1h)
    try:
        out = timezone_utils.jst_to_display("2025-02-17 19:00:00")
        assert out == "2025-02-17 18:00:00", f"jst_to_display 结果不符: got {out}"
        print("[OK] jst_to_display('2025-02-17 19:00:00') => 北京时间 18:00:00")
    except Exception as e:
        errors.append(f"jst_to_display: {e}")

    # 4. timestamp_to_display: 固定 UTC 时间戳 -> 显示时区时间
    # 2025-02-17 10:00:00 UTC = 1739782800  (需确认：datetime(2025,2,17,10,0,0,tzinfo=timezone.utc).timestamp() 在 Python 里是本地？不，timestamp() 返回的是 UTC 秒数)
    try:
        # 使用 2025-02-17 10:00:00 UTC 的时间戳（秒）
        dt_utc = datetime(2025, 2, 17, 10, 0, 0, tzinfo=timezone.utc)
        ts = int(dt_utc.timestamp())
        out = timezone_utils.timestamp_to_display(ts)
        assert out == "2025-02-17 18:00:00", f"timestamp_to_display 结果不符: got {out}"
        print("[OK] timestamp_to_display(UTC 10:00 时间戳) => 北京时间 18:00:00")
    except Exception as e:
        errors.append(f"timestamp_to_display: {e}")

    # 5. parse_display_time
    try:
        dt = timezone_utils.parse_display_time("2025-02-17 18:00:00")
        assert dt is not None and dt.year == 2025 and dt.hour == 18
        print("[OK] parse_display_time('2025-02-17 18:00:00') 解析正确")
    except Exception as e:
        errors.append(f"parse_display_time: {e}")

    # 6. now_in_display_tz 与 now_display_str
    try:
        now_naive = timezone_utils.now_in_display_tz()
        now_str = timezone_utils.now_display_str()
        assert now_naive is not None and now_str
        parsed = timezone_utils.parse_display_time(now_str)
        assert parsed is not None
        # 同一天内时间差应很小
        diff = abs((parsed - now_naive).total_seconds())
        assert diff < 2, f"now_display_str 与 now_in_display_tz 不一致: diff={diff}s"
        print("[OK] now_in_display_tz() / now_display_str() 与 parse_display_time 一致")
    except Exception as e:
        errors.append(f"now_in_display_tz/now_display_str: {e}")

    # 7. 时间差计算（与 main_window / message_processor 用法一致）
    try:
        shock_str = "2025-02-17 18:00:00"
        shock_time = timezone_utils.parse_display_time(shock_str)
        time_diff = (timezone_utils.now_in_display_tz() - shock_time).total_seconds()
        # 若当前时间晚于 18:00，差为正
        assert isinstance(time_diff, (int, float))
        print(f"[OK] 时间差计算正常 (示例: 与 {shock_str} 差 {time_diff:.0f} 秒)")
    except Exception as e:
        errors.append(f"时间差计算: {e}")

    return errors


def test_timezone_names_zh():
    """验证 timezone_names_zh 选项与 iana_to_display。"""
    from utils.timezone_names_zh import get_tz_options, iana_to_display, TZ_OFFSET_CITY

    errors = []
    try:
        options = get_tz_options()
        assert len(options) == len(TZ_OFFSET_CITY)
        assert any(d == "UTC+8 北京" and tid == "Asia/Shanghai" for d, tid in options)
        print("[OK] get_tz_options() 返回完整列表且包含 UTC+8 北京 / Asia/Shanghai")
    except Exception as e:
        errors.append(f"get_tz_options: {e}")

    try:
        d = iana_to_display("Asia/Shanghai")
        assert d == "UTC+8 北京", f"iana_to_display Asia/Shanghai: got {d}"
        d2 = iana_to_display("Asia/Tokyo")
        assert d2 == "UTC+9 东京", f"iana_to_display Asia/Tokyo: got {d2}"
        print("[OK] iana_to_display('Asia/Shanghai') => 'UTC+8 北京', Asia/Tokyo => 'UTC+9 东京'")
    except Exception as e:
        errors.append(f"iana_to_display: {e}")

    return errors


def main():
    print("========== 时区转换功能检查 ==========\n")
    err1 = test_timezone_utils()
    print()
    err2 = test_timezone_names_zh()
    all_errors = err1 + err2
    print("\n========== 结果 ==========")
    if not all_errors:
        print("全部通过，时区转换功能运行正常。")
        return 0
    for e in all_errors:
        print(f"失败: {e}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
