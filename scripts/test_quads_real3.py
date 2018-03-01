#!/usr/bin/env python
# coding=utf-8
import rospy
import time
import threading
from demo_test.srv import *

mutexA = threading.Lock()

def test_server_fun_2():
    # init service
    rospy.wait_for_service('teleop_ctrl_service2')
    teleop_srv_init2 = rospy.ServiceProxy('teleop_ctrl_service2',teleop_ctrl)
    # takeoff
    if mutexA.acquire():
        resp = teleop_srv_init2(teleop_ctrl_mask = teleop_ctrlRequest.MASK_ARM_DISARM,
                           base_contrl = teleop_ctrlRequest.ARM_TAKEOFF)
        print resp
        mutexA.release()
    time.sleep(10)
    # fly to point 1
    if mutexA.acquire():
        resp = teleop_srv_init2(teleop_ctrl_mask = teleop_ctrlRequest.MASK_HOVER_POS,
                           hover_pos_x = 0.866,
                           hover_pos_y = 0.5,
                           hover_pos_z = -1.2,
                           hover_pos_yaw = -1.57)
        print resp
        mutexA.release()
    time.sleep(8)
    # fly to point 2
    if mutexA.acquire():
        resp = teleop_srv_init2(teleop_ctrl_mask = teleop_ctrlRequest.MASK_HOVER_POS,
                           hover_pos_x = -0.866,
                           hover_pos_y = -0.5,
                           hover_pos_z = -1.2,
                           hover_pos_yaw = -1.57)
        print resp
        mutexA.release()
    time.sleep(20)
    # land and disarm
    if mutexA.acquire():
        resp = teleop_srv_init2(teleop_ctrl_mask = teleop_ctrlRequest.MASK_ARM_DISARM,
                           base_contrl = teleop_ctrlRequest.LAND_DISARM)
        print resp
        mutexA.release()
    print 'task done!'
    time.sleep(2)
    
    return resp


def test_server_fun_3():
    # init service
    rospy.wait_for_service('teleop_ctrl_service3')
    teleop_srv_init3 = rospy.ServiceProxy('teleop_ctrl_service3',teleop_ctrl)
    # takeoff
    if mutexA.acquire():
        resp = teleop_srv_init3(teleop_ctrl_mask = teleop_ctrlRequest.MASK_ARM_DISARM,
                           base_contrl = teleop_ctrlRequest.ARM_TAKEOFF)
        print resp
        mutexA.release()
    time.sleep(10)
    # fly to point 1
    if mutexA.acquire():
        resp = teleop_srv_init3(teleop_ctrl_mask = teleop_ctrlRequest.MASK_HOVER_POS,
                           hover_pos_x = -0.866,
                           hover_pos_y = 0.5,
                           hover_pos_z = -1.2,
                           hover_pos_yaw = -1.57)
        print resp
        mutexA.release()
    time.sleep(8)
    # fly to point 2
    if mutexA.acquire():
        resp = teleop_srv_init3(teleop_ctrl_mask = teleop_ctrlRequest.MASK_HOVER_POS,
                           hover_pos_x = 0.866,
                           hover_pos_y = -0.5,
                           hover_pos_z = -1.2,
                           hover_pos_yaw = -1.57)
        print resp
        mutexA.release()
    time.sleep(20)
    # land and disarm
    if mutexA.acquire():
        resp = teleop_srv_init3(teleop_ctrl_mask = teleop_ctrlRequest.MASK_ARM_DISARM,
                           base_contrl = teleop_ctrlRequest.LAND_DISARM)
        print resp
        mutexA.release()
    print 'task done!'
    time.sleep(2)
    
    return resp


def test_server_fun_4():
    # init service
    rospy.wait_for_service('teleop_ctrl_service4')
    teleop_srv_init4 = rospy.ServiceProxy('teleop_ctrl_service4',teleop_ctrl)
    # takeoff
    if mutexA.acquire():
        resp = teleop_srv_init4(teleop_ctrl_mask = teleop_ctrlRequest.MASK_ARM_DISARM,
                           base_contrl = teleop_ctrlRequest.ARM_TAKEOFF)
        print resp
        mutexA.release()
    time.sleep(10)
    # fly to point 1 
    if mutexA.acquire():
        resp = teleop_srv_init4(teleop_ctrl_mask = teleop_ctrlRequest.MASK_HOVER_POS,
                           hover_pos_x = 0.0,
                           hover_pos_y = -1.0,
                           hover_pos_z = -1.2,
                           hover_pos_yaw = -1.57)
        print resp
        mutexA.release()
    time.sleep(8)
    # fly to point 2
    if mutexA.acquire():
        resp = teleop_srv_init4(teleop_ctrl_mask = teleop_ctrlRequest.MASK_HOVER_POS,
                           hover_pos_x = 0.0,
                           hover_pos_y = 1.0,
                           hover_pos_z = -1.2,
                           hover_pos_yaw = -1.57)
        print resp
        mutexA.release()
    time.sleep(20)
    # land and disarm
    if mutexA.acquire():
        resp = teleop_srv_init4(teleop_ctrl_mask = teleop_ctrlRequest.MASK_ARM_DISARM,
                           base_contrl = teleop_ctrlRequest.LAND_DISARM)
        print resp
        mutexA.release()
    print 'task done!'
    time.sleep(2)
    
    return resp


def thread_init():
    threads = []
    t1 = threads.Thread(target = test_server_fun_2)
    t2 = threads.Thread(target = test_server_fun_3)
    t3 = threads.Thread(target = test_server_fun_4)
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    for t in threads:
        t.setDaemon(True)
        t.start()
    rospy.spin()

if __name__ == "__main__":
    print "start test teleop control service"
    thread_init()
    print 'exit!'

