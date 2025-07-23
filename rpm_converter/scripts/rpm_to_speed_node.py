#!/usr/bin/env python3

import rospy
import math
from md.msg import md_robot_msg1  # 정확한 메시지 타입

# === 사용자 설정 ===
WHEEL_RADIUS = 0.107    # 단위: m
GEAR_RATIO = 30        # 감속비

def rpm_to_mps(rpm):
    return (2 * math.pi * WHEEL_RADIUS * rpm) / (60 * GEAR_RATIO)

def callback(msg):
    speed1 = rpm_to_mps(msg.motor1_rpm)
    speed2 = rpm_to_mps(msg.motor2_rpm)
    rospy.loginfo(f"[속도] motor1: {speed1:.3f} m/s, motor2: {speed2:.3f} m/s")

def listener():
    rospy.init_node('rpm_to_speed_node')
    rospy.Subscriber("/md_robot_message1", md_robot_msg1, callback)  # <-- 여기 수정됨
    rospy.spin()

if __name__ == '__main__':
    listener()

